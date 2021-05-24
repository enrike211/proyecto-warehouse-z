class Products:
    def __init__(self,id:int,name:str):
        self.__id:int=id
        self.__name:str=name

    def get_id() -> int:
        return self.__id

    def get_name() -> str:
        return self.__name

    def set_name(name:str) -> None:
        self.__name=name