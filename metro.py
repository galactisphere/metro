import math

# Obtain input data and verify

# passageWidth = input("Passage width: ")
#truckSize = input("Truck size: ")

# Calculate volume of crushed rock and spoil which will be removed
def calculateRockVolume(passageWidth):
    # Returns cubic metres
    return(
        # Round to nearest integer
        round(
            # Add 10%
            1.1 * (
                # Calculate tunnel
                float(math.pi) * math.pow(3, 2) * 16500 +
                # Calculate cross passages
                16500 / 240 * 8 * 3.5 * float(passageWidth)
            )
        )
    )


# Calculate weight of crushed rock
def calculateRockMass(volume):
    # Returns tonnes
    # mass = density * volume
    return(2.35 * volume)

# Calculate number of trucks required for transport
def calculateTrucks(mass, size):
    return(math.ceil(mass / size))

print(float(math.pi) * math.pow(3, 2) * 16500)
