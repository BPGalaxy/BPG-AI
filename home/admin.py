from django.contrib import admin
from .models import *
from djangoql.admin import DjangoQLSearchMixin

@admin.register(Message)
class MessageAdmin(DjangoQLSearchMixin, admin.ModelAdmin):
    list_display = ['id', 'accountid', 'senderuser', 'chatid', 'text']

@admin.register(Status)
class MessageAdmin(DjangoQLSearchMixin, admin.ModelAdmin):
    list_display = ['accountid', 'is_VIP', 'is_owner', 'is_developer', 'is_staff', 'is_banned']

@admin.register(Customization)
class MessageAdmin(DjangoQLSearchMixin, admin.ModelAdmin):
    list_display = ['accountid', 'Name', 'Emoji', 'Occupation', 'Interests']

@admin.register(Chats)
class MessageAdmin(DjangoQLSearchMixin, admin.ModelAdmin):
    list_display = ['id', 'accountid', 'chatname', 'is_deleted', 'is_rp', 'chatid']

@admin.register(Characters)
class MessageAdmin(DjangoQLSearchMixin, admin.ModelAdmin):
    list_display = ['id', 'accountid', 'Name', 'is_deleted']

@admin.register(Settings)
class MessageAdmin(DjangoQLSearchMixin, admin.ModelAdmin):
    list_display = ['id']

