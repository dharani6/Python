from flask import Blueprint, request, jsonify, render_template
from .models import store

bp = Blueprint("main", __name__)


@bp.route("/")
def index():
    return render_template("index.html")


@bp.route("/api/tasks", methods=["GET"])
def list_tasks():
    return jsonify(store.list_tasks()), 200


@bp.route("/api/tasks", methods=["POST"])
def create_task():
    data = request.get_json(silent=True) or {}
    title = str(data.get("title", "")).strip()
    if not title:
        return jsonify({"error": "title is required"}), 400
    task = store.create_task(title)
    return jsonify(task), 201


@bp.route("/api/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    task = store.get_task(task_id)
    if not task:
        return jsonify({"error": "task not found"}), 404
    return jsonify(task), 200


@bp.route("/api/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    data = request.get_json(silent=True) or {}
    if "title" in data and not str(data["title"]).strip():
        return jsonify({"error": "title cannot be empty"}), 400
    task = store.update_task(
        task_id,
        title=data.get("title"),
        completed=data.get("completed"),
    )
    if not task:
        return jsonify({"error": "task not found"}), 404
    return jsonify(task), 200


@bp.route("/api/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    deleted = store.delete_task(task_id)
    if not deleted:
        return jsonify({"error": "task not found"}), 404
    return "", 204


@bp.route("/api/tasks/reset", methods=["POST"])
def reset_tasks():
    """Test-only helper endpoint: gives every test a clean slate."""
    store.reset()
    return "", 204
