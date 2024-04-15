# value = "Hello world!"
# value = ["Hello", "world!", "Jopa"]
# value = ("Hello", "world!", "Jopa")
#
# if "Hello" in value:
#     print("Value exist")
# else:
#     print("Value doesn't exist")

value = "Hello world! Hello world Hello crap"
print(value.count("Hel"))
print(value.count("cr"))
if value.count("Hell") > 0:
    print("Value exist")
else:
    print("Value doesn't exist")
print(value.count("Hel"))
