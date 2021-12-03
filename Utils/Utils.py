from typing import Type
from Utils.GenerateLocations import generate_location_objects
from DataStructures.FlightLocations.Locations import State, City, Airport

class Static:
    """
    Quick hack to make static classes.  """
    
    def __init__(self) -> None:
        raise TypeError("Static classes cannot be instantiated")

class Locations(Static):
    states_dict, cities_dict, airports_dict, states_to_cities, \
        states_to_airports, cities_to_airports, state_abbr_to_state, \
            city_abbr_to_city, airport_names_to_faa = generate_location_objects()
            
    @staticmethod
    def _loc_exists(loc_str:str, code:int) -> tuple[str, int]:
        """
        Args:
            loc_str (str): possible location from input.
            code (int): 1. State, 2. City, 3. Airport

        Returns:
            tuple[str, int]: string in format to query for state, city, or
                country from the dictionaries in this class, as well as the 
                number representing which of the three data sets it found. """
        if not 1 <= code <= 3:
            raise Exception("Code parameter must be an integer between " + \
                "zero and three.")
        
        if code == 1:
            if loc_str in Locations.state_abbr_to_state:
                return Locations.state_abbr_to_state[loc_str], 1
            if loc_str in Locations.states_dict:
                return loc_str, 1
            return None, None
        
        elif code == 2:
            if loc_str in Locations.city_abbr_to_city:
                return Locations.city_abbr_to_city[loc_str], 2
            if loc_str in Locations.cities_dict:
                return loc_str, 2
            return None, None
        
        else:
            if loc_str in Locations.airport_names_to_faa:
                return Locations.airport_names_to_faa[loc_str], 3
            if loc_str in Locations.airports_dict:
                return loc_str, 3
            return None, None
        
    @staticmethod
    def query_state(state_str:str) -> State:
        state_str, _ = Locations._loc_exists(state_str, 1)
        return None if state_str is None else Locations.states_dict[state_str]
    
    @staticmethod
    def query_city(city_str:str) -> City:
        city_str, _ = Locations._loc_exists(city_str, 2)
        return None if city_str is None else Locations.cities_dict[city_str]
    
    @staticmethod
    def query_airport(airport_str:str) -> Airport:
        airport_str, _ = Locations._loc_exists(airport_str, 1)
        return None if airport_str is None else Locations.airports_dict[airport_str]
    
    @staticmethod
    def query_location(loc_str) -> Type[State]:
        for i in range(1, 4):
            loc_str_new, code = Locations._loc_exists(loc_str_new, code)
            if not loc_str_new is None:
                if code == 1:
                    return Locations.query_state(loc_str)
                elif code == 2:
                    return Locations.query_city(loc_str)
                elif code == 3:
                    return Locations.query_airport(loc_str)
                else:
                    raise Exception(f"location query return code was {code}. That's weird :(")
        return None