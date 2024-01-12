"""
SilverServiceTaxi Class
"""

from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    taxi = SilverServiceTaxi("Hummer", 200, 2)
    taxi.drive(18)
    print(taxi)
    print(f"Taxi fare: {(taxi.get_fare())}")


main()
