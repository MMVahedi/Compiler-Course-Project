from Grammer import *


class state:
    All_States = []
    number_of_all_states = 0

    def __init__(self, id, owner, type='middle'):
        self.id = id
        self.owner = owner
        self.type = type  # 'start' 'final' or 'middle'
        self.outgoing_edges = []  # id of outgoing edges

    @classmethod
    def get_state_by_id(cls, s_id):
        return cls.All_States[s_id]


def generate_diagram_for_given_non_terminal(non_terminal: Non_Terminal):
    for rule in non_terminal.rules:
        pass
    # TODO
