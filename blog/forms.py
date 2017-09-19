"""forms.py."""

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from django.utils.encoding import smart_text
from .models import Element, Order, Product, Computing, Electronic, Optic, Chemical, Biological
from .models import Instrumentation, Others, Full_Name_Users, Run, Wafer, Chip, Waveguide


class SignUpForm(UserCreationForm):
    """
    Sign up form docstring.

    This form is useds to create a new username with first name, last name and email.
    """

    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        """
        Meta docstring.

        This function use the User model and the fields: username, first name, last name, email,
        password 1 and password 2.
        """

        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )


class ElementForm(forms.ModelForm):
    """
    Element form docstring.

    This form is useds to create a new element.
    """

    class Meta:
        """
        Meta docstring.

        This function use the Element model and the fields: name, maker and type_item.
        """

        model = Element
        fields = ('name', 'maker', 'type_item',)


class UserFullNameForm(forms.ModelForm):
    """
    User full name form docstring.

    This form is useds to create a new full name of an username.
    """

    class Meta:
        """
        Meta docstring.

        This function use the Full_Name_Users model and the field: name.
        """

        model = Full_Name_Users
        fields = ('name',)


class OrderForm(forms.ModelForm):
    """
    Order form docstring.

    This form is useds to create a new order.
    """

    # name = UserFullnameChoiceField(queryset=User.objects.all())
    # name = UserFullnameChoiceField(User.objects.filter(author=request.user))

    class Meta:
        """
        Meta docstring.

        This function use the Order model and the fields: name, applicant, budget, type_of_purchase,
        payment_conditions, supplier and number_product.
        """

        model = Order
        fields = ('name', 'applicant', 'budget', 'type_of_purchase', 'payment_conditions',
                  'supplier', 'number_product',)


class ProductForm(forms.ModelForm):
    """
    Product form docstring.

    This form is useds to create a new product.
    """

    class Meta:
        """
        Meta docstring.

        This function use the Product model and the fields: description, quantity, unit_price
        and order, moreover, this have a hide field: order that is completed in the views.py.
        """

        model = Product
        fields = ('description', 'quantity', 'unit_price', 'order',)
        widgets = {'order': forms.HiddenInput()}


class ComputingForm(forms.ModelForm):
    """
    Computing form docstring.

    This form is useds to create a new Computer.
    """

    class Meta:
        """
        Meta docstring.

        This function use the Computing model and the fields: name, type_object, location,
        user_name, model, processor, memory, screen_1, screen_2, keyboard, mouse, others and setup.
        """

        model = Computing
        fields = ('name', 'type_object', 'location', 'user_name', 'model', 'processor', 'memory',
                  'screen_1', 'screen_2', 'keyboard', 'mouse', 'others', 'setup',)


class ElectronicForm(forms.ModelForm):
    """
    Electronic form docstring.

    This form is useds to create a new electronic component.
    """

    class Meta:
        """
        Meta docstring.

        This function use the Electronic model and the fields: type_component, location, closet,
        unit and value.
        """

        model = Electronic
        fields = ('type_component', 'location', 'closet', 'unit', 'value',)


class OpticForm(forms.ModelForm):
    """
    Optic form docstring.

    This form is useds to create a new optic component.
    """

    class Meta:
        """
        Meta docstring.

        This function use the Optic model and the fields: type_optic, description, location
        and closet
        """

        model = Optic
        fields = ('type_optic', 'description', 'location', 'closet',)


class ChemicalForm(forms.ModelForm):
    """
    Chemical form docstring.

    This form is useds to create a new chemical.
    """

    class Meta:
        """
        Meta docstring.

        This function use the Chemical model and the fields: type_chemical, name, reference,
        quantity, supplier, concentration, molecular_weight, unit_chemical, location and closet.
        """

        model = Chemical
        fields = ('type_chemical', 'name', 'reference', 'quantity', 'supplier', 'concentration',
                  'molecular_weight', 'unit_chemical', 'location', 'closet',)


class BiologicalForm(forms.ModelForm):
    """
    Biological form docstring.

    This form is useds to create a new biological component.
    """

    class Meta:
        """
        Meta docstring.

        This function use the Biological model and the fields: type_biological, name, reference,
        quantity, supplier, concentration, molecular_weight, unit_chemical, location and closet.
        """

        model = Biological
        fields = ('type_biological', 'name', 'reference', 'quantity', 'supplier', 'concentration',
                  'molecular_weight', 'unit_chemical', 'location', 'closet',)


class InstrumentationForm(forms.ModelForm):
    """
    Instrumentation form docstring.

    This form is useds to create a new instrument.
    """

    class Meta:
        """
        Meta docstring.

        This function use the Instrumentation model and the fields: type_instrumentation,
        characteristics, manufacturer, supplier and location.
        """

        model = Instrumentation
        fields = ('type_instrumentation', 'characteristics', 'manufacturer', 'supplier',
                  'location',)


class OthersForm(forms.ModelForm):
    """
    Others form docstring.

    This form is useds to create a new component without category.
    """

    class Meta:
        """
        Meta docstring.

        This function use the Others model and the field: name.
        """

        model = Others
        fields = ('name',)


class RunForm(forms.ModelForm):
    """
    Run form docstring.

    This form is useds to create a new run.
    """

    class Meta:
        """
        Meta docstring.

        This function use the Run model and the fields: run and run_specifications.
        """

        model = Run
        fields = ('run', 'run_specifications',)


class WaferForm(forms.ModelForm):
    """
    Wafer form docstring.

    This form is useds to create a new wafer.
    """

    class Meta:
        """
        Meta docstring.

        This function use the Wafer model and the fields: wafer.
        """

        model = Wafer
        fields = ('wafer',)


class ChipForm(forms.ModelForm):
    """
    Chip form docstring.

    This form is useds to create a new chip.
    """

    class Meta:
        """
        Meta docstring.

        This function use the Chip model and the fields: chip, date, laser_source, readout
        and user_name.
        """

        model = Chip
        fields = ('chip', 'date', 'laser_source', 'readout', 'user_name',)


class WaveguideForm(forms.ModelForm):
    """
    Waveguide form docstring.

    This form is useds to create a new waveguide.
    """

    class Meta:
        """
        Meta docstring.

        This function use the Waveguide model and the fields: waveguide, amplitude, offset,
        frecuency, i_up, i_down, slope, visibility, noise and lod.
        """

        model = Waveguide
        fields = ('waveguide', 'amplitude', 'offset', 'frecuency', 'i_up', 'i_down', 'slope',
                  'visibility', 'noise', 'lod',)
