from datetime import date, time
from typing import Type
from DataStructures.KnowledgeStructures.KnowledgeTypeBase import Knowledge
from Utils.CustomExceptions import InvalidTypeException


class TimeKnowledge(Knowledge):
    def __init__(self, is_destination:bool=None) -> None:
        super().__init__(is_destination)
        
    def set_time(self, t:time) -> None:
        if not isinstance(t, time):
            raise InvalidTypeException(str(Type(t)), "time")
        self._value = t
    
    def time(self) -> time:
        return self._value
    
    def __str__(self) -> str:
        if self.known():
            t = self.time().strftime("%H:%M")
            return f"TimeKnowledge: {t}, {self.base_info_str()}"
        return "TimeKnowledge: Empty"
    
    def __repr__(self) -> str:
        return str(self)

class OriginTimeKnowledge(TimeKnowledge):
    def __init__(self) -> None:
        super().__init__(is_destination=False)
    def __str__(self) -> str:
        return "Origin" + super().__str__()
    
class DestinationTimeKnowledge(TimeKnowledge):
    def __init__(self) -> None:
        super().__init__(is_destination=False)
    def __str__(self) -> str:
        return "Destination" + super().__str__()
    
    
class DateKnowledge(Knowledge):
    def __init__(self, is_destination:bool=None) -> None:
        self._date = None   # type: time
        super().__init__(is_destination)
        
    def set_date(self, d:date) -> None:
        if not isinstance(d, date):
            raise InvalidTypeException(str(Type(date)), "date")        
        self._date = d
    
    def date(self) -> date:
        return self._date
    
    def __str__(self) -> str:
        if self._date:
            t = self._date.strftime("%b %d %Y")
            return f"TimeKnowledge: {t}, {self.base_info_str()}"
        return "TimeKnowledge: Empty"
    
    def __repr__(self) -> str:
        return str(self)

class OriginDateKnowledge(DateKnowledge):
    def __init__(self) -> None:
        super().__init__(is_destination=False)
    def __str__(self) -> str:
        return "Origin" + super().__str__()
    
class DestinationDateKnowledge(DateKnowledge):
    def __init__(self) -> None:
        super().__init__(is_destination=False)
    def __str__(self) -> str:
        return "Destination" + super().__str__()