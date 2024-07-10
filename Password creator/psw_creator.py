import random

def create():
    f = open("C:\\Users\\ti\\Desktop\\LFA.Labs\\Python_Leetcode\\Password creator\\passwords.txt", "a")
    password = ""
    characters = "abcdefghijklmnopqrstuwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    site = input("what application this password will be for? This Information will be stored in a file ")
    psw_len = input("How long the password should be? ")
    psw_len = int(psw_len)
    for i in range(psw_len):
        password = password + random.choice(characters)
    print(f"Your password for {site} is : {password}")
    f.write(site + " - " + password)
    f.close()
    

def repeat():
    a = input("Do you want a new password? Y/N ")
    a = a.upper()
    if a == "Y":
        return True
    else:
        return False
    

if __name__ == '__main__':
    while repeat() == True:
        create()




    

    