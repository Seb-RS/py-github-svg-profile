from flask import Flask, make_response, request
import requests
from datetime import datetime

app = Flask(__name__)


def get_github_contributions(username, year=None):
    if year is None:
        current_year = datetime.now().year
        url = f"https://skyline.github.com/{username}/{current_year}.json"
    else:
        url = f"https://skyline.github.com/{username}/{year}.json"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        return data

    except requests.RequestException as e:
        print(f"GitHub API request error: {e}")
        raise


def generate_svg(username):
    try:
        year = request.args.get("year")
        contributions_data = get_github_contributions(username, year)

        total_commits = 0

        num_weeks = len(contributions_data["contributions"])
        svg_width = num_weeks * 12 + 27 + 20
        svg_height = 7 * 12 + 50 + 20

        svg = f"""
            <svg width="{svg_width}" height="{svg_height}" xmlns="http://www.w3.org/2000/svg">
                <rect width="{svg_width}" height="{svg_height}" fill="#f0f0f0"/>
        """

        for week_index, week in enumerate(contributions_data.get("contributions", [])):
            for day_index, day_commits in enumerate(week.get("days", [])):
                x = (week_index * 12) + 27
                y = (day_index * 12) + 20

                if "count" in day_commits:
                    if day_commits["count"] > 0:
                        color = f"rgb(0, {day_commits['count'] * 10}, 0)"
                    else:
                        color = "#fff"

                    svg += f"""
                        <rect x="{x}" y="{y}" width="10" height="10" fill="{color}" stroke="#fff"/>
                    """

                    total_commits += day_commits["count"]

        text_y = svg_height - 15
        svg += f"""
                <text x="{svg_width / 2}" y="{text_y}" font-family="Arial" font-size="14" fill="black" text-anchor="middle">
                    {username} has {total_commits} commits in {year}
                </text>
            </svg>
        """

        response = make_response(svg)
        response.headers["Content-Type"] = "image/svg+xml"

        return response

    except Exception as e:
        print(f"Error processing request: {e}")
        return "Internal Server Error", 500


@app.route("/<username>", methods=["GET"])
def svg_chart(username):
    return generate_svg(username)


if __name__ == "__main__":
    app.run(port=3000)
