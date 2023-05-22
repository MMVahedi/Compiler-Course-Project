from Grammer import Non_Terminal
from scanner import TokenTypes, Token


class state:
    All_States = {}

    def __init__(self, owner: Non_Terminal, type='middle'):
        self.owner = owner
        self.type = type  # 'start' 'final' or 'middle'
        self.outgoing_edges = []  # id of outgoing edges
        state.All_States[owner] = self

    def add_outgoing_edge(self, edge):
        self.outgoing_edges.append(edge)

    def get_next_state(self, token: Token):
        if token.token_type == TokenTypes.ID or token.token_type == TokenTypes.NUM:
            token_label = token.token_type
        else:
            token_label = token.value
        epsilon_edge = None
        error_edge = None
        for edge in self.outgoing_edges:
            if edge.label is Non_Terminal:
                non_terminal = edge.label
                if token_label in non_terminal.first:
                    return "Non_terminal", edge
            elif edge.label is str:
                if edge.label == token_label:
                    return "Terminal", edge.destination
            else:  # None = EPSILON
                epsilon_edge = edge
            error_edge = edge
        if epsilon_edge is not None:
            return "EPSILON", epsilon_edge.destination
        # If did not return, means we have error, so we should handle it.
        if self.type == 'start':
            if token_label not in self.owner.follow:
                return "Error", (1, token_label, error_edge)
            else:
                return "Error", (2, self.owner.name, error_edge)
        else:
            return "Error", (3, token_label, error_edge)


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
    non_terminal.start_state = start
    end = state(non_terminal.name, type='end')
    for rule in non_terminal.rules:
        current_state = start
        for i in range(len(rule.rhs)):
            token = rule.rhs[i]
            if i == len(rule.rhs) - 1:
                edge = Edge(token, current_state, end)
                current_state.add_outgoing_edge(edge)
            else:
                next = state(non_terminal.name)
                edge = Edge(token, current_state, next)
                current_state.add_outgoing_edge(edge)
                current_state = next
