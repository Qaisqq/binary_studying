def decimal_to_binary(binary):
    binary_list = [int(bit) for bit in str(binary)]
    binary_list.reverse()
    decimal = 0
    place_value = 1
    for bit in range(len(binary_list)):
        place_value = place_value * 2
        if binary_list[bit] == 1:
            decimal = place_value + decimal
    print(f"Binary: {binary}")
    print(f"Decimal: {int(decimal/2)}")

decimal_to_binary(1010101)