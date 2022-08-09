# https://www.youtube.com/watch?v=5cvM-crlDvg
# __repr__ is a fallback method for __str__
# The goal of __repr__ is to be unambiguous
# The goal of __str__ is to be readable
# __repr__ is for developers for debugging

import datetime
import pytz

a = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)

b = str(a)

print (f'str(a): {str(a)}')
print (f'str(b): {str(b)}')
print('\n')

print (f'repr(a): {repr(a)}')
print (f'repr(b): {repr(b)}')
print('\n')