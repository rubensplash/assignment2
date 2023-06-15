username = "splash"
password = "password@1"
attempts = 3

while attempts > 0:
    input_username = input("Enter your username: ")
    input_password = input("Enter your password: ")

    if input_username == username and input_password == password:
        print("Login successful!")
        break
    else:
        print("Invalid credentials. Please try again.")
        attempts -= 1

if attempts == 0:
    print("Login failed. Please contact the administrator.")
