"""
  File: spiral.py
  Description: Create spiral and sum adjacent numbers

  Student Name: Arham Lodha
  Student UT EID: arl3759

  Partner Name: Tho Lam
  Partner UT EID: tml2532

  Course Name: CS 313E
  Unique Number: 52590
  Date Created: 08/17/2023
  Date Last Modified: 08/17/2023
"""
positions = []


def create_spiral(number):
    """
    Input: number is an odd integer between 1 and 100
    Output: returns a 2-D list representing a spiral
         if number is even add one to n"""

    if number % 2 == 0:
        number += 1

    grid = [[0 for i in range(number)] for j in range(number)]

    # Create Spiral

    # middle element
    row = int((number - 1) / 2)
    col = int((number - 1) / 2)

    grid[row][col] = 1
    positions.append((row, col))

    i = 2
    row_placed = 1
    row_size = 2

    # 0 = right, 1 = down, 2 = left, 3 = up
    direction = 0

    while i <= number * number:
        if row_placed < row_size:
            if direction == 0:
                col += 1
            elif direction == 1:
                row += 1
            elif direction == 2:
                col -= 1
            else:
                row -= 1
            grid[row][col] = i
            positions.append((row, col))
            row_placed += 1
            i += 1
        else:
            row_placed = 2
            if direction == 0:
                row += 1
            elif direction == 1:
                col -= 1
                row_size += 1
            elif direction == 2:
                row -= 1
            else:
                col += 1
                row_size += 1
            grid[row][col] = i
            positions.append((row, col))
            i += 1
            direction = (direction + 1) % 4
    return grid


def sum_adjacent_numbers(spiral, target):
    """
    Input: spiral is a 2-D list and target is an integer
    Output: returns an integer that is the sum of the
            numbers adjacent to n in the spiral
            if target is outside the range return 0"""
    if target < 1 or target > len(positions):
        return 0

    row, col = positions[target - 1]
    total = 0

    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            if (
                row + i < 0
                or row + i >= len(spiral)
                or col + j < 0
                or col + j >= len(spiral)
            ):
                continue
            total += spiral[row + i][col + j]

    return total


def main():
    """
    A Main Function to read the data from input,
    run the program and print to the standard output.
    """

    # read the dimension of the grid and value from input file
    dim = int(input())

    # test that dimension is odd
    if dim % 2 == 0:
        dim += 1

    # create a 2-D list representing the spiral
    mat = create_spiral(dim)

    while True:
        try:
            sum_val = int(input())

            # find sum of adjacent terms
            adj_sum = sum_adjacent_numbers(mat, sum_val)

            # print the sum
            print(adj_sum)
        except EOFError:
            break


if __name__ == "__main__":
    main()
