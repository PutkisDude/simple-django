from django.db import models
from django.contrib.auth.models import User

class Ticket(models.Model):
	user = models.ForeignKey(
		User,
		on_delete=models.CASCADE	
		)
	title = models.CharField(max_length=300)
	description = models.TextField()

	def __str__(self):
		return f"#{self.id} - {self.title}"
