from bdc import calcBDC
from utils import get_incline_compensation
from utils import get_cant_compensation
import math

hold_overs = calcBDC(400)

print()
print("All Points in hold_overs:")
for point in hold_overs.points:
    incline_compensation = get_incline_compensation(point.path_inches, -15)

    cant_compensation = get_cant_compensation(point.seconds, 90, 1.5)

    print("hold_over %8s %8s %s %s %s %s" %
          (point.yards, point.meters, point.path_inches, incline_compensation, abs(point.path_inches-incline_compensation), cant_compensation))

print()
print("Whole Yards Only")
print("%-8s | %-8s  | %-8s | %-8s | %-9s | %-8s |" %
      ("Range", "Drop", "MOA", "Mils", "Time", "Velocity"))
print("%-8s | %-8s  | %-8s | %-8s | %-9s | %-8s |" %
      ("(Yards)", "(Inches)", "", "", "(Seconds)", "(fps)"))
for point in hold_overs.points:
    if float(point.yards).is_integer():
        pi = '{:.3f}'.format(round(point.path_inches, 3))
        moac = '{:.2f}'.format(round(point.moa_correction, 2))
        milc = '{:.2f}'.format(round(point.mil_correction, 2))
        stime = '{:.3f}'.format(round(point.seconds, 3))
        vel = '{:.2f}'.format(round(point.velocity, 2))
        print("%8s | %8s  | %8s | %8s | %9s | %8s |" %
              (point.yards, pi, moac, milc, stime, vel))

print()
print("Whole Meters Only")
print("%-8s | %-8s  | %-8s | %-8s | %-9s | %-8s |" %
      ("Range", "Drop", "MOA", "Mils", "Time", "Velocity"))
print("%-8s | %-8s  | %-8s | %-8s | %-9s | %-8s |" %
      ("(Meters)", "(Inches)", "", "", "(Seconds)", "(fps)"))
for point in hold_overs.points:
    if float(point.meters).is_integer():
        pi = '{:.3f}'.format(round(point.path_inches, 3))
        moac = '{:.2f}'.format(round(point.moa_correction, 2))
        milc = '{:.2f}'.format(round(point.mil_correction, 2))
        stime = '{:.3f}'.format(round(point.seconds, 3))
        vel = '{:.2f}'.format(round(point.velocity, 2))
        print("%8s | %8s  | %8s | %8s | %9s | %8s |" %
              (point.meters, pi, moac, milc, stime, vel))
