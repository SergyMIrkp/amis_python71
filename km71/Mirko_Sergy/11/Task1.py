def CorrectInput():
    x=input('Введите натуральное число')
    if  not x.isdigit():
        return CorrectInput()
    elif int(x)<0:
        return CorrectInput()
    else:
        return x


def ProductOfSequence(x,n,i):
    '''
Фунуція ProductOfSequence обчислює загальний добуток послідовність
x/2^i
Args:
    x: ціле число
    n: ціле число
        
Returns дійсне числa
    '''
    if i>n:
        return 1
    return x/(2**i)*ProductOfSequence(x,n,i+1)



def CheackAnswers():
    assert(CorrectInput(1,1)==0.5)   
    assert(CorrectInput(2,2)==1)    
    print("Все вірно!")
    
Constant=int(CorrectInput())
n=int(CorrectInput())

print(ProductOfSequence(Constant,n,0))

