class Sudoku(object):
    """
    Approach:
Like all other Backtracking problems, Sudoku can be solved by one by one assigning numbers to empty cells. Before assigning a number, check whether it is safe to assign. Check that the same number is not present in the current row, current column and current 3X3 subgrid. After checking for safety, assign the number, and recursively check whether this assignment leads to a solution or not. If the assignment doesn’t lead to a solution, then try the next number for the current empty cell. And if none of the number (1 to 9) leads to a solution, return false and print no solution exists.
    """
    def solve(arr):
        # 'l' is a list variable that keeps the record of row and col in find_empty_location Function
        l =[0, 0]

        # If there is no unassigned location, we are done
        if(not find_empty_location(arr, l)):
            return True

        # Assigning list values to row and col that we got from the above Function
        row = l[0]
        col = l[1]

        # consider digits 1 to 9
        for num in range(1, 10):

            # if looks promising
            if(check_location_is_safe(arr, row, col, num)):

                # make tentative assignment
                arr[row][col]= num

                    # return, if success, ya ! if(solve_sudoku(arr)):
                    return True

                # failure, unmake & try again
                arr[row][col] = 0

        # this triggers backtracking
        return False

    def print_grid(self, arr):
        for i in range(9):
            for j in range(9):
                print arr[i][j]
            print('n')

    def find_empty_location(self, arr, l):
        for row in range(9):
            for col in range(9):
                if(arr[row][col] == 0):
                    l[0] = row
                    l[1] = col
                    return True

        return False

    def used_in_row(self, arr, row, num):
        for i in range(9):
            if(arr[row][i] == num):
                return True

    def used_in_col(self, arr, col, num):
        for i in range(9):
            if(arr[i][col] == num):
                return True
        return False

    def used_in_box(self, arr, row, col, num):
        for i in range(3):
            for j in range(3):
                if(arr[i+row][j+col] == num):
                    return True
        return False

    def check_location_is_safe(self, arr, row, col, num):
        return not self.used_in_box(arr, row, col, num) and
          not self.used_in_row(arr, row, num) and
          not self.used_in_col(arr, col, num)


