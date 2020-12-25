import math


def moaToMil(moa):
    """ This function us used
         Inputs: moa = angle in minutes
         Outputs: none
         returns: angle in milliradians
    """
    return moa * 0.29088821


def milToInch(mil, feet):
    """ This function us used to convert mils to inches
         Inputs:
           mil =  angle in milliradians
           feet = adjacent side in feet
         Outputs: none
         returns: adjacent side in inches
    """
    return (feet * 12) * (mil / 1000)


def moaToInch(moa, feet):
    """ This function us used to convert moa to inches
         Inputs:
           moa =  angle in minutes
           feet = adjacent side in feet
         Outputs: none
         returns: adjacent side in inches
    """
    mil = moaToMil(moa)
    return milToInch(mil, feet)


def get_inital_upward_velocity(sight_height, time_of_flight):
    """ This function calculates the initial upward velocity used in the
    cant compensation calculation
    Inputs:
        sight_height =  distance of sight above bore height in inches
        time_of_flight = total time of flight to the target

    returns: initial upward velocity in feet per second (fps)

    Formula:
        vz0 = ( Sz / t ) - 1/2(gt)
        vz0 = initial upward velocity
        Sz = upward distance
        t = time of flight
        g = −32.137 feet per second squared
      Note:  the minus indicating the acceleration is “down”
      Source: https://www.empyrealsciences.com/Estimation%20of%20Shot%20Error%20due%20to%20Rifle%20Cant.pdf
    """

    return ((sight_height/12) / time_of_flight) + (0.5 * 32.137 * time_of_flight)


def get_incline_compensation(path_inches, incline_angle):
    return path_inches * math.cos(incline_angle) * -1


def get_cant_compensation(time_of_flight, cant_angle, sight_height):
    """
      https://www.empyrealsciences.com/Estimation%20of%20Shot%20Error%20due%20to%20Rifle%20Cant.pdf
    """
    initial_upward_velocity = get_inital_upward_velocity(
        sight_height, time_of_flight)
    horizontal_error = (initial_upward_velocity *
                        math.sin(cant_angle)) * time_of_flight
    vertical_error = -(initial_upward_velocity *
                       (1 - math.cos(cant_angle))) * time_of_flight
    return horizontal_error, vertical_error
