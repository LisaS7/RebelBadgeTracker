from sqlalchemy import func
from flask import render_template
from flask_app import app
from flask_app.models.badge import Badge


# Add sections to context for use in navbar
@app.context_processor
def set_global_html_variable_values():

    sections = [badge.section for badge in Badge.query.all()]
    unique_sections = list(dict.fromkeys(sections))

    badges_names = [badge.name for badge in Badge.query.all()]
    badges_names.sort()

    template_config = {'section_names': unique_sections, 'badge_names': badges_names}
    return template_config


# Render images from SVGs
@app.route('/static/badge_images/<filename>')
def get_image(filename):
    return './static/badge_images' + filename


@app.route('/badges')
def all_badges():
    badges = Badge.query.all()
    in_progress_badges = [badge for badge in badges if not badge.complete]
    complete_badges = [badge for badge in badges if badge.complete]
    return render_template('badges.html', in_progress_badges=in_progress_badges, complete_badges=complete_badges)


@app.route('/section/<choice>')
def section(choice):
    print(choice)
    badges = Badge.query.filter(func.lower(Badge.section) == choice).all()
    return render_template('section.html', badges=badges, section=choice)
