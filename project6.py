ticketprice=int(input("enter the ticket price per person"))
hotelprice=int(input("enter the hotel price"))
days=int(input("enter the number of days want to stay"))
savings=int(input("enter the total savings you have"))
totalcost=ticketprice+(hotelprice*days)
amount=totalcost-savings
if savings>=totalcost+200:
    print("status:pack your bags!you have enough money")
else:
    print("status:keep saving you are short by $ ",amount)

