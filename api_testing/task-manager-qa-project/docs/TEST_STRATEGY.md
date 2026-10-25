# Test Strategy

This document explains *why* the test suite is built the way it is — the
part of the project meant to be talked through with a technical architect
or engineering manager, not just demoed.

## 1. Scope

| Layer | Tool | What it verifies |
|---|---|---|
| REST API | pytest + requests | HTTP contract: status codes, response shape, business rules (e.g. empty titles rejected) |
| UI | Playwright (Python) + Page Object Model | User-visible behavior: adding/completing/deleting tasks renders correctly |
| CI | GitHub Actions | Both suites run automatically on every push/PR; reports are archived as build artifacts |

Deliberately out of scope for this project (called out so reviewers know
it's a conscious choice, not an oversight): load/performance testing,
security testing, accessibility testing, cross-browser matrix beyond
Chromium. Each is a natural "what would you add next" answer in an
interview.

## 2. Why HTTP-level API tests instead of Flask's test client

Flask's built-in test client calls view functions in-process — fast, but
it never serializes a real HTTP request or runs a real WSGI server. This
project's `conftest.py` instead boots a real Flask server on a free local
port and drives it with the `requests` library. That means:

- The tests prove the app behaves correctly *as deployed*, including
  routing, serialization, and headers — not just that the Python function
  returns the right dict.
- The exact same test files work unchanged against a staging or
  production URL by swapping the `base_url` fixture — useful for explaining
  how this scales to testing a real microservice.

## 3. Test isolation strategy

Every test gets a clean slate via an `autouse` fixture that calls a
`/api/tasks/reset` endpoint before each test runs. This avoids the most
common flaky-test cause: tests that pass alone but fail when run in a
different order, in parallel, or after another test leaves data behind.
It also means tests can be safely parallelized later with `pytest-xdist`
with no extra work.

## 4. Positive vs. negative test separation

`test_tasks_api.py` covers the contract working as intended. A separate
file, `test_tasks_api_negative.py`, deliberately tests:

- Missing/blank required fields → expect `400`, not a crash
- Requests for IDs that don't exist → expect `404`
- Malformed ID formats (`"abc"`, `"1.5"`, `"-1"`) → expect `404`, not `500`

That last category matters more than it looks: a malformed path parameter
causing a `500` instead of a clean `404` is a common real-world bug, and
explicitly testing for it shows you think about how an API fails, not just
how it succeeds.

## 5. UI test design: Page Object Model

`tests/ui/pages/task_page.py` wraps every selector and interaction behind
named methods (`add_task`, `toggle_first_task`, `task_count`, …). Tests
read like user stories:

```python
task_page.add_task("Write report")
assert "Write report" in task_page.all_task_titles()
```

If the frontend markup changes, only `task_page.py` needs updating — every
test built on it keeps working. This is the standard pattern for keeping
UI suites maintainable as an app grows past a handful of pages.

`data-testid` attributes are used for every interactive element instead of
CSS classes or text content, so tests don't break when styling changes —
another common source of UI-test flakiness this project avoids by design.

## 6. CI strategy

`.github/workflows/ci.yml` runs on every push and pull request to `main`:
install dependencies, install the Playwright browser binary, run the API
suite, run the UI suite, and upload both HTML reports as build artifacts
regardless of pass/fail (`if: always()`) — so a failed run still leaves a
report to debug from.

## 7. Traceability: requirement → test

| Behavior | Covered by |
|---|---|
| Create task | `test_create_task_returns_201_with_task_payload` |
| Reject empty title | `test_create_task_without_title_returns_400`, `test_create_task_with_blank_title_returns_400` |
| Read single/all tasks | `test_get_task_by_id_returns_correct_task`, `test_list_tasks_reflects_all_created_tasks_in_order` |
| Update title/completion | `test_update_task_marks_it_completed`, `test_update_task_can_change_title` |
| Reject invalid update | `test_update_task_with_blank_title_returns_400`, `test_update_nonexistent_task_returns_404` |
| Delete task | `test_delete_task_removes_it`, `test_delete_nonexistent_task_returns_404` |
| Malformed ID handling | `test_non_integer_id_returns_404_not_500` |
| UI: add task | `test_adding_task_shows_it_in_the_list` |
| UI: complete task | `test_marking_task_complete_applies_strikethrough_style` |
| UI: delete task | `test_deleting_task_removes_it_from_the_list` |
| UI: reject empty input | `test_submitting_empty_input_does_not_add_a_task` |

A reviewer can use this table to confirm coverage maps directly to
requirements — useful for showing requirements-based test design rather
than ad-hoc test writing.
