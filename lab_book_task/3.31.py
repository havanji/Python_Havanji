print("-----3.31-----")

print("а")
n = float(input())  # if 2, 9, 6 == True; if 5 == False

if n % 5 == 0 or n % 7 == 0:
    print(True)
else:
    print(False)

print("б")
a = float(input())  # if 40, 360, 360360  == True; if 44, 256 == False

if a % 10 != 0:
    print(False)
elif a % 4 == 0:
    print(True)
else:
    print(False)
