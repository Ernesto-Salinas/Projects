password="ucertify"
valid = False
while not valid:
    user_pass = input()
    if user_pass == password:
        print("Welcome Back")
        valid = True
    else:
        print("Error")