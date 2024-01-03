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
        container_color = request.args.get("container_color") or "f7f7f7"
        factor_color = request.args.get("factor_color") or 0.9
        primary_color = request.args.get("primary_color") or "39d353"
        primary_text_color = request.args.get("primary_text_color") or "000000"
        secondary_text_color = request.args.get("secondary_text_color") or "262626"
        duration = request.args.get("duration") or 1000
        contributions_data = api.get_contributions(year)
        svg = SVGGenerator.generate_svg(
            username,
            year,
            contributions_data,
            container_color,
            float(factor_color),
            primary_color,
            primary_text_color,
            secondary_text_color,
            int(duration),
        )

        response = make_response(svg)
        response.headers["Content-Type"] = "image/svg+xml"

        return response
    except Exception as e:
        print(f"Error processing request: {e}")
        return "Internal Server Error", 500


if __name__ == "__main__":
    app.run(port=3000)
