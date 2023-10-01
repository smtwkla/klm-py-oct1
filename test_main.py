
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


def test_calc_determinant():
    m = [[1, 2], [4, 5]]
    assert calc_determinant(m) == -3

    m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert calc_determinant(m) == 0


if __name__ == "__main__":
    test_check_square_matrix()
    test_sub_matrix()
    test_calc_determinant()