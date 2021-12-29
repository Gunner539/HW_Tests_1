import unittest
from unittest.mock import patch
import main

class Test_main(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('Тестирование выполняется...')

    def setUp(selfself):

        main.documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]
        main.directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


    def test_det_doc_owner_name(self):
        exp_value = ['passport "2207 876234" "Василий Гупкин"',
                'invoice "11-2" "Геннадий Покемонов"',
                'insurance "10006" "Аристарх Павлов"']
        res = main.show_all_docs_info()
        self.assertListEqual(res, exp_value)

    def test_get_all_doc_owners_names(self):
        exp_value = {"Василий Гупкин", "Геннадий Покемонов", "Аристарх Павлов"}
        self.assertSetEqual(main.get_all_doc_owners_names(), exp_value)

    @patch('builtins.input')
    def test_get_doc_owner_name(self, user_input):
        user_input.side_effect = ['10006']
        self.assertEqual(main.get_doc_owner_name(), "Аристарх Павлов")

    @patch('builtins.input')
    def test_get_doc_shelf(self, user_input):
        user_input.side_effect = ['10006']
        self.assertEqual(main.get_doc_shelf(), '2')

    @patch('builtins.input')
    def test_get_doc_shelf_None(self, user_input):
        user_input.side_effect = ['12']
        self.assertEqual(main.get_doc_shelf(), None)


    @patch('builtins.input')
    def test_add_new_doc(self, user_input):
        input_values = ['invoice', '0404', 'Sub-zero', '1986562']
        user_input.side_effect = input_values
        self.assertEqual(main.add_new_doc(), '1986562')

    @patch('builtins.input')
    def test_delete_doc(self, user_input):
        user_input.side_effect = ['11-2']
        self.assertEqual(main.delete_doc(), ('11-2', True))

    @classmethod
    def tearDownClass(cls):
        print('Тестирование завершено')


if __name__ == "__main__":
    unittest.main()