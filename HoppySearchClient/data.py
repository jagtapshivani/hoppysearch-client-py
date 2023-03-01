import json
class Data:
    def __init__(self, name, no_of_children, no_of_children_original, notes, type):
        self.name = name,
        self.no_of_children = no_of_children,
        self.no_of_children_original = no_of_children_original,
        self.notes = notes,
        self.type = type
        # dict.__init__(self, name=name, no_of_children=no_of_children, no_of_children_original=no_of_children_original, notes=notes, type=type)
    
    def __iter__(self):
        yield from {
            "name": self.name,
            "no_of_children": self.no_of_children,
            "no_of_children_original": self.no_of_children_original,
            "notes": self.notes,
            "type": self.type
        }.items()

    def __str__(self):
        return json.dumps(dict(self), ensure_ascii=False)

    def __repr__(self):
        return self.__str__()

    def to_json(self):
        return self.__str__()
    
    @staticmethod
    def from_json(dct):
        list = []
        for json_dct in dct:
            list.append(Data(json_dct['name'], json_dct['no_of_children'], json_dct['no_of_children_original'],
                    json_dct['notes'], json_dct['type']))
        return list