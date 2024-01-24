def get_exchange_rate_from_json_response(response_in_json, currency):
    return response_in_json['Valute'][currency.upper()]['Value']