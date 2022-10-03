a = int(input("number:" + " "))

min = 100
max = 0

for i in range(0,a):
    b = int(input("score" + " "))
    if min > b:
        min = b
    if max < b:
        max = b

print(("min = "+str(min)) + (" ") + ("max = "+str(max)))


# number = input("number: ").split(',')
#
# min = 100
# max = 0
#
# for i in number:
#     if min > int(i):
#         min = int(i)
#     if max < int(i):
#         max = int(i)
#
# print(("min: " + str(min)) + (" ") + ("mix: " + str(max)))
