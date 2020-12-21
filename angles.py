# Specialty angular conversion functions
import math
import drag
import constants


def deg_to_moa(deg):
    """
    Converts degrees to minutes of angle
    """
    return deg*60


def deg_to_rad(deg):
    """
    Converts degrees to radians
    """
    return deg*math.pi/180


def moa_to_deg(moa):
    """
    Converts minutes of angle to degrees
    """
    return moa/60


def moa_to_rad(moa):
    """
    Converts minutes of angle to radians
    """
    return moa/60*math.pi/180


def rad_to_deg(rad):
    """
    Converts radians to degrees
    """
    return rad*180/math.pi


def rad_to_moa(rad):
    """
    Converts radiants to minutes of angle
    """
    return rad*60*180/math.pi


def zero_angle(drag_function, drag_coefficient, vi, sight_height, zero_range, y_intercept):
    """
    A function to determine the bore angle needed to achieve a target zero at Range yards
    (at standard conditions and on level ground.)
    @param drag_function    G1, G2, G3, G5, G6, G7, or G8
    @param drag_coefficient The coefficient of drag for the projectile, for the supplied drag function.
    @param vi               The initial velocity of the projectile, in feet/s
    @param sight_height     The height of the sighting system above the bore centerline, in inches.
                            Most scopes fall in the 1.6 to 2.0 inch range.
    @param zero_range       The range in yards, at which you wish the projectile to intersect yIntercept.
    @param y_intercept      The height, in inches, you wish for the projectile to be when it crosses ZeroRange yards.
                            This is usually 0 for a target zero, but could be any number.  For example if you wish
                            to sight your rifle in 1.5" high at 100 yds, then you would set yIntercept to 1.5, and ZeroRange to 100
    @return The angle of the bore relative to the sighting system, in degrees.

    """

    # Numerical Integration variables
    t = 0
    # The solution accuracy generally doesn't suffer if its within a foot for each second of time.
    dt = 1/vi
    y = -sight_height/12
    x = 0

    # State variables for each integration loop.

    # velocity
    v = 0
    vx = 0
    vy = 0

    # Last frame's velocity, used for computing average velocity.
    vx1 = 0
    vy1 = 0

    # acceleration
    dv = 0
    dvx = 0
    dvy = 0

    # Gravitational acceleration
    Gx = 0
    Gy = 0

    # The actual angle of the bore.
    angle = 0

    # We know it's time to quit our successive approximation loop when this is 1.
    quit = 0

    # The change in the bore angle used to iterate in on the correct zero angle.
    # Start with a very coarse angular change, to quickly solve even large launch angle problems.
    da = deg_to_rad(14)

    # The general idea here is to start at 0 degrees elevation, and increase the elevation by 14 degrees
    # until we are above the correct elevation.  Then reduce the angular change by half, and begin reducing
    # the angle.  Once we are again below the correct angle, reduce the angular change by half again, and go
    # back up.  This allows for a fast successive approximation of the correct elevation, usually within less
    # than 20 iterations.

    while quit == 0:
        angle = da + angle
        vy = vi * math.sin(angle)
        vx = vi * math.cos(angle)
        Gx = constants.GRAVITY * math.sin(angle)
        Gy = constants.GRAVITY * math.cos(angle)

        t = 0
        x = 0
        y = -sight_height/12

        while x <= zero_range*3:
            vy1 = vy
            vx1 = vx
            v = math.pow((math.pow(vx, 2)+math.pow(vy, 2)), 0.5)
            dt = 1/v

            dv = drag.retard(drag_function, drag_coefficient, v)
            dvy = -dv*vy/v*dt
            dvx = -dv*vx/v*dt

            vx = vx+dvx
            vy = vy+dvy
            vy = vy+dt*Gy
            vx = vx+dt*Gx

            x = x+dt*(vx+vx1)/2
            y = y+dt*(vy+vy1)/2
            # Break early to save CPU time if we won't find a solution.
            if vy < 0 and y < y_intercept:
                break

            if vy > 3*vx:
                break

            t = t+dt

        if y > y_intercept and da > 0:
            da = -da/2

        if y < y_intercept and da < 0:
            da = -da/2

        # If our accuracy is sufficient, we can stop approximating.
        if math.fabs(da) < moa_to_rad(0.01):
            quit = 1
        if angle > deg_to_rad(45):
            quit = 1

        angle = da + angle

    return rad_to_deg(angle)
