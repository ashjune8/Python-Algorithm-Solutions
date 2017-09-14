import sys

def candies(n, arr):
    Sol = [1]*n
    j = 0
    for i in range(1,n):
        if arr[i] > arr[i-1]:
            Sol[i] = Sol[i-1] +1
        elif arr[i] == arr[i-1]:
            if Sol[i-1] ==1:
                Sol[i] =1
            else:
                Sol[i] =1
        elif arr[i] < arr[i-1]:
            j = i
            while j >=1:
                if arr[j-1] > arr[j] and Sol[j] >= Sol[j-1]:
                    Sol[j-1] = Sol[j] +1
                    j -=1
                else:
                    break




    return sum(Sol)

arr = [9,2,3,6,5,4,3,2,2,2]
n = 10
print candies(n,arr)

#if __name__ == "__main__":
    #n = int(raw_input().strip())
    #arr = []
    #arr_i = 0
    #for arr_i in xrange(n):
        #arr_t = int(raw_input().strip())
        #arr.append(arr_t)
    #result = candies(n, arr)
    #print result


