class Country:
    def __init__(self) -> None:
        self.country_name="united states of america"
        self.country_abbr="usa"
        self._location_priority = 1
        
    def abbr(self) -> str:
        return self.country_abbr
        
    def priority(self) -> int:
        return self._location_priority
        
    def __str__(self) -> str:
        return self.country_name.title()
    
    def __repr__(self) -> str:
        return self.country_abbr.upper()
    
    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Country):
            return __o.country_name == self.country_name and \
                __o.country_abbr == self.country_abbr
        return False
        

class State(Country):
    def __init__(self, state_name:str, state_abbr:str) -> None:
        super().__init__()
        self.state_name = state_name
        self.state_abbr = state_abbr
        self._location_priority = 2
        
    def abbr(self) -> str:
        return self.state_abbr.upper()
    
    def country_loc(self) -> Country:
        return self.__class__.__bases__[0]
        
    def __str__(self) -> str:
        return self.state_name.title()
    
    def __repr__(self) -> str:
        return self.abbr()
    
    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, State):
            return self.state_name == __o.state_name and \
                self.state_abbr == __o.state_abbr and \
                    super().__eq__(__o)
        return False
                    
                    
class City(State):
    def __init__(self, city_name: str, city_abbr: str, state_name: str, state_abbr: str) -> None:
        super().__init__(state_name, state_abbr)
        self.city_name = city_name
        self.city_abbr = city_abbr
        self._location_priority = 3
        
    def abbr(self):
        return self.city_abbr.upper() if self.city_abbr else str(self)
    
    def state_loc(self) -> State:
        return self.__class__.__bases__[0]
    
    def country_loc(self) -> Country:
        return self.state_loc().country_loc()
        
    def __str__(self) -> str:
        return self.city_name.title()
    
    def __repr__(self) -> str:
        return self.abbr()
    
    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, City):
            return self.city_name == __o.city_name and \
                self.city_abbr == __o.city_abbr and \
                    super().__eq__(__o)
        return False
                   
        
class Airport(City):
    def __init__(self, airport_name:str, airport_abbr:str, enplanements:int,
                 city_name: str, city_abbr: str,
                 state_name: str, state_abbr: str) -> None:
        super().__init__(city_name, city_abbr, state_name, state_abbr)
        self.airport_name = airport_name
        self.airport_abbr = airport_abbr
        self.enplanements = enplanements
        self._location_priority = 4
        
    def abbr(self) -> str:
        return self.airport_abbr.upper()
    
    def city_loc(self) -> City:
        return self.__class__.__bases__[0]
    
    def state_loc(self) -> State:
        return self.city_loc().state()
    
    def country_loc(self) -> Country:
        return self.state_loc().country_loc()
        
    def __str__(self) -> str:
        return self.airport_name.title()
    
    def __repr__(self) -> str:
        return self.abbr()
    
    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Airport):
            return self.airport_name == __o.airport_name and \
                self.airport_abbr == __o.airport_abbr and \
                    super().__eq__(__o)