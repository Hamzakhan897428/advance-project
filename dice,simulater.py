import random
def dic_roll(num_dice,num_side): 
    return sum(random.randint(1,num_side) for _ in range(num_dice))
def main():
    print("welcome to dice simulater")
    while True:
        num_dice=input("Enter your dice roller:")
        num_side=input("Enter your side for each die:")
        total=dic_roll(num_dice,num_side)
        print(f"\nyou rolled{num_dice}dice with{num_side}dice with")
        print(f"total sum is :{total}")
        choice=input("\n do you wan to roll again?(yes\no): ")
        if choice!=1:
            print("thanks for using Dice simulater")
            break
if __name__ ==" __main__":
     main()