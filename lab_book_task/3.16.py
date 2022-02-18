print("-----3.16-----")
print("-----TT-----")
x = True
y = True
print(not x and not y)
print(x or (not x and y))
print((not x and y) or y)

print("-----TF-----")
x = True
y = False
print(not x and not y)
print(x or (not x and y))
print((not x and y) or y)

print("-----FF-----")
x = False
y = False
print(not x and not y)
print(x or (not x and y))
print((not x and y) or y)

print("-----FT-----")
x = False
y = True
print(not x and not y)
print(x or (not x and y))
print((not x and y) or y)
