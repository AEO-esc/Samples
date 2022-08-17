def getMinimumDays(parcels):
    smallestParcel = getParcelHelper(parcels)
    print(smallestParcel)

    totalDays = 0
    for i in range(0, len(parcels)):
        while parcels[i] > 0:
            deliverDailyParcel
    
    return totalDays
    
    totalDays += 1
    getMinimumDays(parcels)
    totalDays += 1
    print(parcels)
    print(totalDays)

def getParcelHelper(parcels):
    smallestParcel = 1
    largestParcel = parcels[0]
    for i in range(0, len(parcels)):
        if smallestParcel >= parcels[i] and largestParcel <= parcels[i]:
            smallestParcel = parcels[i]
            largestParcel = parcels[i]
        elif largestParcel <= parcels[i]:
            largestParcel = parcels[i]
    return smallestParcel

def deliverDailyParcel(parcels, smallestParcel):
    for i in range(0, len(parcels)):
        if parcels[i] > 0:
            parcels[i] -= smallestParcel
    return parcels

def main() -> None:
    myParcel = [2, 3, 4, 3, 3]
    getMinimumDays(myParcel)

if __name__ == '__main__':
    main()