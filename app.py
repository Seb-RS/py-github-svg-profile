from flask import Flask, make_response, request
from datetime import datetime
from modules.github_api import GitHubAPI
from modules.svg_generator import SVGGenerator

app = Flask(__name__)


@app.route("/<username>", methods=["GET"])
def svg_chart(username):
    try:
        api = GitHubAPI(username)
        current_year = datetime.now().year
        year = request.args.get("year") or current_year
        primary_color = request.args.get("primary_color") or "39d353"
        contributions_data = api.get_contributions(year)
        svg = SVGGenerator.generate_svg(
            username, year, contributions_data, primary_color
        )

        response = make_response(svg)
        response.headers["Content-Type"] = "image/svg+xml"

        return response
    except Exception as e:
        print(f"Error processing request: {e}")
        return "Internal Server Error", 500


if __name__ == "__main__":
    app.run(port=3000)
