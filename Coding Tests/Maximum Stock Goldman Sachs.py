def buyMaximumProducts(n, k, a):
    # Complete this function
    amount_left = k
    stock_bought_asc = 0

    dict = {}
    for i in range(len(a)):
        if a[i] in dict:
            dict[a[i]] = dict[a[i]] + i + 1
        else:
            dict[a[i]] = i + 1

    a = sorted(a)
    visited = []

    for i in range(len(a)):
        if a[i] in visited:
            continue
        visited.append(a[i])
        if amount_left <= 0 :
            break
        if amount_left - dict[a[i]]*a[i] >= 0:
            amount_left = amount_left - dict[a[i]]*a[i]
            stock_bought_asc += dict[a[i]]
        else:
            j = dict[a[i]]
            while j >= 1 and (amount_left - a[i]) >= 0:
                amount_left = amount_left - a[i]
                j -= 1
                stock_bought_asc += 1

    return stock_bought_asc

n = 3
k =100
a = [8 ,16 ,2 ,1 ,1, 9 ,3, 64 ,1]
b = [1 ,2 ,3 ,4 ,5, 6 ,7, 8 ,9]
print buyMaximumProducts(n,k,a)


if __name__ == "__main__":
    n = int(raw_input().strip())
    arr = map(int, raw_input().strip().split(' '))
    k = int(raw_input().strip())
    result = buyMaximumProducts(n, k, arr)
    print result