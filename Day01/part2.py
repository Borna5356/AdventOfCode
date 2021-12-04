count = 0
prev = 100000000000000
sum = 0
index = 0
prev_2 = 0
prev_1 = 0
with open("data.txt", 'r') as file:
    for line in file:
        value = line.strip("\n")
        value = int(value)
        sum += value
        index += 1
        if (index >= 3):
            if(sum > prev):
                count += 1
            prev = sum
            sum -= prev_2
        prev_2 = prev_1
        prev_1 = value

print(count)