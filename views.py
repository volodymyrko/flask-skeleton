from flask import Blueprint, redirect


bp = Blueprint('views', __name__)


@bp.route('/')
def index():
    return 'it works'
