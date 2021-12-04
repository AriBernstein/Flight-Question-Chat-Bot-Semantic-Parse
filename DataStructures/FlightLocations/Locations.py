USA_NAME = "united states of america"
USA_ABBR = "usa"

class BaseLocation:
    def __init__(self, name:str="base location", 
                 abbr:str="bl", priority:int=0) -> None:
        self._name = name
        self._abbr = abbr
        self._location_priority = priority
    
    def name(self) -> str:
        return self._name
    
    def abbr(self) -> str:
        return self._abbr
    
    def priority(self) -> int:
        return self._location_priority

    def __str__(self) -> str:
        return self._name.title()
    
    def __repr__(self) -> str:
        return self._abbr.upper()
    
    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, BaseLocation):
            return self._name == __o.name() and \
                self._location_priority == __o.priority()
        return False


class Country(BaseLocation):
    def __init__(self, name=USA_NAME, abbr=USA_ABBR, priority=1) -> None:
        super().__init__(name=name, abbr=abbr, priority=priority)
        self.country_name=name
        self.country_abbr=abbr


class USState(Country):
    def __init__(self, name:str, abbr:str, priority:int=2) -> None:
        super().__init__(name=name, abbr=abbr, priority=priority)
        self.state_name = name
        self.state_abbr = abbr
    
    def country_loc(self) -> Country:
        return self.__class__.__bases__[0]
                    
                    
class City(USState):
    def __init__(self, name: str, abbr: str,
                 state_name: str, state_abbr: str, 
                 priority=3) -> None:
        super().__init__(state_name, state_abbr, priority)
        self.city_name = name
        self.city_abbr = abbr
    
    def state_loc(self) -> USState:
        return self.__class__.__bases__[0]
    
    def country_loc(self) -> Country:
        return self.state_loc().country_loc()
                   
        
class Airport(City):
    def __init__(self,
                 name:str, abbr:str, enplanements:int,
                 city_name: str, city_abbr: str,
                 state_name: str, state_abbr: str,
                 priority:int=4) -> None:
        
        super().__init__(city_name, city_abbr, state_name, state_abbr, priority)
        self.airport_name = name
        self.airport_abbr = abbr
        self.enplanements = enplanements
            
    def city_loc(self) -> City:
        return self.__class__.__bases__[0]
    
    def state_loc(self) -> USState:
        return self.city_loc().state_loc()
    
    def country_loc(self) -> Country:
        return self.state_loc().country_loc()