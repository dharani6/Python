# Task Manager — REST API + Automated Test Framework (API + UI)

A small, complete project that demonstrates the full QA automation lifecycle:
building a REST API, testing it at the API layer with Python, and testing
the UI layer that consumes it — wired into a CI pipeline.

---

## 1. What is a REST API? (concept primer)

REST (Representational State Transfer) is an architectural style for web
services built on a few core ideas:

- **Resources, not actions.** URLs represent *things* (`/api/tasks`,
  `/api/tasks/3`), not verbs (`/getTaskById`).
- **HTTP methods = CRUD.** `GET` reads, `POST` creates, `PUT`/`PATCH`
  updates, `DELETE` removes.
- **Stateless.** Every request carries everything needed to process it; the
  server doesn't remember the client between requests.
- **Standard status codes carry meaning.** `200` OK, `201` Created, `204`
  No Content, `400` Bad Request, `404` Not Found, `500` Server Error —
  clients can react to the *code*, not just the response body.
- **JSON as the data format** for request and response bodies.

This project's API follows that contract exactly:

| Method | Endpoint            | Purpose              | Success | Failure        |
|--------|----------------------|-----------------------|---------|-----------------|
| GET    | `/api/tasks`         | List all tasks        | 200     | —               |
| POST   | `/api/tasks`         | Create a task          | 201     | 400 (no title)  |
| GET    | `/api/tasks/<id>`    | Get one task           | 200     | 404             |
| PUT    | `/api/tasks/<id>`    | Update title/completed | 200     | 400 / 404       |
| DELETE | `/api/tasks/<id>`    | Delete a task          | 204     | 404             |

---

## 2. Architecture

```
┌─────────────────────┐        HTTP/JSON        ┌──────────────────────┐
│   Browser (UI)       │ ───────────────────────▶│   Flask REST API      │
│  index.html + fetch() │ ◀───────────────────────│   /api/tasks ...      │
└─────────────────────┘                          └──────────────────────┘
        ▲                                                   ▲
        │ Playwright drives                                  │ requests library
        │ real browser clicks                                │ calls raw HTTP
┌─────────────────────┐                          ┌──────────────────────┐
│   UI Test Suite       │                          │   API Test Suite       │
│  Page Object Model     │                          │   pytest + requests    │
└─────────────────────┘                          └──────────────────────┘
              \                                          /
               \________________  CI runs both  ________/
                              GitHub Actions
```

The key design decision: **the UI and the API are tested independently, at
the layer where they each operate.** API tests talk HTTP directly and never
touch a browser. UI tests drive the real browser and never assert on JSON —
they only assert on what a user would see. This is the test pyramid in
practice, not just in theory.

---

## 3. Project structure

```
task-manager-qa-project/
├── app/                      # Flask REST API + minimal frontend
│   ├── __init__.py            # App factory
│   ├── models.py               # In-memory data store
│   ├── routes.py                # REST endpoints
│   └── templates/index.html      # Frontend that consumes the API
├── run.py                    # Entry point: `python run.py`
├── tests/
│   ├── api/                   # pytest + requests (HTTP-level tests)
│   │   ├── conftest.py          # Spins up a real server for tests
│   │   ├── test_tasks_api.py     # Positive/CRUD tests
│   │   └── test_tasks_api_negative.py  # Negative/boundary tests
│   └── ui/                    # Playwright (browser-level tests)
│       ├── conftest.py          # Same live-server pattern as API tests
│       ├── pages/task_page.py    # Page Object Model
│       └── test_tasks_ui.py      # UI behavior tests
├── .github/workflows/ci.yml  # CI: runs both suites on every push
├── pytest.ini
├── requirements.txt
└── docs/TEST_STRATEGY.md     # Test strategy write-up (read this for interviews)
```

---

## 4. Setup (from scratch)

```bash
# 1. Clone/copy the project, then create a virtual environment
python3 -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Install the Playwright browser binary (one-time, ~150MB download)
playwright install chromium

# 4. Run the app manually (optional, to see it in a browser)
python run.py
# visit http://127.0.0.1:5000
```

> **Note on this build:** the API test suite was executed and verified —
> all 16 tests pass. The Playwright browser binary could not be downloaded
> in the sandboxed environment this was built in (restricted network
> egress), so the UI suite was verified for correct syntax and test
> collection (pytest finds and parametrizes all 4 tests correctly) but not
> executed against a real browser here. Running `playwright install
> chromium` followed by `pytest tests/ui` on your own machine or in the
> provided CI pipeline will execute them for real — do this before your
> interview so you have an actual passing run to show.

## 5. Running the tests

```bash
# API tests only
pytest tests/api -v

# UI tests only (headed, so you can watch the browser)
pytest tests/ui -v --headed

# Everything, with an HTML report
pytest -v --html=reports/full-report.html --self-contained-html
```

---

## 6. How to present this in an interview

A few framings that show senior-level thinking, not just "I wrote some tests":

- **"I test at the right layer."** API tests never launch a browser; UI
  tests never parse JSON. Each suite tests only what that layer is
  responsible for — this keeps the suite fast and avoids redundant
  coverage. Explain the test pyramid here.
- **"Every test is independent."** An `autouse` fixture resets server state
  before each test, so tests can run in any order, in parallel, or
  individually — there's no hidden coupling between test cases.
- **"The API tests are black-box and portable."** They talk real HTTP via
  `requests` instead of Flask's internal test client, so the exact same
  test file could point at a staging or production URL with one fixture
  change. That's how you'd explain testing a microservice you didn't write.
- **"The UI tests don't know about implementation details."** The Page
  Object Model means if the frontend's HTML changes, only `task_page.py`
  needs updating — every test built on top of it keeps working.
- **"It's wired into CI."** Every push runs both suites and uploads an HTML
  report as a build artifact — this is what "shift-left" testing looks
  like in practice, not just a slide.
- **Negative testing is a separate, deliberate file** (`test_tasks_api_negative.py`)
  — be ready to explain *why* (400 vs 404 vs 500 semantics, and why a bad
  ID format should never 500).

## 7. Natural next steps to mention (shows you know how to scale this)

- Swap the in-memory store for a real database (SQLite/Postgres) — the API
  contract and all tests stay unchanged, proving good separation of
  concerns.
- Add authentication and test both authorized and unauthorized request
  paths.
- Add contract/schema validation (e.g. `jsonschema` or Pydantic) so a
  response shape change fails tests immediately.
- Parallelize test execution (`pytest-xdist`) and add cross-browser runs
  (Firefox, WebKit) in CI.
- Add Allure or similar for richer, shareable test reporting.
