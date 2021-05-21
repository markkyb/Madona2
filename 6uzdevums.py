"""
Uzrakstiet programmu Python, lai parādītu rītdienas datumu.
"""

import datetime
import sys
import os


sodiena = datetime.date.today()
rit=sodiena+datetime.timedelta(days=1)

print(sodiena)
print(rit)