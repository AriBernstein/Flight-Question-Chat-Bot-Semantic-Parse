import pandas as pd
import json

from typing import Iterable
from collections import OrderedDict
import xmltodict
import requests
import re
"""

Call the TRIPS Parser API to retrieve semantic interpretations of input.
API Documentation can be found here: http://trips.ihmc.us/parser/api.html
"""
SENTENCE = "I want to fly to SF."

GET_URL = "http://trips.ihmc.us/parser/cgi/parse"
MULTIPLE_PARSES_FIELD = "compound-communication-act"
UTT_FIELD = "utt"
PARSES_FIELD = "parses"
TREE_FIELD = "tree"
TERMS_FIELD = "terms"

INDENT_LEN = 3

ITERABLE_CHECKS = {list, set, tuple}
DICT_CHECKS = {dict, OrderedDict}
SKIP_FIELDS = {"rdf:RDF"}

def call_trips_parser_api(sentence:str) -> dict:
    
    resp = requests.get(GET_URL + "?input=" + re.sub(r'\s+', '+', sentence))
    if resp.status_code != 200:
        raise Exception(
            "Bad response when calling call_trips_parser_api\nCode: " + \
                f"{resp.status_code}\nError: {resp.reason}\nURL: {resp.url}\t")
    # Return dictionary    
    ret = {"sentence":sentence, PARSES_FIELD:[]}
    
    # Format XML output into new dictionary with input, parse tree 
    # representation, logical form representation
    d = xmltodict.parse(resp.content)["trips-parser-output"]

    # Handle single or multiple parses
    if MULTIPLE_PARSES_FIELD in d:
        for parse in d[MULTIPLE_PARSES_FIELD][UTT_FIELD]:
            ret[PARSES_FIELD].append([parse[TREE_FIELD], parse[TERMS_FIELD]])

    else:
        d = d[UTT_FIELD]
        for x in d.keys():
            print(f"KEY: {x}:\n{d[x]}\n-------------------------------------\n")
        ret[PARSES_FIELD].append([d[TREE_FIELD], d[TERMS_FIELD]])

    ret["num_parses"] = len(ret[PARSES_FIELD])

    return ret

def dict_str(d:dict, indent:int=0, ret:str="", skip_fields:set[str]=None) -> str:
    for k in d.keys():
        if skip_fields and k in skip_fields:
            continue
        elif type(d[k]) in ITERABLE_CHECKS:
            ret += list_str(it=d[k], indent=indent + INDENT_LEN, ret=ret)
        elif type(d[k]) in DICT_CHECKS:
            ret += dict_str(d=d[k], indent=indent + INDENT_LEN, ret=ret)
        else:
            ret += f"{ret}\n{' ' * indent}KEY: {k} -> {d[k]}"
    return ret

def list_str(it:Iterable, indent:int=0, ret:str="", line_char_lim:int=50, skip_fields:set[str]=SKIP_FIELDS) -> str:
    if not it:
        return "[empty list]"
    
    list_line = f"{' ' * indent}["
    for e in it:        
        appended_to_ret = False
        if type(e) in ITERABLE_CHECKS:
            list_line += list_str(e, indent + INDENT_LEN, ret, line_char_lim, skip_fields)
        elif type(e) in DICT_CHECKS:
            list_line += dict_str(e, indent + INDENT_LEN, ret)
        else:
            list_line += f"{e}, "
            
        if len(list_line) >= line_char_lim:
            appended_to_ret = True
            ret += f"\n{list_line}"
            list_line = f" {' ' * indent}"

    if not appended_to_ret:
        ret += f"\n {list_line}"

    return ret

if __name__ == "__main__":
    parser_data = call_trips_parser_api(SENTENCE)
    
    
    
    # print(parser_data.keys())
    
    # print("1")
    # print(dict_str(parser_data, skip_fields={PARSES_FIELD}))

    print(json.dumps(parser_data, indent=4))
    
        
    # print("\n----------\n\n2")
    # for i, v in enumerate(parser_data[PARSES_FIELD]):
    #     print(f"\n-> 2.{i} ----------\n")
    #     print(f"Interpretation {i}:")
    #     # print(f"\n\tParse Tree:\n\t{dict_str(v[0])}")
    #     print(v)
    #     print(list_str(v))

    #     # print(f"\n\tLogical Form:\n\t{dict_str(a=v[1], skip_fields=SKIP_FIELDS)}\n\n")n