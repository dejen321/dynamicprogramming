import io
import datetime

# https://www.guru99.com/date-time-and-datetime-classes-in-python.html
now = datetime.datetime.now()
now1 = datetime.date.today()
now2 = now1.month



print('now {} {} {}'.format(now, now1, now2 ))
