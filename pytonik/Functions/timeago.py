# Author : BetaCodings
# Author : info@betacodings.com
# Maintainer By: Emmanuel Martins
# Maintainer Email: emmamartinscm@gmail.com
# Created by BetaCodings on 19/11/2019.

import datetime

class timeago:

    def __init__(self, date_time, format=""):
        self.date_time = date_time
        self.fmt = self.format(format)
        self.ago = self.ago()

    def ago(self):
        delta = self.delta()
        if delta.find(',') > 0:
            days, hours = delta.split(',')
            days = int(days.split()[0].strip())
            hours, minutes = hours.split(':')[0:2]
        else:
            hours, minutes = delta.split(':')[0:2]
            days = 0
        days, hours, minutes = int(days), int(hours), int(minutes)
        datelets = []
        years, months, xdays = None, None, None
        plural = lambda x: 's' if x != 1 else ''
        if days >= 365:
            years = int(days / 365)
            datelets.append('%d year%s' % (years, plural(years)))
            days = days % 365
        if days >= 30 and days < 365:
            months = int(days / 30)
            datelets.append('%d month%s' % (months, plural(months)))
            days = days % 30
        if not years and days > 0 and days < 30:
            xdays = days
            datelets.append('%d day%s' % (xdays, plural(xdays)))
        if not (months or years) and hours != 0:
            datelets.append('%d hour%s' % (hours, plural(hours)))
        if not (xdays or months or years):
            datelets.append('%d minute%s' % (minutes, plural(minutes)))

        return ', '.join(datelets) + ' ago.'


    def delta(self):
        current_datetime = datetime.datetime.now()
        try:
            return str(current_datetime - self.fmt)
        except Exception as err:
            return err


    def format(self, fmt=''):
        fmt = '%Y-%m-%d %H:%M:%S' if fmt is "" else  fmt
        try:
            return datetime.datetime.strptime(self.date_time, fmt)
        except Exception as err:
            return err


