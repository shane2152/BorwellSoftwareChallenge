import time

def printintro():
    """This is a basic print intro function to make my main function look a little more tidy"""
    print("Thanks for looking at my Paint Calculator")
    print("By Shane Hadley")


def get_user_input():
    """This is the function where it gets the users dimensions of the room and returns them"""
    print("\nPlease enter your dimensions in Meters.")
    length = float(input("\nWhat is the length of the room? "))
    width = float(input("What is the width of the room? "))
    height = float(input("What is the height of the room? "))
    return length, width, height


def calculations(length,width,height):
    """This is the function that does all the calculations for the area, volume and how much paint is needed"""
    area = length * width
    volume = length * width * height
    paintneeded = ((length * height) *2) + ((width* height) *2)
    return "{:.2f}".format(area), "{:.2f}".format(volume), "{:.2f}".format(paintneeded)


def output(area, volume, paintneeded):
    """This function is what displays the outcome of all the calculations in their proper format"""
    print("\nThe area of the room is {0}m\u00b2".format(area))
    print("The volume of the room is {0}m\u00b3".format(volume))
    print("You need enough paint to cover {0}m\u00b2 of walls.".format(paintneeded))


def main():
    """This is my main function where I store all the needed functions. I do have a while loop in here so
        it can ask the user if they would like to go again. The reason I added a break in the IF statement
        is because the loop would continue to run while the program is being used again. This is one way to
        stop that"""
    printintro()
    length, width, height = get_user_input()
    area, volume, paintneeded = calculations(length,width,height)
    output(area, volume, paintneeded)
    while True:
        again = input("\nWould you like to go again?(y/n) ").lower()
        if again == 'y':
            break
        elif again == 'n':
            print("Thank you for using the software! Goodbye!")
            time.sleep(3)
            exit()
        else:
            print("\nInvalid Input!")
    main()


if __name__ == '__main__':
    main()
