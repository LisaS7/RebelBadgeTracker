from flask import request, redirect, url_for, jsonify
from flask_app import app
from flask_app.models.badge import Badge
from flask_app.models.clause import Clause
from flask_app.config import SECTION_PATCHES


# Render images from SVGs
@app.route("/static/badge_images/<filename>")
def get_image(filename):
    return "./static/badge_images" + filename


@app.route("/patches")
def home():
    badges = Badge.query.all()
    badges = [badge for badge in badges if badge.rating != "✖️"]

    patch_data = {
        section: [
            badge.section
            for badge in badges
            if badge.complete and badge.section == section
        ]
        for section in SECTION_PATCHES
    }

    for section, count in SECTION_PATCHES.items():
        while len(patch_data[section]) < count:
            patch_data[section].append(f"dark_{section}")

    return jsonify({"patches": patch_data})


@app.route("/badges")
def all_badges():
    badges = Badge.query.all()
    json_badges = list(map(lambda x: x.to_json(), badges))
    return jsonify(json_badges)


@app.route("/sections")
def all_sections():
    badges = Badge.query.all()
    sections = list(set([badge.section for badge in badges]))
    return jsonify(sections)


@app.route("/section/<choice>")
def section(choice):
    name = choice.title()
    search = request.args.get("search")

    if search:
        badges = Badge.query.filter(
            Badge.section == name, Badge.name.contains(search)
        ).all()
    else:
        badges = Badge.query.filter(Badge.section == name).all()

    if badges:
        percentage = (
            [badge.complete for badge in badges].count(True) / len(badges) * 100
        )
    else:
        percentage = 0

    context = {"section": name, "badges": badges, "percentage": percentage}
    return None


@app.route("/badge/<id>", methods=["GET", "POST"])
def badge(id):
    if request.method == "POST":
        data = request.get_json()

        if "id" not in data:
            return "No id provided", 400

        badge = Badge.query.get(data["id"])

        field = [key for key in data if key != "id"]
        if not hasattr(badge, field[0]):
            return "Field is invalid", 400

        badge.save_changes(data)

    badge = Badge.query.get(id)
    clauses = Clause.query.filter(Clause.badge_id == id).all()
    clauses_json = [clause.to_json() for clause in clauses]

    return jsonify({"badge": badge.to_json(), "clauses": clauses_json})


@app.route("/clause/<id>", methods=["POST"])
def clause(id):
    data = request.get_json()

    if "id" not in data:
        return "No id provided", 400

    clause = Clause.query.get(id)
    clause.save_changes(data)
    return redirect(url_for("badge", id=clause.badge_id))
