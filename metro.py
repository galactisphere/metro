import math

# Obtain input data

    # 
    # Width for cross passages

# Calculate volume of crushed rock and spoil which will be removed

def calculateRock(passageWidth):
    return(
        # Round to 2 decimal places
        round(
            # Multiply by 8 stations and add 10%
            8 * 1.1 * (
                # Calculate tunnel
                float(math.pi) * math.sqrt(3) * 16500 +
                # Calculate cross passages
                16500 / 240 * 8 * 3.5 * float(passageWidth)
            )
        , 2)
    )

print(calculateRock(input()))

# Calculate weight of crushed rock

# def calculateRockWeight():


# Calculate number of trucks required for transport