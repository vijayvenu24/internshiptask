
print("standard ticket price is $10..if you are 60 or above you will get 20% discount..you have to pay only $8" )
print("standard ticket price is $10..if you are under 12 you will get 50% discount..you have to pay only $5" )

age=int(input("enter your age"))
if age>=60:
    print("ticket price is $8")
elif age<12:
    print("ticket price is $5")
else:
    print("ticket price is $10")