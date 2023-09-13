import os


class SMTH():
    def smth(self):
        x = input("Enter Payment Secret Code: ")
        if x == "PAYMENT_DONE":
            return True
        else:
            return False


trial = 0
while trial < 4:
    y = SMTH().smth()
    if y == True:
        print("Payment Has been made successfully")
        os.system("python ./Host.py")
        break
    else:
        print("Invalid Code, Try again ("+str(4-trial)+" trials left)")
        if trial == 3:
            print("Maximum Number of Attempts Reached")
            break
        trial += 1
