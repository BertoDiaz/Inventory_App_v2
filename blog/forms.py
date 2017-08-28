from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.encoding import smart_text
from .models import Element, Order, Product, Computing, Electronic, Chemical, Instrumentation
from .models import Others, Full_Name_Users


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )


class ElementForm(forms.ModelForm):

    class Meta:
        model = Element
        fields = ('name', 'maker', 'type_item',)


class UserFullNameForm(forms.ModelForm):
    """docstring for UserFullNameForm."""

    class Meta:
        model = Full_Name_Users
        fields = ('name',)


class OrderForm(forms.ModelForm):
    # name = UserFullnameChoiceField(queryset=User.objects.all())
    # name = UserFullnameChoiceField(User.objects.filter(author=request.user))

    class Meta:
        model = Order
        fields = ('name', 'applicant', 'budget', 'type_of_purchase', 'payment_conditions',
                  'supplier', 'number_product',)


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('description', 'quantity', 'unit_price', 'order',)
        widgets = {'order': forms.HiddenInput()}


class ComputingForm(forms.ModelForm):

    class Meta:
        model = Computing
        fields = ('name', 'type_object', 'location', 'user_name', 'model', 'processor', 'memory',
                  'screen_1', 'screen_2', 'keyboard', 'mouse', 'others', 'setup',)


class ElectronicForm(forms.ModelForm):

    class Meta:
        model = Electronic
        fields = ('type_component', 'location', 'closet', 'unit', 'value',)


class ChemicalForm(forms.ModelForm):

    class Meta:
        model = Chemical
        fields = ('type_chemical', 'name', 'reference', 'quantity', 'supplier', 'concentration',
                  'unit_chemical', 'location', 'closet',)


class InstrumentationForm(forms.ModelForm):

    class Meta:
        model = Instrumentation
        fields = ('type_instrumentation', 'characteristics', 'manufacturer', 'supplier',
                  'location',)


class OthersForm(forms.ModelForm):

    class Meta:
        model = Others
        fields = ('name',)
