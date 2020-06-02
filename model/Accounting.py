"""Data to work with"""

import datetime
from model.charge import Charge
from model.petrol import Petrol


class Accounting:
    def __init__(self):
        self._charge_of_gasoline = Charge()
        self._petrol_price = Petrol()
        self._expense = {}

    def __format__(self, format_spec):
        """
        returns formatted string
        :param format_spec: format specifier
        :return: formatted string
        """
        res_format = "Date                                 Car       Charge \n"
        for key, item in self._expense.items():
            for ky, it in item.items():
                res_format += "{:37}{:10}{}\n".format(key, ky, it)
        return res_format

    def __len__(self):
        """
        return length of collection
        :return: amount of User's payments
        """
        return len(self._expense)

    def __getitem__(self, item):
        """
        returns payment with index of item
        :param item: payment index
        :return: payment
        """
        return self._expense[item]

    def __iter__(self):
        """
        iterator
        :return: payment
        """
        for payment in self._expense:
            yield payment

    def add(self, car, petrol, distance):
        """Function to add new record.

        :param car: car name.
        :param petrol: petrol name.
        :param distance: distance made by a car.
        :returns: False if car or petrol is not existing or new record.

        """
        date = datetime.datetime.today().date()
        if car not in self._charge_of_gasoline._gasoline or petrol not in self._petrol_price._price:
            return False
        new_record = {str(date): {car: self._petrol_price.get_price(petrol) * distance * self._charge_of_gasoline._gasoline[car]}}
        self._expense.update(new_record)
        return True

    def show_expense(self):
        """Show all expense records

        """
        mass = [item for item in self._expense.items()]
        mass.sort(key=lambda x: x[0])
        # print("Expense - %s" % mass)
        print("{}".format(self))

    def show_petrol(self):
        """Shows all petrol and their price.

        """

        mass = [item for item in self._petrol_price._price.items()]
        mass.sort(key=lambda x: x[0])
        print("{}".format(self._petrol_price))

    def show_car(self):
        """Shows all cars and their charges.

        """
        mass = [item for item in self._charge_of_gasoline._gasoline.items()]
        mass.sort(key=lambda x: x[0])
        print("{}".format(self._charge_of_gasoline))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
