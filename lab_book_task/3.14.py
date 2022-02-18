print("-----3.14-----")
print("-----TT-----")
x = True
y = True
print(not (x or y))
print(not x and y)
print(x and not y)

print("-----TF-----")
x = True
y = False
print(not (x or y))
print(not x and y)
print(x and not y)

print("-----FF-----")
x = False
y = False
print(not (x or y))
print(not x and y)
print(x and not y)

print("-----FT-----")
x = False
y = True
print(not (x or y))
print(not x and y)
print(x and not y)
