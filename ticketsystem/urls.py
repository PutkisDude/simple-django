"""ticketsystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ticket import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.TicketListView.as_view(), name="ticket_list"),
    path('<int:pk>', views.TicketDetailView.as_view(), name="ticket_detail"),
    path('<int:pk>/update', views.TicketUpdateView.as_view()),
    path('<int:pk>/delete', views.TicketDeleteView.as_view()),
    path('new/', views.TicketCreateView.as_view()),
    
    path('accounts/login/', auth_views.LoginView.as_view(), name="login")
]
