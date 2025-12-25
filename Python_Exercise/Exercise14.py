'''🧠 EXERCISES — Day 14
🔸 Exercise 1 — Composition
Create:
Battery class → charge()
Phone class → HAS-A Battery
use_phone() calls battery charge'''

class Battery:
    def __init__(self):
        self.level = 100

    def charge(self):
        return f"Battery is {self.level}"
class Phone:
    def __init__(self):
        self.battery=Battery()
    def use_phone(self):
        return self.battery.charge()

phn1 = Phone()

print(phn1.use_phone())


'''🧠 Exercise 1 — Engine & Car
Create:
Engine class → start(), stop()
Car class → HAS-A Engine
drive() calls engine.start()
(No inheritance allowed ❌)'''

class Engine:
    def __init__(self):
        pass
    def start(self):
        return "Engine is start....."
    def stop(self):
        return "Engine is stop......"
    
class Car:
    def __init__(self):
        self.engine = Engine()

    def drive(self):
        return "Car is moving....."
car1 = Car()
print(car1.drive())

'''🔸 Exercise 2 — Design Thinking (Answer in words)
Why is composition safer than inheritance?
Can inheritance be replaced by composition? When?
In real companies, why do large systems avoid deep inheritance?'''