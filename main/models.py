from django.db import models


class UserRequest(models.Model):
    ip_address = models.GenericIPAddressField(protocol="both", unpack_ipv4=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    currency = models.CharField(max_length=4)
    exchange_rate = models.DecimalField(max_digits=12, decimal_places=4)
