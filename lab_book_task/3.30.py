print("-----3.30-----")

print("а")
a = float(input())  # if 2, 9, 6 == True; if 5 == False

if a % 2 == 0 or a % 3 == 0:
    print(True)
else:
    print(False)

print("б")
a = float(input())  # if 20, 60 == True; if 30, 60 == False

if a % 10 != 0:
    print(False)
elif a % 3 != 0:
    print(True)
else:
    print(False)
