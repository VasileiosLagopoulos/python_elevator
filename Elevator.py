import time

class Elevator :
    def __init__(self, capacity, num_floors):
        self.capacity = capacity
        self.floor = 0
        self.passengers = []
        self.total_floors = num_floors
        self.direction = "up"
    
    def get_people(self, wanted_floor):

        if int(wanted_floor) > self.floor:
          person_dir = "up"
        else:
          person_dir = "down"
        if len(self.passengers) < self.capacity and self.direction == person_dir:
          self.passengers.append(wanted_floor)
          return True
        elif len(self.passengers) >= self.capacity :
        
          return False
        else:

          return False
    
    def remove_people(self):
        count = 0
        for p in self.passengers.copy():
            if self.floor == p:
                self.passengers.remove(p)
                count = count + 1     
        print(f"{count} passengers left the elevator in floor {self.floor}")
        print(self.passengers)
 

    def move(self):
        if self.direction == "up":
            if len(self.passengers) > 0:
                maximum = max(self.passengers)
                if self.floor == maximum:
                    self.direction = "down"
                    self.floor -= 1
                else:
                    self.floor += 1
            else:
                if self.floor < self.total_floors:
                    self.floor += 1
                else:
                    self.change_dir()
        else:
            if len(self.passengers) > 0:
                minimum = min(self.passengers)
                if self.floor == minimum:
                    self.direction = "up"
                    self.floor += 1
                else:
                    self.floor -= 1
            else:
                if self.floor > 0:
                    self.floor -= 1
                else:
                    self.change_dir()
        return self.floor
          
    
    def print_report(self):
        print(f"We are at floor {self.floor} with {len(self.passengers)} passengers")
        print(self.passengers)
        # time.sleep(1)
    
    def change_dir(self):
        if self.direction == "up":
            self.direction = "down"
        else:
            self.direction = "up"