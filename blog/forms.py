from django import forms
from .models import Element, Order, Product, Computing, Electronic, Chemical, Instrumentation
from .models import Others


class ElementForm(forms.ModelForm):

    class Meta:
        model = Element
        fields = ('name', 'maker', 'type_item',)


class OrderForm(forms.ModelForm):

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
