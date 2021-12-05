from DataStructures.FlightLocations.Locations import USState, City, Airport
from DataStructures.KnowledgeStructures.LocationKnowledgeTypes import \
    OriginStateKnowledge, DestinationStateKnowledge, \
        OriginCityKnowledge, DestinationCityKnowledge, \
            OriginAirportKnowledge, DestinationAirportKnowledge
            

# Define orderings that correlate with knowledge hierarchies, integers
# representing pointers to them. These integers increase with the level of
# information we are looking for, which is itself trimmed in reverse order of
# information needed.
