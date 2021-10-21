def ListInfo(info):
    if len (info) == 0:
        print("there is no info in this list. \n")
        return
    else:
        i = 0
        for row in info:
            print("["+str(i)+"]"+"\t"+ row[0] +"\t"+ row[1] +" \t"+ row[2])
            i += 1
        print()

def InputInfo(info):
    username = input("Enter your username: ")
    password = input("Enter you password: ")
    location = input("Enter where you use this information: ")
    infoList = []
    infoList.append(username)
    infoList.append(password)
    infoList.append(location)
    info.append(infoList)

def DeleteInfo(info):
    ListInfo(info)
    while True:
        try:
            number = int(input("Enter the number you want to delete (Enter zero to exit): "))
            break
        except ValueError:
            print("Please input an integer only...")  
            continue
    if number < 0 or number > len(info):
        print("Invalid number. \n")
    elif number == 0:
        return
    else:
        num = info.pop(number)
        print("Your username and password for "+num[2]+" was deleted")

def EditInfo(info):
    ListInfo(info)
    while True:
        try:
            number = int(input("Enter the number you want to edit (Enter zero to exit): "))
            break
        except ValueError:
            print("Please input an integer only...")
            continue
    if number < 0 or number > len(info):
        print("Invalid Number. \n")
    elif number == 0:
        return
    else:
        num = info.pop(number)        
        username = input("Enter your new username (Type N to cancel): ")
        if username.lower() == "n":
                username = "n"
        else:
            num[0] = username
        password = input("Enter your new password (Type N to cancel): ")
        if password.lower() == "n":
            password = "n"
        else:
            num[1] = password
        location = input("Enter where you use your username and password (Type N to cancel): ")
        if location.lower() == "n":
            location = "n"
        else:
            num[2] = location
        info.insert(number, num)

def Menu():
    print("[1] Input Info")
    print("[2] Print Info")
    print("[3] Delete Info")
    print("[4] Edit Info")
    print("-"*50)
    print()
    
def main():
    info = [["Username","Password","Location"],
                ["username01","password01","location01"],
                ["username02","password02","location02"],
                ["username03","password03","location03"]]
    Menu()
    while True:
        try:
                num = int(input("Enter the number of the action you want to do (Enter 0 to exit): "))
                break
        except ValueError:
            print("Please input an integer from 1-4 only...")  
            continue
        
    while num != 0:
        if num == 1:
            InputInfo(info)
            num = 5
        elif num == 2:
            ListInfo(info)
            num = 5
        elif num == 3:
            DeleteInfo(info)
            num =5
        elif num == 4:
            EditInfo(info)
            num = 5
        else:
            while True:
                try:
                    Menu()
                    num = int(input("Enter the number of the action you want to do (Enter 0 to exit): "))
                    break
                except ValueError:
                    print("Please input an integer from 1-4 only...")  
                    continue
            

    

if __name__ == "__main__":
    main()
