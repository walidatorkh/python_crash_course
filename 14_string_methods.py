text = "hello world and JOPA!"
# print(text)
# print(text[2])
# print(text[0:7])
# print(text[0:12:2])
# print(text[::-1])

# text[2] = "E" TypeError: 'str' object does not support item assignment
# text[2] = "E"
# print(text)
print(text)
print(text.capitalize())
print(text.title())
print(text.upper())
print(text.lower())

text_from_web = "Name\t\nId\t\nDate"
print(text_from_web)
text_formatted = text_from_web.replace("\t\n", ',')
print(text_formatted)
print(type(text_formatted))
list_from_string = text_formatted.split(",")
print(list_from_string)
print(list_from_string[2])
new_string = " | ".join(list_from_string)
print(new_string)

