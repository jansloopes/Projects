def crc_remainder(input_bitstring, polynomial_bitstring, initial_filler):
    '''
    Calculates the CRC remainder of a string of bits using a chosen polynomial.
    initial_filler should be '1' or '0'.
    '''
    polynomial_bitstring = polynomial_bitstring.lstrip('0')
    len_input = len(input_bitstring)
    initial_padding = initial_filler * (len(polynomial_bitstring) - 1)
    input_padded_array = list(input_bitstring + initial_padding)
    while '1' in input_padded_array[:len_input]:
        cur_shift = input_padded_array.index('1')
        for i in range(len(polynomial_bitstring)):
            if polynomial_bitstring[i] == input_padded_array[cur_shift + i]:
                input_padded_array[cur_shift + i] = '0'
            else:
                input_padded_array[cur_shift + i] = '1'
    return ''.join(input_padded_array)[len_input:]


def main():
    input_bitstring = input("give input_bitstring :")
    polynomial_bitstring = input("give polynomial_bitstring :")
    initial_filler = "0"

    print("CRC is {}".format(crc_remainder(input_bitstring, polynomial_bitstring, initial_filler)))


# ------------------------------
# Call Main
# ------------------------------
if __name__ == "__main__":
    main()
