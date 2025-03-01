from django.contrib import admin
from .models import Donor
from django.contrib.admin import ModelAdmin


class DonorAdmin(ModelAdmin):
    list_display = ('name', 'bloodgroup', 'address', 'mobile')
    search_fields = ['address']

    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)
        if search_term:
            queryset = queryset.filter(address__icontains=search_term)
        return queryset, use_distinct

admin.site.register(Donor, DonorAdmin)
