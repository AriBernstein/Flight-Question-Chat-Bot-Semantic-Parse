from collections import OrderedDict
import xmltodict
import requests
import re

"""
Call the TRIPS Parser API to retrieve semantic interpretations of input.
API Documentation can be found here: http://trips.ihmc.us/parser/api.html   """

SAMPLE_SENTENCE = "I want to fly to New York City this July."

GET_URL = "http://trips.ihmc.us/parser/cgi/parse"
MULTIPLE_PARSES_FIELD = "compound-communication-act"
UTT_FIELD = "utt"
PARSES_FIELD = "parses"
TREE_FIELD = "tree"
TERMS_FIELD = "terms"

INDENT_LEN = 3

ITERABLE_CHECKS = {list, set, tuple}
DICT_CHECKS = {dict, OrderedDict}

# Fields from the response from the TRIPS parser API
RDF = "rdf:RDF"
RDF_DESCR = "rdf:Description"

def _call_trips_parser_api(sentence:str) -> dict:
    
    resp = requests.get(GET_URL + "?input=" + re.sub(r'\s+', '+', sentence))
    if resp.status_code != 200:
        raise Exception(
            "Bad response when calling call_trips_parser_api\nCode: " + \
                f"{resp.status_code}\nError: {resp.reason}\nURL: {resp.url}\t")
    # Return dictionary    
    ret = {"sentence":sentence, PARSES_FIELD:[]}
    
    # Format XML output into new dictionary with input, parse tree 
    # representation, logical form representation
    dict_rep = xmltodict.parse(resp.content)["trips-parser-output"]

    # Handle single or multiple parses
    if MULTIPLE_PARSES_FIELD in dict_rep:
        for parse in dict_rep[MULTIPLE_PARSES_FIELD][UTT_FIELD]:
            ret[PARSES_FIELD].append([parse[TREE_FIELD], parse[TERMS_FIELD]])
    else:
        dict_rep = dict_rep[UTT_FIELD]
        ret[PARSES_FIELD].append([dict_rep[TREE_FIELD], dict_rep[TERMS_FIELD]])

    ret["num_parses"] = len(ret[PARSES_FIELD])
    return ret


def get_trips_parser_semantic_analysis(sentence:str=SAMPLE_SENTENCE) -> list[OrderedDict]:
    parser_data_raw = _call_trips_parser_api(sentence)

    if len(parser_data_raw[PARSES_FIELD]) == 1:
        return parser_data_raw[PARSES_FIELD][0][1][RDF][RDF_DESCR]
    else:
        ret = []
        for partial_parse in parser_data_raw[PARSES_FIELD]:
            for info in partial_parse[1][RDF][RDF_DESCR]:
                if not isinstance(info, str):
                    ret.append(info)
        return ret