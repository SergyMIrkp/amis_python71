CustumerInput=input('Введите список через пробел')

def ListCreator(Str,i):

    '''
Ця функція повертає отримує строку й перетворює її у список по пробілах

Args:
   CustumerInput: строка

   Returns:
       CustumerList:список
    '''
    if i+1==len(Str):
        return [Str]
    
    if Str[i]==' ':
        return [Str[:i]]+ ListCreator(Str[i+1:],0)
    else:
        return ListCreator(Str,i+1)

def Min(List):

    """
Ця функція повертає найменший елемент зі списку elemtnts

Args:
   CustumerList: список

Returns:
   Element: дійсне число

Exampples:

  Введите список через пробел3 4 5 6 4 4
  3

     
   """
    
    if len(List)==1:
        return List[0]
    
    if List[0]>=List[1]:
        del(List[1])
    else:
        del(List[1])
        
    return Min(List)


CustumerList=ListCreator(CustumerInput,0)
print(Min(CustumerList))
