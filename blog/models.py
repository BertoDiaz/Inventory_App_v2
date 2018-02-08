"""
File name: models.py.

Name: Inventory App

Description: With this web application you can do the inventory of all
             the material of your laboratory or business. You can also
             place orders but this form is case-specific. Moreover,
             you can track all your manufacturing procedures such as
             wafer fabrication in this case.

Copyright (C) 2017  Heriberto J. Díaz Luis-Ravelo

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see http://www.gnu.org/licenses/.

Email: heriberto.diazluis@gmail.com
"""

from django.db import models
from django.utils import timezone

""" Models Inventory """


class Inventory(models.Model):
    """
    Inventory model docstring.

    This model stores the kinds of inventories that are possible.
    """

    author = models.ForeignKey('auth.User',
                               help_text="Name of the author that created the inventory.")
    type_item = models.ForeignKey('Type', help_text="Type of inventory.")
    name = models.CharField(max_length=200, help_text="Name of the inventory.")
    maker = models.CharField(max_length=200, help_text="Manufacturer of the inventory.")
    created_date = models.DateTimeField(default=timezone.now, help_text="Date when was created.")

    def create(self):
        """
        Create function docstring.

        This function stores the date when the data was created and save the info.
        """
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        """
        Return string function docstring.

        This function returns the name of the kind of inventory.

        @return: a string with the name of the kind of inventory.
        """
        return self.name


class Computing(models.Model):
    """
    Computing model docstring.

    This model stores the computers.
    """

    author = models.ForeignKey('auth.User', null=True)
    name = models.CharField(max_length=200, blank=True, help_text="Name of the computer.")
    type_object = models.ForeignKey('Type_Object', help_text="Type of the computing.")
    location = models.ForeignKey('Location', help_text="Where it is the computer.")
    user_name = models.ForeignKey('Full_Name_Users', blank=True,
                                  help_text="Username of this computer.")
    model = models.CharField(max_length=200, blank=True, help_text="Model of the computer.")
    processor = models.CharField(max_length=200, blank=True, help_text="Processor of the computer.")
    memory = models.CharField(max_length=200, blank=True,
                              help_text="How much memory have the computer.")
    screen_1 = models.CharField(max_length=200, blank=True,
                                help_text="Model of the screen of the computer.")
    screen_2 = models.CharField(max_length=200, blank=True, help_text="Model of the second screen "
                                "of the computer if this have a second screen.")
    keyboard = models.CharField(max_length=200, blank=True, help_text="keyboard of the computer.")
    mouse = models.CharField(max_length=200, blank=True, help_text="Mouse of the computer.")
    others = models.CharField(max_length=200, blank=True,
                              help_text="Others characteristics of the computer.")
    setup = models.ForeignKey('Setup', blank=True, help_text="In order to the computer is used.")
    created_date = models.DateTimeField(default=timezone.now, help_text="Date when was created.")

    def create(self):
        """
        Create function docstring.

        This function stores the date when the computer was created and save the info.
        """
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        """
        Return string function docstring.

        This function returns the location of a computer.

        @return: a string with the location of a computer.
        """
        return self.name


class Electronic(models.Model):
    """
    Electronic model docstring.

    This model stores the electronic components.
    """

    author = models.ForeignKey('auth.User', null=True)
    type_component = models.ForeignKey('Type_Component',
                                       help_text="Type of the electronic component.")
    name_component = models.CharField(max_length=200, blank=True)
    location = models.ForeignKey('Location', help_text="Where it is the electronic component.")
    unit = models.ForeignKey('Unit', help_text="Unit of the value of the electronic componente.")
    value = models.CharField(max_length=200, blank=True,
                             help_text="Value of the electronic component.")
    created_date = models.DateTimeField(default=timezone.now, help_text="Date when was created.")

    def create(self):
        """
        Create function docstring.

        This function stores the date when the electronic component was created and save the info.
        """
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        """
        Return string function docstring.

        This function returns the location of a electronic component.

        @return: a string with the location of a electronic component.
        """
        return self.name_component


class Optic(models.Model):
    """
    Optic model docstring.

    This model stores the optic components.
    """

    author = models.ForeignKey('auth.User', null=True)
    type_optic = models.ForeignKey('Type_Optic', help_text="Type of the optic component.")
    name_optic = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=300, help_text="Description of the optic component.")
    location = models.ForeignKey('Location', help_text="Where it is the optic component.")
    # unit = models.ForeignKey('Unit', help_text="Unit of the value of the optic component.")
    # value = models.CharField(max_length=200, blank=True,
    #                          help_text="Value of the optic component.")
    created_date = models.DateTimeField(default=timezone.now, help_text="Date when was created.")

    def create(self):
        """
        Create function docstring.

        This function stores the date when the optic component was created and save the info.
        """
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        """
        Return string function docstring.

        This function returns the location of a optic component.

        @return: a string with the location of a optic component.
        """
        return self.name_optic


class Chemical(models.Model):
    """
    Chemical model docstring.

    This model stores the chemicals.
    """

    author = models.ForeignKey('auth.User', null=True)
    type_chemical = models.ForeignKey('Type_Chemical', help_text="Type of the chemical.")
    name = models.CharField(max_length=200, blank=True, help_text="Name of the chemical.")
    reference = models.CharField(max_length=200, blank=True, help_text="Reference of the chemical.")
    cas_number = models.CharField(max_length=200, blank=True, help_text="CAS number of the chemical.")
    number_bottle = models.CharField(max_length=200, blank=True, help_text="Number of bottles of the chemical.")
    quantity = models.CharField(max_length=20, help_text="Quantity of the chemical.")
    state = models.ForeignKey('State', help_text="State of the chemical.")
    supplier = models.ForeignKey('Supplier', help_text="Supplier of the chemical.")
    molecular_weight = models.CharField(max_length=200, blank=True,
                                        help_text="Molecular weight of the chemical.")
    # unit_chemical = models.ForeignKey('Unit_Chemical', help_text="Unit to the "
    #                                   "molecular weight of the chemical.")
    unit_chemical = models.CharField(max_length=20, default="g/mol", help_text="Unit to the "
                                     "molecular weight of the chemical.")
    location = models.ForeignKey('Location', help_text="Where it is the chemical.")
    created_date = models.DateTimeField(default=timezone.now, help_text="Date when was created.")

    def create(self):
        """
        Create function docstring.

        This function stores the date when the chemical was created and save the info.
        """
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        """
        Return string function docstring.

        This function returns the name of a chemical.

        @return: a string with the name of a chemical.
        """
        return self.name


class Biological(models.Model):
    """
    Biological model docstring.

    This model stores the biological components.
    """

    author = models.ForeignKey('auth.User', null=True)
    type_biological = models.ForeignKey('Type_Biological_2',
                                        help_text="Type of the biological component.")
    name = models.CharField(max_length=200, blank=True,
                            help_text="Name of the biological component.")
    reference = models.CharField(max_length=200, blank=True,
                                 help_text="Reference of the biological component.")
    number_bottle = models.CharField(max_length=20, null=True, blank=True, help_text="Number of bottles of the biological component.")
    quantity = models.CharField(max_length=20, blank=True, help_text="Quantity of the biological component.")
    supplier = models.ForeignKey('Supplier', help_text="Supplier of the biological component.")
    concentration = models.CharField(max_length=200, blank=True,
                                     help_text="Concentration of the biological component.")
    unit_biological = models.ForeignKey('Unit_Chemical', blank=True, help_text="Unit to the "
                                        "concentration of the biological.")
    location = models.ForeignKey('Location', help_text="Where it is the biological component.")
    aliquots = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now, help_text="Date when was created.")

    def create(self):
        """
        Create function docstring.

        This function stores the date when the biological component was created and save the info.
        """
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        """
        Return string function docstring.

        This function returns the name of a biological component.

        @return: a string with the name of a biological component.
        """
        return self.name


class Instrumentation(models.Model):
    """
    Instrumentation model docstring.

    This model stores the instruments.
    """

    author = models.ForeignKey('auth.User', null=True)
    type_instrumentation = models.ForeignKey('Type_Instrumentation',
                                             help_text="Type of instrument to be stored.")
    characteristics = models.CharField(max_length=200, blank=True,
                                       help_text="Important features of the instrument.")
    manufacturer = models.CharField(max_length=200, blank=True,
                                    help_text="Manufacturer of the instrument.")
    supplier = models.ForeignKey('Supplier', help_text="Seller of the instrument.")
    location = models.ForeignKey('Location', help_text="Where it is the computer.")
    created_date = models.DateTimeField(default=timezone.now, help_text="Date when was created.")

    def create(self):
        """
        Create function docstring.

        This function stores the date when the instrument was created and save the info.
        """
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        """
        Return string function docstring.

        This function returns the manufacturer of the instrument.

        @return: a string with the manufacturer of the instrument.
        """
        return self.manufacturer


class Consumable(models.Model):
    """
    Consumable model docstring.

    This model stores the consumables.
    """

    author = models.ForeignKey('auth.User', null=True)
    name = models.CharField(max_length=200, blank=True, help_text="Name of the consumable.")
    characteristics = models.CharField(max_length=200, blank=True,
                                       help_text="Important features of the consumable.")
    manufacturer = models.CharField(max_length=200, blank=True,
                                    help_text="Manufacturer of the consumable.")
    supplier = models.ForeignKey('Supplier', help_text="Seller of the consumable.")
    location = models.ForeignKey('Location', help_text="Where it is the consumable.")
    created_date = models.DateTimeField(default=timezone.now, help_text="Date when was created.")

    def create(self):
        """
        Create function docstring.

        This function stores the date when the consumable was created and save the info.
        """
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        """
        Return string function docstring.

        This function returns the name of the consumable.

        @return: a string with the name of the consumable.
        """
        return self.name


class Others(models.Model):
    """
    Others model docstring.

    This model stores the other components of the group.
    """

    name = models.CharField(max_length=200, blank=True, help_text="Name of the component.")
    created_date = models.DateTimeField(default=timezone.now, help_text="Date when was created.")

    def create(self):
        """
        Create function docstring.

        This function stores the date when the component was created and save the info.
        """
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        """
        Return string function docstring.

        This function returns the name of the component.

        @return: a string with the name of the component.
        """
        return self.name


class Type(models.Model):
    """
    Type model docstring.

    This model stores the different types of inventories.
    """

    author = models.ForeignKey('auth.User', help_text="Name of the author that created the type.")
    name = models.CharField(max_length=200, help_text="Name of the type of inventory.")
    created_date = models.DateTimeField(default=timezone.now, help_text="Date when was created.")

    def create(self):
        """
        Create function docstring.

        This function stores the date when the type of inventory was created and save the info.
        """
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        """
        Return string function docstring.

        This function returns the name of the type of inventory.

        @return: a string with the name of the type of inventory.
        """
        return self.name


class Type_Object(models.Model):
    """
    Type object model docstring.

    This model stores the different parts of a computer.
    """

    name = models.CharField(max_length=200, help_text="Name of the part of the computer.")
    created_date = models.DateTimeField(default=timezone.now, help_text="Date when was created.")

    def create(self):
        """
        Create function docstring.

        This function stores the date when the part of computer was created and save the info.
        """
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        """
        Return string function docstring.

        This function returns the name of the part of a computer.

        @return: a string with the name of the part of a computer.
        """
        return self.name


class Type_Component(models.Model):
    """
    Type component model docstring.

    This model stores the different electronic components.
    """

    name = models.CharField(max_length=200, help_text="Name of the type of electronic component.")
    created_date = models.DateTimeField(default=timezone.now, help_text="Date when was created.")

    def create(self):
        """
        Create function docstring.

        This function stores the date when the type of electronic component was created
        and save the info.
        """
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        """
        Return string function docstring.

        This function returns the name of the type of electronic component.

        @return: a string with the name of the type of electronic component.
        """
        return self.name


class Type_Optic(models.Model):
    """
    Type optic model docstring.

    This model stores the different optic components.
    """

    name = models.CharField(max_length=200, help_text="Name of the type of optic component.")
    created_date = models.DateTimeField(default=timezone.now, help_text="Date when was created.")

    def create(self):
        """
        Create function docstring.

        This function stores the date when the type of optic component was created
        and save the info.
        """
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        """
        Return string function docstring.

        This function returns the name of the type of optic component.

        @return: a string with the name of the type of optic component.
        """
        return self.name


class Type_Chemical(models.Model):
    """
    Type chemical model docstring.

    This model stores the different chemicals.
    """

    name = models.CharField(max_length=200, help_text="Name of the type of chemical.")
    # state = models.ForeignKey('State', null=True)
    created_date = models.DateTimeField(default=timezone.now, help_text="Date when was created.")

    def create(self):
        """
        Create function docstring.

        This function stores the date when the type of chemical was created and save the info.
        """
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        """
        Return string function docstring.

        This function returns the name of the type of chemical.

        @return: a string with the name of the type of chemical.
        """
        return self.name


class State(models.Model):
    """
    State model docstring.

    This model stores the different states of a chemical.
    """

    name = models.CharField(max_length=200, help_text="Name of the state of chemical.")
    created_date = models.DateTimeField(default=timezone.now, help_text="Date when was created.")

    def create(self):
        """
        Create function docstring.

        This function stores the date when the state of chemical was created
        and save the info.
        """
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        """
        Return string function docstring.

        This function returns the name of the state of chemical.

        @return: a string with the name of the state of chemical.
        """
        return self.name


class Type_Biological_1(models.Model):
    """
    Type biological 1 model docstring.

    This model stores the different biological components.
    """

    name = models.CharField(max_length=200, help_text="Name of the type of biological component.")
    created_date = models.DateTimeField(default=timezone.now, help_text="Date when was created.")

    def create(self):
        """
        Create function docstring.

        This function stores the date when the type of biological component was created
        and save the info.
        """
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        """
        Return string function docstring.

        This function returns the name of the type of biological component.

        @return: a string with the name of the type of biological component.
        """
        return self.name


class Type_Biological_2(models.Model):
    """
    Type biological 2 model docstring.

    This model stores the different biological components.
    """

    name = models.CharField(max_length=200, help_text="Name of the type of biological component.")
    type_biological_1 = models.ForeignKey('Type_Biological_1')
    created_date = models.DateTimeField(default=timezone.now, help_text="Date when was created.")

    def create(self):
        """
        Create function docstring.

        This function stores the date when the type of biological component was created
        and save the info.
        """
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        """
        Return string function docstring.

        This function returns the name of the type of biological component.

        @return: a string with the name of the type of biological component.
        """
        return self.name


class Type_Instrumentation(models.Model):
    """
    Type instrument model docstring.

    This model stores the different instruments.
    """

    name = models.CharField(max_length=200, help_text="Name of the type of instrument.")
    created_date = models.DateTimeField(default=timezone.now, help_text="Date when was created.")

    def create(self):
        """
        Create function docstring.

        This function stores the date when the type of instrument was created and save the info.
        """
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        """
        Return string function docstring.

        This function returns the name of the type of instrument.

        @return: a string with the name of the type of instrument.
        """
        return self.name


class Location(models.Model):
    """
    Location model docstring.

    This model stores the different locations in the labs and the offices.
    """

    name = models.CharField(max_length=200, help_text="Name of the location of the object.")
    created_date = models.DateTimeField(default=timezone.now, help_text="Date when was created.")

    def create(self):
        """
        Create function docstring.

        This function stores the date when the location was created and save the info.
        """
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        """
        Return string function docstring.

        This function returns the name of the location.

        @return: a string with the name of the location.
        """
        return self.name


# class Closet(models.Model):
#     """
#     Closet model docstring.
#
#     This model stores the different closets in the labs and the offices.
#     """
#
#     name = models.CharField(max_length=200, help_text="Name of the closet.")
#     created_date = models.DateTimeField(default=timezone.now, help_text="Date when was created.")
#
#     def create(self):
#         """
#         Create function docstring.
#
#         This function stores the date when the closet was created and save the info.
#         """
#         self.created_date = timezone.now()
#         self.save()
#
#     def __str__(self):
#         """
#         Return string function docstring.
#
#         This function returns the name of the closet.
#
#         @return: a string with the name of the closet.
#         """
#         return self.name


# class Number_Closet(models.Model):
#     """
#     Number closet model docstring.
#
#     This model stores the different closets with your number in the labs and the offices.
#     """
#
#     name = models.CharField(max_length=200, help_text="Number of the closet.")
#     created_date = models.DateTimeField(default=timezone.now, help_text="Date when was created.")
#
#     def create(self):
#         """
#         Create function docstring.
#
#         This function stores the date when the number of the closet was created and save the info.
#         """
#         self.created_date = timezone.now()
#         self.save()
#
#     def __str__(self):
#         """
#         Return string function docstring.
#
#         This function returns the name of the closet.
#
#         @return: a string with the name of the closet.
#         """
#         return self.name


class Unit(models.Model):
    """
    Unit model docstring.

    This model stores the different units of the different electronic components.
    """

    name = models.CharField(max_length=200, help_text="Unit of the electronic component.")
    created_date = models.DateTimeField(default=timezone.now, help_text="Date when was created.")

    def create(self):
        """
        Create function docstring.

        This function stores the date when the unit of the electronic component was created
        and save the info.
        """
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        """
        Return string function docstring.

        This function returns the name of the unit of the electronic component.

        @return: a string with the name of the unit of the electronic component.
        """
        return self.name


class Unit_Chemical(models.Model):
    """
    Unit chemical model docstring.

    This model stores the different units of the different chemical.
    """

    name = models.CharField(max_length=200, help_text="Unit of the chemical.")
    created_date = models.DateTimeField(default=timezone.now, help_text="Date when was created.")

    def create(self):
        """
        Create function docstring.

        This function stores the date when the unit of the chemical was created and save the info.
        """
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        """
        Return string function docstring.

        This function returns the name of the unit of the chemical.

        @return: a string with the name of the unit of the chemical.
        """
        return self.name


class Full_Name_Users(models.Model):
    """
    Full name users model docstring.

    This model stores the different full name of the users.
    """

    name = models.CharField(max_length=200, help_text="Full name of the users.")
    created_date = models.DateTimeField(default=timezone.now, help_text="Date when was created.")

    def create(self):
        """
        Create function docstring.

        This function stores the date when the full name of the user was created and save the info.
        """
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        """
        Return string function docstring.

        This function returns the full name of the user.

        @return: a string with the full name of the user.
        """
        return self.name


class Setup(models.Model):
    """
    Setup model docstring.

    This model stores the different setups of the computers.
    """

    name = models.CharField(max_length=200, help_text="Name of the setup.")
    created_date = models.DateTimeField(default=timezone.now, help_text="Date when was created.")

    def create(self):
        """
        Create function docstring.

        This function stores the date when the setup of the computer was created and save the info.
        """
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        """
        Return string function docstring.

        This function returns the name of the setup.

        @return: a string with the name of the setup.
        """
        return self.name


""" ------------------------------ """


""" Models Order """


class Order(models.Model):
    """
    Order model docstring.

    This model stores the different orders of the group.
    """

    author = models.ForeignKey('auth.User', help_text="Username of who create the order.")
    name = models.CharField(max_length=200, help_text="Name of the order to save it.")
    # name = models.ForeignKey('auth.User')
    applicant = models.CharField(max_length=200, help_text="Name of who do the order.")
    budget = models.ForeignKey('Budget', help_text="Budget in where load the order.")
    type_of_purchase = models.ForeignKey('Type_of_purchase',
                                         help_text="Type of purchase of the order.")
    payment_conditions = models.ForeignKey('Payment',
                                           help_text="Conditions of payment of the order.")
    supplier = models.ForeignKey('Supplier', help_text="Who provide of components of the order.")
    name_supplier = models.CharField(max_length=200, null=True)
    file_exists = models.BooleanField(default=False,
                                      help_text="To know if this order has a file assigned.")
    name_file_attach = models.CharField(max_length=200, help_text="Name of the file upload.",
                                        null=True, blank=True)
    order_sent = models.BooleanField(default=False)
    group_notified = models.BooleanField(default=False)
    # product = models.ForeignKey('Product', null=True)
    # number_product = models.IntegerField(default=1, help_text="Number of products to order.")
    created_date = models.DateTimeField(default=timezone.now, help_text="Date when was created.")

    def create(self):
        """
        Create function docstring.

        This function stores the date when the order was created and save the info.
        """
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        """
        Return string function docstring.

        This function returns the name of the order.

        @return: a string with the name of the order.
        """
        return self.name


class Budget(models.Model):
    """
    Budget model docstring.

    This model stores the different budget of the group.
    """

    name = models.CharField(max_length=200, help_text="Name of the budget.")
    created_date = models.DateTimeField(default=timezone.now, help_text="Date when was created.")

    def create(self):
        """
        Create function docstring.

        This function stores the date when the budget was created and save the info.
        """
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        """
        Return string function docstring.

        This function returns the name of the budget.

        @return: a string with the name of the budget.
        """
        return self.name


class Type_of_purchase(models.Model):
    """
    Type of purchase model docstring.

    This model stores the different purchases possible.
    """

    name = models.CharField(max_length=200, help_text="Name of the purchase.")
    created_date = models.DateTimeField(default=timezone.now, help_text="Date when was created.")

    def create(self):
        """
        Create function docstring.

        This function stores the date when the purchase was created and save the info.
        """
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        """
        Return string function docstring.

        This function returns the name of the purchase.

        @return: a string with the name of the purchase.
        """
        return self.name


class Payment(models.Model):
    """
    Payment model docstring.

    This model stores the different payments possible.
    """

    name = models.CharField(max_length=200, help_text="Name of the conditions of payment.")
    created_date = models.DateTimeField(default=timezone.now, help_text="Date when was created.")

    def create(self):
        """
        Create function docstring.

        This function stores the date when the payment was created and save the info.
        """
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        """
        Return string function docstring.

        This function returns the name of the payment.

        @return: a string with the name of the payment.
        """
        return self.name


class Supplier(models.Model):
    """
    Supplier model docstring.

    This model stores the different suppliers.
    """

    name = models.CharField(max_length=200)
    attention = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    city_postCode = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    fax = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    created_date = models.DateTimeField(default=timezone.now, help_text="Date when was created.")

    def create(self):
        """
        Create function docstring.

        This function stores the date when the supplier was created and save the info.
        """
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        """
        Return string function docstring.

        This function returns the name of the supplier.

        @return: a string with the name of the supplier.
        """
        return self.name


class Product(models.Model):
    """
    Product model docstring.

    This model stores the different products.
    """

    description = models.CharField(max_length=300, help_text="Description of the product.")
    quantity = models.CharField(max_length=20,
                                help_text="Quantity of the product that are ordered.")
    unit_price = models.CharField(max_length=20, help_text="Price per unit of the product.")
    order = models.ForeignKey('Order', null=True, blank=True,
                              help_text="To what order is assigned.")
    created_date = models.DateTimeField(default=timezone.now, help_text="Date when was created.")

    def create(self):
        """
        Create function docstring.

        This function stores the date when the product was created and save the info.
        """
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        """
        Return string function docstring.

        This function returns the name of the product.

        @return: a string with the name of the product.
        """
        return self.description


""" ------------------------------ """


class Run(models.Model):
    """
    Run model docstring.

    This model stores the different runs.
    """

    run = models.IntegerField(help_text="ID of the run.")
    run_specifications = models.TextField(max_length=500, help_text="Specifications of the run.")
    created_date = models.DateTimeField(default=timezone.now, help_text="Date when was created.")

    def create(self):
        """
        Create function docstring.

        This function stores the date when the run was created and save the info.
        """
        self.created_date = timezone.now()
        self.save()

    def __int__(self):
        """
        Return integer function docstring.

        This function returns the ID of the run.

        @return: a integer with the ID of the run.
        """
        return self.run


class Wafer(models.Model):
    """
    Wafer model docstring.

    This model stores the different wafers.
    """

    run = models.ForeignKey('Run', help_text="To what run is assigned.")
    wafer = models.IntegerField(help_text="Id of the wafer.")
    name_wafer = models.CharField(max_length=50, default="", help_text="ID of the wafer.")
    comments = models.TextField(max_length=500, blank=True, default="", help_text="Comments of the wafer.")
    created_date = models.DateTimeField(default=timezone.now, help_text="Date when was created.")

    def create(self):
        """
        Create function docstring.

        This function stores the date when the wafer was created and save the info.
        """
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        """
        Return string function docstring.

        This function returns the ID of the wafer.

        @return: a string with the ID of the wafer.
        """
        return self.name_wafer


class Chip(models.Model):
    """
    Chip model docstring.

    This model stores the different chips.
    """

    run = models.ForeignKey('Run', help_text="To what run is assigned.")
    wafer = models.ForeignKey('Wafer', help_text="To what wafer is assigned.")
    # chip = models.IntegerField(help_text="ID of the chip.")
    chip = models.CharField(max_length=50, help_text="ID of the chip.")
    date = models.DateField(blank=True, null=True, help_text="MM/DD/YY")
    laser_source = models.CharField(max_length=50, blank=True,
                                    help_text="Source of light that is used.")
    readout = models.CharField(max_length=50, blank=True,
                               help_text="What type of sensor is used to read.")
    user_name = models.ForeignKey('Full_Name_Users', blank=True, null=True,
                                  help_text="Who have the chip.")
    comments = models.TextField(max_length=500, blank=True, default="", help_text="Comments of the chip.")
    created_date = models.DateTimeField(default=timezone.now, help_text="Date when was created.")

    def create(self):
        """
        Create function docstring.

        This function stores the date when the chip was created and save the info.
        """
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        """
        Return integer function docstring.

        This function returns the ID of the chip.

        @return: a integer with the ID of the chip.
        """
        return self.chip


class Waveguide(models.Model):
    """
    Waveguide model docstring.

    This model stores the different Waveguides.
    """

    run = models.ForeignKey('Run', help_text="To what run is assigned.")
    wafer = models.ForeignKey('Wafer', help_text="To what wafer is assigned.")
    chip = models.ForeignKey('Chip', null=True, help_text="To what chip is assigned.")
    waveguide = models.ForeignKey('Name_Waveguide', blank=True, help_text="ID of the waveguide.")
    name = models.CharField(max_length=100, blank=True, help_text="Name of the waveguide.")
    amplitude = models.FloatField(blank=True, null=True, help_text="Amplitude of the signal.")
    offset = models.FloatField(blank=True, null=True, help_text="")
    frecuency = models.FloatField(blank=True, null=True, help_text="Frequency of the signal.")
    i_up = models.FloatField(blank=True, null=True, help_text="Value of the current up.")
    i_down = models.FloatField(blank=True, null=True, help_text=" Value of the current down.")
    slope = models.FloatField(blank=True, null=True, help_text="Slope of the signal.")
    visibility = models.FloatField(blank=True, null=True, help_text="Visibility of th e signal.")
    noise = models.FloatField(blank=True, null=True, help_text="Noise in the signal.")
    lod = models.FloatField(blank=True, null=True, help_text="")
    comments = models.TextField(max_length=500, blank=True, default="", help_text="Comments of the waveguide.")
    created_date = models.DateTimeField(default=timezone.now, help_text="Date when was created.")

    def create(self):
        """
        Create function docstring.

        This function stores the date when the waveguide was created and save the info.
        """
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        """
        Return string function docstring.

        This function returns the name of the waveguide.

        @return: a string with the name of the waveguide.
        """
        return self.name


class Name_Waveguide(models.Model):
    """
    Name waveguide model docstring.

    This model stores the different names of the waveguide.
    """

    name = models.CharField(max_length=50, help_text="Name of the waveguide.")
    created_date = models.DateTimeField(default=timezone.now, help_text="Date when was created.")

    def create(self):
        """
        Create function docstring.

        This function stores the date when the name of the waveguide was created and save the info.
        """
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        """
        Return string function docstring.

        This function returns the name of the waveguide.

        @return: a string with the name of the waveguide.
        """
        return self.name


class Messages(models.Model):
    """
    Messages model docstring.

    This model stores the different messages about the updates.
    """

    messageText = models.TextField(help_text="Message about the update.")
    show = models.BooleanField(default=True, help_text="It is used to show the message.")
    author = models.ForeignKey('auth.User',
                               help_text="Name of the author that created the message.")
    created_date = models.DateTimeField(default=timezone.now, help_text="Date when was created.")

    def create(self):
        """
        Create function docstring.

        This function stores the date when the message was created and save the info.
        """
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        """
        Return string function docstring.

        This function returns the message.

        @return: a string with the message.
        """
        return self.messageText
