count = 0
prev = 100000000000000
with open("data.txt", 'r') as file:
    for line in file:
        value = line.strip("\n")
        value = int(value)
        if(value > prev):
            count += 1
        prev = value

print(count)