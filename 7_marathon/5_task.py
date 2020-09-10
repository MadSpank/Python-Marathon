class LeafElement: 
  
    def __init__(self, *args): 
        self.position = args[0]
  
    def showDetails(self): 

        print(f'\t\t{self.position}')
     

class CompositeElement: 
  
    def __init__(self, *args):
        self.position = args[0] 
        self._children = []

    def add(self, child): 
        self._children.append(child)
        child.parent = self

    def remove(self, child): 
        self._children.remove(child)
        child.parent = None

    def showDetails(self): 
        if self.position == 'GeneralManager':
            print(self.position)
        else:
            print(f"\t{self.position}")
        for child in self._children:
            child.showDetails()
        
	
topLevelMenu = CompositeElement("GeneralManager")
subMenuItem1 = CompositeElement("Manager1")
subMenuItem2 = CompositeElement("Manager2")
subMenuItem11 = LeafElement("Developer11")
subMenuItem12 = LeafElement("Developer12")
subMenuItem21 = LeafElement("Developer21")
subMenuItem22 = LeafElement("Developer22")
subMenuItem1.add(subMenuItem11)
subMenuItem1.add(subMenuItem12)
subMenuItem2.add(subMenuItem22)
subMenuItem2.add(subMenuItem22)
topLevelMenu.add(subMenuItem1)
topLevelMenu.add(subMenuItem2)
topLevelMenu.showDetails()