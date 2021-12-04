horezontal_position = 0
depth = 0
aim = 0
with open("data.txt", 'r') as data:
    for line in data:
        elements = line.split(' ')
        command = elements[0]
        value = int(elements[1].strip('\n'))
        if (command == "forward"):
            horezontal_position += value
            depth += aim * value
        elif (command == "down"):
            aim += value
        else:
            aim -= value
    result = horezontal_position * depth
    print(result)