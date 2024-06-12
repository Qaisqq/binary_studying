def binary_to_decimal(binary):
    binary_list = [int(bit) for bit in str(binary)]
    binary_list.reverse()
    decimal = 0
    place_value = 1
    for bit in range(len(binary_list)):
        place_value = place_value * 2
        if binary_list[bit] == 1:
            decimal = place_value + decimal
            return decimal

def decimal_to_binary(decimal):
    if decimal == 0:
        return '0' 
    elif decimal < 0:
        return 'Invalid input'  
    binary_str = ''  
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

# def binary_to_octal(binary):
#     binary_list = [int(bit) for bit in str(binary)]
#     binary_list.reverse()
#     decimal = 0
#     place_value = 1
#     for bit in range(len(binary_list)):
#         place_value = place_value * 2
#         if binary_list[bit] == 1:
#             decimal = place_value + decimal
#             return decimal

# print(binary_to_octal(1101))