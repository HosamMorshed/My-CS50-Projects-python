m=4
for i in range(4):
    for n in range (m):
        print(" ", end="")
    for j in range(i +1):
        print("#" ,end="")
    m -=1
    print()
for c in range(4):
    print("@"*4)