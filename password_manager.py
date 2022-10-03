from cryptography.fernet import Fernet

def load_key():
    with open("key.key","rb") as f:
        return f.read()



key = load_key()
fer = Fernet(key)

# This is to generate key 
# def write_key():
#     key = Fernet.generate_key()
#     with open("key.key","wb") as key_file:
#         key_file.write(key)

# write_key()


    

def view():
    with open('passwords.txt','r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user,passw = data.split('|')
            print('Username: ',user,' Password: ',fer.decrypt(passw.encode()).decode())


def add():
    name = input('Account Name: ')
    pwd = input('Password: ')

    with open('passwords.txt', 'a') as f:
        f.write(name+"|"+fer.encrypt(pwd.encode()).decode()+"\n")


while True:
    mode = input(
        "Would you like to add a new password or view existing ones (view, add, q to quit)? : ").lower()
    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode")
        continue
