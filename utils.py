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
