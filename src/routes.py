from flask import current_app as app, render_template, request, make_response, jsonify

from src.util import dh


@app.route('/')
def index():
    return render_template("index.html", goals=dh.get_goals())


@app.route("/new", methods=["POST"])
def new():
    name = request.json.get("name")
    id_ = int(request.json.get("id"))
    if not name or not id_:
        return make_response(jsonify({}), 400)
    goals = dh.add_goal({"name": name, "id": id_})
    return make_response(jsonify(goals), 200)


@app.route("/done", methods=["POST"])
def done():
    id_ = request.json.get("id")
    if not id_:
        return make_response(jsonify([]), 400)
    id_ = int(id_)
    goals = dh.remove_goal(dh.get_goal(id_))
    return make_response(jsonify(goals), 200)