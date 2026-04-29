print("community pool safety system")
temprature=float(input("enter the water temprature"))
chlorinelevel=float(input("enter chlorine level on a scale of 1.0 to 10.0"))
if temprature>25.0 and chlorinelevel>=3.0 and chlorinelevel <=7.0:
    print("the pool is safe.you may open the pool")
else:
    print("Danger.the pool is not safe")
if temprature<=25.0:
    print("temprature is too low")
if chlorinelevel<3.0 or chlorinelevel>7.0:
    print("unsafe chlorine level")