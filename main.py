def check_square_matrix(m):
    rows = len(m)
    for row in m:
        if len(row) != rows:
            return False
    return True


def get_sub_matrix(matrix, rows, cols):
    r = [[matrix[i][x] for x in cols]for i in rows]
    return r


def calc_determinant(a):
    order = len(a[0])
    if order == 2:
        d = a[0][0] * a[1][1] - a[1][0] * a[0][1]
        return d
    else:
        det_sum = 0
        sign = 1

        for i in range(order):
            r = [x for x in range(order) if x != 0]
            c = [y for y in range(order) if y != i]
            sub_m = get_sub_matrix(a, r, c)

            d = calc_determinant(sub_m)
            det_sum += a[0][i] * d * sign
            sign = sign * -1
        return det_sum


def cof(m):
    order = len(m)
    sign = 1
    A = []
    for j in range(order):
        n = []
        row = [x for x in range(order) if x != j]
        for i in range(order):
            col = [y for y in range(order) if y != i]
            det = calc_determinant(get_sub_matrix(m, row, col))
            n.append(det*sign)
            sign = sign*-1
        A.append(n)
    return A


def transpose(m):
    return [[m[i][j] for i in range(len(m[0]))] for j in range(len(m))]


def adj(m):
    return transpose(cof(m))


def inverse(m):
    det=calc_determinant(m)
    A=adj(m)
    return [[(A[j][i])/det for i in range(len(A[0]))] for j in range(len(A))]
