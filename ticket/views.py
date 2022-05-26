from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from . import models
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class TicketListView(ListView):
	model = models.Ticket

class TicketDetailView(DetailView):
	model = models.Ticket

class TicketUpdateView(UpdateView):
	model = models.Ticket
	fields = ["title", "description"]

class TicketCreateView(LoginRequiredMixin, CreateView):
	model = models.Ticket
	fields = ["title", "description"]
	success_url = reverse_lazy('ticket_list')

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super().form_valid(form)	

class TicketDeleteView(DeleteView):
	model = models.Ticket
	success_url = reverse_lazy('ticket_list')
