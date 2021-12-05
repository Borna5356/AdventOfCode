def parse_file(filename):
    with open(filename, 'r') as file:
        created_list = False
        data = []
        numbers = []
        for line in file:
            values = line.strip('\n')
            numbers.append(values)
            if (created_list == False):
                for index in range(len(values)):
                    data.append({'1': 0, '0': 0})
                created_list = True
            for index in range(len(values)):
                x = data[index]
                value = values[index]
                x[value] += 1
                data[index] = x
        return data, numbers


def calculate_oxygen(data, bin_numbers, place = 0):
    """
    Uses recursion to find the oxygen value
    """
    if (len(bin_numbers) == 1):
        return bin_numbers[0]
    
    place_value = data[place] # This is the value to find if there are more 1s or 0s in a place
    ones = place_value['1']
    zeroes = place_value['0']
    if (ones >= zeroes):
        bin_numbers = eleminate_zeroes(bin_numbers, place)
    else:
        bin_numbers = eleminate_ones(bin_numbers, place)
    data = calculate_num_ones_and_zeros(bin_numbers)
    return calculate_oxygen(data, bin_numbers, place + 1)

def calculate_carbon(data, bin_numbers, place = 0):
    """
    Uses recursion to find the carbon value
    """
    if (len(bin_numbers) == 1):
        return bin_numbers[0]
    
    place_value = data[place] # This is the value to find if there are more 1s or 0s in a place
    ones = place_value['1']
    zeroes = place_value['0']
    if (ones < zeroes):
        bin_numbers = eleminate_zeroes(bin_numbers, place)
    else:
        bin_numbers = eleminate_ones(bin_numbers, place)
    data = calculate_num_ones_and_zeros(bin_numbers)
    return calculate_carbon(data, bin_numbers, place + 1)
        


def eleminate_zeroes(bin_numbers, place):
    """
    Copys the values that have 1 in a given place to a new list
    """
    new_bin_numbers = []
    for value in bin_numbers:
        if (value[place] == '1'):
            new_bin_numbers.append(value)
    return new_bin_numbers

def eleminate_ones(bin_numbers, place):
    """
    Copys the values that have 0 in a given place to a new list
    """
    new_bin_numbers = []
    for value in bin_numbers:
        if (value[place] == '0'):
            new_bin_numbers.append(value)
    return new_bin_numbers

def calculate_num_ones_and_zeros(bin_numbers):
    """
    Calculates the number of ones and zeros for each 
    place in bin numbers
    """
    created_list = False
    data = []
    for values in bin_numbers:
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


def binary_to_decimal(binary):
    result = 0
    length = len(binary)
    for index in range(length):
        value = binary[index]
        place = length - index - 1
        result += int(value) * 2**place 
    return result
    
 
def main():
    data, bin_num = parse_file("data.txt")
    oxygen = calculate_oxygen(data, bin_num)
    carbon = calculate_carbon(data, bin_num)
    oxygen = binary_to_decimal(oxygen)
    carbon = binary_to_decimal(carbon)
    result = oxygen * carbon
    print(result)

if (__name__ == "__main__"):
    main()