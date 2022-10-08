# Function to take multiple arguments
def add(datatype, *args):
    if datatype == 'int':
        answer = 0
    if datatype == 'str':
        answer = ''
    for x in args:
        answer = answer + x
    print(answer)

# Integer
add('int',5,7,9)
# String
add('str', 'Hi ', 'Geeks')

# ======================================

def sub(datatype, pop):
    if datatype=="str":
        print(pop.upper())
    if datatype=='int':
        print(pop*pop)

sub('int', 90)
sub('str', "Aadesh")
