# Base class for Animals
class Animal:
    def run(self):
        print("The animal is running.")

    def swim(self):
        print("The animal is swimming.")

    def fly(self):
        print("The animal is flying.")

# Base class for Vehicles
class Vehicle:
    def drive(self):
        print("The vehicle is driving.")

    def drift(self):
        print("The vehicle is drifting.")

    def spin(self):
        print("The vehicle is spinning.")


def main():
    print("Choose a category:")
    print("1. Animal")
    print("2. Vehicle")
    category = input("Enter 1 or 2: ")

    if category == "1":
        animal = Animal()
        print("\nAnimal actions:")
        print("1. Run")
        print("2. Swim")
        print("3. Fly")
        action = input("Choose an action (1/2/3): ")

        if action == "1":
            animal.run()
        elif action == "2":
            animal.swim()
        elif action == "3":
            animal.fly()
        else:
            print("Invalid action selected.")

    elif category == "2":
        vehicle = Vehicle()
        print("\nVehicle actions:")
        print("1. Drive")
        print("2. Drift")
        print("3. Spin")
        action = input("Choose an action (1/2/3): ")

        if action == "1":
            vehicle.drive()
        elif action == "2":
            vehicle.drift()
        elif action == "3":
            vehicle.spin()
        else:
            print("Invalid action selected.")

    else:
        print("Invalid category selected.")

# Run the program
main()
