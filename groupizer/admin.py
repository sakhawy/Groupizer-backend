from django.contrib import admin

from groupizer import models

class InterestAdmin(admin.ModelAdmin):
	list_diplay = ["__str__"]

class AdAdmin(admin.ModelAdmin):
	list_diplay = ["__str__"]

class MembershipAdmin(admin.ModelAdmin):
	list_diplay = ["__str__"]

class GroupAdmin(admin.ModelAdmin):
	list_diplay = ["__str__"]

admin.site.register(models.Interest, InterestAdmin)
admin.site.register(models.Ad, AdAdmin)
admin.site.register(models.Membership, MembershipAdmin)
admin.site.register(models.Group, GroupAdmin)