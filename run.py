import os, platform

try:

    import requests

except:

    os.system('pip install requests')

import requests

bit = platform.architecture()[0]

if bit == '64bit':

    from KING import approval

    approval()

elif bit == '32bit':

    print('W8 for next update')