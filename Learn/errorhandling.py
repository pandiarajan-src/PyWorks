# There is a difference between error handling and debugging
# Error handling : Something is happening outside of the expectation that I need to handle on the fly
#        Examples: Permission issue, DB down, server name change, etc...
# Debugging : I know there is somthing wrong in the code that I am trying to fix
#        Examples: App Crash, Output is wrong etc...
# Error handling scenarios should not be mixed with Debugging

# There are 3 types of errors
# 1. Syntax errors
#    It will not execute the code
# 2. Runtime errors
#    Code will fail when running
# 3. Logical errors
#    Code won't run at all and give expected output

# Final words on when to use try/except
# you don't have to capture all the errors, only un-expected failures to be captured.

# Runtime error
x = 100
y = 0

try:
    print (x/y)
except ZeroDivisionError as e:
    print (str(e))
else:
    print ("Don't know what is the error")
finally:
    print("run final result " + str(0))


