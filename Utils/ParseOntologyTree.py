from bs4 import BeautifulSoup

_ONTOLOGY_HTML_FP = "DataSet/Ontology/trips_ontology_tree.html"
_ONTOLOGY_STRUCTURE_URL = "https://www.cs.rochester.edu/research/trips/lexicon/cgi/browseontology-ajax"

def parseList(tag) -> tuple:
    if tag.name == 'ul':
        return [parseList(item)
                for item in tag.findAll('li', recursive=False)]
    elif tag.name == 'li':
        if tag.ul is None:
            return tag["id"].strip()
        else:
            return (tag["id"].strip(), parseList(tag.ul))
    
def get_ontology_etree(fp:str=_ONTOLOGY_HTML_FP) -> tuple[str, list]:
    with open(_ONTOLOGY_HTML_FP, "r+") as fp:
        soup = BeautifulSoup(fp, "lxml")
    
    return parseList(soup.ul)