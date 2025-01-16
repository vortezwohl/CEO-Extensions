import datetime
from ceo import ability


@ability
def get_current_datetime(*args, **kwargs) -> str:
    return str(datetime.datetime.now())
