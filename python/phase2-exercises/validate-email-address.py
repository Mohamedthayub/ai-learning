def validateEmail(email):
    if not email:
        print("Provide email address")
        return False
    return True


if(validateEmail("")):
    print("Email is Valid")

else:
    print("Email  is Invalid")