
import windage
import constants
import angles
import math
import drag
import utils
from holdover import holdover
from points import points


def solve(drag_function, drag_coefficient, vi, sight_height, shooting_angle, zero_angle, wind_speed, wind_angle):

    t = 0
    dt = 0
    v = 0
    vx = 0
    vx1 = 0
    vy = 0
    vy1 = 0
    dv = 0
    dvx = 0
    dvy = 0
    x = 0
    y = 0

    hwind = windage.headwind(wind_speed, wind_angle)
    cwind = windage.crosswind(wind_speed, wind_angle)

    gy = constants.GRAVITY * \
        math.cos(angles.deg_to_rad((shooting_angle + zero_angle)))

    gx = constants.GRAVITY * \
        math.sin(angles.deg_to_rad((shooting_angle + zero_angle)))

    vx = vi * math.cos(angles.deg_to_rad(zero_angle))
    vy = vi * math.sin(angles.deg_to_rad(zero_angle))

    # y is in feet
    y = -sight_height/12

    n = 0

    hold_overs = points()

    while True:
        vx1 = vx
        vy1 = vy
        v = math.pow(math.pow(vx, 2)+math.pow(vy, 2), 0.5)
        dt = 0.5/v

        # Compute acceleration using the drag function retardation
        dv = drag.retard(drag_function, drag_coefficient, v+hwind)
        dvx = -(vx/v)*dv
        dvy = -(vy/v)*dv

        # Compute velocity, including the resolved gravity vectors.
        vx = vx + dt*dvx + dt*gx
        vy = vy + dt*dvy + dt*gy

        if x/3 >= n:

            if x > 0:
                range_yards = round(x/3)
                print("range_yards {}".format(range_yards))
                # if range_yards == 400:
                moa_correction = -angles.rad_to_moa(math.atan(y / x))
                print("moa_correction {}". format(moa_correction))
                path_inches = y*12
                print("path_inches {}". format(path_inches))
                impact_in = utils.moaToInch(moa_correction, x)
                seconds = t+dt
                print("seconds {}". format(seconds))
                hold_overs.add_point(
                    holdover(range_yards, moa_correction, impact_in, path_inches, seconds))

            n = n + 1

        # Compute position based on average velocity.
        x = x + dt * (vx+vx1)/2
        y = y + dt * (vy+vy1)/2

        if (math.fabs(vy) > math.fabs(3*vx) or n >= constants.BALLISTICS_COMPUTATION_MAX_YARDS):
            break

        t = t + dt

    return hold_overs
