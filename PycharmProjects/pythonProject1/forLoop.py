max_num = int(input("Set length : "))
num = max_num

for i in range(max_num):
    for s in range(i):
        print(" ", end=' ')

    for n in range(1, num + 1):
        print('*', end=' ')

    num -= 1
    print("")