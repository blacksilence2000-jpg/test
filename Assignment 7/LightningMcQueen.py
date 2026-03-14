import random
class Car:
    def __init__(self, registration_number: str, max_speed: float):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0.0
        self.travelled_distance = 0.0
#question 2 define accelerate
    def accelerate(self, delta: float):
        self.current_speed += delta
        if self.current_speed < 0:
            self.current_speed = 0.0
        elif self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
#question 3 define drive
    def drive(self, hours: float):
        """drive for the given number of hours at the current speed."""
        if hours <= 0:
            return
        self.travelled_distance += self.current_speed * hours

    def __str__(self):
        return (
            f"Car(registration_number={self.registration_number}, "
            f"max_speed={self.max_speed} km/h, "
            f"current_speed={self.current_speed} km/h, "
            f"travelled_distance={self.travelled_distance} km)"
        )

def example_usage():
    reg = input("car registration number: ").strip()
    max_speed = float(input("maximum speed (km/h): ").strip())
    car = Car(reg, max_speed)
#question 2 test
    car.accelerate(30)
    car.accelerate(70)
    car.accelerate(50)
    print(f"speed after acceleration: {car.current_speed} km/h")
#question 3 test
    car.drive(1.5)
    print(f"travelled distance: {car.travelled_distance} km")
    car.accelerate(-200)
    print(f"speed after brake: {car.current_speed} km/h")
#question 4 test
def race():
    cars = [
        Car(f"ABC-{i+1}", random.randint(150, 200))
        for i in range(10)
    ]
    while True:
        for car in cars:
            delta = random.randint(-10, 15)
            car.accelerate(delta)
            car.drive(1)

        if any(car.travelled_distance >= 10000 for car in cars):
            break

    print("\nrace end, the one w ho win is:")
    print(f"{'Reg':<7} {'Max':>5} {'Speed':>7} {'Distance':>10}")
    for car in cars:
        print(
            f"{car.registration_number:<7} "
            f"{car.max_speed:>5.0f} "
            f"{car.current_speed:>7.0f} "
            f"{car.travelled_distance:>10.1f}"
        )

if __name__ == "__main__":
    mode = input("run the example or race ").strip().lower() #i seperated both of them
    if mode.startswith("r"):
        race()
    else:
        example_usage()
