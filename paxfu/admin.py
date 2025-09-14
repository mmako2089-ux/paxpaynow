from django.contrib import admin
from .models import Person,Otp,Amount
# Register your models here.
admin.site.register(Person)
admin.site.register(Otp)
admin.site.register(Amount)