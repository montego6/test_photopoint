from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
import requests

from main.helpers import get_exchange_rate_from_json_response
from . import consts

class CurrencyExchangeRateView(APIView):
    def get(self, request, currency):
        try:
            response = requests.get(consts.EXCHANGE_API_URL, timeout=consts.API_TIMEOUT)
        except requests.exceptions.Timeout:
            return Response({'detail': 'connection to outer api timeout'}, status=status.HTTP_503_SERVICE_UNAVAILABLE)
        else:
            response_in_json = response.json()
            exchange_rate = get_exchange_rate_from_json_response(response_in_json, currency)
            return Response({'exchange-rate': exchange_rate}, status=status.HTTP_200_OK)
