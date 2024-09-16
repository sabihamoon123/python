print("Welcome to the rollercoster!")
height = int(input("What is your height in cm?"))
bill = 0

if height >= 120:
     print("You can ride the rollercoster.")
     age = int(input("What is your age?"))
     if age < 12:
        bill = 5
        print("Child tickets are $5.")
     elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
     else:
        bill = 12
        print("adult tickets are $12.")
wants_photos = input("Do you want a photo taken? Y or N.")
if wants_photos == "Y":
    bill += 3
    print(f"Your bill is {bill}")
else:
     print("Sorry, You have to grow taller before you can ride.")

     

# number = int(input("enter a number "))

# if number % 2 == 0:
#     print("the number is even.")
# else:
#     print("the number is odd.")