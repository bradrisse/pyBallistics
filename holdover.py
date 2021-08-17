class holdover:
    def __init__(self, yards, meters, moa_correction, mil_correction, impact_in, path_inches, seconds):
        self.yards = yards
        self.meters = meters
        self.moa_correction = moa_correction
        self.mil_correction = mil_correction
        self.impact_in = impact_in
        self.path_inches = path_inches
        self.seconds = seconds

    def get_meters(self):
        return self.meters

    def get_yards(self):
        return self.yards

    def get_mil_correction(self):
        return self.mil_correction

    def get_moa_correction(self):
        return self.moa_correction
