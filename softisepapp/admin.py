from django.contrib import admin
from .models import Cours, Logiciel
from django.utils.translation import gettext_lazy as _

# Register your models here.
admin.site.register(Cours)
admin.site.register(Logiciel)

admin.site.site_header = _('SoftIsep Admin')
admin.site.site_title = _('SoftIsep Admin Portal')
admin.site.index_title = _('Welcome to SoftIsep Admin')
