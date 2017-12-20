CustumerInput=input('Введите елементы в списке через пробел')

def ListCreator(Str,i):
    
    if i+1==len(Str):
        return [Str]
    
    if Str[i]==' ':
        return [Str[:i]]+ ListCreator(Str[i+1:],0)
    else:
        return ListCreator(Str,i+1)


def SearchingMax(List):

    '''
Ця функція повертає  максимальний елемент
Args:
 CustumerInput : список
 
 Returns: дійсне числa
 
 Exampples:
 >>> print(SearchingMax(2 3 4 7 4 7 7 4))
      7
 
    '''
    
    if len(List)==1:
        return List[0]
    
    elif List[0]>=List[1]:
        del(List[1])
    else:
        del(List[0])
        
    return SearchingMax(List)


def NumberOfMax (List,x):
    '''
Ця функція повертає кількість елементів,
що доінюють максимальному елементу
Args:
 numbers: список
 
 Returns: дійсне числa
 
 Exampples:
 >>> print(NumberOfMax(2 3 4 7 4 7 7 4))
      3
 
    '''
    
    if len(List)==0:
        return 0
    
    elif x==List[0]:
        del(List[0])
        Aproval=1 
        
    else:
        del(List[0])
        Aproval=0

    return Aproval+ NumberOfMax (List,x)
    

ListForMaxSearch=ListCreator(CustumerInput,0)
ListForMaxCount=ListForMaxSearch[:]

Max=SearchingMax(ListForMaxSearch)


print( NumberOfMax (ListForMaxCount,Max))
    

