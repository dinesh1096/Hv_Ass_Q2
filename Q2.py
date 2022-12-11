Car = {} #Creating Dictionary
Brand = str(input("Enter brand name :")) #Brand name taken from the user(Key)
Color = str(input("Enter color name :")) #Color name taken from the user(Value)
Car={Brand:Color} #{key:value}
x=open("car.txt","a")  #creating car.txt and appending all user brand name and color name  in that file
print("Car brand name and color name would be",Car,file=x) 
print("Car brand name and color name would be",Car) 