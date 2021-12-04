horezontal_position = 0
depth = 0
with open("data.txt", 'r') as data:
    for line in data:
        elements = line.split(' ')
        command = elements[0]
        value = int(elements[1].strip('\n'))
        if (command == "forward"):
            horezontal_position += value
        elif (command == "down"):
            depth += value
        else:
            depth -= value
    result = horezontal_position * depth
    print(result)