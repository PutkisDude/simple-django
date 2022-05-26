from django.views.generic import ListView, DetailView
from . import models

class TicketListView(ListView):
	model = models.Ticket

class TicketDetailView(DetailView):
	model = models.Ticket
