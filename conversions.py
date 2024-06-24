def binary_to_decimal(binary):
    binary_str = str(binary)
    decimal = 0
    place_value = 1
    for bit in range(len(binary_str) - 1, -1, -1):
        if binary_str[bit] == '1':
            decimal += place_value
        place_value *= 2
    return decimal

def binary_to_octal(binary):
    while len(binary) % 3 != 0:
        binary = '0' + binary
    octal = ''
    i = 0
    while i < len(binary):
        group = binary[i:i+3]
        octal_digit = 0
        for bit in group:
            octal_digit = octal_digit * 2 + int(bit)
        octal += str(octal_digit)  
        i += 3
    return octal

def binary_to_hexadecimal(binary):
    binary_to_hexadecimal_map = {
        '0000': '0', '0001': '1', '0010': '2', '0011': '3',
        '0100': '4', '0101': '5', '0110': '6', '0111': '7',
        '1000': '8', '1001': '9', '1010': 'A', '1011': 'B',
        '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'
    }
    while len(binary) % 4 != 0:
        binary = '0' + binary
    hexadecimal = ''
    i = 0
    while i < len(binary):
        group = binary[i:i+4]
        hexadecimal += binary_to_hexadecimal_map[group]
        i += 4
    return hexadecimal

def decimal_to_binary(decimal):
    if decimal == '0':
        return '0' 
    elif decimal < '0':
        return 'Invalid input'  
    binary_str = '' 
    decimal = int(decimal) 
    while decimal > 0:
        binary_str = str(decimal % 2) + binary_str 
        decimal //= 2 
    return binary_str

def octal_to_binary(octal):
    if octal == '0':
        return '0'
    elif int(octal) < 0:
        return None
    elif not all(digit in '01234567' for digit in octal):
        return None
    binary_str = ''
    for digit in octal:
        octal_digit = int(digit)
        binary_digit = ''
        for _ in range(3):
            binary_digit = str(octal_digit % 2) + binary_digit
            octal_digit //= 2
        binary_str += binary_digit
    return binary_str

def hexadecimal_to_binary(hexadecimal):
    hexadecimal_to_binary_map = {
        '0': '0000', '1': '0001', '2': '0010', '3': '0011',
        '4': '0100', '5': '0101', '6': '0110', '7': '0111',
        '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
        'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
    }
    binary = ''
    for digit in hexadecimal:
        binary += hexadecimal_to_binary_map[digit]
    return binary

def binary_to_bcd(binary):
    decimal = binary_to_decimal(binary)
    decimal = str(decimal)
    bcd = ''
    for bit in decimal:
        n_bit = decimal_to_binary(bit)
        while len(n_bit) < 4:
            n_bit = '0' + n_bit
        bcd = bcd + ' ' + n_bit
    return bcd

def bcd_to_binary(bcd):
    binary_list = bcd.split()
    n_decimal = ''
    for bit in binary_list:
        n = binary_to_decimal(bit)
        n_decimal = str(n_decimal) + str(n)
    print(n_decimal)

def bitwise_not(binary):
    new_bin = ''
    for bit in binary:
        if bit == '0':
            new_bin = '1' + new_bin
        if bit == '1':
            new_bin = '0' + new_bin
    return new_bin

def bitwise_and(bin1, bin2):
    bin1 = str(bin1)
    bin2 = str(bin2)
    new_bin = ''
    for bit1, bit2 in zip(bin1,bin2):
        new_bin = new_bin + str((int(bit1)*int(bit2)))
    return new_bin

def bitwise_or(bin1, bin2):
    bin1 = str(bin1)
    bin2 = str(bin2)
    new_bin = ''
