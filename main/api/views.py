from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
import requests
from . import consts

class CurrencyExchangeRateView(APIView):
    def get(self, request):

        response = requests.get(consts.EXCHANGE_API_URL, timeout=consts.API_TIMEOUT)
        response_in_json = response.json()
        currency = self.kwargs.get('currency')
        exchange_rate = response_in_json['Valute'][currency.upper()]['Value']
        return Response({'rate': exchange_rate}, status=status.HTTP_200_OK)
