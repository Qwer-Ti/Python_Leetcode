import os

def admin():
    print("Which action you would like to perform? Choose one")
    choice = input(" A - manage admin access\n B -  manage currencies \n     ").upper()
    if choice == "A":
        try:
            sec_choice = int(input("Choose the action you would like to perform: \n 1 - add new password \n 2 - delete existing password \n"))
            if sec_choice == 1:
                f = open("C:\\Users\\ti\\Desktop\\LFA.Labs\\Python_Leetcode\\currency converter\\passwords.txt")
                new_pas = input("Input new password \n")
                f.writelines(new_pas)
                f.close()
            elif sec_choice == 2:
                deleting = input("type password you would like to delete \n")
                with open("C:\\Users\\ti\\Desktop\\LFA.Labs\\Python_Leetcode\\currency converter\\passwords.txt", "r") as f:
                    lines = f.readlines()
                with open("C:\\Users\\ti\\Desktop\\LFA.Labs\\Python_Leetcode\\currency converter\\passwords.txt", "w") as f:
                    for line in lines:
                        if line.strip("\n") != deleting:
                            f.write(line)
            else:
                print("Print 1 or 2")
        except Exception:
            print("type a digit")


def login():
    f = open("C:\\Users\\ti\\Desktop\\LFA.Labs\\Python_Leetcode\\currency converter\\passwords.txt")
    print("Do you wish to access converter?")
    a = input("                     ")
    if a in f:
        admin()
    else:
        converter(ISO)
    f.close()
    
def converter(ISO):
    currency1 = input("Input the first currency code \n").upper()
    currency2 = input("Input second currency code \n").upper()
    if currency1 in ISO.keys() and currency2 in ISO.keys():
        amount = float(input(f'Whats the amount of {currency1}?'))
        converted_value = amount * ISO[currency2] * ISO[currency1]
        print(f"{amount} {currency1} is {converted_value:.2f} {currency2}")
    else:
        print('Input actual ISO')



ISO = {'USD' : 1, 'EUR' :0.92, 'JPY': 0.0062, 'GBP' : 1.28, 'AUD': 0.67, 'CAD': 0.73, 'CHF':1.11, 'CNY':0.14, 'SEK':0.095, 'NZD':0.61}

login()