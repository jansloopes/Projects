import sys
from icecream import ic


def check_matrix(the_matrix_1: list, the_matrix_2: list) -> bool:
    """
    Function to check if the dimensions of two matrices are equal.

    Args:
        the_matrix_1 (list): First matrix.
        the_matrix_2 (list): Second matrix.

    Returns:
        bool: True if dimensions are equal, False otherwise.
    """
    # calculate length of each matrix
    the_matrix_1_length = sum(len(row) for row in the_matrix_1)
    the_matrix_2_length = sum(len(row) for row in the_matrix_2)

    # calculate number of dimensions of each matrix
    the_matrix_1_number_of_dimensions = _calculate_number_of_dimensions(the_matrix_1)
    the_matrix_2_number_of_dimensions = _calculate_number_of_dimensions(the_matrix_2)

    # check if dimensions and number of dimensions are equal and both matrices are 2D
    if (the_matrix_1_length == the_matrix_2_length and the_matrix_1_number_of_dimensions == 
    the_matrix_2_number_of_dimensions and the_matrix_1_number_of_dimensions==2 and the_matrix_2_number_of_dimensions== 2):
        return True
    else:
        return False


def _calculate_number_of_dimensions(matrix: list) -> int:
    """
    Function to calculate the number of dimensions of a matrix.

    Args:
        matrix (list): Matrix to calculate number of dimensions for.

    Returns:
        int: Number of dimensions.
    """
    dimensions = 0
    while isinstance(matrix, list) and matrix:
        dimensions += 1
        matrix = matrix[0]
    return dimensions
    

def main():
    """
    Main function to demonstrate the usage of the 'add_matrix' function.
    """
    # Define the matrices
    the_matrix_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    the_matrix_2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
    add_matrix = the_matrix_1
    
    # Check if the matrices are of the same size
    if check_matrix(the_matrix_1, the_matrix_2):
        print(f"the matrices are the same size\n")
        
        # Initialize counters
        p = 0
        q = 0
        
        # Add the matrices element-wise
        for i in the_matrix_1:
            for j in i:
                add_matrix[p][q] = the_matrix_1[p][q] + the_matrix_2[p][q]
                q += 1
            q = 0
            p += 1
             # Print the result
        print("add_matrix is: {}".format(add_matrix))
    else:
        print("the matrices are not the same size")
    
   

if __name__ == "__main__":
    main()
