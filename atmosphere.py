import math


def calcFR(temperature, pressure, relative_humidity):
    """
    Drag coefficient atmospheric corrections
    """
    VPw = 4e-6*math.pow(temperature, 3) - 0.0004 * \
        math.pow(temperature, 2)+0.0234*temperature-0.2517
    frh = 0.995*(pressure/(pressure-(0.3783)*(relative_humidity)*VPw))
    return frh


def calcFP(pressure):
    p_std = 29.53  # in-hg; standard pressure at sea level
    fp = (pressure - p_std) / (p_std)
    return fp


def calcFT(temperature, altitude):
    t_std = -0.0036 * altitude + 59
    FT = (temperature - t_std) / (459.6 + t_std)
    return FT


def calcFA(altitude):
    fa = 0
    fa = -4e-15*math.pow(altitude, 3)+4e-10 * \
        math.pow(altitude, 2)-3e-5*altitude+1
    return (1/fa)


def atmosphere_correction(drag_coefficient, altitude, barometer, temperature, relative_humidity):
    """
      A function to correct a "standard" Drag Coefficient for differing atmospheric conditions.
      @param drag_coefficient  G1, G2, G3, G4, G5, G6, G7, or G8
      @param altitude          The altitude above sea level in feet.  Standard altitude is 0 feet above sea level.
      @param barometer         The barometric pressure in inches of mercury (in Hg).
                              This is not "absolute" pressure, it is the "standardized" pressure reported in the papers and news.
                              Standard pressure is 29.53 in Hg.
      @param temperature       The temperature in Fahrenheit.  Standard temperature is 59 degrees.
      @param relative_humidity The relative humidity fraction.  Ranges from 0.00 to 1.00, with 0.50 being 50% relative humidity.
                              Standard humidity is 78%
      @return The corrected drag coefficient for the supplied drag coefficient and atmospheric conditions.
    """
    fa = calcFA(altitude)
    ft = calcFT(temperature, altitude)
    fr = calcFR(temperature, barometer, relative_humidity)
    fp = calcFP(barometer)

    # Calculate the atmospheric correction factor
    cd = (fa*(1+ft-fp)*fr)
    return drag_coefficient*cd
