
alien_colour = ["green", "yellow", "red"]
print(input("Enter your clour: "))


if "green" in alien_colour:
    print('you hae earned 5 point')
elif "yellow" in alien_colour:
    print("you've earned 10 point.")
elif "red" in alien_colour:
    print("you just earned 15 point")
else:
    print("try again next time")


ages_in_life = 100
print(input("Enter your age: "))
if ages_in_life <=  2:
     print("You are a Baby")
elif ages_in_life <=13:
     print("You are a kid")
elif ages_in_life <= 13:
     print("ypu are teenager")


items = ['mushrooms', 'olives', 'green peppers',
          'pepperoni', 'pineapple', 'extra cheese']

Available_items = ['mushrooms', 'french fries', 'extra cheese']

print(input("Please enter your order:  "))

for x in Available_items:
    if  Available_items in items:
        print("we are out of " + x + "for now\n Would you love to place another order. ")
    else:
        print("please enjoy while your" + x + "meal is being severd ^-^ .")

user_name = ['james', 'sam, katline', 'admin', 'jake', 'david', 'princess', 'lidia', 'dede' ]

print(input("Enter your user name: "))

if 'admin' in user_name:
    print('hello ' + user_name[2])
else:
    Name = print(input("Enter your name:" ))
    print("hello " + Name +  ' thanks for loging')