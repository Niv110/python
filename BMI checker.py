height=float(input("enter your height: "))
weight=float(input("enter your weight: "))

BMI=weight/(height/100)**2

if BMI <= 18.4:
    print("you are under weight")
elif BMI <= 24.9:
        print ("your are healthy")
elif BMI <= 29.9:
      print("your are overweight")
elif BMI <= 34.9:
      print("your severly over weight")
elif BMI <= 39.9:
      print("your obese")
else:
      print("your severly obese")
