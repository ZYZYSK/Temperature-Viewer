from django import template
from django.utils import timezone
register = template.Library()


@register.simple_tag
def previous_year(year, month=None, day=None):
    # 引数により前日/前月/前年を計算し、その年を返す
    # 年
    if month is None and day is None:
        return year - 1
    # 月
    elif day is None:
        dt = timezone.datetime(year, month, 1)
        return (dt - timezone.timedelta(months=1)).year
    # 日
    else:
        dt = timezone.datetime(year, month, day)
        return (dt - timezone.timedelta(days=1)).year


@register.simple_tag
def previous_month(year, month, day=None):
    # 引数により前日/前月を計算し、その月を返す
    # 前月
    if day is None:
        dt = timezone.datetime(year, month, 1)
        return (dt - timezone.timedelta(months=1)).month
    # 前日
    else:
        dt = timezone.datetime(year, month, day)
        return (dt - timezone.timedelta(days=1)).month


@register.simple_tag
def previous_day(year, month, day):
    # 引数により前日を計算し、その日を返す
    dt = timezone.datetime(year, month, day)
    return (dt - timezone.timedelta(days=1)).day


@register.simple_tag
def next_year(year, month=None, day=None):
    # 引数により翌日/翌月/翌年を計算し、その年を返す
    # 年
    if month is None and day is None:
        return year + 1
    # 月
    elif day is None:
        dt = timezone.datetime(year, month, 1)
        return (dt + timezone.timedelta(months=1)).year
    # 日
    else:
        dt = timezone.datetime(year, month, day)
        return (dt + timezone.timedelta(days=1)).year


@register.simple_tag
def next_month(year, month, day=None):
    # 引数により翌日/翌月を計算し、その月を返す
    # 翌月
    if day is None:
        dt = timezone.datetime(year, month, 1)
        return (dt + timezone.timedelta(months=1)).month
    # 翌日
    else:
        dt = timezone.datetime(year, month, day)
        return (dt + timezone.timedelta(days=1)).month


@register.simple_tag
def next_day(year, month, day):
    # 引数により翌日を計算し、その日を返す
    dt = timezone.datetime(year, month, day)
    return (dt + timezone.timedelta(days=1)).day