import requests
import random
import string

def generate_random_name():
    first_name = ''.join(random.choices(string.ascii_uppercase, k=5))
    last_name = ''.join(random.choices(string.ascii_uppercase, k=5))
    return f'{first_name} {last_name}'

def generate_random_email():
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    domain = ''.join(random.choices(string.ascii_lowercase, k=5))
    # domain = "gmail"
    return f'{username}@{domain}.com'

def generate_random_phone():
    return ''.join(random.choices(string.digits, k=10))
    
def generate_random_id():
    return ''.join(random.choices(string.digits, k=5))

def generate_random_password(length=10):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choices(characters, k=length))

def generate_random_review():
    reviews = [
        "Excellent service, highly recommend!",
        "Not satisfied with the product quality.",
        "Great experience, will come back again.",
        "Average service, could be better.",
        "Amazing product, very happy with the purchase!"
    ]
    return random.choice(reviews)

def generate_random_option(options):
    return random.choice(options)

def generate_random_data():
    return {
        'id': generate_random_id(),
        'name': generate_random_name(),
        'option': generate_random_option(['excellent', 'good', 'average','poor']), 
        'phone': generate_random_phone(),
        'email': generate_random_email(),
        'review': generate_random_review(),
        'password': generate_random_password()
        
        
    }

def fill_form(url, entries):
    for _ in range(entries):
        data = generate_random_data()
        try:
            response = requests.post(url, data=data, timeout=10)
            print(f'Submitted data: {data}')
            print(f'Response: {response.status_code}')
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

def main():
    ascii_art = r"""
     ______                        _____                          ___   __  __             __  
   / ____/___  _________ ___     / ___/____  ____ _____ ___     /   | / /_/ /_____ ______/ /__
  / /_  / __ \/ ___/ __ `__ \    \__ \/ __ \/ __ `/ __ `__ \   / /| |/ __/ __/ __ `/ ___/ //_/
 / __/ / /_/ / /  / / / / / /   ___/ / /_/ / /_/ / / / / / /  / ___ / /_/ /_/ /_/ / /__/ ,<   
/_/    \____/_/  /_/ /_/ /_/   /____/ .___/\__,_/_/ /_/ /_/  /_/  |_\__/\__/\__,_/\___/_/|_|  
                                   /_/                                                        
"""
    print(ascii_art)
    print("Form Bulk Spam Bot")
    url = input("url_endpoint: ")
    # url = 'http://127.0.0.1:5000/submit'  # Ensure it's the correct endpoint
    try:
        entries = int(input("entries: "))
    except ValueError:
        print("Please enter a valid number")
        return
    
    fill_form(url, entries)
    print("Done ;) ")


if __name__ == '__main__':
    main()
