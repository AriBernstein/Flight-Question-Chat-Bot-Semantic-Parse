from Utils.StringUtils import clean_str


USA_NAME = "united states of america"
USA_ABBR = "usa"

class BaseLocation:
    def __init__(self, name:str="base location", 
                 abbr:str="bl", priority:int=0) -> None:
        self._name = clean_str(name)
        self._abbr = clean_str(abbr)
        self._location_priority = priority
    
    def search_id(self) -> str:
        return self._name
    
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
    
    def __hash__(self) -> int:
        return hash(self.name)


class Country(BaseLocation):
    def __init__(self, name:str=USA_NAME, abbr:str=USA_ABBR, 
                 country_name:str=USA_NAME, country_abbr:str=USA_ABBR,
                 priority=1) -> None:
        super().__init__(name=name, abbr=abbr, priority=priority)
        self.country_name=country_name
        self.country_abbr=country_abbr


class USState(Country):
    def __init__(self, name:str, abbr:str,
                 state_name:str, state_abbr:str,
                 country_name=USA_NAME, country_abbr=USA_ABBR,
                 priority:int=2,) -> None:
        super().__init__(name=name, abbr=abbr,
                         country_name=country_name, 
                         country_abbr=country_abbr,
                         priority=priority)
        self.state_name = state_name
        self.state_abbr = state_abbr
    
    def country_loc(self) -> Country:
        return self.__class__.__bases__[0]

                    
class City(USState):
    def __init__(self, name: str, abbr: str,
                 city_name:str, city_abbr:str,
                 state_name: str, state_abbr: str, 
                 country_name:str=USA_NAME, country_abbr:str=USA_ABBR,
                 priority=3) -> None:
        super().__init__(name, abbr, state_name, state_abbr,
                         country_name, country_abbr, priority)
        self.city_name = city_name
        self.city_abbr = city_abbr
    
    def state_loc(self) -> USState:
        return self.__class__.__bases__[0]
    
    def country_loc(self) -> Country:
        return self.state_loc().country_loc()
                   
        
class Airport(City):
    def __init__(self,
                 name:str, abbr:str, enplanements:int,
                 city_name: str, city_abbr: str,
                 state_name: str, state_abbr: str,
                 country_name:str=USA_NAME, country_abbr:str=USA_ABBR,
                 priority:int=4) -> None:
        
        super().__init__(name, abbr, city_name, city_abbr, state_name, state_abbr,
                         country_name, country_abbr, priority)
        self._airport_name = name
        self._airport_abbr = abbr
        self._enplanements = enplanements
        
    def search_id(self) -> str:
        return self._abbr
            
    def city_loc(self) -> City:
        return self.__class__.__bases__[0]
    
    def state_loc(self) -> USState:
        return self.city_loc().state_loc()
    
    def country_loc(self) -> Country:
        return self.state_loc().country_loc()
    
    def enplanements(self) -> int:
        return self._enplanements