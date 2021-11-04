for i in range(int(input())):
    result = []
    for j in range(int(input())):
        city = input()
        if city not in result:
            result.append(city)
    print(len(result))
