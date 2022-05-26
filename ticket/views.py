from django.views.generic import ListView
from . import models

class TicketListView(ListView):
	model = models.Ticket
