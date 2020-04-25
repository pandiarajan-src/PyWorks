'''Create your own string split method'''

def my_split(inputdata):
    """my own split method equal to stirng.split()"""
    #
    # Your task is to write your own function,
    # which behaves almost exactly like the original split() method
    # 1. it should accept exactly one argument - a string;
    # 2. it should return a list of words created from the string,
    #       divided in the places where the string contains whitespaces;
    # 3. if the string is empty, the function should return an empty list;
    # its name should be mysplit(), strip out the string at the start and bottom
    #
    inputdata.strip()
    start = 0
    end = len(inputdata)
    output = []
    while start < end:
        pos = inputdata.find(" ", start, end)
        #if it can't find space after the full length of the string,
        #it starts return -1, -2 (reverse position), hence make it to end
        if pos < 0:
            pos = end
        temp = inputdata[start:pos]
        if temp.strip() != "":
            output.append(temp)
        start = pos+1
    return output


if __name__ == "__main__":
    print(my_split("To be or not to be, that is the question"))
    print(my_split("To be or not to be,that    is the question"))
    print(my_split("   "))
    print(my_split(" abc "))
    print(my_split(""))
