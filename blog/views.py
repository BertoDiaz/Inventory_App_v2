"""views.py."""

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.forms.formsets import formset_factory
from django.utils import timezone
from django.contrib.auth import login, authenticate
import openpyxl
from openpyxl.styles.borders import Border, Side
from openpyxl.drawing.image import Image
from .models import Element, Order, Product, Computing, Electronic, Chemical, Instrumentation
from .models import Others, Full_Name_Users, Run, Chip, Wafer, Waveguide
from .forms import ElementForm, OrderForm, ProductForm, ComputingForm, ElectronicForm, ChemicalForm
from .forms import InstrumentationForm, OthersForm, SignUpForm, RunForm, WaferForm, ChipForm
from .forms import WaveguideForm


def home(request):
    """
    Home function docstring.

    This function shows the main page.

    @param request: HTML request page.
    @return: Main page.
    """
    return render(request, 'blog/home.html')


def signup(request):
    """
    Signup function docstring.

    This function carries out the registration of a new user.

    @param request: HTML request page.
    @return: First time, return to sign up page. If the sign up form is completed, return to home
             page with your username.
    """
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            firstname = form.cleaned_data.get('first_name')
            lastname = form.cleaned_data.get('last_name')
            nameFull = firstname + ' ' + lastname
            fullName = Full_Name_Users()
            fullName.name = nameFull
            fullName.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('blog:home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


def element_list(request):
    """
    Element_list function docstring.

    This function shows the different elements of this web app that are ordered by creation date.

    @param request: HTML request page.
    @return: list of elements.
    """
    elements = Element.objects.filter(created_date__lte=timezone.now()).order_by('created_date')

    return render(request, 'blog/element_list.html', {'elements': elements})


def element_detail(request, pk):
    """
    Element_detail function docstring.

    This function shows the information of an element.

    @param request: HTML request page.
    @param pk: primary key of the element.
    @return: one element.
    @raise 404: element does not exists.
    """
    element = get_object_or_404(Element, pk=pk)

    return render(request, 'blog/element_detail.html', {'element': element})


@login_required
def element_new(request):
    """
    Element_new function docstring.

    This function shows the form to create a new element.

    @param request: HTML request page.
    @return: First time, this shows the form to a new element. If the form is completed, return the
             details of this new element.
    """
    if request.method == "POST":
        form = ElementForm(request.POST)
        if form.is_valid():
            element = form.save(commit=False)
            element.author = request.user
            # element.published_date = timezone.now()
            element.save()
            return redirect('blog:element_detail', pk=element.pk)
    else:
        form = ElementForm()
    return render(request, 'blog/element_edit.html', {'form': form})


@login_required
def element_edit(request, pk):
    """
    Element_edit function docstring.

    This function shows the form to modify an element.

    @param request: HTML request page.
    @param pk: primary key of the element to modify.
    @return: First time, this shows the form to edit the element. If the form is completed, return
             the details of this element.
    @raise 404: element does not exists.
    """
    element = get_object_or_404(Element, pk=pk)
    if request.method == "POST":
        form = ElementForm(data=request.POST, instance=element)
        if form.is_valid():
            element = form.save(commit=False)
            element.author = request.user
            element.save()
            return redirect('blog:element_detail', pk=element.pk)
    else:
        form = ElementForm(instance=element)
    return render(request, 'blog/element_edit.html', {'form': form})


@login_required
def element_remove(request, pk):
    """
    Element_remove function docstring.

    This function removes an element.

    @param request: HTML request page.
    @param pk: primary key of the element to remove.
    @return: list of elements.
    @raise 404: element does not exists.
    """
    element = get_object_or_404(Element, pk=pk)
    element.delete()
    return redirect('blog:element_list')


def computing_list(request):
    """
    Computing_list function docstring.

    This function shows the list of computers that are stored in this web app and they are
    ordered by creation date.

    @param request: HTML request page.
    @return: list of computers.
    """
    computings = Computing.objects.filter(created_date__lte=timezone.now()).order_by('created_date')

    return render(request, 'blog/computing_list.html', {'computings': computings})


def computing_detail(request, pk):
    """
    Computing_detail function docstring.

    This function shows the information of a computer.

    @param request: HTML request page.
    @param pk: primary key of the computer.
    @return: one computer.
    @raise 404: computer does not exists.
    """
    computing = get_object_or_404(Computing, pk=pk)

    return render(request, 'blog/computing_detail.html', {'computing': computing})


@login_required
def computing_new(request):
    """
    Computing_new function docstring.

    This function shows the form to create a new computer.

    @param request: HTML request page.
    @return: First time, this shows the form to a new computer. If the form is completed, return the
             details of this new computer.
    """
    if request.method == "POST":
        form = ComputingForm(request.POST)
        if form.is_valid():
            computing = form.save(commit=False)
            computing.save()
            return redirect('blog:computing_detail', pk=computing.pk)
    else:
        form = ComputingForm()
    return render(request, 'blog/computing_edit.html', {'form': form})


@login_required
def computing_edit(request, pk):
    """
    Computing_edit function docstring.

    This function shows the form to modify a computer.

    @param request: HTML request page.
    @param pk: primary key of the computer to modify.
    @return: First time, this shows the form to edit the computer information. If the form is
    completed, return the details of this computer.
    @raise 404: computer does not exists.
    """
    computing = get_object_or_404(Computing, pk=pk)
    if request.method == "POST":
        form = ComputingForm(data=request.POST, instance=computing)
        if form.is_valid():
            computing = form.save(commit=False)
            computing.save()
            return redirect('blog:computing_detail', pk=computing.pk)
    else:
        form = ComputingForm(instance=computing)
    return render(request, 'blog/computing_edit.html', {'form': form})


@login_required
def computing_remove(request, pk):
    """
    Computing_remove function docstring.

    This function removes a computer.

    @param request: HTML request page.
    @param pk: primary key of the computer to remove.
    @return: list of computers.
    @raise 404: computer does not exists.
    """
    computing = get_object_or_404(Computing, pk=pk)
    computing.delete()
    return redirect('blog:computing_list')


def electronic_list(request):
    """
    Electronic_list function docstring.

    This function shows the list of electronic components that are stored in this web app and
    they are ordered by creation date.

    @param request: HTML request page.
    @return: list of electronic components.
    """
    electronics = Electronic.objects.filter(
        created_date__lte=timezone.now()).order_by('created_date')

    print(electronics)

    return render(request, 'blog/electronic_list.html', {'electronics': electronics})


def electronic_detail(request, pk):
    """
    Electronic_detail function docstring.

    This function shows the information of a electronic component.

    @param request: HTML request page.
    @param pk: primary key of the electronic component.
    @return: one electronic component.
    @raise 404: electronic component does not exists.
    """
    electronic = get_object_or_404(Electronic, pk=pk)

    return render(request, 'blog/electronic_detail.html', {'electronic': electronic})


@login_required
def electronic_new(request):
    """
    Electronic_new function docstring.

    This function shows the form to create a new electronic component.

    @param request: HTML request page.
    @return: First time, this shows the form to a new electronic component. If the form is
    completed, return the details of this new electronic component.
    """
    if request.method == "POST":
        form = ElectronicForm(request.POST)
        if form.is_valid():
            electronic = form.save(commit=False)
            electronic.save()
            return redirect('blog:electronic_detail', pk=electronic.pk)
    else:
        form = ElectronicForm()
    return render(request, 'blog/electronic_edit.html', {'form': form})


@login_required
def electronic_edit(request, pk):
    """
    Electronic_edit function docstring.

    This function shows the form to modify a electronic component.

    @param request: HTML request page.
    @param pk: primary key of the electronic component to modify.
    @return: First time, this shows the form to edit the electronic component information. If the
    form is completed, return the details of this electronic component.
    @raise 404: electronic component does not exists.
    """
    electronic = get_object_or_404(Electronic, pk=pk)
    if request.method == "POST":
        form = ElectronicForm(data=request.POST, instance=electronic)
        if form.is_valid():
            electronic = form.save(commit=False)
            electronic.save()
            return redirect('blog:electronic_detail', pk=electronic.pk)
    else:
        form = ElectronicForm(instance=electronic)
    return render(request, 'blog/electronic_edit.html', {'form': form})


@login_required
def electronic_remove(request, pk):
    """
    Electronic_remove function docstring.

    This function removes a electronic component.

    @param request: HTML request page.
    @param pk: primary key of the electronic component to remove.
    @return: list of electronic components.
    @raise 404: electronic component does not exists.
    """
    electronic = get_object_or_404(Electronic, pk=pk)
    electronic.delete()
    return redirect('blog:electronic_list')


def chemical_list(request):
    """
    Chemical_list function docstring.

    This function shows the list of chemicals that are stored in this web app and they are
    ordered by creation date.

    @param request: HTML request page.
    @return: list of chemicals.
    """
    chemicals = Chemical.objects.filter(created_date__lte=timezone.now()).order_by('created_date')

    return render(request, 'blog/chemical_list.html', {'chemicals': chemicals})


def chemical_detail(request, pk):
    """
    Chemical_detail function docstring.

    This function shows the information of a chemical.

    @param request: HTML request page.
    @param pk: primary key of the chemical.
    @return: one chemical.
    @raise 404: chemical does not exists.
    """
    chemical = get_object_or_404(Chemical, pk=pk)

    return render(request, 'blog/chemical_detail.html', {'chemical': chemical})


@login_required
def chemical_new(request):
    """
    Chemical_new function docstring.

    This function shows the form to create a new chemical.

    @param request: HTML request page.
    @return: First time, this shows the form to a new chemical. If the form is completed, return
             the details of this new chemical.
    """
    if request.method == "POST":
        form = ChemicalForm(request.POST)
        if form.is_valid():
            chemical = form.save(commit=False)
            chemical.save()
            return redirect('blog:chemical_detail', pk=chemical.pk)
    else:
        form = ChemicalForm()
    return render(request, 'blog/chemical_edit.html', {'form': form})


@login_required
def chemical_edit(request, pk):
    """
    Chemical_edit function docstring.

    This function shows the form to modify a chemical.

    @param request: HTML request page.
    @param pk: primary key of the chemical to modify.
    @return: First time, this shows the form to edit the chemical information. If the form is
             completed, return the details of this chemical.
    @raise 404: chemical does not exists.
    """
    chemical = get_object_or_404(Chemical, pk=pk)
    if request.method == "POST":
        form = ChemicalForm(data=request.POST, instance=chemical)
        if form.is_valid():
            chemical = form.save(commit=False)
            chemical.save()
            return redirect('blog:chemical_detail', pk=chemical.pk)
    else:
        form = ChemicalForm(instance=chemical)
    return render(request, 'blog/chemical_edit.html', {'form': form})


@login_required
def chemical_remove(request, pk):
    """
    Chemical_remove function docstring.

    This function removes a chemical.

    @param request: HTML request page.
    @param pk: primary key of the chemical to remove.
    @return: list of chemicals.
    @raise 404: chemical does not exists.
    """
    chemical = get_object_or_404(Chemical, pk=pk)
    chemical.delete()
    return redirect('blog:chemical_list')


def instrumentation_list(request):
    """
    Instrumentation_list function docstring.

    This function shows the list of instruments that are stored in this web app and they are
    ordered by creation date.

    @param request: HTML request page.
    @return: list of instruments.
    """
    instrumentations = Instrumentation.objects.filter(
        created_date__lte=timezone.now()).order_by('created_date')

    return render(request, 'blog/instrumentation_list.html', {'instrumentations': instrumentations})


def instrumentation_detail(request, pk):
    """
    Instrumentation_detail function docstring.

    This function shows the information of a instrument.

    @param request: HTML request page.
    @param pk: primary key of the instrument.
    @return: one instrument.
    @raise 404: instrument does not exists.
    """
    instrumentation = get_object_or_404(Instrumentation, pk=pk)

    return render(request, 'blog/instrumentation_detail.html', {'instrumentation': instrumentation})


@login_required
def instrumentation_new(request):
    """
    Instrumentation_new function docstring.

    This function shows the form to create a new instrument.

    @param request: HTML request page.
    @return: First time, this shows the form to a new instrument. If the form is completed, return
             the details of this new instrument.
    """
    if request.method == "POST":
        form = InstrumentationForm(request.POST)
        if form.is_valid():
            instrumentation = form.save(commit=False)
            instrumentation.save()
            return redirect('blog:instrumentation_detail', pk=instrumentation.pk)
    else:
        form = InstrumentationForm()
    return render(request, 'blog/instrumentation_edit.html', {'form': form})


@login_required
def instrumentation_edit(request, pk):
    """
    Instrumentation_edit function docstring.

    This function shows the form to modify a instrument.

    @param request: HTML request page.
    @param pk: primary key of the instrument to modify.
    @return: First time, this shows the form to edit the instrument information. If the form is
             completed, return the details of this instrument.
    @raise 404: instrument does not exists.
    """
    instrumentation = get_object_or_404(Instrumentation, pk=pk)
    if request.method == "POST":
        form = InstrumentationForm(data=request.POST, instance=instrumentation)
        if form.is_valid():
            instrumentation = form.save(commit=False)
            instrumentation.save()
            return redirect('blog:instrumentation_detail', pk=instrumentation.pk)
    else:
        form = InstrumentationForm(instance=instrumentation)
    return render(request, 'blog/instrumentation_edit.html', {'form': form})


@login_required
def instrumentation_remove(request, pk):
    """
    Instrumentation_remove function docstring.

    This function removes a instrument.

    @param request: HTML request page.
    @param pk: primary key of the instrument to remove.
    @return: list of instruments.
    @raise 404: instrument does not exists.
    """
    instrumentation = get_object_or_404(Instrumentation, pk=pk)
    instrumentation.delete()
    return redirect('blog:instrumentation_list')


def others_list(request):
    """
    Others_list function docstring.

    This function shows the list of components whithout type that are stored in this web app and
    they are ordered by creation date.

    @param request: HTML request page.
    @return: list of components whithout type.
    """
    otherss = Others.objects.filter(created_date__lte=timezone.now()).order_by('created_date')

    return render(request, 'blog/others_list.html', {'otherss': otherss})


def others_detail(request, pk):
    """
    Others_detail function docstring.

    This function shows the information of a component whithout type.

    @param request: HTML request page.
    @param pk: primary key of the component.
    @return: one components whithout type.
    @raise 404: component does not exists.
    """
    others = get_object_or_404(Others, pk=pk)

    return render(request, 'blog/others_detail.html', {'others': others})


@login_required
def others_new(request):
    """
    Others_new function docstring.

    This function shows the form to create a new component without type.

    @param request: HTML request page.
    @return: First time, this shows the form to a new component. If the form is completed, return
             the details of this new component without type.
    """
    if request.method == "POST":
        form = OthersForm(request.POST)
        if form.is_valid():
            others = form.save(commit=False)
            others.save()
            return redirect('blog:others_detail', pk=others.pk)
    else:
        form = OthersForm()
    return render(request, 'blog/others_edit.html', {'form': form})


@login_required
def others_edit(request, pk):
    """
    Others_edit function docstring.

    This function shows the form to modify a component without type.

    @param request: HTML request page.
    @param pk: primary key of the component to modify.
    @return: First time, this shows the form to edit the component information. If the form is
             completed, return the details of this component without type.
    @raise 404: component does not exists.
    """
    others = get_object_or_404(Others, pk=pk)
    if request.method == "POST":
        form = OthersForm(data=request.POST, instance=others)
        if form.is_valid():
            others = form.save(commit=False)
            others.save()
            return redirect('blog:others_detail', pk=others.pk)
    else:
        form = OthersForm(instance=others)
    return render(request, 'blog/others_edit.html', {'form': form})


@login_required
def others_remove(request, pk):
    """
    Others_remove function docstring.

    This function removes a component that does not have type.

    @param request: HTML request page.
    @param pk: primary key of the component to remove.
    @return: list of components.
    @raise 404: component does not exists.
    """
    others = get_object_or_404(Others, pk=pk)
    others.delete()
    return redirect('blog:others_list')


def order_list(request):
    """
    Order_list function docstring.

    This function shows the list of orders carried out in this web app and they are ordered by
    creation date.

    @param request: HTML request page.
    @return: list of orders.
    """
    orders = Order.objects.filter(created_date__lte=timezone.now()).order_by('created_date')

    return render(request, 'blog/order_list.html', {'orders': orders})


def order_detail(request, pk):
    """
    Order_detail function docstring.

    This function shows the information of an order.

    @param request: HTML request page.
    @param pk: primary key of the order.
    @return: one order.
    @raise 404: order does not exists.
    """
    order = get_object_or_404(Order, pk=pk)
    products = Product.objects.filter(order=order.pk).order_by('created_date')

    noItem = False
    if not products.exists():
        noItem = True

    return render(request, 'blog/order_detail.html', {'order': order, 'products': products,
                                                      'noItem': noItem})


@login_required
def order_new(request):
    """
    Order_new function docstring.

    This function shows the first step of the form to create a new order.

    @param request: HTML request page.
    @return: First time, this shows the form to a new order. If the form is completed, return
             the next step to finish the order.
    """
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.author = request.user
            order.save()
            return redirect('blog:order_new_next', pk=order.pk)
    else:
        form = OrderForm()
    return render(request, 'blog/order_new.html', {'form': form})


def setBordersCell(sheet):
    """
    setBordersCell function docstring.

    This function modify the cells of the Excel page to carry out an order and include the image of
    ICN2 logo.

    @param sheet: Excel sheet to modify the cells.
    @return: Excel sheet modified.
    """
    border_TopBottomThin = Border(top=Side(style='thin'), bottom=Side(style='thin'))

    border_RightTopBottomThin = Border(right=Side(style='thin'), top=Side(style='thin'),
                                       bottom=Side(style='thin'))

    border_TopThin = Border(top=Side(style='thin'))

    border_BottomThin = Border(bottom=Side(style='thin'))

    border_TopThinBottomDouble = Border(top=Side(style='thin'), bottom=Side(style='double'))

    border_RightTopBottomMedium = Border(right=Side(style='medium'), top=Side(style='medium'),
                                         bottom=Side(style='medium'))

    sheet.cell('D6').border = border_TopBottomThin
    sheet.cell('E6').border = border_RightTopBottomThin
    sheet.cell('D7').border = border_TopBottomThin
    sheet.cell('E7').border = border_RightTopBottomThin
    sheet.cell('D8').border = border_TopBottomThin
    sheet.cell('E8').border = border_RightTopBottomThin
    sheet.cell('D9').border = border_TopBottomThin
    sheet.cell('E9').border = border_RightTopBottomThin
    sheet.cell('D10').border = border_TopBottomThin
    sheet.cell('E10').border = border_RightTopBottomThin
    sheet.cell('D11').border = border_TopBottomThin
    sheet.cell('E11').border = border_RightTopBottomThin
    sheet.cell('D12').border = border_TopBottomThin
    sheet.cell('E12').border = border_RightTopBottomThin

    sheet.cell('G12').border = border_RightTopBottomMedium

    sheet.cell('D14').border = border_TopBottomThin
    sheet.cell('E14').border = border_TopBottomThin
    sheet.cell('F14').border = border_TopBottomThin
    sheet.cell('G14').border = border_TopBottomThin

    sheet.cell('D18').border = border_TopBottomThin
    sheet.cell('E18').border = border_TopBottomThin
    sheet.cell('F18').border = border_TopBottomThin
    sheet.cell('G18').border = border_TopBottomThin
    sheet.cell('H18').border = border_RightTopBottomThin

    sheet.cell('G30').border = border_RightTopBottomThin

    sheet.cell('B36').border = border_TopThin
    sheet.cell('C36').border = border_TopThin
    sheet.cell('D36').border = border_TopThin
    sheet.cell('E36').border = border_TopThin

    sheet.cell('B37').border = border_BottomThin
    sheet.cell('C37').border = border_BottomThin
    sheet.cell('D37').border = border_BottomThin
    sheet.cell('E37').border = border_BottomThin
    sheet.cell('F37').border = border_BottomThin
    sheet.cell('G37').border = border_BottomThin

    for num in range(38, 65):
        numStr = str(num)
        sheet.cell('B' + numStr).border = border_TopBottomThin
        sheet.cell('C' + numStr).border = border_TopBottomThin
        sheet.cell('D' + numStr).border = border_TopBottomThin
        sheet.cell('E' + numStr).border = border_TopBottomThin
        sheet.cell('F' + numStr).border = border_TopBottomThin
        sheet.cell('G' + numStr).border = border_RightTopBottomThin

    sheet.cell('I67').border = border_TopBottomThin
    sheet.cell('I68').border = border_TopBottomThin
    sheet.cell('I69').border = border_TopThinBottomDouble

    img = Image('blog/static/images/icn2.png')
    # img.anchor(sheet.cell('H2'))
    sheet.add_image(img, 'H2')
    return sheet


@login_required
def order_new_next(request, pk):
    """
    order_new_next function docstring.

    This function shows the second step of the form to create a new order.

    @param request: HTML request page.
    @param pk: primary key of the new order.
    @return: First time, this shows the form to complete a new order. If the form is completed,
             the Excel sheet is completed with the data and return the details of the new order.
    @raise 404: order does not exists.
    """
    order = get_object_or_404(Order, pk=pk)
    ProductFormSet = formset_factory(ProductForm, extra=order.number_product)
    if request.method == "POST":
        product = ProductForm()
        formset = ProductFormSet(request.POST)
        doc = openpyxl.load_workbook('blog/formulariosPedidos/Formulario_Pedido_v2.xlsx')
        doc.get_sheet_names()
        sheet = doc.get_sheet_by_name('Order Form')
        sheet['C6'] = order.applicant
        sheet['C7'] = order.budget.name
        sheet['C10'] = order.type_of_purchase.name
        sheet['C12'] = order.payment_conditions.name
        sheet['C18'] = order.supplier.name
        num = 38
        nameFile = "FP_" + order.name
        if (formset.is_valid()):
            for form in formset:
                product = form.cleaned_data
                product = form.save(commit=False)
                numString = str(num)
                sheet['A' + numString] = product.description
                sheet['H' + numString] = product.quantity
                sheet['I' + numString] = product.unit_price
                num = num + 1
                product.order = order
                product.save()

            sheet = setBordersCell(sheet)
            doc.save('blog/formulariosPedidos/' + nameFile + '.xlsx')

            return redirect('blog:order_detail', pk=order.pk)
    else:
        formset = ProductFormSet()
    return render(request, 'blog/order_new_next.html', {'formset': formset})


@login_required
def order_edit(request, pk):
    """
    Order_edit function docstring.

    This function shows the form to modify an order.

    @param request: HTML request page.
    @param pk: primary key of the order to modify.
    @return: First time, this shows the form to edit the order information. If the form is
             completed, return the details of this order.
    @raise 404: order does not exists.
    """
    order = get_object_or_404(Order, pk=pk)
    products = Product.objects.filter(order=order.pk).order_by('created_date')
    ProductFormSet = formset_factory(ProductForm)
    if request.method == "POST":
        order_form = OrderForm(data=request.POST, instance=order, prefix="orderForm")
        formset = ProductFormSet(data=request.POST, prefix="productForm")
        if order_form.is_valid() and formset.is_valid():
            order = order_form.save(commit=False)
            order.author = request.user
            order.save()
            for num in range(0, len(products)):
                product = formset[num].save(commit=False)
                product.order = order
                if products[num].description != product.description:
                    products[num].description = product.description

                if products[num].quantity != product.quantity:
                    products[num].quantity = product.quantity

                if products[num].unit_price != product.unit_price:
                    products[num].unit_price = product.unit_price

                products[num].save()
            return redirect('blog:order_detail', pk=order.pk)
    else:
        order_form = OrderForm(instance=order, prefix="orderForm")
        products = Product.objects.filter(order=order.pk).order_by('created_date')
        noItem = False
        if not products.exists():
            noItem = True
        products_formset = ProductFormSet(initial=[{'description': form.description,
                                                    'quantity': form.quantity,
                                                    'unit_price': form.unit_price}
                                                   for form in products], prefix="productForm")
        count = products.count
    return render(request, 'blog/order_edit.html', {'order_form': order_form,
                                                    'products_formset': products_formset,
                                                    'noItem': noItem,
                                                    'count': count})


@login_required
def order_remove(request, pk):
    """
    Order_remove function docstring.

    This function removes an order.

    @param request: HTML request page.
    @param pk: primary key of the order to remove.
    @return: list of orders.
    @raise 404: order does not exists.
    """
    order = get_object_or_404(Order, pk=pk)
    order.delete()
    return redirect('blog:order_list')


def run_list(request):
    """
    Run_list function docstring.

    This function shows the list of runs that are stored in this web app and they are ordered by
    creation date.

    @param request: HTML request page.
    @return: list of runs.
    """
    runs = Run.objects.filter(created_date__lte=timezone.now()).order_by('created_date')

    return render(request, 'blog/run_list.html', {'runs': runs})


def run_detail(request, pk):
    """
    Run_detail function docstring.

    This function shows the information of a run. BUT THIS FUNCTION IS NOT IN USE NOW.

    @param request: HTML request page.
    @param pk: primary key of the run.
    @return: one run.
    @raise 404: run does not exists.
    """
    run = get_object_or_404(Run, pk=pk)

    return render(request, 'blog/run_detail.html', {'run': run})


@login_required
def run_new(request):
    """
    Run_new function docstring.

    This function shows the form to create a new run. BUT THIS FUNCTION IS NOT IN USE NOW.

    @param request: HTML request page.
    @return: First time, this shows the form to a new run. If the form is completed, return
             the details of this new run.
    """
    if request.method == "POST":
        form = RunForm(request.POST)
        if form.is_valid():
            run = form.save(commit=False)
            run.save()
            return redirect('blog:run_detail', pk=run.pk)
    else:
        form = RunForm()
    return render(request, 'blog/run_edit.html', {'form': form})


@login_required
def run_edit(request, pk):
    """
    Run_edit function docstring.

    This function shows the form to modify a run. BUT THIS FUNCTION IS NOT IN USE NOW.

    @param request: HTML request page.
    @param pk: primary key of the run to modify.
    @return: First time, this shows the form to edit the run information. If the form is
             completed, return the details of this run.
    @raise 404: run does not exists.
    """
    run = get_object_or_404(Run, pk=pk)
    if request.method == "POST":
        form = RunForm(data=request.POST, instance=run)
        if form.is_valid():
            run = form.save(commit=False)
            run.save()
            return redirect('blog:run_detail', pk=run.pk)
    else:
        form = RunForm(instance=run)
    return render(request, 'blog/run_edit.html', {'form': form})


@login_required
def run_remove(request, pk):
    """
    Run_remove function docstring.

    This function removes a run. BUT THIS FUNCTION IS NOT IN USE NOW.

    @param request: HTML request page.
    @param pk: primary key of the run to remove.
    @return: list of runs.
    @raise 404: run does not exists.
    """
    run = get_object_or_404(Run, pk=pk)
    run.delete()
    return redirect('blog:run_list')


def run_chip_list(request, pk):
    """
    Run_chip_list function docstring.

    This function shows the list of chips of a run that are stored in this web app.

    @param request: HTML request page.
    @param pk: primary key of the run.
    @return: list of chips.
    """
    chips = Chip.objects.filter(run=pk)

    return render(request, 'blog/chip_list.html', {'chips': chips})


def chip_list(request):
    """
    Chip_list function docstring.

    This function shows the list of chips that are stored in this web app nd they are ordered by
    creation date.

    @param request: HTML request page.
    @return: list of chips.
    """
    chips = Chip.objects.filter(created_date__lte=timezone.now()).order_by('created_date')

    return render(request, 'blog/chip_list.html', {'chips': chips})


def chip_detail(request, pk):
    """
    Chip_detail function docstring.

    This function shows the information of a chip.

    @param request: HTML request page.
    @param pk: primary key of the chip.
    @return: one chip.
    @raise 404: chip does not exists.
    """
    chip = get_object_or_404(Chip, pk=pk)

    return render(request, 'blog/chip_detail.html', {'chip': chip})


def chip_detail_exist(request, pk):
    """
    Chip_detail_exist function docstring.

    This function shows the information of a chip when a chip is created but this already exists.

    @param request: HTML request page.
    @param pk: primary key of the chip.
    @return: one chip.
    @raise 404: chip does not exists.
    """
    chip = get_object_or_404(Chip, pk=pk)

    return render(request, 'blog/chip_detail_exist.html', {'chip': chip})


@login_required
def chip_new(request):
    """
    Chip_new function docstring.

    This function shows the form to create a new chip. This function uses 3 forms to create a new
    chip (Run form, Wafer form and Chip form), moreover, when the form is completed, this function
    search if the run or wafer or chip already exists.

    @param request: HTML request page.
    @return: First time, this shows the form to a new chip. If the form is completed and the run or
             wafer or chip does not exists, return the details of this new chip.
    """
    if request.method == "POST":
        runForm = RunForm(request.POST, prefix='run')
        waferForm = WaferForm(request.POST, prefix='wafer')
        chipForm = ChipForm(request.POST, prefix='chip')
        # waveguideForm = WaveguideForm(request.POST, prefix='waveguide')
        if runForm.is_valid():
            run = runForm.save(commit=False)
            run_ex = Run.objects.get(run=run.run)
            print(run)
            if not run_ex:
                # print(run_ex)
                run.save()
            else:
                run = run_ex
        if waferForm.is_valid():
            wafer = waferForm.save(commit=False)
            wafer_ex = Wafer.objects.get(wafer=wafer.wafer, run=run)
            # print(wafer)
            if not wafer_ex:
                # print(wafer_ex)
                wafer.run = run
                wafer.save()
            else:
                wafer = wafer_ex
        if chipForm.is_valid():
            chip = chipForm.save(commit=False)
            chip_ex = Chip.objects.get(chip=chip.chip, wafer=wafer, run=run)
            # print(chip)
            if not chip_ex:
                # print(chip_ex)
                chip.run = run
                chip.wafer = wafer
                chip.save()
                return redirect('blog:chip_detail', pk=chip.pk)
            else:
                chip = chip_ex
                return redirect('blog:chip_detail_exist', pk=chip.pk)
    else:
        runForm = RunForm(prefix='run')
        waferForm = WaferForm(prefix='wafer')
        chipForm = ChipForm(prefix='chip')
        # waveguideFrom = WaveguideForm(prefix='waveguide')
    return render(request, 'blog/chip_edit.html', {'runForm': runForm, 'waferForm': waferForm,
                                                   'chipForm': chipForm})


@login_required
def chip_edit(request, pk):
    """
    Chip_edit function docstring.

    This function shows the form to modify a chip.

    @param request: HTML request page.
    @param pk: primary key of the chip to modify.
    @return: First time, this shows the form to edit the chip information. If the form is
             completed, return the details of this chip.
    @raise 404: chip does not exists.
    """
    chip = get_object_or_404(Run, pk=pk)
    if request.method == "POST":
        form = RunForm(data=request.POST, instance=chip)
        if form.is_valid():
            chip = form.save(commit=False)
            chip.save()
            return redirect('blog:chip_detail', pk=chip.pk)
    else:
        form = RunForm(instance=chip)
    return render(request, 'blog/chip_edit.html', {'form': form})


@login_required
def chip_remove(request, pk):
    """
    Chip_remove function docstring.

    This function removes a chip.

    @param request: HTML request page.
    @param pk: primary key of the chip to remove.
    @return: list of chips.
    @raise 404: chip does not exists.
    """
    chip = get_object_or_404(Run, pk=pk)
    chip.delete()
    return redirect('blog:chip_list')


# def waveguide_list(request):
#
#     waveguides = Waveguide.objects.filter(
#        created_date__lte=timezone.now()).order_by('created_date')
#
#     return render(request, 'blog/waveguide_list.html', {'waveguides': waveguides})

def waveguide_list(request, pk):
    """
    Waveguide_list function docstring.

    This function shows the list of waveguides of a chip that are stored in this web app.

    @param request: HTML request page.
    @param pk: primary key of the chip.
    @return: list of waveguides of a chip.
    """
    waveguides = Waveguide.objects.filter(chip=pk)

    return render(request, 'blog/waveguide_list.html', {'waveguides': waveguides, 'chip': pk})


def waveguide_detail(request, pk, pk2):
    """
    Waveguide_detail function docstring.

    This function shows the information of a waveguide of a chip.

    @param request: HTML request page.
    @param pk: primary key of the chip.
    @param pk2: primary key of the waveguide.
    @return: one waveguide.
    @raise 404: waveguide does not exists.
    """
    waveguide = get_object_or_404(Waveguide, pk=pk2)

    return render(request, 'blog/waveguide_detail.html', {'waveguide': waveguide})


def waveguide_detail_exist(request, pk, pk2):
    """
    Waveguide_detail_exist function docstring.

    This function shows the information of a waveguide of a chip when a waveguide is created but
    this already exists.

    @param request: HTML request page.
    @param pk: primary key of the chip.
    @param pk2: primary key of the waveguide.
    @return: one waveguide.
    @raise 404: waveguide does not exists.
    """
    waveguide = get_object_or_404(Waveguide, pk=pk2)

    return render(request, 'blog/waveguide_detail_exist.html', {'waveguide': waveguide})


@login_required
def waveguide_new(request, pk):
    """
    Waveguide_new function docstring.

    This function shows the form to create a new waveguide of a chip. When the form is completed,
    this function search if the waveguide already exists.

    @param request: HTML request page.
    @param pk: primary key of the chip.
    @return: First time, this shows the form to a new waveguide to a chip already created. If the
             form is completed and waveguide does not exists, return the details of this new
             waveguide.
    @raise 404: chip does not exists.
    """
    if request.method == "POST":
        # runForm = RunForm(request.POST, prefix='run')
        # waferForm = WaferForm(request.POST, prefix='wafer')
        waveguideForm = WaveguideForm(request.POST, prefix='waveguide')
        # waveguideForm = WaveguideForm(request.POST, prefix='waveguide')
        # if runForm.is_valid():
        #     run = runForm.save(commit=False)
        #     run_ex = Run.objects.get(run=run.run)
        #     print(run)
        #     if not run_ex:
        #         # print(run_ex)
        #         run.save()
        #     else:
        #         run = run_ex
        # if waferForm.is_valid():
        #     wafer = waferForm.save(commit=False)
        #     wafer_ex = Wafer.objects.get(wafer=wafer.wafer, run=run)
        #     # print(wafer)
        #     if not wafer_ex:
        #         # print(wafer_ex)
        #         wafer.run = run
        #         wafer.save()
        #     else:
        #         wafer = wafer_ex
        if waveguideForm.is_valid():
            waveguide = waveguideForm.save(commit=False)
            # print(waveguide)
            chip = Chip.objects.get(pk=pk)
            # print(chip.wafer)
            waveguide_ex = Waveguide.objects.get(waveguide=waveguide.waveguide, chip=chip,
                                                 wafer=chip.wafer, run=chip.run)
            # print(waveguide)
            if not waveguide_ex:
                # print(waveguide_ex)
                waveguide.run = chip.run
                waveguide.wafer = chip.wafer
                waveguide.chip = chip
                waveguide.name = waveguide.waveguide.name
                waveguide.save()
                return redirect('blog:waveguide_detail', pk=chip.pk, pk2=waveguide.pk)
            else:
                waveguide = waveguide_ex
                print(waveguide.pk)
                return redirect('blog:waveguide_detail_exist', pk=chip.pk, pk2=waveguide.pk)
    else:
        # runForm = RunForm(prefix='run')
        # waferForm = WaferForm(prefix='wafer')
        chip = get_object_or_404(Chip, pk=pk)
        waveguideForm = WaveguideForm(prefix='waveguide')
        # waveguideFrom = WaveguideForm(prefix='waveguide')
    return render(request, 'blog/waveguide_edit.html', {'waveguideForm': waveguideForm,
                                                        'chip': chip})


@login_required
def waveguide_edit(request, pk):
    """
    Waveguide_edit function docstring.

    This function shows the form to modify a waveguide.

    @param request: HTML request page.
    @param pk: primary key of the waveguide to modify.
    @return: First time, this shows the form to edit the waveguide information. If the form is
             completed, return the details of this waveguide.
    @raise 404: waveguide does not exists.
    """
    waveguide = get_object_or_404(Run, pk=pk)
    if request.method == "POST":
        form = RunForm(data=request.POST, instance=waveguide)
        if form.is_valid():
            waveguide = form.save(commit=False)
            waveguide.save()
            return redirect('blog:waveguide_detail', pk=waveguide.pk)
    else:
        form = RunForm(instance=waveguide)
    return render(request, 'blog/waveguide_edit.html', {'form': form})


@login_required
def waveguide_remove(request, pk):
    """
    Waveguide_remove function docstring.

    This function removes a waveguide.

    @param request: HTML request page.
    @param pk: primary key of the waveguide to remove.
    @return: list of waveguides.
    @raise 404: waveguide does not exists.
    """
    waveguide = get_object_or_404(Run, pk=pk)
    waveguide.delete()
    return redirect('blog:waveguide_list')
