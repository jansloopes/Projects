def crc_check(input_bitstring, polynomial_bitstring, check_value):
    '''
    Calculates the CRC check of a string of bits using a chosen polynomial.
    '''
    polynomial_bitstring = polynomial_bitstring.lstrip('0')
    len_input = len(input_bitstring)
    initial_padding = check_value
    input_padded_array = list(input_bitstring + initial_padding)
    while '1' in input_padded_array[:len_input]:
        cur_shift = input_padded_array.index('1')
        for i in range(len(polynomial_bitstring)):
            if polynomial_bitstring[i] == input_padded_array[cur_shift + i]:
                input_padded_array[cur_shift + i] = '0'
            else:
                input_padded_array[cur_shift + i] = '1'
    if '1' not in ''.join(input_padded_array)[len_input:]:
        return True
    else:
        return False



def main():
    print ("return is {}".format(crc_check('1000110010', '1001', '101')))



# ------------------------------
# Call Main
# ------------------------------
if __name__ == "__main__":
    main()
