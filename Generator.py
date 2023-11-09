import random

# Generator's role is to create sample text files that represent the queues of people waiting 
class Generator:
    
    def create_sample(self, floors):
        # Create from scratch the text file if already created, because later I use append
        with open(f"./queues{floors}.txt", "w") as file:
            file.close()

        # The text file is writen character by character so I use "a" - append
        with open(f"./queues{floors}.txt", "a") as file:
            for i in range(floors + 1):
                # I set here a limit of 50 person waiting per queue, it can be modified though
                num_of_people = random.randint(1,50)
                for p in range(num_of_people):
                    number = random.randint(0, floors)
                    while number == i:
                        number = random.randint(0, floors)
                    file.write(str(number))
                if i != floors:
                    file.write('\n')
                    
                