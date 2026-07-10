count=1
while count<=3:
    print("Basic example of while loop:",count)
    count+=1





    #simple program:countdown timer.
    seconds=5
    while seconds>0:
        print("Countdown timer:",seconds)
        seconds-=1









    #new program
    foods = []
    while True:
        food = input("Enter a food item (or 'done' to finish): ")
        if food.lower() == 'done':
            break
        foods.append(food)
    print ("\n You have entered the following food items:")
    for food in foods:
        print(food)
    rating = len(foods)
    print("\n Rating of food items:",rating)


