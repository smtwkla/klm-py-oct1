
from main import check_square_matrix, get_sub_matrix, calc_determinant


def test_check_square_matrix():
    test_matrix = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
    assert check_square_matrix(test_matrix)

    test_matrix = [[1, 2, 3], [1, 2, 3], [1, 2]]
    assert not check_square_matrix(test_matrix)

    test_matrix = [[1, 2], [1, 2], [1, 2]]
    assert not check_square_matrix(test_matrix)


def test_sub_matrix():
    m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    g = get_sub_matrix(m,[1,2],[0,2])
    assert g == [[4, 6], [7, 9]]

    g = get_sub_matrix(m,[0,2],[1,2])
    assert g == [[2, 3], [8, 9]]


def test_calc_determinant4x4():
    m = [[1, 2, 3, 4], [0, 6, 7, 8], [9, 10, 11, 12], [0, 0, 1, 19]]
    assert calc_determinant(m) == -680


def test_calc_determinant3x3():
    m = [[1, 2], [4, 5]]
    assert calc_determinant(m) == -3
    print("2x2 success.")
    m = [[5, 6], [8, 9]]
    assert calc_determinant(m) == -3

    m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert calc_determinant(m) == 0

    m = [[10, 20, 30], [14, 15, 16], [77, 78, 0]]
    assert calc_determinant(m) == 10270


if __name__ == "__main__":
    test_check_square_matrix()
    test_sub_matrix()
    #test_calc_determinant3x3()
    test_calc_determinant4x4()