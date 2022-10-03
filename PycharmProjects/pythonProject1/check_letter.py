A = "ABCDEFG"
B = "abcdefg"
C = "AbCdEfG"


def check_letter(S):
    if S.isupper():
        print("All Capital Letter")
    elif S.islower():
        print("All Small Letter")
    else:
        print("mix")


check_letter(A)
check_letter(B)
check_letter(C)