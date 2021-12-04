with open("data.txt", 'r') as file:
    created_list = False
    data = []
    for line in file:
        values = line.strip('\n')
        if (created_list == False):
            for index in range(len(values)):
                data.append({'1': 0, '0': 0})
            created_list = True
        for index in range(len(values)):
            x = data[index]
            value = values[index]
            x[value] += 1
            data[index] = x
    first_string = ""
    second_string = ""
    for element in data:
        numOnes = element['1']
        numZeros = element['0']
        if (numOnes > numZeros):
            first_string += '1'
            second_string += '0'
        else:
            first_string += '0'
            second_string += '1'
    print(first_string)
    print(second_string)
    firstDecimal = 0
    secondDecimal = 0
    length = len(first_string)
    for index in range(length):
        value = first_string[index]
        valueTwo = second_string[index]
        place = length - index - 1
        firstDecimal += int(value) * 2**place 
        secondDecimal += int(valueTwo) * 2**place
    print(firstDecimal)
    print(secondDecimal)
    print(firstDecimal * secondDecimal)