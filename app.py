from datetime import datetime
from flask import Flask, render_template, request, redirect
import csv
import os
import pandas as pd
import plotly.graph_objects as go
import json
import plotly.utils
import requests



app = Flask(__name__)
data_file = 'data/submissions.csv'
spam_file = 'data/spams.csv'


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    real_id = request.form.get('dtx000')
    real_name = request.form.get('dtx001')
    real_option = request.form.get('dtx010')
    real_phone = request.form.get('dtx011')
    real_email = request.form.get('dtx100')
    real_review = request.form.get('dtx101')

    ip_address = request.remote_addr
    user_agent = request.headers.get('User-Agent')
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    hpot_id = request.form.get('id')
    hpot_name = request.form.get('name')
    hpot_option = request.form.get('option')
    hpot_phone = request.form.get('phone')
    hpot_email = request.form.get('email')
    hpot_review = request.form.get('review')

    if (hpot_id or hpot_name or hpot_option or
        hpot_phone or hpot_email or hpot_review):
        print("HoneyPot triggered! Potential spam detected.")
        with open(spam_file, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([
                timestamp,
                ip_address,
                user_agent,
                hpot_id,
                hpot_name,
                hpot_option,
                hpot_phone,
                hpot_email,
                hpot_review
            ])
        return redirect('/')

    with open(data_file, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([real_id, real_name, real_option, real_phone, real_email, real_review])
    return "Form submitted successfully!"

# @app.route('/dashboard')
# def dashboard():
#     try:
#         # Read data files
#         authentic_df = pd.read_csv(data_file)
#         spam_df = pd.read_csv(spam_file)
        
#         # Spam vs. Authentic
#         total_submissions = len(authentic_df) + len(spam_df)
#         spam_count = len(spam_df)
#         authentic_count = len(authentic_df)
#         spam_chart = go.Figure(data=[go.Pie(labels=['Authentic', 'Spam'], values=[authentic_count, spam_count])])
#         spam_chart_json = json.dumps(spam_chart, cls=plotly.utils.PlotlyJSONEncoder)
        
#         # Authentic Data Table
#         authentic_data = authentic_df.to_dict('records')
        
#         # Bot Data Table
#         bot_data = spam_df[['Timestamp', 'IP Address', 'User Agent']].to_dict('records')
        
#         return render_template('dashboard.html',
#                                spam_chart=spam_chart_json,
#                                authentic_data=authentic_data,
#                                bot_data=bot_data)
    
#     except Exception as e:
#         return str(e)
# def get_geo_data(ip_addresses):
#     # Replace with your preferred geolocation API
#     url = "http://ip-api.com/json/"
#     locations = []
#     for ip in ip_addresses:
#         response = requests.get(url + ip)
#         data = response.json()
#         if data['status'] == 'success':
#             locations.append({
#                 'ip': ip,
#                 'lat': data['lat'],
#                 'lon': data['lon'],
#                 'city': data['city'],
#                 'country': data['country']
#             })
#     return locations

# @app.route('/dashboard')
# def dashboard():
#     try:
#         # Read data files
#         authentic_df = pd.read_csv(data_file)
#         spam_df = pd.read_csv(spam_file)
        
#         # Debug: Print dataframes to verify contents
#         print("Authentic DataFrame:\n", authentic_df.head())
#         print("Spam DataFrame:\n", spam_df.head())
        
#         # Spam vs. Authentic
#         total_submissions = len(authentic_df) + len(spam_df)
#         spam_count = len(spam_df)
#         authentic_count = len(authentic_df)
#         spam_chart = go.Figure(data=[go.Pie(labels=['Authentic', 'Spam'], values=[authentic_count, spam_count])])
#         spam_chart_json = json.dumps(spam_chart, cls=plotly.utils.PlotlyJSONEncoder)
        
#         # Authentic Data Table
#         authentic_data = authentic_df.to_dict('records')
        
#         # Bot Data Table
#         bot_data = spam_df[['Timestamp', 'IP Address', 'User Agent']].to_dict('records')
        
#         # Debug: Print data to be passed to template
#         print("Authentic Data:", authentic_data)
#         print("Bot Data:", bot_data)
        
        
#         return render_template('dashboard.html',
#                                spam_chart=spam_chart_json,
#                                authentic_data=authentic_data,
#                                bot_data=bot_data)
    
#     except Exception as e:
#         return str(e)



# def get_geo_data(ip_addresses):
#     url = "http://ip-api.com/json/"
#     locations = []
#     for ip in ip_addresses:
#         response = requests.get(url + ip)
#         data = response.json()
#         locations.append({
#                 'ip': ip,
#                 'lat': data.get('lat', 'N/A'),
#                 'lon': data.get('lon', 'N/A'),
#                 'city': data.get('city', 'N/A'),
#                 'country': data.get('country', 'N/A')})
#         # if data.get('status') == 'fail':
#         #     locations.append({
#         #         'ip': ip,
#         #         'lat': 'N/A',
#         #         'lon': 'N/A',
#         #         'city': 'N/A',
#         #         'country': 'N/A'
#         #     })
#         # else:
#         #     locations.append({
#         #         'ip': ip,
#         #         'lat': data.get('lat', 'N/A'),
#         #         'lon': data.get('lon', 'N/A'),
#         #         'city': data.get('city', 'N/A'),
#         #         'country': data.get('country', 'N/A')
#         #     })
#     return locations

@app.route('/dashboard')
def dashboard():
    try:
        # Read data files
        authentic_df = pd.read_csv(data_file)
        spam_df = pd.read_csv(spam_file)
        
        # Extract IP addresses
        ip_addresses = spam_df['IP Address'].unique()
        

        # Spam vs. Authentic
        total_submissions = len(authentic_df) + len(spam_df)
        spam_count = len(spam_df)
        authentic_count = len(authentic_df)
        spam_chart = go.Figure(data=[go.Pie(labels=['Authentic', 'Spam'], values=[authentic_count, spam_count])])
        spam_chart_json = json.dumps(spam_chart, cls=plotly.utils.PlotlyJSONEncoder)
        
        # Authentic Data Table
        authentic_data = authentic_df.to_dict('records')
        
        # Bot Data Table with geo data
        bot_data = spam_df[['Timestamp', 'IP Address', 'User Agent']].to_dict('records')
        
        return render_template('dashboard.html',
                               spam_chart=spam_chart_json,
                               authentic_data=authentic_data,
                               bot_data=bot_data)
    
    except Exception as e:
        return str(e)


if __name__ == '__main__':
    if not os.path.exists('data'):
        os.makedirs('data')

    if not os.path.isfile(data_file):
        with open(data_file, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['ID', 'Name', 'Rating', 'Phone', 'Email', 'Review'])

    if not os.path.isfile(spam_file):
        with open(spam_file, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([
                'Timestamp', 
                'IP Address', 
                'User Agent', 
                'hpot ID', 
                'hpot Name', 
                'hpot Option', 
                'hpot Phone', 
                'hpot Email', 
                'hpot Review'
            ])

    app.run(debug=True)
