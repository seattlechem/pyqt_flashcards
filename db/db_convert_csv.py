import datetime

def convert_str_datetime(date_str: str) -> datetime:
    # convert string to datetime
    format_str = '%m/%d/%Y'
    datetime_obj = datetime.datetime.strptime(date_str, format_str)

    return datetime_obj
