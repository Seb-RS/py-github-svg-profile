# py-github-svg-profile

A simple Python script to generate SVG GitHub contribution charts for a given user.

## Usage

The project utilizes the JSON data from [GitHub Skyline](https://skyline.github.com/) to generate SVG contribution charts.

### Parameters

- `/<username>`: Displays an SVG contribution chart for the provided user in the current year.
- `/<username>?year=<year>`: Displays an SVG contribution chart for the specified user and year.

Examples:

- `http://localhost:3000/seb-rs`: Shows GitHub contributions for the user "seb-rs" in the current year.
- `http://localhost:3000/seb-rs?year=2023`: Shows GitHub contributions for the user "seb-rs" in the year 2022.

## Installation

1. Clone the repository: `git clone https://github.com/yourusername/py-github-svg-profile.git`
2. Install dependencies: `pip install -r requirements.txt`

## Execution

1. Navigate to the project directory: `cd py-github-svg-profile`
2. Run the application: `python app.py`

The application will be available at `http://localhost:3000`.

## Contributions

Contributions are welcome! If you encounter any issues or have suggestions, feel free to open an issue or submit a pull request.
