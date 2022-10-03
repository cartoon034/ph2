import random
def random_number_num_generator():
    first = str(random.randint(100, 999))
    second = str(random.randint(1, 888)).zfill(3)
    last = (str(random.randint(1, 999)).zfill(3))
    while last in ['1111', '2222', '3333', '4444', '5555', '6666', '7777', '8888']:
        last = (str(random.randint(1, 999)).zfill(3))
    return '{}{}{}'.format(first, second, last)
n = 0
for i in range(0, n):
    print(random_number_num_generator())

#zero = "0"+random_number_num_generator()
#print(zero)