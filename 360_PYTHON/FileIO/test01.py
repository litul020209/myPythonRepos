import pickle as p
try:
   with open("sample.pkl","rb") as fp:
        # data=[1,2,3,4,5,6,7,8,9]   #pickling the data in file
        # p.dump(data,fp)  
                     
        d=p.load(fp)  
        print(d)
        
        

except:
    print("Check the logic")
