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
    return render_template("homepage.html")

# Route to render analysis.html template
@app.route("/analysis")
def analysis():
    # Return template and data
    return render_template("analysis.html")

# Route to render analysis.html template
@app.route("/recommender")
def recommender():
    # Return template and data
    return render_template("recommender.html")

# Route to render analysis.html template
@app.route("/the-team")
def team():
    # Return template and data
    return render_template("the-team.html")

# Route to render analysis.html template
@app.route("/works-cited")
def references():
    # Return template and data
    return render_template("works-cited.html")             

if __name__ == "__main__":
    app.run()