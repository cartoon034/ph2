A = 1
B = 5
C = 3

array = []
array.append(A)
array.append(B)
array.append(C)

for i in range(len(array)):
    for p in range(len(array)):
        if array[i] < array[p]:
            top = array[i]
            array[i] = array[p]
            array[p] = top
print(array)