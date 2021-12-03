from pprint import pprint

from Utils.GenerateLocations import get_airports_dataframe, generate_location_objects
from Utils.ParseOntologyTree import build_ontology_tree


if __name__ == "__main__":
    x = get_airports_dataframe()
    states_dict, cities_dict, airports_dict, states_to_cities, \
        states_to_airports, cities_to_airports, state_abbr_to_state, \
            city_abbr_to_city, airport_names_to_faa = generate_location_objects(x)
    # ontology_tree = build_ontology_tree()
    # print(ontology_tree.get_root())
    # print(ontology_tree.get_root().get_children()[0].get_children()[0].ancestors())
    
    print(airports_dict["jfk"].priority())