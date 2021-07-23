for i in range(1,101):
    count=0
    for j in range(2,(i//2+1)):
        if(i%j==0):
            count=count+1
<<<<<<< HEAD
            #tmp='count'
            break
        if(count==0 and i!=1):
            #tmp='%s ' % tmp
=======
            break
        if(count==0 and i!=1):
>>>>>>> ad69712c78471f9d5cf122675fb465f586009797
            print('%s' % i)
