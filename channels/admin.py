from django.contrib import admin
from .models import Tags, Channel, Message
# Register your models here.


admin.site.register(Tags)
admin.site.register(Channel)
admin.site.register(Message)