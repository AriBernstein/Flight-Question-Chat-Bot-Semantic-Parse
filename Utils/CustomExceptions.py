

class OriginDestinationException(Exception):
    def __init__(self) -> None:
        super().__init__("Only call this method on OrigStateKnowledge, " + \
                "DestStateKnowledge, OrigCityKnowledge, DestCityKnowledge, " + \
                    "OrigAirportKnowledge, DestAirportKnowledge")


class InvalidTypeException(Exception):
    def __init__(self, given_type:str, expected_type:str, 
                 field_name:str=None, class_name:str=None) -> None:
        msg = f"Invalid type, received: {given_type}, expected: {expected_type}"
        msg += ", in field: " + field_name if field_name else ""
        msg += " in class: " + class_name if class_name else "" + '.'
        super().__init__(msg)
        
        
class InvalidModeException(Exception):
    def __init__(self, current_mode:int, min_mode:int, 
                 max_mode:int, in_range=True) -> None:
        """
        Some methods have functionality which varies depending on an integer
        parameter called Mode. This Exception is for when an unexpected Mode is
        given.

        Args:
            current_mode (int): given mode
            min_mode (int): expected mode 1 or low mode in range.
            max_mode (int): expected_mode 2 or high mode in range.
            in_range (bool, optional): If true (default), modes are a range
                between min_mode and max_mode. Otherwise binary.    """
        
        super().__init__(f"Invalid mode, received: {current_mode}, expected " + \
            f"between {min_mode} and {max_mode} (inclusive)." if in_range else \
                f"{min_mode} or {max_mode}.")
        
        
class ExpectingRelativeException(Exception):
    def __init__(self, given:str, expected:str, mode:int=1) -> None:
        if not 1 <= mode <= 3:
            raise InvalidModeException(given, 1, 5)
        ret = f"Invalid value, given {given} when "                
        if mode == 2: ret += f"less than "
        elif mode == 3: ret += f"less than or equal to "
        elif mode == 4: ret += f"greater than "
        elif mode == 5: ret += f"greater than or equal to "        
        return ret + f"{expected} was expected."