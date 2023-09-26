from random import * 

x = randint(0, 100)

def main(_numAttempts):
    numAttempts = _numAttempts + 1
    u = int(input("Enter number: "))
    if u == x:
        print("Well done ! You found the correct number : " + str(numAttempts) + " tries.")
    else:
        if u > x:
            print("Too big.")
        else: 
            print("Too small.")
        main(numAttempts) 
main(0)
