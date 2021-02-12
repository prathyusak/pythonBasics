###################
#ITerators
s = 'abc'
it = iter(s)
it  #<iterator object at >
next(it) #a
next(it) #b
next(it) #c
#next(it) #StopIteration

class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]
rev = Reverse([1,2,3,4])
print(list(rev))                    #[4,3,2,1]
# print(next(rev))                  #StopIteration      
# print(iter(rev).__next__())       #StopIteration
print(rev)                          #<__main__.Reverse object at >
for i in rev:
    print(i) 

##################################
#Generators   (create iterators with yield keyword.iter and next (stopIteration) are created automatically)

def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]
for char in reverse('golf'):
    print(char)
print(reverse('golf'))   #<generator object reverse at >

r = reverse([1,2,3,4])
print(next(r))   #4
print(next(r))   #3
print(next(r))   #2
print(next(r))   #1
# print(next(r)) #StopIteration
print(iter(r))   #<generator object reverse at >
# print(next(r)) #StopIteration


###################################
#Generator Expressions
#Simple generators as expressions ||r to list comprehensions. 
#Memory friendly than list comprehensions
sum(i*i for  i in range(10))    #285
page= '''There lived Yasodha who has a beautiful son named Krishna.
Yashoda likes to decorate his son with many ornaments and perals.
 Krishna has curly hair tucked togther with a peacock feather'''

unique_words = set(word for line in page.split('\n') for word in line.split())
print(unique_words)
class Student:
    def __init__(self,name,gpa):
        self.name =name
        self.gpa =gpa

graduates =[Student('ram',99),Student('sita',98)]
valedictorian = max((student.gpa, student.name) for student in graduates)
print(valedictorian)
data='golf'
list(data[i] for i in range(len(data)-1, -1, -1))





