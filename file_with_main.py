from Utils.DataSetGeneration.GenerateLocations import get_airports_dataframe, generate_location_objects

if __name__ == "__main__":
    x = get_airports_dataframe()
    states_dict, cities_dict, airports_dict, states_to_cities, \
        states_to_airports, cities_to_airports, state_abbr_to_state, \
            city_abbr_to_city = generate_location_objects(x)
            
    print("lol")