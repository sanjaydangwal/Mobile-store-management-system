from django.contrib import admin
from .models import phone,basic,smart,Profile,checkout
# Register your models here.

admin.site.register(phone)
admin.site.register(basic)
admin.site.register(smart)
admin.site.register(Profile)
admin.site.register(checkout)


