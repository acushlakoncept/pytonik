# Author : BetaCodings
# Author : info@betacodings.com
# Maintainer By: Emmanuel Martins
# Maintainer Email: emmamartinscm@gmail.com
# Created by BetaCodings on 08/01/2020.

class count:


    def __getattr__(self, item):
        return item

    def __call__(self, *args, **kwargs):

        return None

    def __init__(self, *args,  **kwargs):
        return None


    def digit(self, num=0):
        num = float(num)
        if (float(num) > 1000000000) is True:
            getcount = str(float(round((num / 1000000000), ))) + str('T')

        elif (float(num) > 1000000):

            getcount = str(float(round((num / 1000000), 1))) + str('M')

        elif (float(num) > 1000) is True:

            getcount = str(float(round((num / 1000), 1))) + str('K')
        else:

            getcount = str(float(round((num / 1), 1)))

        return getcount

    def bytes(self, bit=0):
        # Return the given bytes as a human friendly KB, MB, GB, or TB string'
        B = float(bit)
        KB = float(1024)
        MB = float(KB ** 2)  # 1,048,576
        GB = float(KB ** 3)  # 1,073,741,824
        TB = float(KB ** 4)  # 1,099,511,627,776

        if B < KB:
            return '{0} {1}'.format(B, 'Bytes' if 0 == B > 1 else 'Byte')
        elif KB <= B < MB:
            return '{0:.2f} KB'.format(B / KB)
        elif MB <= B < GB:
            return '{0:.2f} MB'.format(B / MB)
        elif GB <= B < TB:
            return '{0:.2f} GB'.format(B / GB)
        elif TB <= B:
            return '{0:.2f} TB'.format(B / TB)

