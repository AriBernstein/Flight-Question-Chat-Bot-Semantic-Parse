
class OntologyNode:
    """
    Class representing a node in the Ontology tree.
    
    Fields:
         _ontology_label (str): The UID of this OntologyNode.
         
         _parent (OntologyNode): The parent of this OntologyNode in the tree.
         
         _children set[OntologyNode]: 
            Set containing the children of this OntologyNode. Defaults to None
            for the sake of Leaf checks.    """
            
    def __init__(self, ontology:str, 
                 parent:'OntologyNode'=None) -> None:
        
        self._ontology_label = ontology # type: str
        self._parent = parent           # type: 'OntologyNode'
        self._children = None           # type: set['OntologyNode']
        
    def parent(self) -> 'OntologyNode':
        """
        Returns: OntologyNode: the parent of this OntologyNode instance.
        """
        return self._parent

    def get_children(self) -> set['OntologyNode']:
        return self._children
        
    def set_children(self, children:list['OntologyNode']) -> None:
        self._children = children

    def is_root(self) -> bool:
        return self._parent is None
    
    def ancestors(self) -> set['OntologyNode']:
        """
        Returns: set[OntologyNode]: 
            Set of OntologyNode instances that are ancestors of this instance.
        """
        ancestors = set()
        cur_ancestor = self
        while not cur_ancestor.is_root():
            ancestors.add(cur_ancestor)
            cur_ancestor = cur_ancestor.parent()
        return ancestors
    
    def is_or_decends_from(self, ont_label:str) -> bool:
        """
        Args: ont_label (str): ontology label of self or possible ancestor.

        Returns: bool: 
            True if this node or any of its ancestors have _ontology_label equal 
            to ont_label. False otherwise.  """
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