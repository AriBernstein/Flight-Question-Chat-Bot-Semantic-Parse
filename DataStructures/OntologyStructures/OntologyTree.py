from DataStructures.OntologyStructures.OntologyNode import OntologyNode

class OntologyTree:
    
    def __init__(self, root_node:OntologyNode, nodes_dict:dict[str, OntologyNode]) -> None:
        self._root = root_node
        self._ont_dict = nodes_dict
        
    def find_node(self, ontology_label:str) -> OntologyNode:
        return self._ont_dict[ontology_label]
    
    def get_root(self) -> OntologyNode:
        return self._root
    
    def get_ont_node(self, ont_label:str) -> OntologyNode:
        return self._ont_dict[ont_label]
    
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