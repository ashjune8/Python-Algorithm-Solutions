def maxEvents(arrival, duration):

    maxEvents = 0

    i = 0
    while i < len(arrival) - 1:
        if((arrival[i] + duration[i]) <= arrival[i+1] ):
            maxEvents += 1
            i += 1
        else:
            i += 1
    
    # Add last event 
    maxEvents += 1

    return maxEvents

print maxEvents([1,1,2,2], [2,3,1,4])
