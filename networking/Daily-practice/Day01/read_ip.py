devices = [
    "10.1.1.1",
    "10.1.1.2",
    "10.1.1.3"
]



for device in devices:
    print(device)


# 2nd method or way to print the list.

l = len(devices)
while l > 0:
    print(devices[l-1])
    l -= 1

