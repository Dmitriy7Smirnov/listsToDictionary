import unittest

"""
Тестовое задание на вакансию python разработчика в Yandex
Есть два списка разной длины. В первом содержатся ключи, а во втором значения.
Напишите функцию, которая создаёт из этих ключей и значений словарь.
Если ключу не хватило значения, в словаре должно быть значение None.
Значения, которым не хватило ключей, нужно игнорировать.
Подробнее: http://company.yandex.ru/job/vacancies/dev_python_mysql.xml
"""

def dict_from_lists(key_list, value_list):
    delta = len(key_list) - len(value_list)

    if delta > 0:
        for i in range(0, delta):
            value_list.append(None)

    dictionary = dict(zip(key_list, value_list))
    return dictionary


class test(unittest.TestCase):
    def test_fewer_keys_than_values(self):
        key_list = [2, 3, 44]
        value_list = ['S', 'D', 'k', 0]
        result_dict = {
            2: 'S',
            3: 'D',
            44: 'k'
        }
        self.assertEqual(dict_from_lists(key_list, value_list), result_dict)

    def test_keys_and_values_equally(self):
        key_list = [2, 3, 44, 9]
        value_list = ['S', 'D', 'k', 0]
        result_dict = {
            2: 'S',
            3: 'D',
            44: 'k',
            9: 0
        }
        self.assertEqual(dict_from_lists(key_list, value_list), result_dict)

    def test_fewer_values_than_keys(self):
        key_list = [2, 3, 44, 9, 4, 5, '9']
        value_list = ['S', 'D', 'k', 0]
        result_dict = {
            2: 'S',
            3: 'D',
            44: 'k',
            9: 0,
            4: None,
            5: None,
            '9': None
        }
        self.assertEqual(dict_from_lists(key_list, value_list), result_dict)


if __name__ == "__main__":
    unittest.main()