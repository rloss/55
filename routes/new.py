from flask import Blueprint, render_template

lab_bp = Blueprint('new', __name__)

@home_bp.route("/new")
def new():
    return render_template("new.html")