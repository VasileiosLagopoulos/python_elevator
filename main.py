import queue
from Elevator import Elevator

def finished():
  passengers = 0
  for i in header:
    for k in i:
      passengers = passengers + 1
  if passengers > 0:
    return False
  else:
    return True

def count_passengers():
  passengers = 0
  for i in header:
    for k in i:
      passengers = passengers + 1
  return passengers

def print_status():
  for i in header:
    print(i)


floor = 0
num_of_floors = -1
elevator_capacity = -1


# Get number of floors - validate
print("Type the number of floors(>1): ")
num_of_floors = int(input())
while num_of_floors < 2:
    print("Number of floors must be over 1, please type again: ")
    num_of_floors = int(input())


# Get elevator capacity - validate
print("Type the capacity of the elevator(>0): ")
elevator_capacity = int(input())
while elevator_capacity < 1:
    print("The capacity of the elevator must be over 0, please type again: ")
    elevator_capacity = int(input())


print("The number of floors is:" , num_of_floors)
print("The capacity of the elevator is: " , elevator_capacity)

header_count = num_of_floors + 1
header = []
for i in range(header_count):
  header.append([])


with open(f"./queues{num_of_floors}.txt", "r") as file:
  count = 0
  k = file.readlines()
  for i in k:
    header[count] = [*i.strip("\n")]
    count = count + 1

elevator = Elevator(elevator_capacity, num_of_floors)



while(not finished()):
    for p in header[floor].copy():
        if(elevator.get_people(int(p))):
          header[floor].remove(p)
    elevator.print_report()
    floor = elevator.move()
    elevator.print_report()
    elevator.remove_people()
    print("---------------------------------------------------------------------------")
    print(f"Number of people to be served {count_passengers()}")
    print_status()
    print("---------------------------------------------------------------------------")
  
print("Everyone was served!")

  