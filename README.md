# COMP0034 2025 Computer practicals - tutor solutions

The sub-packages are:

- `dash_single_t`: Dash single page app from weeks 1-4
- `dash_multi_t`: Dash multipage app from week 1
- `data`: the database and data files
- `flask_para_t`: Flask activities in weeks 6-9 (SQLAlchemy from week 7 on)
- `flask_para_tsq3`: Flask activities weeks 7-9 (sqlite3 instead of SQLAlchemy)

Run commands:

`flask --app tutor.flask_para_t run --debug`

For the SQLite3 version you need
to [initialise the database](https://flask.palletsprojects.com/en/stable/tutorial/database/#initialize-the-database-file)
before running the app.

1. Initialise the database: `flask --app tutor.flask_para_tsq3 init-db`
2. Run the app: `flask --app tutor.flask_para_tsq3 run --debug`
