for num in range(10,20):
    for i in range(2,num):
        if num%i ==0:
            j = num/i
            print("%d * %d equal %d"%(i,j,num))
            break
    else:
        print(num,"is a prime number")
