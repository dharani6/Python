"""
Page Object Model for the Task Manager page.

Tests never touch raw selectors directly -- they call methods on TaskPage.
If the frontend's markup changes, only this one file needs updating; every
test built on top of it keeps working unchanged.
"""
from playwright.sync_api import expect


class TaskPage:
    def __init__(self, page):
        self.page = page

    def goto(self, base_url):
        self.page.goto(base_url)

    def add_task(self, title):
        self.page.fill('[data-testid="task-input"]', title)
        self.page.click('[data-testid="add-task-btn"]')

    def all_task_titles(self):
        return self.page.locator('#task-list li span').all_inner_texts()

    def expect_task_title(self, title):
        expect(self.page.locator('#task-list li span')).to_contain_text(title)

    def task_count(self):
        return self.page.locator('#task-list li').count()

    def expect_task_count(self, count):
        expect(self.page.locator('#task-list li')).to_have_count(count)

    def toggle_first_task(self):
        self.page.locator('[data-testid^="toggle-btn-"]').first.click()

    def delete_first_task(self):
        self.page.locator('[data-testid^="delete-btn-"]').first.click()

    def completed_task_count(self):
        return self.page.locator('#task-list li span.completed').count()

    def expect_completed_task_count(self, count):
        expect(self.page.locator('#task-list li span.completed')).to_have_count(count)
