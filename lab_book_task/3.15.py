print("-----3.15-----")
print("-----TT-----")
a = True
b = True
print(not a or not b)
print(a and (a or not b))
print((not a or b) and b)

print("-----TF-----")
a = True
b = False
print(not a or not b)
print(a and (a or not b))
print((not a or b) and b)

print("-----FF-----")
a = False
b = False
print(not a or not b)
print(a and (a or not b))
print((not a or b) and b)

print("-----FT-----")
a = False
b = True
print(not a or not b)
print(a and (a or not b))
print((not a or b) and b)
