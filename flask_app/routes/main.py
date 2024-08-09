from flask import render_template, request, redirect, url_for
from flask_app import app
from flask_app.models.badge import Badge
from flask_app.models.clause import Clause
from flask_app.config import SECTION_COLOURS


# Add sections to context for use in navbar
@app.context_processor
def set_global_html_variable_values():

    sections = [badge.section for badge in Badge.query.all()]
    unique_sections = list(dict.fromkeys(sections))

    badges = Badge.query.all()
    badges.sort(key=lambda x: x.name)

    template_config = {"section_names": unique_sections, "badges": badges}
    return template_config


# Render images from SVGs
@app.route("/static/badge_images/<filename>")
def get_image(filename):
    return "./static/badge_images" + filename


@app.route("/")
def home():
    return render_template("pages/home.html")


@app.route("/badges")
def all_badges():
    search = request.args.get("search")

    if search:
        badges = Badge.query.filter(Badge.name.contains(search)).all()
    else:
        badges = Badge.query.all()

    context = {"badges": badges, "search": search}
    return render_template("pages/badges.html", context=context)


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

    context = {
        "section": name,
        "badges": badges,
        "percentage": percentage,
        "colour": SECTION_COLOURS[name],
    }
    return render_template("pages/section.html", context=context)


@app.route("/badge/<id>", methods=["GET", "POST"])
def badge(id):
    if request.method == "POST":
        data = request.get_json()

        if "id" not in data:
            return "No id provided", 400

        badge = Badge.query.get(data["id"])
        badge.save_changes(data)

    badge = Badge.query.get(id)
    clauses = Clause.query.filter(Clause.badge_id == id).all()

    return render_template("pages/badge.html", badge=badge, clauses=clauses)


@app.route("/clause/<id>", methods=["POST"])
def clause(id):
    data = request.get_json()
    print(data)

    if "id" not in data:
        return "No id provided", 400

    clause = Clause.query.get(id)
    clause.save_changes(data)
    return redirect(url_for("badge", id=clause.badge_id))
