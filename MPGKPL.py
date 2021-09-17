#!/usr/bin/python

# Create the MPGKPL Class

class MPGKPL(float):

    # Constructor
    def __init__(self, mileage):
        self.mileage = float(mileage)
        self.MileToKm = 1.609344
        self.GalToLtr = 3.785411784

    # Method to get Miles per Liter
    def MPGtoMPL(self):
        return(self.mileage/self.GalToLtr)

    # Method to get Kilometers per Liter
    def MPLtoKPL(self):
        return(self.MPGtoMPL() * self.MileToKm)

while True:
    mileage = input("Please enter the mileage in MPG [Enter to Terminate]: ")
    if mileage == '':
        print('Program terminated by user.')
        break

    newmileagecalc = MPGKPL(mileage)

    newmileage = newmileagecalc.MPLtoKPL()

    print(f'The mileage in Kilometers per Liter is {newmileage:.2f}')

