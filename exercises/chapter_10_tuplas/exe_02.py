#EXERCISE 2 => READING THE TUPLES ELEMENTS

def reading_first_element(elements):
    print("\nreading_first_element")
    print("Tuple Elements ",elements)
    print("Reading first element of tuple => ", elements[0])

def reading_last_element(elements):
    print("\nreading_last_element")
    print("Tuple Elements ",elements)
    print("Reading last element of tuple=> ", elements[-1])

def reading_first_two_elements(elements):
    print("\nreading_first_two_elements")
    print("Tuple Elements ",elements)
    print("First two element of tuple=> ", elements[:2])

def reading_last_three_elements(elements):
    print("\nreading_last_three_elements")
    print("Tuple Elements ",elements)
    print("Last three element of tuple=> ", elements[-3:])

def reading_middle_element(elements):
    print("\nreading_middle_element")
    print("Tuple Elements ",elements)
    middle = int((len(elements) - 1) / 2)
    print("Middle element of tuple=> ", elements[middle])

if __name__ =="__main__":
    elements = ('A','B','C','D','E','F','G','H',)
    reading_first_element(elements)
    reading_last_element(elements)
    reading_first_two_elements(elements)
    reading_last_three_elements(elements)
    reading_middle_element(elements)