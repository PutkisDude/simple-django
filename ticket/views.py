from django.views.generic import ListView, DetailView, UpdateView
from . import models

class TicketListView(ListView):
	model = models.Ticket

class TicketDetailView(DetailView):
	model = models.Ticket

class TicketUpdateView(UpdateView):
	model = models.Ticket
	fields = ["title", "description"]
	success_url = ""
