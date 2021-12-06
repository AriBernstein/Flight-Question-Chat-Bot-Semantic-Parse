from datetime import time
from pprint import pprint
import json
from Utils.GenerateFlights import generate_flights
from Utils.Utils import LocationsDB
from Utils.GenerateLocations import get_airports_dataframe, generate_location_objects
from Utils.ParseOntologyTree import build_ontology_tree
from Utils.CallTripsParserAPI import get_trips_parser_semantic_analysis
from Utils.StringUtils import clean_str, pretty_list

def small_demo(input:str="I want to fly out of LAX.") -> None:
    """
    Check for wh-question, location, movement. 
    """
    ont_tree = build_ontology_tree()
    asked_question = False
    mentioned_a_location = False
    mentioned_travel = False
    something_about_flights = False
    location_val = None
    location_code = None
    abbr_not_recognized_as_location = False

    logical_form = get_trips_parser_semantic_analysis(input)
    
    # print(json.dumps(logical_form, indent=4))
    for lf in logical_form:
        
        # Handle location
        lf_type = lf["LF:type"]
        ancestors = ont_tree.get_ont_node_ancestors(lf_type.strip().lower())
        if "GEOGRAPHIC-REGION".lower() in ancestors:
            location_obj, location_code = LocationsDB.query_location(
                    clean_str(lf["LF:word"]))
            
            if location_obj is not None:
                mentioned_a_location = True
                location_mentioned = clean_str(lf["LF:word"])
            
        elif "REFERENTIAL-SEM".lower() in ancestors:
            if "LF:word" in lf:
                location_obj, location_code = \
                    LocationsDB.query_location(clean_str(lf["LF:word"]))
                if location_obj is not None:
                    mentioned_a_location = True
                    abbr_not_recognized_as_location = True
                    location_mentioned = clean_str(lf["LF:word"])
                                    
        elif lf_type =="SA_WH-QUESTION":
            asked_question = True
                
    if mentioned_a_location:
        print(f"Looks like you mentioned location: {str(location_obj).title()}")
        if abbr_not_recognized_as_location:
            print(f"By the way, TRIPS doesn't even realize that {location_mentioned} is a {LocationsDB.MODES_DICT[location_code]}")
        print("Here is a list of airports located there:")
        print(pretty_list(LocationsDB.find_airports_faa(location_obj.name())))
        
        if asked_question:
            print("We detect a wh question, ie when, where, or what!")
        

if __name__ == "__main__":
    
    demo_sentences = ["Want to fly to NYC?", "How about Texas?", "I want to fly out of LAX."]
    for s in demo_sentences:
        small_demo(s)
        print("---------------------\n")

    
    # nyc = LocationsDB.query_city("new_york_city")
    # tx = LocationsDB.query_state("texas")
    # x = generate_flights(5, [tx], [nyc, ] )

    # x = get_airports_dataframe()
    # states_dict, cities_dict, airports_dict, states_to_cities, \
    #     states_to_airports, cities_to_airports, state_abbr_to_state, \
    #         city_abbr_to_city, airport_names_to_faa = generate_location_objects(x)
            
    # # print(airports_dict["jfk"].priority())
    
    # ontology_tree = build_ontology_tree()
    # print(ontology_tree.get_root())
    # print(ontology_tree.get_root().get_children()[0].get_children()[0].ancestors())
    
    # ny_airports = LocationsDB.find_airports_faa("Montana")
    
    # la_airports = LocationsDB.find_airports_faa("Los Angeles")
    # print(ny_airports)
    # print(la_airports)
    
    # x = generate_flights(5, list(ny_airports), list(la_airports), departure_time_mode=5)
    # for f in x:
    #     print(f)