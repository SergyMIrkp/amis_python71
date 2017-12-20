CustumerInput=input('Введите елементы в списке через пробел')

def ListCreator(Str,i):
    
    if i+1==len(Str):
        return [Str]
    
    if Str[i]==' ':
        return [Str[:i]]+ ListCreator(Str[i+1:],0)
    else:
        return ListCreator(Str,i+1)

CustumerList=list(set(ListCreator(CustumerInput,0)))

def SecondMax(List):
    """
Ця функція повертає другий максимальний елемент
Args:
   numbers: список
 
Returns: дійсне числa

Exampples:
>>> print(SecondMax([1 2 3 4 5 6 7 8 9]))
  8
    """
    
    if len(List)==1:
        return 'Все числа одинаковые'
    
    if len(List)==2:
        
        if List[0]<List[1]:
            return List[0]
        else:
            return List[1]
    
    if List[0]<=List[1]and List[0]<=List[2]:
        List=List[1:]
    elif List[1]<=List[0]and List[1]<=List[2]:
        List=List[0:1]+List[2:]
    else:
        List=List=List[0:2]+List[3:]
        
    return SecondMax(List)

print(SecondMax(CustumerList))
