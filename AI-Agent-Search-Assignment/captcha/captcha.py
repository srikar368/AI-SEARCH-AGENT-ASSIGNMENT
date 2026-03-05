import random
import string

def generate_captcha(length=6):

    characters = string.ascii_letters + string.digits
    captcha = ''.join(random.choice(characters) for i in range(length))

    return captcha


def captcha_verification():

    captcha = generate_captcha()

    print("CAPTCHA:", captcha)

    user_input = input("Enter CAPTCHA: ")

    if user_input == captcha:
        print("Verification Successful. Human detected.")
    else:
        print("Verification Failed. Try Again.")


captcha_verification()