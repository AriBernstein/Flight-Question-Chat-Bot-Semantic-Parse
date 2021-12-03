
class OntologyNode:
    
    def __init__(self, ontology:str, children:list['OntologyNode']=[], 
                 parent:'OntologyNode'=None) -> None:
        
        self._ontology_label = ontology
        self._children = children
        self._parent = parent
        
    def __str__(self) -> str:
        return self._ontology_label
    
    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, OntologyNode) or isinstance(__o, str):
            return self._ontology_label == str(__o)