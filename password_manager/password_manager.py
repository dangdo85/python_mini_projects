# allows you to encrypt text
from cryptography.fernet import Fernet

# CREATE KEY
# def write_key():
#     key = Fernet.generate_key()
#     with open("password_manager/key.key", "wb") as key_file:
#         key_file.write(key)

# write_key()

# ACCESS KEY
def load_key():
    file = open("password_manager/key.key", "rb")
    key = file.read()
    file.close()
    return key

# master_pwd = input("What is the master password? ")

# use ".encode" since key is in bytes therefore master_pwd needs to be converted to bytes
key = load_key()
fer = Fernet(key)


def view():
    with open('password_manager/passwords.txt', 'r') as f:
        for line in f.readlines():
            # 'rstrip' strip \n from lines
            data = line.rstrip()
            # split the string by "|" and return in list []
            # since we will only have name and password, the list [] will only have 2 elements
            # those elements are assigned to 'user' and 'passw'
            user, passw = data.split("|")
            print("User:", user, "| Password:", fer.decrypt(passw.encode()).decode())

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    # "with" will open the file then automatically close when done
    # 'a' (append) mode - create file if does not exist and add new something to the end
    # 'w' (write) mode - overwrite the file with new thing
    # 'r' (read) mode - read only mode
    with open('password_manager/passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

while True:
    mode = input("Would you like to add a new password or view existing ones (view, add), press q to quit? ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue