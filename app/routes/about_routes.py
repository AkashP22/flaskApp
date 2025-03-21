from flask import Blueprint

bp = Blueprint('about', __name__)

@bp.route('/about')
def about():
    return "About Page"