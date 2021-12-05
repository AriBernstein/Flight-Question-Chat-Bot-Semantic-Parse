from typing import Type

from Utils.GenerateLocations import generate_location_objects
from Utils.CustomExceptions import InvalidModeException
from DataStructures.LocationTypes import USState, City, Airport
from Utils.StringUtils import clean_str
        
class StaticClass:
    """
    Quick hack to make static classes.  """
    
    def __init__(self) -> None:
        raise TypeError("Static classes cannot be instantiated")

class LocationsDB(StaticClass):
    states_dict, cities_dict, airports_dict, states_to_cities, \
        states_to_airports, cities_to_airports, state_abbr_to_state, \
            city_abbr_to_city, airport_names_to_faa = generate_location_objects()
            
    @staticmethod
    def _loc_exists(loc_str:str, mode:int) -> tuple[str, int]:
        """
        Args:
            loc_str (str): possible location from input.
            code (int): 1. State, 2. City, 3. Airport

        Returns:
            tuple[str, int]: string in format to query for state, city, or
                country from the dictionaries in this class, as well as the 
                number representing which of the three data sets it found. """
        
        loc_str = clean_str(loc_str)
        if mode == 1:
            if loc_str in LocationsDB.state_abbr_to_state:
                return LocationsDB.state_abbr_to_state[loc_str], 1
            if loc_str in LocationsDB.states_dict:
                return LocationsDB.states_dict[loc_str].name(), 1
            return None, None
        
        elif mode == 2:
            if loc_str in LocationsDB.city_abbr_to_city:
                return LocationsDB.city_abbr_to_city[loc_str], 2
            if loc_str in LocationsDB.cities_dict:
                return LocationsDB.cities_dict[loc_str].name(), 2
            return None, None
        
        elif mode == 3:
            if loc_str in LocationsDB.airport_names_to_faa:
                return LocationsDB.airport_names_to_faa[loc_str], 3
            if loc_str in LocationsDB.airports_dict:
                return LocationsDB.airports_dict[loc_str].abbr(), 3
            return None, None
        
        raise InvalidModeException(mode, 1, 3)
        
    @staticmethod
    def query_state(state_str:str) -> USState:
        state_str, _ = LocationsDB._loc_exists(state_str, 1)
        return None if state_str is None else LocationsDB.states_dict[state_str]
    
    @staticmethod
    def query_city(city_str:str) -> City:
        city_str, _ = LocationsDB._loc_exists(city_str, 2)
        return None if city_str is None else LocationsDB.cities_dict[city_str]
    
    @staticmethod
    def query_airport(airport_str:str) -> Airport:
        airport_str, _ = LocationsDB._loc_exists(airport_str, 3)
        return None if airport_str is None else LocationsDB.airports_dict[airport_str]
    
    
    @staticmethod
    def find_airports_faa(loc_str:str) -> set[str]:
        for i in range(1, 4):
            loc_str_new, code = LocationsDB._loc_exists(loc_str, i)

            if not loc_str_new is None:
                if code == 1:
                    print("a")
                    return LocationsDB.states_to_airports[loc_str_new]
                elif code == 2:
                    print("b")
                    return LocationsDB.cities_to_airports[loc_str_new]
                elif code == 3:
                    print("c")
                    return {LocationsDB.query_airport(loc_str_new).abbr()}
                else:
                    raise Exception("location query return code was " + \
                        f"{code}. That's weird :(")
                
    def find_airports_obj(loc_str:str) -> set[Airport]:
        ret = set()
        for faa_code in LocationsDB.find_airports_faa(loc_str):
            ret.add(LocationsDB.airports_dict[faa_code])
        return ret
    
    @staticmethod
    def query_location(loc_str:str) -> tuple[Type[USState], int]:
        for i in range(1, 4):
            loc_str_new, code = LocationsDB._loc_exists(loc_str, i)
            if not loc_str_new is None:
                if code == 1:
                    return LocationsDB.query_state(loc_str), code
                elif code == 2:
                    return LocationsDB.query_city(loc_str), code
                elif code == 3:
                    return LocationsDB.query_airport(loc_str), code
                else:
                    raise Exception(f"location query return code was {code}. That's weird :(")
                
        return None, None