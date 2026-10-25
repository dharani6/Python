"""
UI tests against the same backend the API tests cover -- proving the
frontend correctly drives the REST API rather than re-testing the API
itself. Each test starts from a clean slate via the autouse reset fixture.
"""
from tests.ui.pages.task_page import TaskPage


def test_adding_task_shows_it_in_the_list(page, live_server_url):
    task_page = TaskPage(page)
    task_page.goto(live_server_url)

    task_page.add_task("Write report")

    task_page.expect_task_title("Write report")


def test_marking_task_complete_applies_strikethrough_style(page, live_server_url):
    task_page = TaskPage(page)
    task_page.goto(live_server_url)
    task_page.add_task("Finish slides")

    task_page.toggle_first_task()

    task_page.expect_completed_task_count(1)


def test_deleting_task_removes_it_from_the_list(page, live_server_url):
    task_page = TaskPage(page)
    task_page.goto(live_server_url)
    task_page.add_task("Temp task")
    task_page.expect_task_count(1)

    task_page.delete_first_task()

    task_page.expect_task_count(0)


def test_submitting_empty_input_does_not_add_a_task(page, live_server_url):
    task_page = TaskPage(page)
    task_page.goto(live_server_url)

    task_page.add_task("")

    task_page.expect_task_count(0)

