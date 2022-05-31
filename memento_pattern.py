import logging
# Used for Undo Command 


class EditorState:
    __content = None

    def __init__(self,content) -> None:
        self.__content = content
    
    def getContent(self) -> str:
        return self.__content



class History:
    __states = []

    def addToHistory(self,state:EditorState):
        self.__push(state=state)

    def removeFromHistory(self):
        self.__pop()

    def __push(self,state:EditorState):
        self.__states.append(state)

    def __pop(self)-> EditorState:
        return self.__states.pop()
    

class Editor:
    
    __content = None

    def __init__(self,content) -> None:
        self.__content = content

    def getContent(self):
        return self.__content

    def __create_state(self) -> EditorState:
        logging.info('Creating State')
        return EditorState(self.__content)


    def __restore(self,state:EditorState):
        logging.info('Restoring the state')
        self.__content = state.getContent()

    
