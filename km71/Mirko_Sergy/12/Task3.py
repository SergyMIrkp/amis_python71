CustumerInput=input('Введите список через пробел')

def ListCreator(Str,i):
    
    if i+1==len(Str):
        return [Str]
    
    if Str[i]==' ':
        return [Str[:i]]+ ListCreator(Str[i+1:],0)
    else:
        return ListCreator(Str,i+1)

def FindGroup(List,Coincidence):
    """
Ця функця розбиваэ список на групи елементів
Args:
    CustumerList: список натуральних чисел
Returns:
    список груп
    """
    if Coincidence+1==len(List):
        return [List]
        
    if List[Coincidence]==List[Coincidence+1]:
        return FindGroup(List,Coincidence+1)
    else:
        Group= [List[:Coincidence+1]]
        del([List[:Coincidence+1]])
        return Group + FindGroup(List,0)

def MaxGroup(List):
    """
Ця функця повертає найбільшу групу
Args:
    GroupList: ссписок груп
Returns:
    найбільша група
    """
    
    if len(List)==1:
        return List[0]
    
    if len(List[0])>=len(List[1]):
        del(List[1])
    else:
        del(List[0])
        
    return MaxGroup(List)

def StrCreator(List):
    if len(List)==0:
        return ''
    else:
        return str(List[0])+' '+StrCreator(List[1:])

CustumerList=ListCreator(CustumerInput,0)
GroupList=FindGroup(CustumerList,0)
BiggestGroup=MaxGroup(GroupList)
print(StrCreator(BiggestGroup))
