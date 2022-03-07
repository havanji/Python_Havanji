print("-----3.33-----")

print("а")
x = float(input())  # -5
y = float(input())  # -1

if x <= -2 and y <= -1:
    print(True)
else:
    print(False)

print("б")
x = float(input())  # -3
y = float(input())  # 465

if y >= 1:
    print(True)
elif y <= -3:
    print(True)
else:
    print(False)

print("в")
x = float(input())  # 46
y = float(input())  # -4

if y >= 1:
    print(True)
elif y <= -3 and y >= -4:
    print(True)
else:
    print(False)

print("г")
x = float(input())  # 0
y = float(input())  # 1

if x <= 1.5 and x >= -1 and y <= 1.5 and y >= -0.5:
    print(True)
else:
    print(False)

print("д")
x = float(input())  # 3
y = float(input())  # 2.8

if x >= 1 and x <= 4 and y >= 2 and y <= 4:
    print(True)
else:
    print(False)

print("е")
x = float(input())  # 4
y = float(input())  # 8

if x >= 2 and y >= 1:
    print(True)
elif x <= -1 and y >= 1:
    print(True)
else:
    print(False)

print("ж")
x = float(input())  # 2.3
y = float(input())  # -1.5

if x >= 1 and x <= 3 and y <= 1 and y >= -3:
    print(True)
else:
    print(False)

print("з")
x = float(input())  # 45
y = float(input())  # 32

if x >= 1 and x <= 2.5 and y <= -2:
    print(True)
elif y >= 1.5:
    print(True)
else:
    print(False)
