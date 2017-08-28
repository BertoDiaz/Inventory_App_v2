from django.db import models
from django.utils import timezone

""" Models Inventory """


class Element(models.Model):
    """docstring for Element."""

    author = models.ForeignKey('auth.User')
    type_item = models.ForeignKey('Type')
    name = models.CharField(max_length=200)
    maker = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)

    def create(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name


class Computing(models.Model):
    """docstring for Computing."""

    name = models.CharField(max_length=200, blank=True)
    type_object = models.ForeignKey('Type_Object')
    location = models.ForeignKey('Location')
    user_name = models.ForeignKey('Full_Name_Users', blank=True)
    model = models.CharField(max_length=200, blank=True)
    processor = models.CharField(max_length=200, blank=True)
    memory = models.CharField(max_length=200, blank=True)
    screen_1 = models.CharField(max_length=200, blank=True)
    screen_2 = models.CharField(max_length=200, blank=True)
    keyboard = models.CharField(max_length=200, blank=True)
    mouse = models.CharField(max_length=200, blank=True)
    others = models.CharField(max_length=200, blank=True)
    setup = models.ForeignKey('Setup', blank=True)
    created_date = models.DateTimeField(default=timezone.now)

    def create(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.location


class Electronic(models.Model):
    """docstring for Electronic."""

    type_component = models.ForeignKey('Type_Component')
    location = models.ForeignKey('Location')
    closet = models.ForeignKey('Closet')
    unit = models.ForeignKey('Unit')
    value = models.CharField(max_length=200, blank=True)
    created_date = models.DateTimeField(default=timezone.now)

    def create(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.location


class Chemical(models.Model):
    """docstring for Chemical."""

    type_chemical = models.ForeignKey('Type_Chemical')
    name = models.CharField(max_length=200, blank=True)
    reference = models.CharField(max_length=200, blank=True)
    quantity = models.CharField(max_length=20)
    supplier = models.ForeignKey('Supplier')
    concentration = models.CharField(max_length=200, blank=True)
    unit_chemical = models.ForeignKey('Unit_Chemical')
    location = models.ForeignKey('Location')
    closet = models.ForeignKey('Closet')
    created_date = models.DateTimeField(default=timezone.now)

    def create(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name


class Instrumentation(models.Model):
    """docstring for Instrumentation."""

    type_instrumentation = models.ForeignKey('Type_Instrumentation')
    characteristics = models.CharField(max_length=200, blank=True)
    manufacturer = models.CharField(max_length=200, blank=True)
    supplier = models.ForeignKey('Supplier')
    location = models.ForeignKey('Location')
    created_date = models.DateTimeField(default=timezone.now)

    def create(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.manufacturer


class Others(models.Model):
    """docstring for Others."""

    name = models.CharField(max_length=200, blank=True)
    created_date = models.DateTimeField(default=timezone.now)

    def create(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name


class Type(models.Model):
    """docstring for Type."""

    author = models.ForeignKey('auth.User')
    name = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)

    def create(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name


class Type_Object(models.Model):
    """docstring for Type_Object."""

    name = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)

    def create(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name


class Type_Component(models.Model):
    """docstring for Type_Component."""

    name = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)

    def create(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name


class Type_Chemical(models.Model):
    """docstring for Type_Chemical."""

    name = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)

    def create(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name


class Type_Instrumentation(models.Model):
    """docstring for Type_Instrumentation."""

    name = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)

    def create(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name


class Location(models.Model):
    """docstring for Location."""

    name = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)

    def create(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name


class Closet(models.Model):
    """docstring Closet."""

    name = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)

    def create(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name


class Number_Closet(models.Model):
    """docstring for Number_Closet."""

    name = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)

    def create(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name


class Unit(models.Model):
    """docstring for Unit."""

    name = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)

    def create(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name


class Unit_Chemical(models.Model):
    """docstring for Unit_Chemical."""

    name = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)

    def create(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name


class Full_Name_Users(models.Model):
    """docstring for Full_Name_Users."""

    name = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)

    def create(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name


class Setup(models.Model):
    """docstring for Setup."""

    name = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)

    def create(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name


""" ------------------------------ """


""" Models Order """


class Order(models.Model):
    """docstring for Order."""

    author = models.ForeignKey('auth.User')
    name = models.CharField(max_length=200)
    # name = models.ForeignKey('auth.User')
    applicant = models.CharField(max_length=200)
    budget = models.ForeignKey('Budget')
    type_of_purchase = models.ForeignKey('Type_of_purchase')
    payment_conditions = models.ForeignKey('Payment')
    supplier = models.ForeignKey('Supplier')
    # product = models.ForeignKey('Product', null=True)
    number_product = models.IntegerField(default=1)
    created_date = models.DateTimeField(default=timezone.now)

    def create(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name


class Budget(models.Model):
    """docstring for Budget."""

    name = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)

    def create(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name


class Type_of_purchase(models.Model):
    """docstring for Type_of_purchase."""

    name = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)

    def create(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name


class Payment(models.Model):
    """docstring for Payment."""

    name = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)

    def create(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name


class Supplier(models.Model):
    """docstring for Supplier."""

    name = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)

    def create(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name


class Product(models.Model):
    """docstring for Product."""

    description = models.CharField(max_length=300)
    quantity = models.CharField(max_length=20)
    unit_price = models.CharField(max_length=20)
    order = models.ForeignKey('Order', null=True, blank=True)
    created_date = models.DateTimeField(default=timezone.now)

    def create(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.description


""" ------------------------------ """
