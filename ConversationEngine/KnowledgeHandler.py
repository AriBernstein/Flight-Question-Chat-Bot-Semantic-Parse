from DataStructures.QueryTypes import QueryTypes, AirportsQuery, \
    SingleFlightQuery, RoundTripFlightQuery
from Utils.CallTripsParserAPI import get_trips_parser_semantic_analysis

# Semantic parse field constants:
# -> Semantic fields
LF_TYPE = "LF:type"
LF_WORD = "LF:word"

# -> Semantic values
# --> Location
TO_FROM = "path"
GEOGRAPHIC_LOC = "geographic-region"
REFERENTIAL_SEM = "referential-sem"
TO_LOCATION = "to-loc"
FROM_LOCATION = "from-loc"
SOURCE_AS_LOC = "source-as-loc"

# --> Date/Time (highest ancestor to closest)
ABY_TIME = "any-time-object"
RELATIVE_TIME = "time-loc"  # Parent of today/tomorrow
TODAY = "today"
TOMORROW = "tomorrow"
EVENT_TIME_REL = "event_time_rel"
START_TIME = "start_time"

INTERVAL = "time-interval"
RELATIVE_DATE = "date_obj_in"
MONTH = "month"
WEEK = "week"
WEEK_OBJ = "week_object"    # Usually for cases like "they had a long week", but
                            # "this week" is caught with this one
DAY_STAGE = "day_stage" # Parent of "Morning", "Night", "Evening", ...
MONTH_NAME = "month_name"
AFTERNOON = "afternoon"
DAY_STAGE_PM = "day-stage-pm"
EVENING = "evening"
NIGHT = "night"


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