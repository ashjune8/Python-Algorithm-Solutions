def chooseFleets(wheels):
    combinations = []
    for i in range(len(wheels)):
        tempsum = 0
        straightDiv = False
        if(wheels[i]%2 == 0):
            tempsum += 1
        if(wheels[i]%4 == 0):
            tempsum += 1
        if(wheels[i]%6 == 0):
            tempsum += 1
        if( wheels[i]%2 != 0 and ((wheels[i]%2)%4) == 0):
            tempsum += 1
        if( wheels[i]%4 != 0 and ((wheels[i]%4)%2) == 0):
            tempsum += 1
        combinations.append(tempsum)
    
    return combinations

def chooseFleetsv1(wheels):
    combinations = []
    for i in range(len(wheels)):
        
        result = 0
        tempsum = wheels[i]
        while(tempsum > 0):
            tempsum = tempsum -2
            if(tempsum == 0):
                result += 1
                break
        tempsum = wheels[i]
        while(tempsum > 0):
            tempsum = tempsum -4
            if(tempsum == 0):
                result += 1
                break
        tempsum = wheels[i]
        while(tempsum > 0):
            tempsum = tempsum -2
            if(tempsum == 4):
                result += 1
                break
        tempsum = wheels[i]
        while(tempsum > 0):
            tempsum = tempsum -4
            if(tempsum == 2):
                result += 1
                break
        combinations.append(result)
        
    
    return combinations







print chooseFleetsv1([6,3,2])