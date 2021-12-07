from sys import maxsize


class Group:

    def __init__(self, group_name=None, group_header=None, group_footer=None, group_id=None):
        self.group_name = group_name
        self.group_header = group_header
        self.group_footer = group_footer
        self.id = group_id

    def __repr__(self):
        return "{0}: {1}; Header: {2}, Footer: {3}".format(self.id, self.group_name, self.group_header, self.group_footer)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.group_name == other.group_name

    def id_or_max(self):  # функция для определения, есть ли у группы идентификатор
        if self.id:
            return int(self.id)
        else:
            return maxsize
