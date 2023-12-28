from django.contrib import admin

# Register your models here.
from .models import Tblone
from .models import Tbltwo
from .models import Tblthree

admin.site.register(Tblone)
admin.site.register(Tbltwo)
admin.site.register(Tblthree)