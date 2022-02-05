from django.db import models
from django.conf import settings

class Interest(models.Model):
	title = models.CharField(max_length=50)
	users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="interests", blank=True, null=True)

	def __str__(self):
		return self.title

class Group(models.Model):
	title = models.CharField(max_length=50)

	def __str__(self):
		return self.title

class Membership(models.Model):
	PENDING = "PENDING"
	REJECTED = "REJECTED"
	MEMBER = "MEMBER"
	ADMIN = "ADMIN"
	ROLES = (
		(PENDING, "Pending"),
		(REJECTED, "Rejected"),
		(MEMBER, "Member"),
		(ADMIN, "Admin"),
	)

	role = models.CharField(max_length=30, choices=ROLES)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="memberships")
	group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="memberships")

	def __str__(self):
		return self.user.email

class Ad(models.Model):
	title = models.CharField(max_length=150)
	description = models.TextField()
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="ads", blank=True, null=True)
	group = models.OneToOneField(Group, on_delete=models.CASCADE, blank=True, null=True)

	def __str__(self):
		return self.title

# class Chat(models.Model):
# 	pass