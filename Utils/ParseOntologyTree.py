from typing import Union
from bs4 import BeautifulSoup

from DataStructures.OntologyNode import OntologyNode
from DataStructures.OntologyTree import OntologyTree

_ONTOLOGY_HTML_FP = "DataSet/Ontology/trips_ontology_tree.html"
_ONTOLOGY_STRUCTURE_URL = "https://www.cs.rochester.edu/research/trips/lexicon/cgi/browseontology-ajax"

def _parseList(tag) -> tuple:
    if tag.name == 'ul':
        return [_parseList(item)
                for item in tag.findAll('li', recursive=False)]
    elif tag.name == 'li':
        if tag.ul is None:
            return tag["id"].strip()
        else:
            return (tag["id"].strip(), _parseList(tag.ul))
    
def _read_ontology_html(fp:str=_ONTOLOGY_HTML_FP) -> tuple[str, list]:
    with open(_ONTOLOGY_HTML_FP, "r+") as fp:
        soup = BeautifulSoup(fp, "lxml")
    
    return _parseList(soup.ul)


def _build_ontology_tree_helper(cur_node: Union[tuple, str],
                                parent:'OntologyNode'=None,
                                node_dict:dict=None) -> OntologyNode:
    
    if isinstance(cur_node, str):   # Leaf
        return OntologyNode(cur_node, parent)
    
    ont_label = cur_node[0]
    ont_node = OntologyNode(ont_label, parent)
    
    if node_dict is not None:
        node_dict[ont_label] = ont_node

    ont_children = []   # type: list[OntologyNode]
        
    ont_children = [_build_ontology_tree_helper(c, ont_node, node_dict) for c in cur_node[1]]
    ont_node.set_children(ont_children)
    return ont_node
    

def build_ontology_tree(fp:str=_ONTOLOGY_HTML_FP) -> OntologyTree:
    ontology_nodes = {}
    ontology_root = _build_ontology_tree_helper(
        cur_node=_read_ontology_html(fp)[0], node_dict=ontology_nodes)
    return OntologyTree(ontology_root, ontology_nodes)