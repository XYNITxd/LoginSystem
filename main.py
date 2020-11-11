import json

ec = input("Do you have an existing account?(y/n) ")
if ec.lower() == "y":
    login = input("Would you like to login?(y/n) ")
    if login.lower() == "y":
        un = input("Username: ")
        try:
            pw = input("Password: ")
            with open(f"{un}.json", 'r') as r:
                read = r.read()
                rr = json.loads(read)
                pw_check = rr['Password']
                if pw_check == pw:
                    print("Successfully logged in.")
                else:
                    print("Incorrect password.")
        except:
            print(f"There is no account registered under {un}")
    elif login.lower() == "n":
        print("Quitting program.")
    else:
        print(f"{login} is not a valid answer.")
elif ec.lower() == "n":
    reg = input("Would you like to create an account?(y/n) ")
    if reg.lower() == "y":
        un = input("Username: ")
        email = input("Email adress: ")
        pw = input("Password: ")
        pw2 = input("Confirm your password: ")
        if pw == pw2:
            w = open(f"{un}.json", "w")
            reg_json = {
                "Username": un,
                "Email adress": email,
                "Password": pw
            }
            reg_json = json.dumps(reg_json, indent = 4)
            w.write(reg_json)
        else:
            print("Passwords do not match.")
    elif reg.lower() == "n":
        print("Quitting program.")
    else:
        print(f"{reg} is not a valid answer.")
else:
    print(f"{ec} is not a valid answer.")
