import time
hours=int(input("How many hours until your alarm?\n"))
minutes=int(input("How many minutes?\n"))
seconds=int(input("How many second?"))
hours=hours*6000
minutes=minutes*60
total_time=hours+minutes+seconds
time.sleep(total_time)
print("timer up!")