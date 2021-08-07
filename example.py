from bdc import calcBDC
from utils import get_incline_compensation
from utils import get_cant_compensation
import math

import sys, logging

#logLevel=logging.DEBUG
logLevel=logging.INFO
#logLevel=logging.WARNING

# If logLevel is unset, we will only display the most serious messages.
try:
    logLevel
except NameError:
    logLevel=logging.CRITICAL
finally:
    logging.basicConfig(format='%(levelname)s : %(filename)s : %(funcName)s : %(lineno)4d : %(message)s', level=logLevel, handlers=[logging.StreamHandler(sys.stdout)])

logging.debug('Example Debug Message')
logging.info('Example Info Message')
logging.warning('Example Warning Message')

hold_overs = calcBDC(400)

for point in hold_overs.points:
    incline_compensation = get_incline_compensation(point.path_inches, -15)

    cant_compensation = get_cant_compensation(point.seconds, 90, 1.5)

    print("hold_over %s %s %s %s %s" %
          (point.yards, point.path_inches, incline_compensation, abs(point.path_inches-incline_compensation), cant_compensation))
