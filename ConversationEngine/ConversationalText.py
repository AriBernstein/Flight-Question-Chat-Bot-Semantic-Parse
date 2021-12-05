from Utils.StringUtils import either_any, pretty_list

INITIAL_OPENING = "Hello, I am a bot designed to answer questions related " + \
    "to airports and flights, both one way and round trip. Ask away!"
    
RE_OPENING = "Any other airport or flight related questons?"
CONCLUSION = "Thanks for chatting, goodbye!"

def found_cities_w_airports_state(state_name:str, cities:list[str]) -> str:
    return f"I was able to find airports in airports in {len(cities)} in " + \
        f"{state_name}: {pretty_list(cities)}. Would you like more " + \
            f"information about the airport(s) in {either_any(len(cities))}?"