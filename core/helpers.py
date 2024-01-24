import datetime
from . import consts


def is_interval_not_elapsed(last_request_time):
    return last_request_time > datetime.datetime.now() - datetime.timedelta(
        seconds=consts.INTERVAL_IN_SECS_BETWEEN_REQUESTS
    )
