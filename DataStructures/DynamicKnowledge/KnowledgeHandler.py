
class OriginDestinationException(Exception):
    def __init__(self) -> None:
        super().__init__("Only call this method on OrigStateKnowledge, " + \
                "DestStateKnowledge, OrigCityKnowledge, DestCityKnowledge, " + \
                    "OrigAirportKnowledge, DestAirportKnowledge")

class Knowledge:
    def __init__(self, is_destination:bool=None) -> None:
        self._relevant = True
        self._known = False
        self._is_destination = is_destination
        
    def relevant(self) -> bool:
        return self._relevant
    
    def known(self) -> bool:
        return self._known
    
    def make_known(self) -> None:
        self._known = True
        
    def base_info_str(self) -> str:
        if not self._relevant:
            return "irrelevant"
        known_str = "known" if self._known else "unknown"
        return f"relevant, and currently {known_str}"
    
    def is_base_type():
        return True
    
    def is_destination(self) -> bool:
        if self._is_destination is None: raise OriginDestinationException
        return self._is_destination
    
    def is_origin(self) -> bool:
        if self._is_destination is None: raise OriginDestinationException
        return not self._is_destination
    
    def __str__(self) -> str:
        return "Base Knowledge class instance. You're probably looking for " + \
            "one of my children."
    
    def __repr__(self) -> str:
        return str(self)