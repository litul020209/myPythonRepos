#copy the one file to anthor file

src_file_name=input("Enter source file name: ")

dest_file_name=input("Enter source file name: ")
try:
    with open(src_file_name,"r") as fp1:
        with open(dest_file_name,"w") as fp2:
            data=fp1.read()
            fp2.write(data)
            fp2.close()
        fp1.close()
    print(f"copy the data from {src_file_name} to {dest_file_name}")
    
except:
    print("check the logic")