from numpy import NaN
import pandas as p

_AIRPORTS_FP = "airport_data/airport_data.csv"
_STATE_ABBR_FP = "airport_data/us_state_abbr.csv"

def get_airport_df() -> p.DataFrame:
    """
    Data comes in format for each given state:
    City   ,    FAA,    IATA,   ICAO,   Airport,    Role,   Enplanements
    Alabama,       ,        ,       ,          ,        ,               
    Birmingham, BHM,     BHM,    BHM,   Birm...,     P-S,      1,516,075
    
    Returns:
        p.DataFrame: Dataframe of form:
            city,       city_abbr,   state, state_abbr, faa, airport_name, enplanements
            birmingham,      None, alabama,         al, bhm, birmingha...,      1516075
    """
    
    ap_df = p.read_csv(_AIRPORTS_FP, 
                       usecols=["City", "FAA", "Airport", "Enplanements\n"])
    
    # Eliminate whitespace & newlines
    cols = list(ap_df.columns)    # type: list[str]
    new_cols = {}
    for c in cols: new_cols[c] = c.strip().lower()
    new_cols["Airport"] = "airport_name"
    
    ap_df.rename(columns=new_cols, inplace=True)
    ap_df = ap_df.applymap(lambda x: x.strip().lower() if isinstance(x, str) else x)

    # Find the rows that represent each state:
    state_rows = list(ap_df.index[ap_df["faa"].isnull()])
    state_rows.append(len(ap_df))   #   For getting final subset.
    
    # Prep to rename states:
    state_abbr_df = p.read_csv(_STATE_ABBR_FP, usecols=["State Name", "USPS Abbreviation"])
    new_state_cols = {"State Name": "state_full", "USPS Abbreviation": "state_abbr"}
    state_abbr_df.rename(columns=new_state_cols, inplace=True)
    state_abbr_df = state_abbr_df.applymap(lambda x: x.strip().lower())
    
    # Construct new dataframe
    cleaned_ap_df_cols = ["city", "city_abbr", "state", "state_abbr", "faa",
                          "airport_name", "enplanements"]
    cleaned_ap_df = p.DataFrame(columns=cleaned_ap_df_cols)
    
    def city_abbr(name:str) -> str:
        names_split = name.split()
        if len(names_split) == 1:
            return name
        ret = ""
        for i in names_split: ret += i[0]
        return ret

    for i, state_row_index in enumerate(state_rows):
        if i == len(state_rows) - 1: continue
        
        # Find state name & abbreviation
        state = ap_df.at[state_row_index, "city"]
        state_abbr = \
            state_abbr_df[state_abbr_df["state_full"] == state]["state_abbr"]
        state_abbr = state_abbr.values[0] if len(state_abbr) >= 1 else None
        
        # Build row for each airport (must happen one at a time because of city abbreviations.)
        airports_in_state = ap_df.iloc[state_row_index + 1:state_rows[i + 1]].copy()    # type: p.DataFrame
        airports_in_state["state"] = state
        airports_in_state["state_abbr"] = state_abbr
        airports_in_state["city_abbr"] = airports_in_state["city"].apply(city_abbr)
        cleaned_ap_df = cleaned_ap_df.append(airports_in_state)
    
    return cleaned_ap_df
        
# def generate_flight_set() -> list[]
if __name__ == "__main__":
    get_airport_df()