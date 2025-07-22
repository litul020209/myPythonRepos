import random



total_question=5

correct=0
incorrect=0
for i in range(total_question): 
    random_number=random.randint(1,5)
    print(random_number)
    g=int(input("guess the number between 1 to 5 : "))

    if random_number==g:
        print("your guess is correct")
        correct=correct+1
    else:
        print("your guess is incoreect")
        incorrect=incorrect+1

percentage=(correct/total_question)*100
print(f"your result {correct}/{incorrect} and you score{percentage}%")