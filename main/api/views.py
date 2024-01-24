import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from main.models import UserRequest
from main.api.serializers import UserRequestSerializer
from main.helpers import get_client_ip, get_exchange_rate_from_json_response
from . import consts


class CurrencyExchangeRateView(APIView):
    def get(self, request, currency):
        try:
            response = requests.get(consts.EXCHANGE_API_URL, timeout=consts.API_TIMEOUT)
        except requests.exceptions.Timeout:
            return Response(
                {"detail": "connection to external api timeout"},
                status=status.HTTP_503_SERVICE_UNAVAILABLE,
            )
        else:
            if response.status_code >= 400:
                return Response(
                    {"detail": "some problem with external api"},
                    status=status.HTTP_503_SERVICE_UNAVAILABLE,
                )
            response_in_json = response.json()
            exchange_rate = get_exchange_rate_from_json_response(
                response_in_json, currency
            )
            UserRequest.objects.create(
                ip_address=get_client_ip(request),
                currency=currency.upper(),
                exchange_rate=exchange_rate,
            )
            last_ten_requests = UserRequest.objects.filter(
                ip_address=get_client_ip(request)
            ).order_by("-timestamp")[:10]
            return Response(
                {
                    "exchange-rate": exchange_rate,
                    "last-10-requests": UserRequestSerializer(
                        last_ten_requests, many=True
                    ).data,
                },
                status=status.HTTP_200_OK,
            )
