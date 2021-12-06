from random import randint
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
    LF_TYPE_FIELD = "LF:type"
    LF_WORD_FIELD = "LF:word"
    GEO_REGION_ONT = "geographic-region"
    GENERAL_REFERENTIAL_ONT = "referential-sem"
    SA_WH_QUESTION_ONT = "sa_wh-question"
    SA_YN_QUESTION_ONT = "sa_yn-question"
    
    
    ont_tree = build_ontology_tree()
    asked_wh_question = False
    asked_yn_question = False
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
        lf_type = str(lf[LF_TYPE_FIELD]).lower()
        ancestors = ont_tree.get_ont_node_ancestors(lf_type.strip().lower())
        if GEO_REGION_ONT in ancestors:
            location_obj, location_code = LocationsDB.query_location(
                    clean_str(lf[LF_WORD_FIELD]))
            
            if location_obj is not None:
                mentioned_a_location = True
                location_mentioned = clean_str(lf[LF_WORD_FIELD])
            
        elif GENERAL_REFERENTIAL_ONT in ancestors:
            if LF_WORD_FIELD in lf:
                location_obj, location_code = \
                    LocationsDB.query_location(clean_str(lf[LF_WORD_FIELD]))
                if location_obj is not None:
                    mentioned_a_location = True
                    abbr_not_recognized_as_location = True
                    location_mentioned = clean_str(lf[LF_WORD_FIELD])
                                    
        if SA_WH_QUESTION_ONT in ancestors:
            asked_wh_question = True
        if SA_YN_QUESTION_ONT in ancestors:
            asked_yn_question = True
                            
    if mentioned_a_location:
        print(f"\nLooks like you mentioned {LocationsDB.MODES_DICT[location_code]}: {str(location_obj).title()}")
        if abbr_not_recognized_as_location:
            print("By the way, TRIPS doesn't even realize that " + \
                f"{location_mentioned} is a {LocationsDB.MODES_DICT[location_code]}. " + \
                    f"It considers the phrase \"{location_mentioned}\" to be of " + \
                        f"ontological type \"{lf_type}\". Instead it just used some " + \
                            "ancestor-related pattern matching to figure it out :)")
        
        airports_at_loc = LocationsDB.find_airports_faa(location_obj.search_id())
        if len(airports_at_loc) > 1:
            print("Here is a list of airports located there:")
            print(pretty_list(airports_at_loc))
        else:
            print(f"Here are between 3 and 6 randomly generated flights out of {str(location_obj).title()}:")
            dest_state = "new york" if location_obj.state_name != "new york" else "california"
            flights_list = generate_flights(num_flights=randint(3, 6), 
                                            origin_range=[location_mentioned],
                                            dest_range=[dest_state])
            for f in flights_list:
                print('\t' + str(f))
        
    if asked_wh_question:
        print("\nWh question detected! IE. when, where, or what! (Though specifically not 'why'.)")
    
    if asked_yn_question:
        print("\nYes-No question detected!")

        
if __name__ == "__main__":
    
    demo_sentences = ["Can we fly to NYC?", "How about Texas?",
                      "I want to fly out of LAX.", "I want to fly from JFK.",
                      "Are there flights out of california tomorrow?"]
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