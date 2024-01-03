from modules.color import Color


class SVGGenerator:
    @staticmethod
    def generate_svg(username, year, contributions_data, global_color, duration):
        try:
            total_commits = 0

            num_weeks = len(contributions_data["contributions"])
            svg_width = num_weeks * 12 + 27 + 20
            svg_height = 7 * 12 + 50 + 20

            p80_commits = contributions_data["p80"]
            p90_commits = contributions_data["p90"]
            p99_commits = contributions_data["p99"]

            github_icon_svg = f"""
                <svg width="20" height="20" viewBox="0 0 16 16" fill="black">
                    <path d="M8 0c4.42 0 8 3.58 8 8a8.013 8.013 0 0 1-5.45 7.59c-.4.08-.55-.17-.55-.38 0-.27.01-1.13.01-2.2 0-.75-.25-1.23-.54-1.48 1.78-.2 3.65-.88 3.65-3.95 0-.88-.31-1.59-.82-2.15.08-.2.36-1.02-.08-2.12 0 0-.67-.22-2.2.82-.64-.18-1.32-.27-2-.27-.68 0-1.36.09-2 .27-1.53-1.03-2.2-.82-2.2-.82-.44 1.1-.16 1.92-.08 2.12-.51.56-.82 1.28-.82 2.15 0 3.06 1.86 3.75 3.64 3.95-.23.2-.44.55-.51 1.07-.46.21-1.61.55-2.33-.66-.15-.24-.6-.83-1.23-.82-.67.01-.27.38.01.53.34.19.73.9.82 1.13.16.45.68 1.31 2.69.94 0 .67.01 1.3.01 1.49 0 .21-.15.45-.55.38A7.995 7.995 0 0 1 0 8c0-4.42 3.58-8 8-8Z"></path>
                </svg>
            """

            svg = f"""
                <svg width="{svg_width}" height="{svg_height}" xmlns="http://www.w3.org/2000/svg">
                    <rect width="{svg_width}" height="{svg_height}" fill="#f7f7f7"/>
                    <style>
                        .commit-rect {{
                            transition: opacity 0.5s ease-in-out;
                            opacity: 0;
                        }}
                        
                        .commit-text {{
                            transition: opacity 0.5s ease-in-out;
                            opacity: 0;
                        }}
                    </style>
            """

            for week_index, week in enumerate(
                contributions_data.get("contributions", [])
            ):
                is_first_week = week_index == 0

                for day_index, day_commits in enumerate(week.get("days", [])):
                    x = (week_index * 12) + 27

                    y_adjustment = (7 - len(week["days"])) * 12 if is_first_week else 0
                    y = (day_index * 12) + 20 + y_adjustment

                    if "count" in day_commits:
                        if day_commits["count"] > 0:
                            if day_commits["count"] >= p99_commits:
                                color = f"""#{global_color}"""
                            elif day_commits["count"] >= p90_commits:
                                color = Color.darken(global_color, 0.8)
                            elif day_commits["count"] >= p80_commits:
                                color = Color.darken(global_color, 0.6)
                            else:
                                color = Color.darken(global_color, 0.4)

                        else:
                            color = "#eeeeee"

                        svg += f"""
                            <rect class="commit-rect" x="{x}" y="{y}" width="10" height="10" fill="{color}" rx="2" ry="2"/>
                        """

                        total_commits += day_commits["count"]

            peer_index_duration = duration / 365

            text_y = svg_height - 15
            svg += f"""
                   <g>
                        <foreignObject id="github-icon" class="commit-text" x="{27}" y="{text_y - 15}" width="20" height="20">
                            {github_icon_svg}
                        </foreignObject>
                        <text id="username-text" class="commit-text" x="{27+20+5}" y="{text_y}" font-family="Arial" font-size="14" fill="black" font-weight="bold">
                            {username}
                        </text>
                        <text id="contributions-text" class="commit-text" x="{svg_width-25}" y="{text_y}" font-family="Arial" font-size="14" text-anchor="end" fill="black">
                            {total_commits} contributions in {year}
                        </text>
                    </g>
                    <script>
                        setTimeout(() => {{
                            const commitRects = document.querySelectorAll('.commit-rect');
                            const githubIconElement = document.getElementById('github-icon');
                            const usernameTextElement = document.getElementById('username-text');
                            const contributionsTextElement = document.getElementById('contributions-text');

                            commitRects.forEach((rect, index) => {{
                                setTimeout(() => {{
                                    rect.style.opacity = '1';
                                }}, index * {peer_index_duration});
                            }});
                            
                            setTimeout(() => {{
                                githubIconElement.style.opacity = '1';
                                usernameTextElement.style.opacity = '1';
                                contributionsTextElement.style.opacity = '1';
                            }}, {duration});
                        }}, 100);
                    </script>
                </svg>
            """

            return svg
        except Exception as e:
            print(f"Error generating SVG: {e}")
            raise
