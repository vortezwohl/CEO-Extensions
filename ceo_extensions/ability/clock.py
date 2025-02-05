import datetime
from ceo import ability


@ability
def get_current_datetime(*args, **kwargs) -> str:
    # `get_current_datetime` provides the current time to the user
    return str(datetime.datetime.now())
