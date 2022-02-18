print("-----3.17-----")
print("-----TT-----")
a = True
b = True
print(not a and not b or a)
print((b or (not a)) and (not b))
print(b and not (a and not b))

print("-----TF-----")
a = True
b = False
print(not a and not b or a)
print((b or (not a)) and (not b))
print(b and not (a and not b))

print("-----FF-----")
a = False
b = False
print(not a and not b or a)
print((b or (not a)) and (not b))
print(b and not (a and not b))

print("-----FT-----")
a = False
b = True
print(not a and not b or a)
print((b or (not a)) and (not b))
print(b and not (a and not b))
