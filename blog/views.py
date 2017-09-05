from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.forms.formsets import formset_factory
from django.utils import timezone
from django.contrib.auth import login, authenticate
# from django.contrib.auth.models import User
# from django.db.models.functions import Concat
import openpyxl
from openpyxl.styles.borders import Border, Side
from openpyxl.drawing.image import Image
from .models import Element, Order, Product, Computing, Electronic, Chemical, Instrumentation
from .models import Others, Full_Name_Users, Run, Chip, Wafer, Waveguide
from .forms import ElementForm, OrderForm, ProductForm, ComputingForm, ElectronicForm, ChemicalForm
from .forms import InstrumentationForm, OthersForm, SignUpForm, RunForm, WaferForm, ChipForm
from .forms import WaveguideForm


def home(request):

    return render(request, 'blog/home.html')


def signup(request):
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


def run_list(request):

    runs = Run.objects.filter(created_date__lte=timezone.now()).order_by('created_date')

    return render(request, 'blog/run_list.html', {'runs': runs})


def run_detail(request, pk):
    run = get_object_or_404(Run, pk=pk)

    return render(request, 'blog/run_detail.html', {'run': run})


@login_required
def run_new(request):
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
    run = get_object_or_404(Run, pk=pk)
    run.delete()
    return redirect('blog:run_list')


def run_chip_list(request, pk):

    chips = Chip.objects.filter(run=pk)

    return render(request, 'blog/chip_list.html', {'chips': chips})


def chip_list(request):

    chips = Chip.objects.filter(created_date__lte=timezone.now()).order_by('created_date')

    return render(request, 'blog/chip_list.html', {'chips': chips})


def chip_detail(request, pk):
    chip = get_object_or_404(Chip, pk=pk)

    return render(request, 'blog/chip_detail.html', {'chip': chip})


def chip_detail_exist(request, pk):
    chip = get_object_or_404(Chip, pk=pk)

    return render(request, 'blog/chip_detail_exist.html', {'chip': chip})


@login_required
def chip_new(request):
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
    chip = get_object_or_404(Run, pk=pk)
    chip.delete()
    return redirect('blog:chip_list')


# def waveguide_list(request):
#
#     waveguides = Waveguide.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
#
#     return render(request, 'blog/waveguide_list.html', {'waveguides': waveguides})

def waveguide_list(request, pk):

    waveguides = Waveguide.objects.filter(chip=pk)

    return render(request, 'blog/waveguide_list.html', {'waveguides': waveguides, 'chip': pk})


def waveguide_detail(request, pk, pk2):
    waveguide = get_object_or_404(Waveguide, pk=pk2)

    return render(request, 'blog/waveguide_detail.html', {'waveguide': waveguide})


def waveguide_detail_exist(request, pk, pk2):
    waveguide = get_object_or_404(Waveguide, pk=pk2)

    return render(request, 'blog/waveguide_detail_exist.html', {'waveguide': waveguide})


@login_required
def waveguide_new(request, pk):
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
    waveguide = get_object_or_404(Run, pk=pk)
    waveguide.delete()
    return redirect('blog:waveguide_list')
