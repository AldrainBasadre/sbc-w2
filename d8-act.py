import os
folder = "log.txt"
def read():
    history = {}
    if os.path.exists(folder):
        file = open(folder, "r")
        for line in file:
            username,password = line.strip().split(",")
            history[username] = password
    return history
def save(history):
        file = open(folder, "w")
        for username,password in history.items():
            file.write(f"{username},{password}\n")  
def login(username, password):
    if not username in history:
        print(f"Username Not Found")
    elif history[username] == password:
        print(f"Login Successful")
    else:
        return f"Password Incorrect"
def register(username,password):
    if username in history:
        return f"Username Already Exist"
    else:
        history[username] = password
        save(history)
        return f"Register successful"
def change(username,password,npassword):
    if not username in history:
        print(f"Username Not Found")
    elif history[username] == password:
        history[username] = npassword
        save(history)
        return f"Password Change Successfully"
    else:
        return f"Password Incorrect" 
def main():
    global history
    history = read()
    while True:
        print(f"options:login,register,modify,exit")
        option = input("Enter: ").lower().strip()
        if option == "login":
            print(f"LOGIN")
            username = input("Username: ")
            password = input("Password: ")
            print(login(username, password))
        elif option == "register":
            username = input("Username: ")
            password = input("Password: ")
            print(register(username, password))
        elif option == "modify":
            username = input("Username: ")
            password = input("Password: ")
            npassword = input(f"New Password: ")
            print(change(username, password,npassword))
        elif option == "exit":
            print(f"System signing Off")
            break
        else:
            print(f"Invalid Credentials")      
if __name__ == "__main__":
    main()