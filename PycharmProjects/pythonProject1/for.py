length = int(input("Set length : "))

def piramit(length, total):
  global range
  if length:
    length = length - 1
    stars = []
    for star in range(1, (total + 1)):
      stars.append('*')
    show = total - length
    print(" ".join(stars[:show]))
    piramit(length, total)

def test(length):
  piramit(length, length)

test(length)