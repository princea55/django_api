from django.contrib import admin

from .models import College, Students, Professors

admin.site.register(College)
admin.site.register(Students)
admin.site.register(Professors)
