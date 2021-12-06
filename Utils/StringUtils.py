from datetime import datetime
import re

from Utils.CustomExceptions import ExpectingRelativeException, InvalidModeException

def clean_str(s:str, spaces:bool=True, lowercase=True) -> str:
    d = ' ' if spaces else '-'
    ret = re.sub('[^0-9a-zA-Z]+', d, s).strip()
    return ret.lower() if lowercase else ret
    
def either_any(list_len:int) -> str:
    if list_len < 2: raise ExpectingRelativeException(list_len, 2, 5)
    return "either" if list_len == 2 else "any"

def pretty_date_time(t:datetime) -> str:
    return t.strftime("%m-%d-%Y %H:%M")

def pretty_list(l:list[str], capitalization_mode:int=0, add_and:bool=True) -> str:
    """
    Turn list into pretty string.
    Modes:
        0: Do not reformat list elements.
        1: Capitalize the first level of each list element.
        2: Capitalize every letter in each list element.
        3: Make lowercase each letter in each list element.

    Args:
        l (list[str]): List to stringify.
        capitalization_mode (int, optional): Affects formatting of strings in 
            list. See method description.
        add_and (bool): If true (default), add 'and' before the final element.
            Ex. "One, Two, Three" -> "One, Two, and Three"

    Returns:
        str: List as a pretty string.   """
    
    l = list(l) if isinstance(l, set) else l 
    
    if len(l) == 0: return ""
    elif not 0 <= capitalization_mode <= 3:
        raise(InvalidModeException(capitalization_mode, 0, 3))
    ret = ""
    for i in range(len(l)):
        if capitalization_mode == 0:
            ret += l[i]
        elif capitalization_mode == 1:
            ret += l[i].title()
        elif capitalization_mode == 2:
            ret += l[i].upper()
        elif capitalization_mode == 3:
            ret += l[i].lower()
            
        if i != len(l) - 1:
            ret += ', '
        elif i == len(l) - 2 and add_and:
            ret += "and "
    
    return ret