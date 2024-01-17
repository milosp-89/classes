class List(): # class

    def __init__(self, array): # constructor
        self.array = array

    def print(self): # print the whole original list
            print(self.array)

    def cnt(self): # check the lenght of the array # count 
        res = 0
        for x in self.array:
            res += 1
        return res

    def appd(self, value): # append at the end of the list
         self.array += [value]
         return self.array
    
    def pappd(self, value): # pre append at the begining of the list
         self.array = [value] + self.array
         return self.array
    
    def ins(self, idx, value): # insert element anywhere within a list
        if idx > self.cnt(): # call class method cnt
                print("ERROR: index out of range please try again!")
        else:
            self.array = self.array[:idx] + [value] + self.array[idx:]
            return self.array
    
    def reml(self): # remove last element from a list
         if self.cnt() == 0:
              print("ERROR: no elements to remove within a list!")
         elif self.cnt() == 1:
              return []
         else:
            self.array = self.array[0:-1]
            return self.array
    
    def remf(self): # remove first element from a list
          if self.cnt() == 0:
               print("ERROR: no elements to remove within a list!")
          elif self.cnt() == 1:
              return []
          else:
            self.array = self.array[1:]
            return self.array
    
    def rem(self, value): # remove any element from a list / specified if in a list
         if value in self.array:
              ac = 0
              for x in self.array:
                   ac += 1
                   if x == value:
                        i = ac - 1
              self.array = self.array[:i] + self.array[i + 1:]
              return self.array
         else:
              print("ERROR: element dosent exist within a list, please try again!")

    def cl(self): # clear whole list and return []
            self.array = []
            return self.array
    
    def srt(self, sign): # sort asc and sort desc
         res = []
         while self.array:
              m = self.array[0]
              for x in self.array:
                   # eval as operations with string expression
                   if eval("%s" % x + sign + f"{m}"):
                        m = x
              res = res + [m]
              self.array = self.rem(m) # called rem class method
         self.array = res
         return self.array
    
# test:
my_list = List([1,2,3,4,5,6]) # instance of the List class

# methods:
my_list.print() # to print original list
print(my_list.cnt()) # to check the lenght of the list
print(my_list.appd(8)) # append a new element to existing list
print(my_list.pappd(3)) # saves previous and pre append at the begining of the list
print(my_list.ins(3, 99)) # saves and insert a value with a specified index
print(my_list.reml()) # removes last element from a list
print(my_list.remf()) # removes first element from a list
print(my_list.rem(3)) # removes specified element from a list
print(my_list.srt("<")) # sort in ascending order elements within a list
print(my_list.srt(">")) # sort descending order elements within a list
print(my_list.cl()) # clear all elements
