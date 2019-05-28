#!/usr/bin/python
import ast
import sys

def top_level_functions(body):
    return (f for f in body if isinstance(f, ast.FunctionDef))

def parse_ast(filename):
    with open(filename, "rt") as file:
        return ast.parse(file.read(), filename=filename)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print ("usage: "+sys.argv[0]+" 'python module to inspect'")
        print ("default is inspecting itself")
        sys.argv.append(sys.argv[0])

    for filename in sys.argv[1:]:
        print(filename)
        tree = parse_ast(filename)
        for func in top_level_functions(tree.body):
            print("  %s" % func.name)
