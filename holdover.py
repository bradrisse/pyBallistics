class holdover:
    def __init__(self, yards, moa_correction, impact_in, path_inches, seconds):
        self.yards = yards
        self.moa_correction = moa_correction
        self.impact_in = impact_in
        self.path_inches = path_inches
        self.seconds = seconds

    def get_yards(self):
        return self.yards

    def get_moa_correction(self):
        return self.moa_correction
