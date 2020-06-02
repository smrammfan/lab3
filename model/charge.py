class Charge:
    def __init__(self):
        self._gasoline = {}

    def __format__(self, format_spec):
        """
        returns formatted string
        :param format_spec: format specifier
        :return: formatted string
        """
        res_format = "Type of car      Charge \n"
        for key, item in self._gasoline.items():
            res_format += "{:17}{}\n".format(key, item)
        return res_format

    def __len__(self):
        """
        return length of collection
        :return: amount of User's payments
        """
        return len(self._gasoline)

    def __getitem__(self, item):
        """
        returns payment with index of item
        :param item: payment index
        :return: payment
        """
        return self._gasoline[item]

    def __iter__(self):
        """
        iterator
        :return: payment
        """
        for payment in self._gasoline:
            yield payment

    def get_charge_of_car(self, name):
        """Function to get charge of car.

        :param name: car name.
        :returns: charge of named car.

        """
        return self._gasoline.get(name)

    def add_car(self, name, charge):
        """Function to add new car.

        :param name: car name.
        :param charge: car charge.
        :returns: updates dictionary of cars.

        """
        self._gasoline.update({name: charge})
        return name

    def del_car(self, name):
        """Function to delete existing car.

        :param name: car name.
        :returns: deletes car from dictionary.

        """
        return self._gasoline.pop(name)

    def change_car(self, name, new_charge):
        """Function to change existing car.

        :param name: car name.
        :param new_charge: new charge of a car.
        :returns: modifies car dictionary.

        """
        self._gasoline.update({name: new_charge})
        return new_charge
