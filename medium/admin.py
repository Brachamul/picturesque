from django.contrib import admin

from .models import *

#class PostAdmin(admin.ModelAdmin):
#    readonly_fields = ('date',)

#admin.site.register(Post,PostAdmin)

admin.site.register(Medium)
admin.site.register(Actor)
