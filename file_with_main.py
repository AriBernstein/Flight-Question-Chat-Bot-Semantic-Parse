from datetime import time
from pprint import pprint
import json
from Utils.GenerateFlights import generate_flights
from Utils.Utils import LocationsDB
from Utils.GenerateLocations import get_airports_dataframe, generate_location_objects
from Utils.ParseOntologyTree import build_ontology_tree
from Utils.CallTripsParserAPI import get_trips_parser_semantic_analysis
from Utils.StringUtils import clean_str

def small_demo(input:str="Want to fly to New York City?") -> None:
    """
    Check for wh-question, location, movement. 
    """
    asked_question = False
    mentioned_a_location = False
    mentioned_travel = False
    something_about_flights = False
    location_val = None
    location_code = None
    
    logical_form = get_trips_parser_semantic_analysis(input)
    
    # print(json.dumps(logical_form, indent=4))
    
    for lf in logical_form:
        
        # Handle location
        lf_type = lf["LF:type"]
        if lf_type == "GEOGRAPHIC-REGION":
            mentioned_a_location = True
            location_val = clean_str(lf["LF:word"])
        elif lf_type == "REFERENTIAL-SEM" and "LF:word" in lf:
            location_val, location_code = LocationsDB.query_location(
                clean_str(lf["LF:word"])
            )
            if not location_val is None:
                mentioned_a_location = True
                
                
        elif lf_type =="SA_WH-QUESTION":
            asked_question = True
                
    if mentioned_a_location:
        print(f"Looks like you mentioned location: {str(location_val).title()}")
        print("Here is a list of airports located there:")
        
        print(LocationsDB.find_airports_faa(location_val))
        

if __name__ == "__main__":
    
    # nyc = LocationsDB.query_city("new_york_city")
    # tx = LocationsDB.query_state("texas")
    # x = generate_flights(5, [tx], [nyc, ] )
    # small_demo()
    # x = get_airports_dataframe()
    # states_dict, cities_dict, airports_dict, states_to_cities, \
    #     states_to_airports, cities_to_airports, state_abbr_to_state, \
    #         city_abbr_to_city, airport_names_to_faa = generate_location_objects(x)
            
    # # print(airports_dict["jfk"].priority())
    
    # ontology_tree = build_ontology_tree()
    # print(ontology_tree.get_root())
    # print(ontology_tree.get_root().get_children()[0].get_children()[0].ancestors())
    
    ny_airports = LocationsDB.find_airports_faa("Montana")
    
    la_airports = LocationsDB.find_airports_faa("Los Angeles")
    print(ny_airports)
    print(la_airports)
    
    x = generate_flights(5, list(ny_airports), list(la_airports), departure_time_mode=5)
    for f in x:
        print(f)