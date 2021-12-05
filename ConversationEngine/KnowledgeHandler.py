from DataStructures.QueryTypes import QueryTypes, AirportsQuery, \
    SingleFlightQuery, RoundTripFlightQuery
from Utils.CallTripsParserAPI import get_trips_parser_semantic_analysis

# Semantic parse field constants:
# -> Semantic fields
LF_TYPE = "LF:type"
LF_WORD = "LF:word"

# -> Semantic values
# --> Location
TO_FROM = "PATH"
GEOGRAPHIC_LOC = "GEOGRAPHIC-REGION"
REFERENTIAL_SEM = "REFERENTIAL-SEM"
TO_LOCATION = "TO-LOC"
FROM_LOCATION = "FROM-LOC"
SOURCE_AS_LOC = "SOURCE-AS-LOC"

# --> Date/Time (highest ancestor to closest)
ABY_TIME = "ANY-TIME-OBJECT"
RELATIVE_TIME = "TIME-LOC"  # Parent of today/tomorrow
TODAY = "TODAY"
TOMORROW = "TOMORROW"
EVENT_TIME_REL = "EVENT_TIME_REL"
START_TIME = "START_TIME"

INTERVAL = "TIME-INTERVAL"
RELATIVE_DATE = "DATE_OBJ_IN"
MONTH = "MONTH"
WEEK = "WEEK"
WEEK_OBJ = "WEEK_OBJECT"    # Sometimes, "this week" is caught with this one
DAY_STAGE = "DAY_STAGE" # Parent of "Morning", "Night", "Evening", ...
MONTH_NAME = "MONTH_NAME"
AFTERNOON = "AFTERNOON"
DAY_STAGE_PM = "DAY-STAGE-PM"
EVENING = "EVENING"
NIGHT = "NIGHT"


# Query hierarchy - ordered from most to least information required to complete
# the query.
# TODO - add round trips. I'm too tired for that shit rn
QUERY_HIERARCHY = [SingleFlightQuery, AirportsQuery]

class KnowledgeHandler:    
    
    def __init__(self) -> None:
        self._o_loc_pointer = self._d_loc_pointer
    
    def parse_information(resp:str) -> None:

        for ontology_node in get_trips_parser_semantic_analysis(resp):
            pass