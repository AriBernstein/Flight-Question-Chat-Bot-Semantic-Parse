from enum import Enum
from typing import Type

from DataStructures.KnowledgeStructures.KnowledgeTypeBase import Knowledge
from DataStructures.KnowledgeStructures.DateTimeKnowledgeTypes import \
    DestinationDateKnowledge, DestinationTimeKnowledge, \
        OriginDateKnowledge, OriginTimeKnowledge
from DataStructures.KnowledgeStructures.LocationKnowledgeTypes import \
    DestinationAirportKnowledge, DestinationCityKnowledge, \
        DestinationStateKnowledge, OriginAirportKnowledge, \
            OriginCityKnowledge, OriginStateKnowledge      

class QueryTypes(Enum):
    airport = "airport"
    flight_one_way = "flight_one_way"
    flights_round_trip = "flight_round_trip"

# Orderings that correlate with knowledge hierarchies.
_QUESTION_HIERARCHY = \
    [QueryTypes.flights_round_trip, QueryTypes.flight_one_way, QueryTypes.airport]

_O_LOCATIONS_HIERARCHY = \
    [OriginStateKnowledge, OriginCityKnowledge, OriginAirportKnowledge]

_D_LOCATIONS_HIERARCHY = \
    [DestinationStateKnowledge, DestinationCityKnowledge,
     DestinationAirportKnowledge]

# Can be cases where the date is needed but time is not, never vice versa
_O_DATE_TIME_SET = [OriginDateKnowledge, OriginTimeKnowledge]
_D_DATE_TIME_SET = [DestinationDateKnowledge, DestinationTimeKnowledge]

class BaseQuery:
    def __init__(self, query_type:QueryTypes, 
                 unknown_data:list[list[Type[Knowledge]]]) -> None:
        self._query_type = query_type
        self._current_knowledge = unknown_data
    
    def query_type(self) -> QueryTypes:
        return self._query_type
    
    def get_all_data(self) -> list[list[Type[Knowledge]]]:
        return self._current_knowledge
    
    def get_unknown_data(self, get_known=False) -> list[list[Type[Knowledge]]]:
        ret = []
        for knowledge_type in self._current_knowledge:
            knowledge_type_sub_list = []
            for knowledge_piece in knowledge_type:
                if not (get_known or knowledge_piece.known()):
                    # not (A or B) = (not A) and (not B)
                    knowledge_type_sub_list.append(knowledge_piece)
                elif get_known and knowledge_piece.known():
                    knowledge_type_sub_list.append(knowledge_piece)
            ret.append(knowledge_type_sub_list)    
        return ret
    
    def get_known_data(self) -> list[list[Type[Knowledge]]]:
        return self.get_unknown_data(get_known=True)
    
class AirportsQuery(BaseQuery):
    def __init__(self) -> None:
        super().__init__(QueryTypes.airport, [_O_LOCATIONS_HIERARCHY])
        
class SingleFlightQuery(BaseQuery):
    def __init__(self) -> None:
        super().__init__(QueryTypes.flight_one_way,
                         [_O_LOCATIONS_HIERARCHY, _O_DATE_TIME_SET])

class RoundTripFlightQuery(BaseQuery):
    def __init__(self) -> None:
        super().__init__(QueryTypes.flights_round_trip, 
                         [_O_LOCATIONS_HIERARCHY, _O_DATE_TIME_SET,
                          _D_LOCATIONS_HIERARCHY, _D_DATE_TIME_SET])