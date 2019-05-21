from django.contrib import admin
from .models import *

admin.site.register(GoodsInfo)


class GoodsInline(admin.StackedInline):
    model = GoodsInfo
    extra = 1


@admin.register(TypeInfo)
class TyepAdmin(admin.ModelAdmin):
    inlines = [GoodsInline]
