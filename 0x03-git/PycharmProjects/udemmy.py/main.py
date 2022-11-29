import re

print ("our magic calculator \n")
print("print quit to exit")

previous = 0
run = True


def performmath():
    global run
    global previous
    equation = ""
    if previous  == 0:
          equation = input("enter eqution: ")
    else:
        equation == input(str(previous))
        if equation ==  "quit":
            run = False
        else:
            equation = re.sub('[a-zaA-z.,:()""]', '', equation)
            previous = eval(equation)


            print("you typed", equation )

