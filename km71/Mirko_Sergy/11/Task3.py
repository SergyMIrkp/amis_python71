CustumerInput=input('Введите список из чисел через пробел: ')

def ListCreator(Str,i):
    
    if i+1==len(Str):
        return [Str]
    
    if Str[i]==' ':
        return [Str[:i]]+ ListCreator(Str[i+1:],0)
    else:
        return ListCreator(Str,i+1)


def Reverse(List):
    '''
 Ця функція повертає список  в зворотньому порядку
 
    Args:
       list: список

    Returns:
        list: список

    Exampples:
        1 2 3 4 5 6 7 8 9
        
        9 8 7 6 5 4 3 2 1
    '''
    
    ReverseList=[]
    
    if len(List)==1:
        return ReverseList + List
    
    ReverseList.append(List[len(List)-1])
    del(List[len(List)-1])
    
    return ReverseList+Reverse(List)


CustumerList=ListCreator(CustumerInput,0)
print(Reverse(CustumerList))
