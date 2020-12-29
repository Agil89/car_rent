from django.contrib import admin
from main.models import CarModel,Car,CarYear,CarClass,CarMarka,Images,Transmission,\
    Type,Fuel,OrderData,AboutUs,Contacts,SendList
# Register your models here.
admin.site.register(CarMarka)
admin.site.register(CarModel)
admin.site.register(CarYear)
admin.site.register(CarClass)
admin.site.register(Transmission)
admin.site.register(Type)
admin.site.register(Fuel)
admin.site.register(OrderData)
admin.site.register(AboutUs)
admin.site.register(Contacts)
admin.site.register(SendList)

class CarImages(admin.TabularInline):
    model = Images
    extra = 1

@admin.register(Car)
class TyresAdmin(admin.ModelAdmin):
    inlines = [CarImages]
    list_display = ('get_car', 'price')
    # list_filter = ('height', 'radius', 'published', 'width')
    # search_fields = ('name',)
    # list_editable = ('published',)