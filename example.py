from bdc import calcBDC
from utils import get_incline_compensation
from utils import get_cant_compensation
import math

hold_overs = calcBDC(400)

for point in hold_overs.points:
    incline_compensation = get_incline_compensation(point.path_inches, -15)

    cant_compensation = get_cant_compensation(point.seconds, 90, 1.5)

    print("hold_over %s %s %s %s %s" %
          (point.yards, point.path_inches, incline_compensation, abs(point.path_inches-incline_compensation), cant_compensation))
