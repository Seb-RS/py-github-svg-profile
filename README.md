# py-github-svg-profile

A simple Python script to generate SVG GitHub contribution charts for a given user.

## Usage

The project utilizes the JSON data from [GitHub Skyline](https://skyline.github.com/) to generate SVG contribution charts.

### Parameters

- `/<username>`: Displays an SVG contribution chart for the provided user in the current year.
- `/<username>?year` (default: current year): Specifies the year for which the contribution chart should be generated.
- `/<username>?container_color` (default: "f7f7f7"): Specifies the background color of the SVG container.
- `/<username>?factor_color` (default: 0.9): Specifies the factor affecting the intensity of the container color. This parameter influences the visual representation of days without contributions, giving them a subdued appearance.
- `/<username>?primary_color` (default: "39d353"): Specifies the primary color used for the contribution chart.
- `/<username>?primary_text_color` (default: "000000"): Specifies the text color for primary elements in the chart.
- `/<username>?secondary_text_color` (default: "262626"): Specifies the text color for secondary elements in the chart.
- `/<username>?duration` (default: 1000): Specifies the duration of the animation in milliseconds.

Examples:

- `http://localhost:3000/Seb-RS`: Shows GitHub contributions for the user "Seb-RS" in the current year.
- `http://localhost:3000/Seb-RS?year=2023`: Shows GitHub contributions for the user "Seb-RS" in the year 2023.
- `http://127.0.0.1:3000/Seb-RS?year=2023&container_color=1c1b1b&factor_color=1.5&primary_color=2bffff&primary_text_color=ffffff&secondary_text_color=c3c3c3`: Shows GitHub contributions for the user "Seb-RS" in the year 2023 with custom colors.

## Installation

1. Clone the repository: `git clone https://github.com/Seb-RS/py-github-svg-profile.git`
2. Install dependencies: `pip install -r requirements.txt`

## Execution

1. Navigate to the project directory: `cd py-github-svg-profile`
2. Run the application: `python app.py`

The application will be available at `http://localhost:3000`.

## Contributions

Contributions are welcome! If you encounter any issues or have suggestions, feel free to open an issue or submit a pull request.
