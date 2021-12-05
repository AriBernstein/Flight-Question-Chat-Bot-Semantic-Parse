

class OriginDestinationException(Exception):
    def __init__(self) -> None:
        super().__init__("Only call this method on OrigStateKnowledge, " + \
                "DestStateKnowledge, OrigCityKnowledge, DestCityKnowledge, " + \
                    "OrigAirportKnowledge, DestAirportKnowledge")

class InvalidTypeException(Exception):
    def __init__(self, given_type:str, expected_type:str) -> None:
        super().__init__(
            f"Invalid type, received: {given_type}, expected: {expected_type}.")
        
class InvalidModeException(Exception):
    def __init__(self, current_mode:int, min_mode:int, max_mode:int, in_range=True) -> None:
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