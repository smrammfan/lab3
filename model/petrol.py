class Petrol:
    def __init__(self):
        self._price = {}

    def __format__(self, format_spec):
        """
        returns formatted string
        :param format_spec: format specifier
        :return: formatted string
        """
        res_format = "Type of petrol      Price \n"
        for key, item in self._price.items():
            res_format += "{:20}{}\n".format(key, item)
        return res_format

    def __len__(self):
        """
        return length of collection
        :return: amount of User's payments
        """
        return len(self._price)

    def __getitem__(self, item):
        """
        returns payment with index of item
        :param item: payment index
        :return: payment
        """
        return self._price[item]

    def __iter__(self):
        """
        iterator
        :return: payment
        """
        for payment in self._price:
            yield payment

    def add(self, name, price):
        """Function to add new petrol.

        :param name: petrol name.
        :param price: petrol price.
        :returns: updates dictionary of petrols.

        """
        self._price.update({name: price})
        return "petrol %s added" % name

    def get_price(self, name):
        """Function to get price of existing petrol.

        :param name: petrol name.
        :returns: price by name.

        """
        return self._price.get(name)

    def delete(self, name):
        """Function to delete existing petrol.

        :param name: petrol name.
        :returns: deletes petrol from dictionary.

        """
        return self._price.pop(name)

    def change(self, name, new_price):
        """Function to change existing petrol.

        :param name: petrol name.
        :param new_price: new price of a petrol.
        :returns: changes petrol price.

        """
        self._price.update({name: new_price})
        return "petrol %s changed" % name


