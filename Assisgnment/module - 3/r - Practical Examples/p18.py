class Elder:
    def greet(self):
        print("Greetings from the Elder class")

class Younger(Elder):
    def greet(self):
        super().greet()  # call parent method
        print("Greetings from the Younger class")

young_instance = Younger()
young_instance.greet()
