import pytest


############### тесты на list

def test_pop_list():
    """
    Проверить корректность работы pop при пустом list
    :return:
    """
    val_list = list()
    try:
        good_val = 0
        if len(val_list) != 0:
            good_val = val_list[-1]
        assert good_val == val_list.pop()
    except IndexError:
        pass


def test_str_list():
    """
    Проверить, что str(list) выводит правильную строку
    :return:
    """
    assert str([1, 2, 3, 4]) == "[1, 2, 3, 4]"


@pytest.mark.parametrize("val_list_left,val_list_right,expected",
                         [([], [], []), ([], [1], [1]), ([1], [], [1]), ([1], [2], [1, 2])])
def test_plus_equals_extend(val_list_left: list, val_list_right: list, expected: list):
    """
    Проверить, что list_left + list_light корректно работает
    :param expected:
    :param val_list_left:
    :param val_list_right:
    :return:
    """

    assert val_list_left + val_list_right == expected


############# тесты на int
## пункты 4 и 5 задания уже выполнены, здесь будут только assert без параметризации и негативных тестов


def test_one_and_zero_equals_true_and_false():
    """
    Прверить, что 1 == True и 0 == False
    :return: 
    """
    assert 1 == True and 0 == False


def test_one_and_zero_are_not_true_and_false():
    """
    Прверить, что 1 не ссылается на True и 0 не ссылается на False
    :return:
    """
    assert 1 is not True and 0 is not False


def test_more_for_int():
    """
    Проверить, что "больше" работает корректно
    :return:
    """
    assert 1 > 0 > -1
