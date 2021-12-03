
class OntologyNode:
    
    def __init__(self, ontology:str, 
                 parent:'OntologyNode'=None) -> None:
        
        self._ontology_label = ontology # type: str
        self._parent = parent  # type: 'OntologyNode'
        self._children = None
        
    def parent(self) -> 'OntologyNode':
        return self._parent
        
    def set_parent(self, parent: 'OntologyNode') -> None:
        self._parent = parent
    
    def get_children(self) -> set['OntologyNode']:
        return self._children
    
    def add_child(self, child:'OntologyNode') -> None:
        self._children.append(child)
        
    def set_children(self, children:list['OntologyNode']) -> None:
        self._children = children
        
    def leaf(self) -> bool:
        return self._children is None
    
    def is_root(self) -> bool:
        return self._parent is None
    
    def ancestors(self) -> set['OntologyNode']:
        a = set()
        cur_ancestor = self
        while not cur_ancestor.is_root():
            a.add(cur_ancestor)
            cur_ancestor = cur_ancestor.parent()
        return a
    
    def is_or_decends_from(self, ont_label:str) -> bool:
        return ont_label in self.ancestors()
        
    def __str__(self) -> str:
        return f"{self._ontology_label} - {self._children}"
    
    def __repr__(self) -> str:
        return self._ontology_label
    
    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, OntologyNode) or isinstance(__o, str):
            return self._ontology_label == str(__o)
        return False
        
    def __hash__(self) -> int:
        return hash(self._ontology_label)