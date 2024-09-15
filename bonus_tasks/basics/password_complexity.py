while True:
    password = input("Enter your password: ")

    if password == 'exit':
        break

    # Rules: more than 8 characters, at least 1 digit, at least 1 upper case letter

    res_digit = False
    res_upper = False
    for item in password:
        if item.isdigit():
            res_digit = True
        elif item.isupper():
            res_upper = True

    if len(password) >= 8 and res_digit and res_upper:
        print("The password is strong!")
    else:
        print("The password is weak!")
