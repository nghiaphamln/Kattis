string = input()
result = ""

for i in string:
    if i == "e":
        result += "ee"
    else:
        result += i

print(result)
