from flask import Flask, render_template, request
import sqlite3
import pathlib
from pathlib import Path
import math

app = Flask(__name__)

cwd = Path.cwd()
db_name = 'Health.db'
file_path = cwd/db_name

@app.route('/')
def index():
    return render_template("index_fillin.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route("/data")
def data():

    con = sqlite3.connect(file_path)
    cursor = con.cursor()

    # Selecting the first 10 reords alone.
    Sleep_Health = cursor.execute(f"SELECT * FROM Sleep_Health ORDER BY 1 ASC LIMIT 10").fetchall()

    con.close()

    return render_template("data_table_fillin.html", students=Sleep_Health)

if __name__ == "__main__":
    app.run(debug=True)