import requests
import random
import string

# Define the URL of the form endpoint
url = 'http://127.0.0.1:5000/submit'  # Ensure it's the correct endpoint

def generate_random_name():
    first_name = ''.join(random.choices(string.ascii_uppercase, k=5))
    last_name = ''.join(random.choices(string.ascii_uppercase, k=5))
    return f'{first_name} {last_name}'

def generate_random_email():
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    domain = ''.join(random.choices(string.ascii_lowercase, k=5))
    return f'{username}@{domain}.com'

def generate_random_data():
    return {
        'name': generate_random_name(),  # Real name field
        'email': generate_random_email() # Real email field
    }

def fill_form():
    for _ in range(5):  # Number of random submissions
        data = generate_random_data()
        response = requests.post(url, data=data)
        print(f'Submitted data: {data}')
        print(f'Response: {response.status_code}')

if __name__ == '__main__':
    fill_form()
