def find_nb(m):
    i = 0
    j = 1
    while i < m :
        i += j**3
        j += 1
        if i == m :
            return j - 1
    return -1

def get_sum(a,b):
    #addition = 0
    #for i in range(min(a,b) , max(a,b)+1):
    #    addition += i
   
    return sum([i for i in range(min(a,b) , max(a,b) + 1)])

def remove_element(input : list):

    if input[0] == 5:
        input.pop(0)
        return True
    
    return False

def capitalize_string_with_a_twist(input : str):

    if len(input) > 5:
        output = input.upper()
        return len(input) , output
    elif len(input) < 5:
        output = input.title()
        return len(input) , output
    else:
        output = input.lower()
        return False , output

class Car():
    
    def __init__(self, top_speed, weight, num_wheels):
        self.top_speed  = top_speed
        self.weight     = weight
        self.num_wheels = num_wheels

    def apply_breaks(self, speed : int, level : int):
        new_speed = speed / level
        if new_speed > self.top_speed:
            self.num_wheels -= 1
            self.top_speed  = self.top_speed / self.num_wheels


if __name__ == "__main__" :
    print(find_nb(4183059834009))
    print(find_nb(24723578342962))
    print(find_nb(135440716410000))
    print(find_nb(40539911473216))
    print(find_nb(26825883955641))
    print(get_sum(-1,2))
    print(get_sum(4,-1))