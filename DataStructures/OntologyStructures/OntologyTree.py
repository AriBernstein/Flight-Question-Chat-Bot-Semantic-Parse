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
    
    def __sizeof__(self) -> int:
        return len(self._ont_dict)