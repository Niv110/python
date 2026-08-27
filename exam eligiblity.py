Medicalcause=input("did you have an medical cause? (Y/N):").strip().upper()
if Medicalcause == 'Y':
    print("you are allowed")
else:

    atten=int(input("enter your attendence: "))
    if atten>75:
        print("you are allowed")
    else:
        print("your not allowed")