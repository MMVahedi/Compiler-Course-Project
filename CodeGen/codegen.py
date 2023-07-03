from .instructions import *
from .semantic_Routines import SemanticRoutines
from .symbol import SymbolTable
from .runtime_stack import RuntimeStack
from .register_file import RegisterFile
from Scanner.scanner import Token

WORD_SIZE = 4

class CodeGen:
    def __init__(self):
        self.i = 0
        self.data_address = 100000
        self.temp_address = 500004
        self.stack_start_address = 500000
        self.semantic_stack = []
        self.data_and_temp_stack = []


        self.function_data_start_pointer = 0
        self.function_temp_start_pointer = 0

        self.program = []

        self.symbol_table = SymbolTable(self)
        self.register_file = RegisterFile(self)
        self.runtime_stack = RuntimeStack(self, self.register_file)
        self.routines = SemanticRoutines(self, self.symbol_table)

        initialization_instructions = [
            Assign(f"#{self.stack_start_address}", self.register_file.stack_pointer_register_address),
            Assign("#0", self.register_file.return_address_register_address),
            Assign("#0", self.register_file.return_value_register_address),
        ]

        self.push_instructions(initialization_instructions)

        self.jump_to_main_address = len(self.program)
        self.program.append(None)
        self.i += 1

        self.add_output_function()

    def act(self, action, previous_token, current_token):
        action = action[1:]
        if action == 'pid':
            self.routines.pid(previous_token, current_token)
        elif action == 'pnum':
            self.routines.pnum(previous_token)
        elif action == 'label':
            self.routines.label()
        elif action == 'save':
            self.routines.save()
        elif action == 'pushOperation':
            self.routines.push_operation(previous_token)
        elif action == 'execute':
            self.routines.execute()
        elif action == 'startArgumentList':
            self.routines.start_argument_list()
        elif action == 'endArgumentList':
            self.routines.end_argument_list()
        elif action == 'jpfFromSaved':
            self.routines.jpf_from_saved()
        elif action == 'jpFromSaved':
            self.routines.jp_from_saved()
        elif action == 'saveAndJpfFromLastSave':
            self.routines.save_and_jpf_from_last_save()
        elif action == 'assign':
            self.routines.assign()
        elif action == 'startNoPush':
            self.routines.start_no_push()
        elif action == 'endNoPush':
            self.routines.end_no_push()
        elif action == 'declareArray':
            self.routines.declare_array()
        elif action == 'array':
            self.routines.array()
        elif action == 'until':
            self.routines.until()
        elif action == 'handleBreaks':
            self.routines.handle_breaks()
        elif action == 'break':
            self.routines.add_break()
        elif action == 'pop':
            self.routines.pop()
        elif action == 'checkDeclaration':
            self.routines.check_declaration()
        elif action == 'uncheckDeclaration':
            self.routines.uncheck_declaration()
        elif action == 'declareFunction':
            self.routines.declare_function()
        elif action == 'openScope':
            self.routines.open_scope()
        elif action == 'closeScope':
            self.routines.close_scope()
        elif action == 'setFunctionScopeFlag':
            self.routines.set_function_scope_flag()
        elif action == 'popParam':
            self.routines.pop_param(previous_token)
        elif action == 'call':
            self.routines.call()
        elif action == 'setReturnValue':
            self.routines.set_return_value()
        elif action == 'jumpBack':
            self.routines.jump_back()
        elif action == 'addArgumentCount':
            self.routines.add_argument_count()
        elif action == 'zeroInitialize':
            self.routines.zero_initialize()
        elif action == 'arrayParam':
            self.routines.array_param()
        elif action == 'startBreakScope':
            self.routines.start_break_scope()
        elif action == 'setForceDeclarationFlag':
            self.routines.set_force_declaration_flag()
        elif action == 'unsetForceDeclarationFlag':
            self.routines.unset_force_declaration_flag()
        elif action == 'voidCheck':
            self.routines.void_check()
        elif action == 'voidCheckThrow':
            self.routines.void_check_throw()
        elif action == 'saveType':
            self.routines.save_type(previous_token)
        elif action == 'checkType':
            self.routines.check_type(current_token)
        elif action == 'startRHS':
            self.routines.start_rhs()
        elif action == 'endRHS':
            self.routines.end_rhs()
        else:
            print('Invalid Action Symbol!')

    def check_program_size(self, size=None):
        if not size:
            size = self.i
        if type(size) == str:
            if size[0] == "#":
                size = size[1:]
            size = int(size)
        while len(self.program) <= size:
            self.program.append(None)

    def push_instruction(self, instruction):
        self.check_program_size()
        self.program[self.i] = instruction.to_code()
        self.i += 1

    def save_space(self):
        self.i += 1

    def insert_instruction(self, instruction, destination):
        if type(destination) == str:
            if destination[0] == "#":
                destination = destination[1:]
            destination = int(destination)
        self.check_program_size(destination)
        self.program[destination] = instruction.to_code()

    def push_instructions(self, instructions):
        for instruction in instructions:
            self.push_instruction(instruction)

    def get_next_data_address(self, size=WORD_SIZE):
        address = self.data_address
        self.data_address += size
        return address

    def get_next_temp_address(self, size=WORD_SIZE):
        address = self.temp_address
        self.temp_address += size
        return address

    def add_output_function(self):
        self.act('#pid', Token(lexeme='output'), None)
        self.act('#declareFunction', None, None)
        self.act('#openScope', None, None)
        self.act('#setFunctionScopeFlag', None, None)
        self.act('#pid', Token(lexeme="a"), None)
        self.act('#popParam', None, None)
        self.act('#pid', Token(lexeme="a"), None)
        self.act('#openScope', None, None)
        self.push_instruction(
            Print(self.semantic_stack.pop()))
        self.act('#closeScope', None, None)
        self.act('#jumpBack', None, None)
