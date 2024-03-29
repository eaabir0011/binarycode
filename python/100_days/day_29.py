#doc strings
def square(n):
    """Hey this is a doc strings and it places at the beginig of a function
    and there should be no function before the doc string"""
    print(n**2)

square(5)
print(square.__doc__)
#doc string can change the output
#but a comment can't change the programe output
