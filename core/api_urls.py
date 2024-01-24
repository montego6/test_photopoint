

from django.urls import path

from main.api.views import CurrencyExchangeRateView


urlpatterns = [
    path('exchange-rates/<str:currency>/', CurrencyExchangeRateView.as_view(), name='exchange-rates'),
]