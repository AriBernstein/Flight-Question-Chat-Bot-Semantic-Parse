
class Knowledge:
    def __init__(self) -> None:
        self._relevant = True
        self._known = False
        
    def relevant(self) -> bool:
        return self._relevant
    
    def known(self) -> bool:
        return self._known
    
    def make_known(self) -> None:
        self._known = True
    
    
class StateKnowledge(Knowledge):
    def __init__(self) -> None:
        super().__init__()
        self._state = None
        
    # def set_state(state_str) -> bool:
        