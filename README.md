# COMP0034 2025 Computer practicals - tutor solutions

The sub-packages are:

- `choropleth` : Dash app with London geojson file (small file size version) and choropleth map
- `dash_single`: Dash single page app from weeks 1-4
- `dash_multi`: Dash multipage app from week 1
- `data`: the database and data files
- `flask_para`: Flask activities in weeks 6-9 (SQLAlchemy from week 7 on)
- `flask_para_sq3`: Flask activities weeks 7-9 (sqlite3 instead of SQLAlchemy)

Run commands:

- `python3 src/choropleth/dash_choropleth.py`
- `python3 src/dash_single/para_dash.py`
- `python3 src/dash_multi/app_multi.py`
- `flask --app flask_para run --debug`

For the SQLite3 version you need
to [initialise the database](https://flask.palletsprojects.com/en/stable/tutorial/database/#initialize-the-database-file)
before running the app for the first time. Once the database is created in `instance/paralympics.sqlite` you don't need
to create it again.

1. Initialise the database: `flask --app flask_para_sq3 init-db`
2. Run the app: `flask --app flask_para_sq3 run --debug`
