

def calc_determinant(a):
    order = len(a[0])
    if order == 2:
        d = a[0][0] * a[1][1] - a[1][0] * a[0][1]
        return d
    else:
        # calculate sub-matrix for each element in row[0]
        # call calc_determinant recursively
        # add determinant with sum
        pass


def check_square_matrix(m):
    rows = len(m)
    for row in m:
        if len(row) != rows:
            return False
    return True

