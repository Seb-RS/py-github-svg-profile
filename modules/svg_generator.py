from modules.color import Color

class SVGGenerator:
    @staticmethod
    def generate_svg(username, year, contributions_data, global_color="#39d353"):
        try:
            total_commits = 0

            num_weeks = len(contributions_data["contributions"])
            svg_width = num_weeks * 12 + 27 + 20
            svg_height = 7 * 12 + 50 + 20

            max_commits = contributions_data["max"]
            p80_commits = contributions_data["p80"]
            p90_commits = contributions_data["p90"]
            p99_commits = contributions_data["p99"]

            svg = f"""
                <svg width="{svg_width}" height="{svg_height}" xmlns="http://www.w3.org/2000/svg">
                    <rect width="{svg_width}" height="{svg_height}" fill="#f7f7f7"/>
            """

            for week_index, week in enumerate(
                contributions_data.get("contributions", [])
            ):
                for day_index, day_commits in enumerate(week.get("days", [])):
                    x = (week_index * 12) + 27
                    y = (day_index * 12) + 20

                    if "count" in day_commits:
                        if day_commits["count"] > 0:
                            commit_percentage = (
                                day_commits["count"] / max_commits
                            ) * 100

                            if commit_percentage >= p99_commits:
                                color = global_color
                            elif commit_percentage >= p90_commits:
                                color = Color.darken(global_color, 0.8)
                            elif commit_percentage >= p80_commits:
                                color = Color.darken(global_color, 0.6)
                            else:
                                color = Color.darken(global_color, 0.4)

                        else:
                            color = "#eeeeee"

                        svg += f"""
                            <rect x="{x}" y="{y}" width="10" height="10" fill="{color}" rx="2" ry="2"/>
                        """

                        total_commits += day_commits["count"]

            text_y = svg_height - 15
            svg += f"""
                    <text x="{svg_width / 2}" y="{text_y}" font-family="Arial" font-size="14" fill="black" text-anchor="middle">
                        {username} has {total_commits} commits in {year}
                    </text>
                </svg>
            """

            return svg
        except Exception as e:
            print(f"Error generating SVG: {e}")
            raise
