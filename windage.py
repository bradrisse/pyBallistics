import math
import angles


def windage(wind_speed, vi, x, t):
    """
      A function to compute the windage deflection for a given crosswind speed,
      given flight time in a vacuum, and given flight time in real life.
      @param wind_speed The wind velocity in mi/hr.
      @param vi         The initial velocity of the projectile (muzzle velocity).
      @param x         The range at which you wish to determine windage, in feet.
      @param t          The time it has taken the projectile to traverse the range x, in seconds.
      @return The amount of windage correction, in inches, required to achieve zero on a target at the given range.
    """
    # Convert to inches per second.
    vw = wind_speed*17.60
    return (vw*(t-x/vi))


def headwind(wind_speed, wind_angle):
    """
      Resolve any wind / angle combination into headwind.
      Headwind is positive at {@code wind_angle=0}
      @param wind_speed The wind velocity, in mi/hr.
      @param wind_angle The angle from which the wind is coming, in degrees.
                        0 degrees is from straight ahead
                        90 degrees is from right to left
                        180 degrees is from directly behind
                        270 or -90 degrees is from left to right.
      @return the headwind velocity component, in mi/hr.
    """
    w_angle = angles.deg_to_rad(wind_angle)
    return (math.cos(w_angle) * wind_speed)


def crosswind(wind_speed, wind_angle):
    """
     Resolve any wind / angle combination into crosswind.
     Positive is from Shooter's Right to Left (Wind from 90 degree)
     @param wind_speed The wind velocity, in mi/hr.
     @param wind_angle The angle from which the wind is coming, in degrees.
                       0 degrees is from straight ahead
                       90 degrees is from right to left
                       180 degrees is from directly behind
                       270 or -90 degrees is from left to right.
     @return the crosswind velocity component, in mi/hr.
    """
    w_angle = angles.deg_to_rad(wind_angle)
    return (math.sin(w_angle) * wind_speed)
