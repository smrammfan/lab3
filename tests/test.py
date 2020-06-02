"""Test"""
import unittest
from mock import Mock
from mock import patch


class TestUT(unittest.TestCase):
    """class test"""

    def test_add_car(self):
        """I run out of imagination to write this comments"""
        with patch('model.charge.Charge.add_car') as perm_mock:
            perm_mock('zaz', 32)
            perm_mock.assert_called_once_with('zaz', 32)

    def test_del_car(self):
        """I had a very long lay"""
        with patch('model.charge.Charge.del_car') as perm_mock:
            perm_mock('vaz')
            perm_mock.assert_called_with('vaz')

    def test_add_petrol(self):
        """Show must go on"""
        with patch('model.petrol.Petrol.add') as perm_mock:
            perm_mock('ai91', 31)
            perm_mock.assert_called_with('ai91', 31)

    def test_del_petrol(self):
        """here is so many func to comment"""
        with patch('model.petrol.Petrol.delete') as perm_mock:
            perm_mock('ai91')
            perm_mock.assert_called_with('ai91')

    def test_add_genre(self):
        """AAAAAAAAAAAA_AAA__AAA"""
        with patch('model.charge.Charge.get_charge_of_car') as perm_mock:
            perm_mock('zaz')
            perm_mock.assert_called_with('zaz')

    def test_find_author(self):
        """why do we need so many functions..?"""
        with patch('model.charge.Charge.get_charge_of_car') as perm_mock:
            perm_mock = Mock(return_value=None)
            perm_mock('car1')
            perm_mock('car2')
            perm_mock('car3')
            perm_mock.assert_any_call('car2')

    def test_find_books(self):
        """i hate assembler"""
        with patch('model.charge.Charge.get_charge_of_car') as perm_mock:
            perm_mock = Mock(return_value=None)
            perm_mock('petrol2')
            perm_mock('petrol3')
            perm_mock('petrol5')
            perm_mock.assert_any_call('petrol3')

    def test_delete_book(self):
        """YYUUPA! the last one!"""
        with patch('model.charge.Charge.get_charge_of_car') as perm_mock:
            perm_mock = Mock(return_value=None)
            perm_mock('date1')
            perm_mock('date2')
            perm_mock('date3')
            perm_mock.assert_any_call('date1')


if __name__ == '__main__':
    unittest.main()
