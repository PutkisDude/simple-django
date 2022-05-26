from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Ticket(models.Model):
	user = models.ForeignKey(
		User,
		on_delete=models.CASCADE	
		)
	title = models.CharField(max_length=300)
	description = models.TextField()

	def get_absolute_url(self):
		return reverse('ticket_detail', kwargs={'pk' : self.pk})

	def __str__(self):
		return f"#{self.id} - {self.title}"
