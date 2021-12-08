from DataStructures.OntologyStructures.OntologyNode import OntologyNode

class OntologyTree:
    
    """
    Class representing all Ontology knowledge, in both tree form and hash table
    form.
    
    Fields:
        _root (OntologyNode): The root of the tree structure.
        
        _ont_dict (dict[str, OntologyNode]): 
            key -> _ontology_label, pair -> associated OntologyNode """
    
    def __init__(self, root_node:OntologyNode, nodes_dict:dict[str, OntologyNode]) -> None:
        self._root = root_node
        self._ont_dict = nodes_dict
        
    def find_node(self, ontology_label:str) -> OntologyNode:
        """
        Args: ontology_label (str): key associated with OntologyNode.
        Returns: OntologyNode: OntologyNode associated with ontology_label  """
        return self._ont_dict[ontology_label]
    
    def get_root(self) -> OntologyNode:
        return self._root
    
    def get_ont_node_ancestors(self, ont_label:str) -> set[OntologyNode]:
        """
        Turns out there are ontological identifiers that do not have nodes in
        the tree - semantic evaluations can still evaluate to them. Because of
        this, we have to check for their existence and gloss over if they don't.

        Args ont_label (str):  
            ontological label of a given element of a semantic parse.

        Returns set[OntologyNode]: set of OntologyNodes which represent the
            OntologyNode associated with one_label and each of its ancestors."""
        return self._ont_dict[ont_label].ancestors() \
            if ont_label in self._ont_dict else set()
    
    def __sizeof__(self) -> int:
        return len(self._ont_dict)