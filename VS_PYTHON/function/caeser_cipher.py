
def encrypte(senc,type_shift):
    shift=type_shift
    res=""
    for letter in senc:
       a= letter.isalpha()
       if a==True:
           b=letter.isupper()
           c=letter.islower()
           if b==True:
               new_letter_asci=(((ord(letter)-65)+shift)%26)+65
               new_letter=chr(new_letter_asci)
           elif c==True:
               new_letter_asci=(((ord(letter)-97)+shift)%26)+97
               new_letter=chr(new_letter_asci)
       else:
            new_letter=letter   
               
       res=res+new_letter
    return res

def decrypted(ans_02):
    if ans_02=="yes":
       senc_decr=input("enter the decrypted sentence: ")
       shift_03=int(input("enter the shift: "))
       shift_04=-(shift_03)
       print(encrypte(senc_decr,shift_04)) 
    else:
       print("thank you for your ans. ")

enc_sentence=input("enter the sentence: ")
type_shift=int(input("enter the shift: ")) 
senc=enc_sentence
print("the encrypted sentence is: ", encrypte(senc,type_shift))
ans_01=input("do you want to decrypted the sentence: ")
ans_02=ans_01.lower()
decrypted(ans_02)



       


