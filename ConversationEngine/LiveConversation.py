from Utils.CustomExceptions import ExpectingRelativeException
from Utils.Utils import StaticClass
from ConversationEngine.ConversationalText import *

class LiveConversation(StaticClass):    
    
    def either_any(list_len:int) -> str:
        if list_len < 2: raise ExpectingRelativeException(list_len, 2, 5)
        return "either" if list_len == 2 else "any"
    
    def ask_and_return(msg:str) -> str:
        return str(input(msg + '\n'))
    
    def initialize(self) -> str:
        return self.ask_and_return(INITIAL_OPENING)
    
    def re_initialize(self) -> str:
        return self.ask_and_return(RE_OPENING)
            
    def conclude() -> str:
        return CONCLUSION
    
    