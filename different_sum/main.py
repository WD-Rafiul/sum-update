times = int(input("How many times you want to try:"))
num = int(input("Enter the number:"))
loop = 0
while loop < times:
    next_num = int(input("Enter other number:"))
    num += next_num
    loop += 1
    print(f"You try {loop}, and Your result is:{num}")
