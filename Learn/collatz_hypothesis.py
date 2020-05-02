'''Play on Collatz's hypothesis'''
# In 1937, a German mathematician named Lothar Collatz formulated
# an intriguing hypothesis (it still remains unproven)
#
# Steps for this hypothesis:
# 1. take any non-negative and non-zero integer number and name it c0;
# 2. if it's even, evaluate a new c0 as c0 ÷ 2;
# 3. otherwise, if it's odd, evaluate a new c0 as 3 × c0 + 1;
# 4. if c0 ≠ 1, skip to point 2.
# RESULT : The hypothesis says that regardless of the initial value of c0,
#          it will always go to 1.

def collatz_hypothesis(c0):
    """Implement the collatz hypothesis described in the file comment"""
    #Step1 : non-negative and non-zero number
    if c0 > 0:
        #step4 : Do the work until c0 is 1
        while c0 != 1:
            #Step2: if it is even
            if c0 % 2 == 0:
                c0 /= 2
            else:
                c0 = 3 * c0 + 1
        if c0 == 1:
            print("Hence proved collatz hypothesis")

if __name__ == "__main__":
    INPUT_DATA = int(input("enter non-negative and non-zero integer to prove collatz hypothesis:"))
    collatz_hypothesis(INPUT_DATA)
