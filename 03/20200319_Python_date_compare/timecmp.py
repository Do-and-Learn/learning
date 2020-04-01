from datetime import datetime, timedelta

if __name__ == '__main__':
    time1 = datetime.strptime('10:00:00', '%H:%M:%S')
    time2 = datetime.strptime('12:00:00', '%H:%M:%S')

    assert (timedelta(hours=1) > time2 - time1) is False
    assert (timedelta(hours=2) > time2 - time1) is False
    assert (timedelta(hours=2, seconds=1) > time2 - time1) is True
    assert (timedelta(hours=2, seconds=1) > time2 - time1 > timedelta(hours=2)) is False
    assert (timedelta(hours=2, seconds=1) > time2 - time1 >= timedelta(hours=2)) is True
