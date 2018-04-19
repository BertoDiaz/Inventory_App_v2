"""
File name: admin.py.

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

from django.contrib import admin
from .models import Inventory, Type
from .models import Order, Budget, Type_of_purchase, Payment, Supplier, Product
from .models import Computing, Type_Object, Location, Full_Name_Users, Setup
from .models import Electronic, Type_Component, Unit
from .models import Optic, Type_Optic
from .models import Chemical, Type_Chemical, Unit_Chemical, State
from .models import Biological, Type_Biological_1, Type_Biological_2
from .models import Instrumentation, Type_Instrumentation
from .models import Consumable
from .models import Others
from .models import Run, Wafer, Chip, Waveguide, Name_Waveguide
from .models import Messages

admin.site.register(Inventory)
admin.site.register(Type)
admin.site.register(Order)
admin.site.register(Budget)
admin.site.register(Type_of_purchase)
admin.site.register(Payment)
admin.site.register(Supplier)
admin.site.register(Product)
admin.site.register(Computing)
admin.site.register(Type_Object)
admin.site.register(Location)
admin.site.register(Full_Name_Users)
admin.site.register(Setup)
admin.site.register(Electronic)
admin.site.register(Type_Component)
admin.site.register(Unit)
admin.site.register(Optic)
admin.site.register(Type_Optic)
admin.site.register(Chemical)
admin.site.register(Type_Chemical)
admin.site.register(Unit_Chemical)
admin.site.register(State)
admin.site.register(Biological)
admin.site.register(Type_Biological_1)
admin.site.register(Type_Biological_2)
admin.site.register(Instrumentation)
admin.site.register(Type_Instrumentation)
admin.site.register(Consumable)
admin.site.register(Others)
admin.site.register(Run)
admin.site.register(Wafer)
admin.site.register(Chip)
admin.site.register(Waveguide)
admin.site.register(Name_Waveguide)
admin.site.register(Messages)
