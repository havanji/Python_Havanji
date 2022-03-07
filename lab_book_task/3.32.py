print("-----3.32-----")

print("а")
x = float(input())  # -3
y = float(input())  # 5

if x >= -2:
    print(True)
elif y >= 1:
    print(True)
else:
    print(False)

print("б")
x = float(input())  # 123
y = float(input())  # 0

if y <= 1.5 and y >= -2:
    print(True)
else:
    print(False)

print("в")
x = float(input())  # 2
y = float(input())  # 4

if y >= 1 and y <= 4 and x >= 1 and x <= 2:
    print(True)
else:
    print(False)

print("г")
x = float(input())  # 54
y = float(input())  # 3

if x >= 1 and y >= 2 and y <= 4:
    print(True)
else:
    print(False)

print("д")
x = float(input())  # 87
y = float(input())  # -8

if x >= 2 and y >= 0:
    print(True)
elif x >= 1 and y <= -1:
    print(True)
else:
    print(False)

print("е")
x = float(input())  # 3
y = float(input())  # -4

if x >= 2 and y >= 1:
    print(True)
elif x >= 2 and y <= -1.5:
    print(True)
else:
    print(False)

print("ж")
x = float(input())  # 2
y = float(input())  # -1.5

if x >= 1 and x <= 3 and y <= -1 and y >= -2:
    print(True)
else:
    print(False)

print("з")
x = float(input())  # -156
y = float(input())  # 0.7

if x >= 2:
    print(True)
elif y >= 0.5 and y <= 1.5:
    print(True)
else:
    print(False)
