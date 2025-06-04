inventory = {"potion": 1, "scroll": 2, "holy sword": 3}

for key in inventory:
    print(key)

for value in inventory.values():
    print(value)

a = {"a":1, "b":5, "c":6}
del a["b"]
print(a)

a = [2, 3, 5, 7]
print(a)
del a[2]
print(a)