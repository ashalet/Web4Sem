from django.urls import path
from portfolio.views import *
from api.views import *



urlpatterns = [
    path('mailing/<int:pk>/', mailing_view, name='mailing_view'),
    path('mailing/', mailing_view, name='mailing_view'),
]
