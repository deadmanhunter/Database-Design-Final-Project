from django.contrib import admin
from .models import Heroes, Ultimate, Universe, Abilities

# Register your models here.

admin.site.register(Heroes)
admin.site.register(Ultimate)
admin.site.register(Universe)
admin.site.register(Abilities)
