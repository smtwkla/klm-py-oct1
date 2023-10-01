
from main import check_square_matrix


def test_check_square_matrix():
    test_matrix = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
    assert check_square_matrix(test_matrix)

    test_matrix = [[1, 2, 3], [1, 2, 3], [1, 2]]
    assert not check_square_matrix(test_matrix)

    test_matrix = [[1, 2], [1, 2], [1, 2]]
    assert not check_square_matrix(test_matrix)


if __name__ == "__main__":
    test_check_square_matrix()
