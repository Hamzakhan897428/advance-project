import os
if __name__ =="__main__":
    print("welcome to robo speaker. created by Hamza khan")
    while True:
        x=input("what do you want me to speak:")
        if x=='q':
            os.system("say'bye bye friends'")
            break
        command=f"say {x}"
        os.system(command)