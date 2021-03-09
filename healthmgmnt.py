#Health Management System

def getdate(): #function for getting the date and time of logging
    import datetime
    return datetime.datetime.now()

def log(k):  #function for logging
    if k==1:
        t= int(input("Enter 1 for exercise and 2 for food"))
        if(t==1):
            value = input("Enter \n")
            with open("Harry-ex.txt", "a") as f:
                f.write(str([str(getdate())])+":"+value+"\n")
                print("Successfuly stored")
        elif(t==2):
            value = input("Enter \n")
            with open("Harry-food.txt", "a") as f:
                f.write(str([str(getdate())])+":"+value+"\n")
                print("Successfuly stored")
    elif k==2:
        t= int(input("Enter 1 for exercise and 2 for food"))
        if(t==1):
            value = input("Enter \n")
            with open("Rohan-ex.txt", "a") as f:
                f.write(str([str(getdate())])+":"+value+"\n")
                print("Successfuly stored")
        elif(t==2):
            value = input("Enter \n")
            with open("Rohan-food.txt", "a") as f:
                f.write(str([str(getdate())])+":"+value+"\n")
                print("Successfuly stored")
    elif(k==3):
        t= int(input("Enter 1 for exercise and 2 for food"))
        if(t==1):
            value = input("Enter \n")
            with open("Hammad-ex.txt", "a") as f:
                    f.write(str([str(getdate())])+":"+value+"\n")
                    print("Successfuly stored")
        elif(t==2):
            value = input("Enter \n")
            with open("Hammad-food.txt", "a") as f:
                f.write(str([str(getdate())])+":"+value+"\n")
                print("Successfuly stored")
        else:
            print("Wrong input please re-enter")


def retrieve(k): #function for retrieving the logs
    if k==1:
        c= int(input("Enter 1 for exercise and 2 for food"))
        if(c==1):
            with open("Harry-ex.txt") as f2:
                for i in f2:
                    print(i,end= " ")
        elif(c==2):
            with open("Harry-food.txt") as f2:
                for i in f2:
                    print(i, end= " ")
    elif k==2:
        c= int(input("Enter 1 for exercise and 2 for food"))
        if(c==1):
            with open("Rohan-ex.txt") as f2:
                for i in f2:
                    print(i,end= " ")
        elif(c==2):
            with open("Rohan-food.txt") as f2:
                for i in f2:
                    print(i, end= " ")
    elif k==3:
        c= int(input("Enter 1 for exercise and 2 for food"))
        if(c==1):
            with open("Hammad-ex.txt") as f2:
                for i in f2:
                    print(i,end= " ")
        elif(c==2):
            with open("Hammad-food.txt") as f2:
                for i in f2:
                    print(i, end= " ")





print("Health Management System")
a= int(input("press 1 for logging and 2 for retrieving"))

if a==1:
    b= int(input("Press 1 for Harry 2 for Rohan and 3 for Hammad"))
    log(b)
else:
    b=int(input("Press 1 for Harry 2 for Rohan 3 for Hammad"))
    retrieve(b)

        

