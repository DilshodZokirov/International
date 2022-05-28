class GroupDTO:
    def __init__(self, unique_id: str = None, name: str = None, created_by: str = None):
        self.id = unique_id
        self.name = name
        self.created_by = created_by

class ListeningDto:
    def __init__(self, unique_id: str = None,
                 listening_id: str = None,
                 name: str = None,
                 created_by : str = None ,
                 content_type : str = None) -> None:
        self.unique_id = unique_id
        self.listening_id = listening_id
        self.name = name
        self.created_by = created_by
        self.content_type= content_type

class MaterialDto:
    def __init__(self, unique_id: str = None,
                 name: str = None,
                 material: str = None,
                 created_by : str = None ,
                 content_type : str = None) -> None:
        self.unique_id = unique_id
        self.material = material
        self.name = name
        self.created_by = created_by
        self.content_type= content_type
