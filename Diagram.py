from Grammer import Non_Terminal


class state:
    All_States = []
    number_of_all_states = 0

    def __init__(self, owner, type='middle'):
        self.id = id
        self.owner = owner
        self.type = type  # 'start' 'final' or 'middle'
        self.outgoing_edges = []  # id of outgoing edges
        state.All_States.append(self)

    @classmethod
    def get_state_by_id(cls, s_id):
        return cls.All_States[s_id]

    def add_outgoing_edge(self, edge):
        self.add_outgoing_edge(edge)


class Edge:
    def __init__(self, label, source: state, destination: state):
        self.label = label
        self.source = source
        self.destination = destination


def initializer(All_Non_Terminals):
    for non_terminal in All_Non_Terminals.values():
        generate_diagram_for_given_non_terminal(non_terminal)


def generate_diagram_for_given_non_terminal(non_terminal: Non_Terminal):
    start = state(non_terminal.name, type='start')
    non_terminal.start_state_id = start.id
    end = state(non_terminal.name, type='end')
    for rule in non_terminal.rules:
        current_state = start
        for i in range(len(rule)):
            token = rule[i]
            if i == len(rule) - 1:
                edge = Edge(token, current_state, end)
                current_state.add_outgoing_edge(edge)
            else:
                next = state(non_terminal.name)
                edge = Edge(token, current_state, next)
                current_state.add_outgoing_edge(edge)
                current_state = next