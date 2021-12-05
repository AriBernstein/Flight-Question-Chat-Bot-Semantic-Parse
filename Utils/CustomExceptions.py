

class OriginDestinationException(Exception):
    def __init__(self) -> None:
        super().__init__("Only call this method on OrigStateKnowledge, " + \
                "DestStateKnowledge, OrigCityKnowledge, DestCityKnowledge, " + \
                    "OrigAirportKnowledge, DestAirportKnowledge")

class InvalidTypeException(Exception):
    def __init__(self, given_type:str, expected_type:str) -> None:
        super().__init__(
            f"Invalid type, received: {given_type}, expected: {expected_type}.")