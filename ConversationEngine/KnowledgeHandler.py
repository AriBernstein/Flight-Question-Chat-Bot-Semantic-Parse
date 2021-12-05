from DataStructures.QueryTypes import QueryTypes, AirportsQuery, \
    SingleFlightQuery, RoundTripFlightQuery

class KnowledgeHandler:    
    
    def __init__(self) -> None:
        self._o_loc_pointer = self._d_loc_pointer = \
            self._o_date_time_pointer = self._d_date_time_pointer = 0
    
    