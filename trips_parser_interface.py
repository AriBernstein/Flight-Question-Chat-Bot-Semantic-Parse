from typing import OrderedDict
import xmltodict
import requests
import re
"""

Call the TRIPS Parser API to retrieve semantic interpretations of input.
API Documentation can be found here:
http://trips.ihmc.us/parser/api.html

"""

GET_URL = "http://trips.ihmc.us/parser/cgi/parse"
MULTIPLE_PARSES_FIELD = "compound-communication-act"
UTT_FIELD = "utt"
PARSES_FIELD = "parses"
TREE_FIELD = "tree"
TERMS_FIELD = "terms"

def call_trips_parser_api(sentence:str) -> dict:
    resp = requests.get(
        GET_URL + "?input=" + re.sub(r'\s+', '+', sentence) + \
            "?output-parts=word-lisp lf-lisp")
    if resp.status_code != 200:
        raise Exception(
            f"Bad response when calling call_trips_parser_api\nCode: \
                {resp.status_code}\nError: {resp.reason}\nURL: {resp.url}\t")
    
    # Return dictionary    
    ret = {"sentence":sentence, PARSES_FIELD:[]}
    
    # Format XML output into new dictionary with input, parse tree 
    # representation, logical form representation
    d = xmltodict.parse(resp.content)
    d = d["trips-parser-output"]
    
    # Handle single or multiple parses
    if MULTIPLE_PARSES_FIELD in d:
        for parse in d[MULTIPLE_PARSES_FIELD][UTT_FIELD]:
            ret[PARSES_FIELD].append([parse[TREE_FIELD], parse[TERMS_FIELD]])

    else:
        d = d[UTT_FIELD]
        ret[PARSES_FIELD].append([d[TREE_FIELD], d[TERMS_FIELD]])

    ret["num_parses"] = len(ret[PARSES_FIELD])

    return ret

def print_dicts(a:dict, indent=0, skip_fields=None) -> None:
    for k in a.keys():
        if skip_fields and k in skip_fields:
            continue
        if isinstance(a[k], dict) or isinstance(a[k], OrderedDict):
            print_dicts(a[k], indent + 1)
        else:
            print(f"{' ' * indent}KEY: {k} ->\t {a[k]}")
    
if __name__ == "__main__":
    sentence = "I want to fly."
    x = call_trips_parser_api(sentence)
    print("1")
    print(x)
    print_dicts(x, skip_fields=set([PARSES_FIELD]))
    
    print("2")
    for i, v in enumerate(x[PARSES_FIELD]):
        print(f"Interpretation {i}:\n\t")
        print(f"\tParse Tree:\n\t{v[0]}")
        print_dicts(v[0])
        
        print(f"\tLogical Form:{v[1]}")
        print_dicts(v[1])
        
