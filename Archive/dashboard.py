from flask import Flask, render_template, request, redirect
import csv
import os
from collections import Counter
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import json

app = Flask(__name__)

data_file = 'data/submissions.csv'
spam_file = 'data/spams.csv'

# ... (your existing routes)


if __name__ == '__main__':
    app.run(debug=True)