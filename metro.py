import math

# Calculate volume of crushed rock and spoil which will be removed
def calculateRockVolume(passageWidth):
    # Returns cubic metres
    return(
        # Round to two decimal places
        round(
            # Add 10%
            1.1 * (
                # Calculate two tunnels
                float(math.pi) * 3 * 3 * 16500 * 2 +
                # Calculate cross passages
                16500 / 240 * 8 * 3.5 * float(passageWidth)
            )
        , 2)
    )


# Calculate weight of crushed rock
def calculateRockMass(volume):
    # Returns tonnes
    # mass = density * volume
    return(round(2.35 * volume, 2), 2)

# Calculate number of trucks required for transport
def calculateTrucks(mass, size):
    return(math.ceil(mass / size))

# Create header in output
print("\n\n\nSydney Metro —")
print("Material Recycling Calculator")
print("=============================")

# Obtain input data and verify
try:
    passageWidth = int(input("\nEnter the passage width of the tunnels (m, int): "))
except ValueError:
    raise TypeError("Passage width — Please enter a positive integer.")
if passageWidth < 0:
    raise Exception("Passage width — Please enter a positive integer.")

truckSize = input("\nA: 11 tonne\nB: 15 tonne\nC: 20 tonne\nEnter the truck size from the above options, with A, B, or C: ")
if truckSize == "A":
    truckSize = 11
elif truckSize == "B":
    truckSize = 15
elif truckSize == "C":
    truckSize = 20
else:
    raise Exception("Truck size — Please enter either A, B, or C.")

# Calculate and return values
rockVol = calculateRockVolume(passageWidth)
print("\nRock volume to two decimal places: " + str(rockVol) + " m³")

rockMass = calculateRockMass(rockVol)
print("Rock mass to two decimal places: " + str(rockMass) + " tonnes")

numberOfTrucks = calculateTrucks(rockMass, truckSize)
print("Number of trucks required for transport: " + str(numberOfTrucks))
