#building secret game
secret_world = "giraffe"
guess_count = 0
guess_limit = 5
while guess_count < guess_limit:
    secret = input("make A lucky guess: ")
    guess_count += 1
    if secret == "giraffe":
        print("you won!")
        break

else:
    print('sorry you failed')

#building a car racing
command = ""
started = False
while True:
    command = input(">")
    if command.lower() == "start":
        if started:
            print("car is already started")
        else:
            started = True
            print("Car raedy  to go.")
    elif command.lower() == "stop":
        if not started:
            print("car is Already stopped!")
        else:
            started = False
            print("Car stopped.")
    elif command.lower() == "help":
        print("""
start - to start the car
stop - to stop the car 
quit - to exit""")
    elif command == "quit":
        break
    else:
        print("I don't understand that....")
        break
#FOR LOOP
for item in ['python', 'james', 'sam']:
    print(item)

for items in range(1,50):
     print (items)

prices = [10, 20, 30]

total = 0

for price in prices:
    total += price
print(f"Total: {total}")                                                        

numbers = [5, 2, 5, 2, 2]
 for x_count in numbers:
     output = ""
     for count in range(x_count):
         output += 'x'
         print(output)