igork_name = "Igork"
igork_age = 47
igork_grades = 105.5

igork_info = {
    "name": "Igork",
    "age": 47,
    "grades": 105.5,
    "my_languages":{
        "first:": "Java",
        "second:": "C#",
    },
    ("first_name ", "Last_name "): ["Igor", "Khaykin"]
}

# print(igork_name, igork_age, igork_grades)
# print("==============================================")
# print(igork_info)
# print("==============================================")
# print(igork_info.keys())
# print("==============================================")
# print(igork_info.values())
# print("==============================================")
# print(igork_info.items())
# print("==============================================")
# print(list(igork_info.items())[-1])
# 
# print(igork_info.get("grades"))
# print(igork_info["grades"])
# print(igork_info)
# print("==============================================")
# print(igork_info.popitem())
# print("==============================================")
# print(igork_info)

print(igork_info)
print("==============================================")
#print(igork_info.pop("grades"))
print(igork_info.update({"has_car": True}))
igork_info["address"] = "Rishon LeZion"
igork_info["car"] = igork_info.pop("has_car")
print("==============================================")
print(igork_info)
igork_info.pop("my_languages")
print(f"{igork_info} + !!!!!!!")

