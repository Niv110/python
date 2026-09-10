for i in range (4):
    print("*" *4)

print()

for i in range (4):
    for j in range (4):
        print("*" , end=" ")
    print()

print()

for i in range (1,6):
    for j in range (i):
        print("*", end=" ")

    print()

for i in range (1,6):
    for j in range (i):
        print(i, end=" ")
    print()


num=1
for i in range (1,5):
    for j in range (i):
        print(num,end=" ")
        num += 1
    print()
    

