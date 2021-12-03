from collections import defaultdict
import pandas as p
import re

from DataStructures.FlightLocations.Locations import Airport, City, State

# File locations
_DIR = "DataSet/Locations/"
_AIRPORTS_FP = _DIR + "airport_data.csv"
_STATE_ABBR_FP = _DIR + "us_state_abbr.csv"

# Field name constants:
# -> Initial input:
# ---> Airport data
_I_CITY = "City"
_I_FAA = "FAA"
_I_AIRPORT = "Airport"
_I_ENPLANEMENTS = "Enplanements\n"

# --> US State name data:
_I_STATE = "State Name"
_I_STATE_ABBR = "USPS Abbreviation"

# -> Cleaned output:
CITY = "city"
CITY_ABBR = "city_abbr"
STATE = "state"
STATE_ABBR = "state_abbr"
FAA = "faa"
AIRPORT = "airport_name"
ENPLANEMENTS = "enplanements"

def get_airports_dataframe() -> p.DataFrame:
    """
    Read in airport and USA State abbreviation data from CSV files, convert into
    Pandas dataframe formatted as follows:
    
    Data comes in format for each given state:
        City   ,    FAA,    IATA,   ICAO,   Airport,    Role,   Enplanements
        Alabama,       ,        ,       ,          ,        ,               
        Birmingham, BHM,     BHM,    BHM,   Birm...,     P-S,      1,516,075
        
    Returns:
        p.DataFrame: Dataframe of form:
            city,       city_abbr,   state, state_abbr, faa, airport_name, enplanements
            birmingham,      None, alabama,         al, bhm, birmingha...,      1516075
    """
    
    ap_df = p.read_csv(_AIRPORTS_FP, usecols=[
        _I_CITY, _I_FAA, _I_AIRPORT, _I_ENPLANEMENTS])
    
    # Eliminate whitespace & newlines
    cols = list(ap_df.columns)    # type: list[str]
    new_cols = {}
    for c in cols: new_cols[c] = c.strip().lower()
    new_cols[_I_AIRPORT] = AIRPORT
    
    ap_df.rename(columns=new_cols, inplace=True)
    ap_df = ap_df.applymap(lambda x: x.strip().lower() if isinstance(x, str) else x)

    # Find the rows that represent each state:
    state_rows = list(ap_df.index[ap_df[FAA].isnull()])
    state_rows.append(len(ap_df))   #   For getting final subset.
    
    # Prep to rename states:
    state_abbr_df = p.read_csv(_STATE_ABBR_FP, usecols=[_I_STATE, _I_STATE_ABBR])
    new_state_cols = {_I_STATE: STATE, _I_STATE_ABBR: STATE_ABBR}
    state_abbr_df.rename(columns=new_state_cols, inplace=True)
    state_abbr_df = state_abbr_df.applymap(lambda x: x.strip().lower())
    
    # Construct new dataframe
    cleaned_ap_df_cols = [CITY, CITY_ABBR, STATE, STATE_ABBR, 
                          FAA, AIRPORT, ENPLANEMENTS]
    cleaned_ap_df = p.DataFrame(columns=cleaned_ap_df_cols)
    
    def clean_city(city_name:str) -> str:
        name_split = re.split('[,\/]', city_name)
        return name_split[0].strip()

    def city_abbr(city_name:str) -> str:
        """
        Args:
            name (str): Full name of a city.

        Returns:
            str: If city_name is made up of more than one word, return the first
                letter of each word comprising it. Otherwise return city_name.
                Ex. new york -> ny, chicago -> chicago. """
                
        name_split = city_name.split()
        if len(name_split) == 1: return city_name
        
        abbr = ""
        for i in name_split: abbr += i[0]
        return abbr
    
    
    for i, state_row_index in enumerate(state_rows):
        if i == len(state_rows) - 1: continue
        
        # Find state name & abbreviation
        state = ap_df.at[state_row_index, CITY]
        state_abbr = \
            state_abbr_df[state_abbr_df[STATE] == state][STATE_ABBR]
        state_abbr = state_abbr.values[0] if len(state_abbr) >= 1 else None
        
        # Build row for each airport.
        airports_in_state = ap_df.iloc[state_row_index + 1:state_rows[i + 1]].copy()    # type: p.DataFrame
        airports_in_state[STATE] = state
        airports_in_state[STATE_ABBR] = state_abbr
        airports_in_state[CITY] = airports_in_state[CITY].apply(clean_city)
        airports_in_state[CITY_ABBR] = airports_in_state[CITY].apply(city_abbr)
        cleaned_ap_df = cleaned_ap_df.append(airports_in_state)
        
    # Convert enplanements to integers
    # -> Fill empty cells with '0', then convert the entire column to integer.
    cleaned_ap_df[ENPLANEMENTS] = \
        cleaned_ap_df[ENPLANEMENTS].apply(lambda x: '0' if x == '' else x)
    cleaned_ap_df[ENPLANEMENTS] = \
        cleaned_ap_df[ENPLANEMENTS].str.replace(',', '').astype(int)
    print(cleaned_ap_df)
    return cleaned_ap_df

        
def generate_location_objects(airports_df:p.DataFrame) -> tuple[
        dict[str, State], dict[str, City], dict[str, Airport], 
        dict[str, set[City]], dict[str, set[Airport]], dict[str, set[Airport]]]:
    """
    Load airports & locations into data structures accessibly by the semantic
    parser.

    Args:
        airports_df (p.DataFrame): Output of read_and_clean_csv_data

    Returns:
        tuple[ dict[str, str], dict[str, str], dict[str, State],  
               dict[str, City], dict[str, Airport], dict[str, set[str]], 
               dict[str, set[str]], dict[str, set[str]]]:
                
            1. states - key -> state abbr, pair -> State Obj
            2. cities - key -> city full lowercase, pair -> City Obj
            3. airports - key -> FAA code lowercase, pair -> Airport obj
            4. states to cities - key -> state abbr lowercase, pair -> set of city full lowercase city names
            5. states to airports - key -> state abbr lowercase, pair -> set of lowercase FAA codes
            6. cities to airports - key -> city full name lowercase, pair -> set of lowercase FAA codes
            7. state abbr to state - key -> state abbr lowercase, pair -> str state full name lowercase
            8. city abbr to city - key -> city abbr lowercase, pair -> city name full   """
    
    states_dict = {}    # type: dict[str, State]
    cities_dict = {}    # type: dict[str, City]
    airports_dict = {}  # type: dict[str, Airport]
    
    states_to_cities = defaultdict(set)
    states_to_airports = defaultdict(set)
    cities_to_airports = defaultdict(set)

    state_abbr_to_state = {}    # type: dict[str, str]    
    city_abbr_to_city = {}      # type: dict[str, str]
    
    state_list = list(airports_df[STATE].unique())
    for state in state_list:
        airports_in_state = airports_df[airports_df[STATE] == state].reset_index(drop=True)
        state_abbr = airports_in_state.loc[0, STATE_ABBR]
        
        if not state_abbr or state_abbr == "None":  # Not enough time :(
            continue

        state_obj = State(state, state_abbr)
        
        states_dict[state_obj.abbr()] = state_obj
        state_abbr_to_state[state_abbr] = state
        
        for city in list(airports_in_state[CITY].unique()):
            airports_in_city = airports_in_state[airports_in_state[CITY] == city].reset_index(drop=True)
            city_abbr = airports_in_city.loc[0, CITY_ABBR]
            city_obj = City(city, city_abbr, state_obj.state_name, state_obj.state_abbr)
            
            cities_dict[city] = city_obj
            
            if city_abbr != city:
                city_abbr_to_city[city_abbr] = city
                
            states_to_cities[state].add(city)
            
            for airport in list(airports_in_city[AIRPORT].unique()):
                individual_airport_series = airports_in_city[airports_in_city[AIRPORT] == airport].head(1).reset_index(drop=True)
                airport_faa = individual_airport_series[FAA].iloc[0]
                airport_enplanements = individual_airport_series.loc[0, ENPLANEMENTS]
                airport_obj = Airport(airport, airport_faa, airport_enplanements, city, city_abbr, state, state_abbr)
                
                airports_dict[airport_faa] = airport_obj
                
                states_to_airports[state].add(airport_faa)
                cities_to_airports[city].add(airport_faa)
                
    return states_dict, cities_dict, airports_dict, states_to_cities, \
        states_to_airports, cities_to_airports, state_abbr_to_state, \
            city_abbr_to_city