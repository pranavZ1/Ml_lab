def calc_difference():
    l1 = []
    n = int(input("Enter number of elements in a list:"))
    
    if n < 3:
        print("Error: List must have at least 3 elements")
    else:
        for i in range(n):
            l1.append(int(input("Enter element into the list:")))
    
        ma = max(l1)
        mi = min(l1)
        print("List:", l1)
        print("Difference:",ma-mi)  
        
calc_difference()
