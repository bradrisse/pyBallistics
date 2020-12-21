import math


def G1(vp):
    acceleration = -1
    mass = -1

    if (vp > 4230):
        acceleration = 1.477404177730177e-04
        mass = 1.9565
    elif (vp > 3680):
        acceleration = 1.920339268755614e-04
        mass = 1.925
    elif (vp > 3450):
        acceleration = 2.894751026819746e-04
        mass = 1.875
    elif (vp > 3295):
        acceleration = 4.349905111115636e-04
        mass = 1.825
    elif (vp > 3130):
        acceleration = 6.520421871892662e-04
        mass = 1.775
    elif (vp > 2960):
        acceleration = 9.748073694078696e-04
        mass = 1.725
    elif (vp > 2830):
        acceleration = 1.453721560187286e-03
        mass = 1.675
    elif (vp > 2680):
        acceleration = 2.162887202930376e-03
        mass = 1.625
    elif (vp > 2460):
        acceleration = 3.209559783129881e-03
        mass = 1.575
    elif (vp > 2225):
        acceleration = 3.904368218691249e-03
        mass = 1.55
    elif (vp > 2015):
        acceleration = 3.222942271262336e-03
        mass = 1.575
    elif (vp > 1890):
        acceleration = 2.203329542297809e-03
        mass = 1.625
    elif (vp > 1810):
        acceleration = 1.511001028891904e-03
        mass = 1.675
    elif (vp > 1730):
        acceleration = 8.609957592468259e-04
        mass = 1.75
    elif (vp > 1595):
        acceleration = 4.086146797305117e-04
        mass = 1.85
    elif (vp > 1520):
        acceleration = 1.954473210037398e-04
        mass = 1.95
    elif (vp > 1420):
        acceleration = 5.431896266462351e-05
        mass = 2.125
    elif (vp > 1360):
        acceleration = 8.847742581674416e-06
        mass = 2.375
    elif (vp > 1315):
        acceleration = 1.456922328720298e-06
        mass = 2.625
    elif (vp > 1280):
        acceleration = 2.419485191895565e-07
        mass = 2.875
    elif (vp > 1220):
        acceleration = 1.657956321067612e-08
        mass = 3.25
    elif (vp > 1185):
        acceleration = 4.745469537157371e-10
        mass = 3.75
    elif (vp > 1150):
        acceleration = 1.379746590025088e-11
        mass = 4.25
    elif (vp > 1100):
        acceleration = 4.070157961147882e-13
        mass = 4.75
    elif (vp > 1060):
        acceleration = 2.938236954847331e-14
        mass = 5.125
    elif (vp > 1025):
        acceleration = 1.228597370774746e-14
        mass = 5.25
    elif (vp > 980):
        acceleration = 2.916938264100495e-14
        mass = 5.125
    elif (vp > 945):
        acceleration = 3.855099424807451e-13
        mass = 4.75
    elif (vp > 905):
        acceleration = 1.185097045689854e-11
        mass = 4.25
    elif (vp > 860):
        acceleration = 3.566129470974951e-10
        mass = 3.75
    elif (vp > 810):
        acceleration = 1.045513263966272e-08
        mass = 3.25
    elif (vp > 780):
        acceleration = 1.291159200846216e-07
        mass = 2.875
    elif (vp > 750):
        acceleration = 6.824429329105383e-07
        mass = 2.625
    elif (vp > 700):
        acceleration = 3.569169672385163e-06
        mass = 2.375
    elif (vp > 640):
        acceleration = 1.839015095899579e-05
        mass = 2.125
    elif (vp > 600):
        acceleration = 5.71117468873424e-05
        mass = 1.950
    elif (vp > 550):
        acceleration = 9.226557091973427e-05
        mass = 1.875
    elif (vp > 250):
        acceleration = 9.337991957131389e-05
        mass = 1.875
    elif (vp > 100):
        acceleration = 7.225247327590413e-05
        mass = 1.925
    elif (vp > 65):
        acceleration = 5.792684957074546e-05
        mass = 1.975
    elif (vp > 0):
        acceleration = 5.206214107320588e-05
        mass = 2.000

    return acceleration, mass


def retard(drag_function, drag_coefficient, vp):
    """
      A function to calculate ballistic retardation values based on standard drag functions.
      @param drag_function    G1, G2, G3, G4, G5, G6, G7, or G8
      @param drag_coefficient The coefficient of drag for the projectile for the given drag function.
      @param vp               The Velocity of the projectile.
      @return The function returns the projectile drag retardation velocity, in ft/s per second.
    """

    drag_functions = {
        "G1": G1(vp)
    }

    # Get the function from switcher dictionary
    acceleration, mass = drag_functions.get(drag_function, 1)

    if (acceleration != -1 and mass != -1 and vp > 0 and vp < 10000):
        return acceleration * math.pow(vp, mass)/drag_coefficient
    else:
        return -1
