def get_exchange_rate_from_json_response(response_in_json, currency):
    return response_in_json["Valute"][currency.upper()]["Value"]


def get_client_ip(request):
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0]
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip
