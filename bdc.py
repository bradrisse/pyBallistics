import atmosphere
import angles
import ballistics


def calcBDC(range):
    k = 0
    # The ballistic coefficient for the projectile.
    bc = 0.269
    # Intial velocity, in ft/s
    v = 3165
    # The Sight height over bore, in inches.
    sh = 1.5
    # The shooting angle (uphill / downhill), in degrees.
    angle = 0
    # The zero range of the rifle, in yards.
#    zero = 50
#    zero = 100
    zero = 200
#    zero_unit = 'm'
    zero_unit = 'y'
    # The wind speed in miles per hour.
    windspeed = 0
    # The wind angle (0=headwind, 90=right to left, 180=tailwind, 270/-90=left to right)
    windangle = 0

    # Numbers for 22lr CCI Standard Velocity
#    bc = 0.122
#    v = 1070

    altitude = 0
    barometer = 29.59
    temperature = 59
    relative_humidity = 0.7

    drag_function = "G1"

    # If we wish to use the weather correction features, we need to
    # Correct the BC for any weather conditions.  If we want standard conditions,
    # then we can just leave this commented out.

    bc = atmosphere.atmosphere_correction(
        bc, altitude, barometer, temperature, relative_humidity)

    print("bc {}".format(bc))

    # Convert zero range in meters to yards for calculating the zero angle
    if zero_unit.lower() == 'm':
#        zero = zero*1.093613
        zero = zero*((100/2.54)/36)

    # First find the angle of the bore relative to the sighting system.
    # We call this the "zero angle", since it is the angle required to
    # achieve a zero at a particular yardage.  This value isn't very useful
    # to us, but is required for making a full ballistic solution.
    # It is left here to allow for zero-ing at altitudes (bc) different from the
    # final solution, or to allow for zero's other than 0" (ex: 3" high at 100 yds)
    zeroangle = angles.zero_angle(drag_function, bc, v, sh, zero, 0)

    # Now we have everything needed to generate a full solution.
    # So we do.  The solution is stored in the pointer "sln" passed as the last argument.
    # k has the number of yards the solution is valid for, also the number of rows in the solution.
    hold_overs = ballistics.solve(drag_function, bc, v, sh, angle,
                                  zeroangle, windspeed, windangle)

    return hold_overs
