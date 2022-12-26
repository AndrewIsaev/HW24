import os

from flask import Blueprint, request, abort

from utils import execute

perform_query_blueprint = Blueprint("perform_query", __name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")


@perform_query_blueprint.post("/perform_query")
def perform_query():
    # Check request
    data = request.json
    if "query" not in data.keys() or "file_name" not in data.keys():
        abort(400, description="Check query or filename")
    # Check filename
    filename = os.path.join(DATA_DIR, data["file_name"])
    if not os.path.exists(filename):
        abort(400, "File is not exist")

    query = data["query"]
    return execute(query, filename)
