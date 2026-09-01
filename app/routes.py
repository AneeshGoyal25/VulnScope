from flask import Blueprint, render_template, request
from .scanners.website_info import get_website_info

main = Blueprint("main", __name__)


@main.route("/", methods=["GET", "POST"])
def home():

    result = None

    if request.method == "POST":
        url = request.form["url"]
        result = get_website_info(url)

    return render_template("index.html", result=result)