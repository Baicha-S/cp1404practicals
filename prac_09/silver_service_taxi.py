"""Silver service taxi Class"""
from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Silver Service Taxi"""
    flagfall = 4.5

    def __int__(self, name, fuel, fanciness):
        """Initialise SilverServiceTaxi"""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        """Return string."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        """Get current fare."""
        return self.flagfall + super().get_fare()
