from random import random
from random import randint
class Main:
    def generate_random_array(self):
        self.bubble_array = []
        for i in range(1000):
            random_value = randint(0, 1000)
            self.bubble_array.append(random_value)
        print(self.bubble_array)

    def split_array(self):
        chunk_size = 100
        self.chunks = [self.bubble_array[i:i + chunk_size] for i in range(0, len(self.bubble_array), chunk_size)]

    def bubble_sort(self):
        self.n = len(self.bubble_array)
        for i in range(self.n):
            swapped = False
            for j in range(self.n - i - 1):
                if self.bubble_array[j] > self.bubble_array[j + 1]:
                    self.bubble_array[j], self.bubble_array[j + 1] = self.bubble_array[j + 1], self.bubble_array[j]
                    swapped = True
            if not swapped:
                break
    def split_chunks(self):
        for chunk in self.chunks:
            self.bubble_array = chunk  
            self.bubble_sort()

if __name__ == "__main__":
    main_instance = Main()
    main_instance.generate_random_array()
    main_instance.bubble_sort()
    print(f"Array sorted without slicing: {main_instance.bubble_array}")
    main_instance.split_array()
    main_instance.split_chunks()
    print(f"Array sorted using slicing: {main_instance.bubble_array}")



    
    




