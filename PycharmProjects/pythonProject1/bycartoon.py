Students = {
'Johny' : 99,
'Jimmy' : 58,
'Jonathan' : 34,
'Job' : 69,
'Jess' : 97,
'Jress' : 86,
'Juan_Mata' : 65,
'Jessi' : 78,
'Justin' : 45,
'Jegian' : 55,
'Jobby' : 35,
'Jark' : 21,
'Joker' : 56,
'Jatman' : 67,
}
def bycartoon (name , score):
    if score >= 90:
        print("{} เกรด 4" .format(name))
    elif score >= 75:
        print("{} เกรด 3".format(name))
    elif score >= 65:
        print("{} เกรด 2".format(name))
    elif score >= 50:
        print("{} เกรด 1".format(name))
    else:
        print("{} เกรด 0".format(name))

for name , score in Students.items():
    bycartoon(name , score)