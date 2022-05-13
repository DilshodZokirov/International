class GroupDTO:
    def __init__(self, unique_id: str = None, name: str = None, created_by: str = None):
        self.id = unique_id
        self.name = name
        self.created_by = created_by
