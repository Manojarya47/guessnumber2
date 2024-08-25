import  random
secrete=random.randint(0,50)
count=0
print(secrete)
while True:
 guess=int(input("Enter your choess the number within (0/50) >> "))
 if guess==secrete:
     print("it's is right answer!")
     break
 else:
     print("It's is worng! try Again.")
     count+=1
print(f"You took {count} chancen")