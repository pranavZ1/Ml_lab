def count_pair():
    l = [2,7,4,1,3,6]
    count = 0
    for i in l:
        for j in l:
            if i+j == 10:
                print("{},{}".format(i,j))
                count = count+1
    print("Total number of pairs :",count)

count_pair()
