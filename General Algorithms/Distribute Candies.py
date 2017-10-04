def distributeCandies(candies):
    """
    :type candies: List[int]
    :rtype: int
    """
    numberofcandies = len(candies)
    typeofcandies = len(set(candies))

    if typeofcandies < (numberofcandies/2):
        return typeofcandies
    else:
        return numberofcandies/2