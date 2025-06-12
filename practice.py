print("Hello to my Simple Login Register Program")

select0 = ""

#Function
def login():
    if user_name in usernames:
            index = usernames.index(user_name)
            if passwords[index] == password:
                print("Login successful")
            else:
                print("Wrong password.")
    else:
        print("Username not found.")

def auth():
        if new_user in usernames:
            print("Username already exists.")
        else:
            usernames.append(new_user)
            passwords.append(new_pass)
            print("Account created successfully.")


##Start
usernames = ["admin"]
passwords = ["admin"]
while select0 != "3":
    select0 = input("Press \n[1]: Login\n[2]: Create Account\n[3]: Quit\n")

    if select0 == "1":
        user_name = input("Username: ")
        password = input("Password: ")
        login()


    elif select0 == "2":
        new_user = input("Enter new username: ")
        new_pass = input("Enter new password: ")
        auth()


    elif select0 == "3":
        print("Quitting program.")
    else:
        print("Invalid choice. Please try again.")

