class Graph:
    def __init__(self):
        self.numberofNodes = 0
        self.adjacentList = {}

    # def __str__(self):
    #     return str(self.__dict__)

    def addNode(self,node):
        self.adjacentList[node] = []
        self.numberofNodes +=1
        return

    def edges(self,node1,node2):
        self.adjacentList[node1].append(node2)
        self.adjacentList[node2].append(node1)
        return

    def showConn(self):
        for i in self.adjacentList:
            print("\n"+ i + "---->", end='')
            for j in self.adjacentList[i]:
                print(j, end="")


ucg = Graph()
ucg.addNode('0')
ucg.addNode('1')
ucg.addNode('2')
ucg.addNode('3')
ucg.addNode('4')
ucg.addNode('5')
ucg.addNode('6')
ucg.edges('0','1')
ucg.edges('0','2')
ucg.edges('1','2')
ucg.edges('2','4')
ucg.edges('1','3')
ucg.edges('4','3')
ucg.edges('4','5')
ucg.edges('5','6')
ucg.showConn()
print(ucg.adjacentList)

