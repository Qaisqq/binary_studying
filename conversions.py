binary_number = "11010101011"
binary_list = [int(bit) for bit in binary_number]
binary_list.reverse()

def decimal_to_binary(binary_list):
    decimal = 0
    place_value = 1
    for bit in range(len(binary_list)):
        place_value = place_value * 2
        if binary_list[bit] == 1:
            decimal = place_value + decimal
    return decimal/2

y = decimal_to_binary(binary_list)
print(f"Binary: {binary_number}")
print(f"Decimal: {int(y)}")