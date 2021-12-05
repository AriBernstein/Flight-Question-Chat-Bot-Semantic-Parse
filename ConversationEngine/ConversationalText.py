from DataStructures.Flight import Flight
from Utils.StringUtils import either_any, pretty_list

INITIAL_OPENING = "Hello, I am a bot designed to answer questions related " + \
    "to airports and flights, both one way and round trip. Ask away!"
    
RE_OPENING = "Any other airport or flight related questons?"
CONCLUSION = "Thanks for chatting, goodbye!"

def found_cities_w_airports_state(state_name:str, cities:list[str]) -> str:
    return f"I was able to find airports in airports in {len(cities)} in " + \
        f"{state_name}: {pretty_list(cities)}. Would you like more " + \
            f"information about the airport(s) in {either_any(len(cities))}?"
            
def found_airports_in(city_name:str, airports: list[str]) -> str:
    return f"Here are the airports I was able to find in {city_name}:\n\t" + \
        f"{pretty_list(airports, 1)}"
        
def found_n_flights_from_to(start_loc_name:str, end_loc_name, 
                            flights:list[Flight]) -> str:
    return f"I found the following {len(flights)} from " + \
        f"{start_loc_name} to {end_loc_name}:\n\t{pretty_list(flights)}"

def found_flights_out_of_airport(airport_name:str, flight_list:list[str],
                                 when_label:str) -> str:
    return f"I found the following flights out of {airport_name} " + \
        f"{when_label}:\n\t{pretty_list(flight_list)}"

def state_flights_follow_up(state_name:str, out_of:bool=True) -> str:
    out_of_str = "out of" if out_of else "into"
    return f"Okay, should I look for all flights {out_of_str} {state_name} " + \
        "or would you prefer to learn about the airports located there instead?"
        
def departure_loc_prompt() -> str:
    "From which state, city, or airport would you like to fly?"
    
def arrival_loc_prompt() -> str:
    "To which state, city, or airport would you like to fly?"

def time_to_leave_prompt(loc_str:str=None) -> str:
    if loc_str is None:
        return "When would you like to head out?"
    else:
        return f"When would you like to head out from {loc_str}?"