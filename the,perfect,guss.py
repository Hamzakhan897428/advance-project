import random
randnumber=random.randint(1,100)
print(randnumber)
user_guess=None
guess=0
while(user_guess!=randnumber):
    user_guess=int(input("Enter your guess:"))
    if user_guess==randnumber:
     guess+=1
     print("your guess is right:")
    else:
       if(user_guess>randnumber):
          print("your guess is wrong!, enter smaller number")
       else:
           print("your guess is wrong!, enter larger number")
print(f"you guess number is{guess}guess")