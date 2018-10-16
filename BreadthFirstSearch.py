from collections import deque

graph={}


graph["Alice"]=["You","Peggy"]
graph["You"]=["Claire","Bob"]
graph["Bob"]=["Peggy","Anuj"]
graph["Peggy"]=[]
graph["Claire"]=["Thom","Jonny"]
graph["Thom"]=[]
graph["Anuj"]=[]
graph["Jonny"]=[]





def MangoSellerSearch(graph,name):

    checkable=deque()
    checkable.extend(graph[name])
    checked=[]

    while checkable:
        currentlychecking=checkable.popleft()

        if  IsMangoSeller(currentlychecking):
            print(currentlychecking+" is a mangoseller")
            return
        checkable.extend(graph[currentlychecking])


    print("There is no mango seller!")

def IsMangoSeller(name):
    if name[-1]=="m":
        return True
    else:
        False

MangoSellerSearch(graph, "Alice")

