from flask import Flask, render_template, redirect, request
import pandas as pd
import numpy as np
# import pickle

# Create an instance of Flask
app = Flask(__name__)

# Route to render index.html template
@app.route("/")
def home():
    # Return template and data
    return render_template("index.html")

# Route to render analysis.html template
@app.route("/analysis")
def analysis():
    # Return template and data
    return render_template("page/analysis.html")

# Route to render recommender.html template
@app.route("/recommender")
def recommender():
    # Return template and data
    return render_template("page/recommender.html")

# Route to render the-team.html template
@app.route("/the-team")
def team():
    # Return template and data
    return render_template("page/the-team.html")

# Route to render report.html template
@app.route("/report")
def report():
    # Return template and data
    return render_template("page/report.html")     

# Route to render works-cited.html template
@app.route("/works-cited")
def references():
    # Return template and data
    return render_template("page/works-cited.html")             

if __name__ == "__main__":
    app.run(debug=True)