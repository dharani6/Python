import itertools
from threading import Lock


class TaskStore:
    """
    In-memory data store for tasks.

    A real project would swap this for SQLAlchemy + a database, but keeping
    it in-memory keeps the project runnable with zero setup -- the API
    contract (and therefore the tests) stays identical either way.
    """

    def __init__(self):
        self._tasks = {}
        self._id_counter = itertools.count(1)
        self._lock = Lock()

    def list_tasks(self):
        with self._lock:
            return list(self._tasks.values())

    def get_task(self, task_id):
        with self._lock:
            return self._tasks.get(task_id)

    def create_task(self, title):
        with self._lock:
            task_id = next(self._id_counter)
            task = {"id": task_id, "title": title, "completed": False}
            self._tasks[task_id] = task
            return task

    def update_task(self, task_id, title=None, completed=None):
        with self._lock:
            task = self._tasks.get(task_id)
            if not task:
                return None
            if title is not None:
                task["title"] = title
            if completed is not None:
                task["completed"] = completed
            return task

    def delete_task(self, task_id):
        with self._lock:
            return self._tasks.pop(task_id, None) is not None

    def reset(self):
        with self._lock:
            self._tasks.clear()
            self._id_counter = itertools.count(1)


# Module-level singleton -- simple and sufficient for this project's scope.
store = TaskStore()
