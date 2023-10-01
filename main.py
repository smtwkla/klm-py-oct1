

def check_square_matrix(m):
    rows = len(m)
    for row in m:
        if len(row) != rows:
            return False
    return True

