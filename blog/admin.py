from django.contrib import admin
from .models import Element, Type
from .models import Order, Budget, Type_of_purchase, Payment, Supplier, Product
from .models import Computing, Type_Object, Location, Full_Name_Users, Setup
from .models import Electronic, Type_Component, Unit
from .models import Chemical, Type_Chemical, Unit_Chemical, Closet
from .models import Instrumentation, Type_Instrumentation
from .models import Others

admin.site.register(Element)
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
admin.site.register(Chemical)
admin.site.register(Type_Chemical)
admin.site.register(Unit_Chemical)
admin.site.register(Closet)
admin.site.register(Instrumentation)
admin.site.register(Type_Instrumentation)
admin.site.register(Others)
