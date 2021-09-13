
def load_file():

    with open("cars.txt" ,'r') as f:
        cars = []
        line = f.readlines()
        for n in line: 
            cars.append(n)
    return cars

class Car():
    def __init__(self, brand, year) -> None:
        self.brand = brand
        self.year = year

    # def print():



if __name__ == "__main__":
    cars = load_file()
    year = 2017
    car_list = []
    for item in cars:
        car = Car(item, year)
        car_list.append(car)
        year +=1 

    count = 1
    for i, n in enumerate(car_list):
        brand = n.brand.replace("\n", "")
        print("%s %s %s" %(i+1, brand, n.year))
        
