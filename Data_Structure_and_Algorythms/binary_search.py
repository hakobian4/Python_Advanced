class Algorithm():
    
    def __init__(self, list, value):
        self.list = list
        self.value = value

    def binary_search(self):
        self.list.sort()    
        while len(self.list) > 1:
            if self.list[len(self.list) // 2] > self.value:
                self.list = self.list[ : len(self.list) // 2]
            else:
                self.list = self.list[len(self.list) // 2 : ]
        if self.list[0] == self.value:
            return True
        else:
            return False
            

def main():
    print('Please, input array')
    try: 
        my_list = [] 
        while True: 
            my_list.append(int(input())) 
    except: 
        number = int(input('Input a number to search in the array: '))
    
    obj = Algorithm(my_list, number)

    if obj.binary_search():
        print('{} exists in the given array.'.format(number))
    else:
        print('{} does not exist in the given array.'.format(number))


if __name__ == "__main__":
    main()
