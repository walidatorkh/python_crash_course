num = 0

while num < 5:
    if num == 7:
        print(num)
        break
    print(num)
    num += 1
else:
    print("Else block")
    print("After whlile loop")

for num in range(5):
    print(num)
comp_num = 55
user_num = int(input("Guess a number: "))

while comp_num != user_num:
    if user_num < comp_num:
        print("your number a smallest")
    elif user_num > comp_num:
        print("your number a biggest")

    user_num = int(input("Guess a number: "))
    print("your number equal!")
else:
    print("You win!")