from datetime import datetime, timezone, timedelta

def stem(label: str, blacklist: list):
    '''
    This function stems a given event label.

    Inputs:
    - label: single label to stem
    - blacklist: list of terms, that should be excluded from the label

    Return: stemmed label
    '''
    parts = label.split(' ')
    parts = list(filter(lambda x: x not in blacklist, parts))
    return ' '.join(parts)

def time_dif(x: tuple, interval: str):
    '''
    Calculate the differences between two points in time.

    Inputs:
        - x: tuple of two datetime objects
        - interval: indicator of the return type; accepted values: 'd', 'h', 's'

    Return: interval in days, hours or seconds
    '''
    res = time_wrap(x[0], x[1])

    days = res.days
    hours = res.seconds//60//60
    seconds = res.seconds

    if interval is 'd':
        return days
    elif interval is 'h':
        return hours + (days * 24)
    elif interval is 's':
        return seconds + (days * 24 * 60 * 60)

def number_of_non_workdays(start, end):
    '''
    Compute the number of days between two points in time, excluding weekends.

    Input:
        - start: datetime object
        - end: datetime object

    Return:
        int: number of days
    '''
    # 0: Monday
    days = []

    while(start <= end):
        days.append(start.weekday())
        start = start + timedelta(days=1)

    days = len(list(filter(lambda x: x > 4, days)))

    return days

def time_wrap(start: datetime, end: datetime, s_hour = 8, e_hour = 18):
    '''
    Return the temporal difference between two points in time, adjusted to a given workschedule.

    Input:
        - start: datetime object
        - end: datetime object
        - s_hour: start of workschedule
        - e_hour: end of workschedule
    
    Return:
        - timedelta in seconds
    '''

    # worktime after start event
    e_time = datetime(start.year, start.month, start.day, e_hour)
    start = start.replace(tzinfo=None)
    t1 = (e_time - start).seconds
    
    # worktime before end event
    end = end.replace(tzinfo=None)
    s_time = datetime(start.year, start.month, start.day, s_hour)
    t3 = (end - s_time).seconds
    
    # calculate days between start and end exclusive non-working days
    days_total = (end - start).days
    non_workingdays = number_of_non_workdays(start, end)
    
    working_days = days_total - non_workingdays
    if working_days > 1:
        working_days -= 1 # consider only complete day in between
        total_hours_between = (e_hour - s_hour) * working_days
        
        # convert into seconds
        t2 = total_hours_between * 60 * 60
    else:
        # in this case, there is no full working day between start and end
        t2 = 0
    
    total_dif = t1 + t2 + t3
    
    return timedelta(seconds=total_dif)