from django.template import Library
from dateutil import parser
from dateutil import tz
register = Library()

@register.filter(name="getISTTimeFromUTCTime")
def get_IST_time_from_UTC_time(utc_date):
    if isinstance(utc_date,unicode) :
        utc_date = parser.parse(utc_date)
    try:
        return get_IST_time_from_utc_time(utc_date)
    except Exception as e:
        print e
        return ""


def get_IST_time_from_utc_time(datetime_obj):
    from_zone = tz.gettz('UTC')
    to_zone = tz.gettz('Asia/Kolkata')
    gmt = datetime_obj.replace(tzinfo=from_zone)
    local_time = gmt.astimezone(to_zone)
    return local_time

@register.filter(name="getNameLabel")
def get_user_name_lable(name_string):
    if name_string:
        name_string = name_string[:2]
        name_string = name_string.upper()
        return name_string