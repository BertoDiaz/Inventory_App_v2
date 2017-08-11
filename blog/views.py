from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.forms.formsets import formset_factory
from django.utils import timezone
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
import openpyxl
from openpyxl.styles.borders import Border, Side
from openpyxl.drawing.image import Image
from .models import Element, Order, Product, Computing, Electronic, Chemical, Instrumentation
from .models import Others
from .forms import ElementForm, OrderForm, ProductForm, ComputingForm, ElectronicForm, ChemicalForm
from .forms import InstrumentationForm, OthersForm


def home(request):

    return render(request, 'blog/home.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('blog:home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


def element_list(request):

    elements = Element.objects.filter(created_date__lte=timezone.now()).order_by('created_date')

    return render(request, 'blog/element_list.html', {'elements': elements})


def element_detail(request, pk):
    element = get_object_or_404(Element, pk=pk)

    return render(request, 'blog/element_detail.html', {'element': element})


@login_required
def element_new(request):
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
    element = get_object_or_404(Element, pk=pk)
    element.delete()
    return redirect('blog:element_list')


def computing_list(request):

    computings = Computing.objects.filter(created_date__lte=timezone.now()).order_by('created_date')

    return render(request, 'blog/computing_list.html', {'computings': computings})


def computing_detail(request, pk):
    computing = get_object_or_404(Computing, pk=pk)

    return render(request, 'blog/computing_detail.html', {'computing': computing})


@login_required
def computing_new(request):
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
    computing = get_object_or_404(Computing, pk=pk)
    computing.delete()
    return redirect('blog:computing_list')


def electronic_list(request):

    electronics = Electronic.objects.filter(
        created_date__lte=timezone.now()).order_by('created_date')

    print(electronics)

    return render(request, 'blog/electronic_list.html', {'electronics': electronics})


def electronic_detail(request, pk):
    electronic = get_object_or_404(Electronic, pk=pk)

    return render(request, 'blog/electronic_detail.html', {'electronic': electronic})


@login_required
def electronic_new(request):
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
    electronic = get_object_or_404(Electronic, pk=pk)
    electronic.delete()
    return redirect('blog:electronic_list')


def chemical_list(request):

    chemicals = Chemical.objects.filter(created_date__lte=timezone.now()).order_by('created_date')

    return render(request, 'blog/chemical_list.html', {'chemicals': chemicals})


def chemical_detail(request, pk):
    chemical = get_object_or_404(Chemical, pk=pk)

    return render(request, 'blog/chemical_detail.html', {'chemical': chemical})


@login_required
def chemical_new(request):
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
    chemical = get_object_or_404(Chemical, pk=pk)
    chemical.delete()
    return redirect('blog:chemical_list')


def instrumentation_list(request):

    instrumentations = Instrumentation.objects.filter(
        created_date__lte=timezone.now()).order_by('created_date')

    return render(request, 'blog/instrumentation_list.html', {'instrumentations': instrumentations})


def instrumentation_detail(request, pk):
    instrumentation = get_object_or_404(Instrumentation, pk=pk)

    return render(request, 'blog/instrumentation_detail.html', {'instrumentation': instrumentation})


@login_required
def instrumentation_new(request):
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
    instrumentation = get_object_or_404(Instrumentation, pk=pk)
    instrumentation.delete()
    return redirect('blog:instrumentation_list')


def others_list(request):

    otherss = Others.objects.filter(created_date__lte=timezone.now()).order_by('created_date')

    return render(request, 'blog/others_list.html', {'otherss': otherss})


def others_detail(request, pk):
    others = get_object_or_404(Others, pk=pk)

    return render(request, 'blog/others_detail.html', {'others': others})


@login_required
def others_new(request):
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
    others = get_object_or_404(Others, pk=pk)
    others.delete()
    return redirect('blog:others_list')


def order_list(request):

    orders = Order.objects.filter(created_date__lte=timezone.now()).order_by
    ('created_date')

    return render(request, 'blog/order_list.html', {'orders': orders})


def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)
    products = Product.objects.filter(order=order.pk).order_by('created_date')

    noItem = False
    if not products.exists():
        noItem = True

    return render(request, 'blog/order_detail.html', {'order': order, 'products': products,
                                                      'noItem': noItem})


@login_required
def order_new(request):
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


def setBordersCell(hoja):

    border_TopBottomThin = Border(top=Side(style='thin'),
                                  bottom=Side(style='thin'))

    border_RightTopBottomThin = Border(right=Side(style='thin'),
                                       top=Side(style='thin'),
                                       bottom=Side(style='thin'))

    border_TopThin = Border(top=Side(style='thin'))

    border_BottomThin = Border(bottom=Side(style='thin'))

    border_TopThinBottomDouble = Border(top=Side(style='thin'),
                                        bottom=Side(style='double'))

    border_RightTopBottomMedium = Border(right=Side(style='medium'),
                                         top=Side(style='medium'),
                                         bottom=Side(style='medium'))

    hoja.cell('D6').border = border_TopBottomThin
    hoja.cell('E6').border = border_RightTopBottomThin
    hoja.cell('D7').border = border_TopBottomThin
    hoja.cell('E7').border = border_RightTopBottomThin
    hoja.cell('D8').border = border_TopBottomThin
    hoja.cell('E8').border = border_RightTopBottomThin
    hoja.cell('D9').border = border_TopBottomThin
    hoja.cell('E9').border = border_RightTopBottomThin
    hoja.cell('D10').border = border_TopBottomThin
    hoja.cell('E10').border = border_RightTopBottomThin
    hoja.cell('D11').border = border_TopBottomThin
    hoja.cell('E11').border = border_RightTopBottomThin
    hoja.cell('D12').border = border_TopBottomThin
    hoja.cell('E12').border = border_RightTopBottomThin

    hoja.cell('G12').border = border_RightTopBottomMedium

    hoja.cell('D14').border = border_TopBottomThin
    hoja.cell('E14').border = border_TopBottomThin
    hoja.cell('F14').border = border_TopBottomThin
    hoja.cell('G14').border = border_TopBottomThin

    hoja.cell('D18').border = border_TopBottomThin
    hoja.cell('E18').border = border_TopBottomThin
    hoja.cell('F18').border = border_TopBottomThin
    hoja.cell('G18').border = border_TopBottomThin
    hoja.cell('H18').border = border_RightTopBottomThin

    hoja.cell('G30').border = border_RightTopBottomThin

    hoja.cell('B36').border = border_TopThin
    hoja.cell('C36').border = border_TopThin
    hoja.cell('D36').border = border_TopThin
    hoja.cell('E36').border = border_TopThin

    hoja.cell('B37').border = border_BottomThin
    hoja.cell('C37').border = border_BottomThin
    hoja.cell('D37').border = border_BottomThin
    hoja.cell('E37').border = border_BottomThin
    hoja.cell('F37').border = border_BottomThin
    hoja.cell('G37').border = border_BottomThin

    for num in range(38, 65):
        numStr = str(num)
        hoja.cell('B' + numStr).border = border_TopBottomThin
        hoja.cell('C' + numStr).border = border_TopBottomThin
        hoja.cell('D' + numStr).border = border_TopBottomThin
        hoja.cell('E' + numStr).border = border_TopBottomThin
        hoja.cell('F' + numStr).border = border_TopBottomThin
        hoja.cell('G' + numStr).border = border_RightTopBottomThin

    hoja.cell('I67').border = border_TopBottomThin
    hoja.cell('I68').border = border_TopBottomThin
    hoja.cell('I69').border = border_TopThinBottomDouble

    img = Image('blog/static/images/icn2.png')
    # img.anchor(hoja.cell('H2'))
    hoja.add_image(img, 'H2')
    return hoja


@login_required
def order_new_next(request, pk):
    order = get_object_or_404(Order, pk=pk)
    ProductFormSet = formset_factory(ProductForm, extra=order.number_product)
    if request.method == "POST":
        product = ProductForm()
        formset = ProductFormSet(request.POST)
        # doc = openpyxl.load_workbook('blog/formulariosPedidos/Formulario_Pedido_v2.xlsx',
        #                              formatting_info=True)
        doc = openpyxl.load_workbook('blog/formulariosPedidos/Formulario_Pedido_v2.xlsx')
        doc.get_sheet_names()
        hoja = doc.get_sheet_by_name('Order Form')
        hoja['C6'] = order.applicant
        hoja['C7'] = order.budget.name
        hoja['C10'] = order.type_of_purchase.name
        hoja['C12'] = order.payment_conditions.name
        hoja['C18'] = order.supplier.name
        num = 38
        nameFile = "FP_" + order.name
        if (formset.is_valid()):
            for form in formset:
                product = form.cleaned_data
                product = form.save(commit=False)
                numString = str(num)
                hoja['A' + numString] = product.description
                hoja['H' + numString] = product.quantity
                hoja['I' + numString] = product.unit_price
                num = num + 1
                product.order = order
                product.save()

            hoja = setBordersCell(hoja)
            doc.save('blog/formulariosPedidos/' + nameFile + '.xlsx')

            return redirect('blog:order_detail', pk=order.pk)
    else:
        formset = ProductFormSet()
    return render(request, 'blog/order_new_next.html', {'formset': formset})


@login_required
def order_edit(request, pk):
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
    order = get_object_or_404(Order, pk=pk)
    order.delete()
    return redirect('blog:order_list')
