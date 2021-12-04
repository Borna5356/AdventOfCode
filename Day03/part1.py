def parse_file(filename):
    with open(filename, 'r') as file:
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
        return data
    
def create_gamma_and_consumption(data):
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
    return first_string, second_string

def binary_to_decimal(binary):
    result = 0
    length = len(binary)
    for index in range(length):
        value = binary[index]
        place = length - index - 1
        result += int(value) * 2**place 
    return result
    
 
def main():
    data = parse_file("data.txt")
    gamma, consumption = create_gamma_and_consumption(data)
    valueOne = binary_to_decimal(gamma)
    valueTwo = binary_to_decimal(consumption)
    print(valueOne * valueTwo)

if (__name__ == "__main__"):
    main()