from Parser.CMinusParser import Parser
from Scanner.scanner import Scanner
from CodeGen.codegen import CodeGen



def run(mode):
    if mode == 0:
        scanner = Scanner('input.txt')
        codegen = CodeGen()
        parser = Parser(scanner, codegen)
        parser.parse()
        parse_tree = parser.get_parse_tree()
        semantic_errors = parser.semantic_errors
        if len(semantic_errors) == 0:
            result_program = ""
            for lineno, line in enumerate(parser.code_generator.program):
                result_program += f"{lineno}\t{line}"
                result_program += "\n"
            semantic_errors = ["The input program is semantically correct."]
        else:
            result_program = "The output code has not been generated."
        with open('parse_tree.txt', 'w', encoding="utf-8") as f:
            f.write(parse_tree)
        with open("output.txt", "w", encoding="utf-8") as f:
            print(result_program, file=f)
        with open("semantic_errors.txt", "w", encoding="utf-8") as f:
            print("\n".join(semantic_errors), file=f)
    else:
        for i in range(1,mode+1):
            print(i)
            scanner = Scanner('input'+str(i)+'.txt')
            codegen = CodeGen()
            parser = Parser(scanner, codegen)
            parser.parse()
            parse_tree = parser.get_parse_tree()
            semantic_errors = parser.semantic_errors
            if len(semantic_errors) == 0:
                result_program = ""
                for lineno, line in enumerate(parser.code_generator.program):
                    result_program += f"{lineno}\t{line}"
                    result_program += "\n"
                semantic_errors = ["The input program is semantically correct."]
            else:
                result_program = "The output code has not been generated."
            with open('parse_tree'+str(i)+'.txt', 'w', encoding="utf-8") as f:
                f.write(parse_tree)
            with open("output"+str(i)+".txt", "w", encoding="utf-8") as f:
                print(result_program, file=f)
            with open("semantic_errors"+str(i)+".txt", "w", encoding="utf-8") as f:
                print("\n".join(semantic_errors), file=f)

run(0)