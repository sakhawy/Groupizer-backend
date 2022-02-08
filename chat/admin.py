from django.contrib import admin

from chat import models

class ChatAdmin(admin.ModelAdmin):
	list_diplay = ["__str__"]

class MessageAdmin(admin.ModelAdmin):
	list_diplay = ["__str__"]

admin.site.register(models.Chat, ChatAdmin)
admin.site.register(models.Message, MessageAdmin)
