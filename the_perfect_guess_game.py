import random
n=random.randint(1,100)
a=-1
gusses=1
while (a != n ):
    a=int(input("Guess the number : "))
    if (a>n):
        print("Lower number please ")
        gusses+=1
    elif(a<n):
        print("Hight number please ")
        gusses+=1

print(f"You have gussed the number {n} correctly in {gusses} attempt")
