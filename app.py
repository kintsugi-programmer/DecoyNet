from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)
data_file = 'data/submissions.csv'
spam_file = 'data/spams.csv'

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    real_name = request.form.get('nameksljf')
    real_email = request.form.get('emaillkjkl')
    honeypot_name = request.form.get('name')
    honeypot_email = request.form.get('email')

    if honeypot_name or honeypot_email:
        print("Honeypot triggered! Potential spam detected.")
        # Save spam data to a separate file
        with open(spam_file, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([honeypot_name, honeypot_email])
        return redirect('/')

    # Save real form data to submissions file
    with open(data_file, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([real_name, real_email])

    return "Form submitted successfully!"

if __name__ == '__main__':
    # Ensure the header rows are added (only when the file is first created)
    # Note: Files will be created automatically when the first write occurs
    with open(data_file, 'a', newline='') as file:
        if file.tell() == 0:  # Check if the file is empty
            writer = csv.writer(file)
            writer.writerow(['Name', 'Email'])

    with open(spam_file, 'a', newline='') as file:
        if file.tell() == 0:  # Check if the file is empty
            writer = csv.writer(file)
            writer.writerow(['Honeypot Name', 'Honeypot Email'])

    app.run(debug=True)
