# fibonacci pograme
def fibo():
    starting = int(input("Give the the sarting Number"))
    ending = int(input("How many fibonacchi number?"))
    second=starting+1
    result = 0 
    for i in range(1,ending+1):
        result = starting+second
        starting=result
        
    return result

# if(main==__name__)
x=fibo()
print(x)
