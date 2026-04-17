

class Car:
    def __init__(self, make, model, plate , top_speed):
        self.make = make
        self.model = model
        self.plate = plate
        self.top_speed = top_speed


with open("input_2.txt", "r") as file:

    for lines in file:

        temp = lines.strip()
        temp = temp.split(", ")
        
        cars.append(Car(temp[0], temp[1], temp[2], temp[3]))

for idx in range(len(cars)):
    print(cars[idx].make)