from sqlalchemy import func
from flask import render_template
from flask_app import app
from flask_app.models.badge import Badge
from flask_app.models.clause import Clause
from flask_app.utils.sections_chart import make_sections_chart


# Add sections to context for use in navbar
@app.context_processor
def set_global_html_variable_values():

    sections = [badge.section for badge in Badge.query.all()]
    unique_sections = list(dict.fromkeys(sections))

    badges = Badge.query.all()
    badges.sort(key=lambda x: x.name)

    template_config = {'section_names': unique_sections, 'badges': badges}
    return template_config


# Render images from SVGs
@app.route('/static/badge_images/<filename>')
def get_image(filename):
    return './static/badge_images' + filename

@app.route('/')
def home():
    return render_template('pages/home.html')


@app.route('/badges')
def all_badges():
    badges = Badge.query.all()
    in_progress_badges = [badge for badge in badges if not badge.complete]
    complete_badges = [badge for badge in badges if badge.complete]
    return render_template('pages/badges.html', in_progress_badges=in_progress_badges, complete_badges=complete_badges)


@app.route('/section/<choice>')
def section(choice):
    badges = Badge.query.filter(func.lower(Badge.section) == choice).all()
    chart = make_sections_chart()
    return render_template('pages/section.html', badges=badges, section=choice, chart=chart)


@app.route('/badge/<id>')
def badge(id):
    badge = Badge.query.get(id)
    clauses = Clause.query.filter(Clause.badge_id==id).all()
    return render_template('pages/badge.html', badge=badge, clauses=clauses)