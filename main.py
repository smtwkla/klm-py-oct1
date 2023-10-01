def check_square_matrix(m):
    rows = len(m)
    for row in m:
        if len(row) != rows:
            return False
    return True


def get_sub_matrix(matrix, rows, cols):
    m = []
    for i in rows:
        r = [matrix[i][x] for x in cols]
        m.append(r)
    return m


def calc_determinant(a):
    order = len(a[0])
    if order == 2:
        d = a[0][0] * a[1][1] - a[1][0] * a[0][1]
        return d
    else:
        det_sum = 0
        sign = 1

        for i in range(order):
            r = []
            c = []
            sub_m = get_sub_matrix(a, r, c)
            d = calc_determinant(sub_m)
            det_sum += a[i] * d * sign




