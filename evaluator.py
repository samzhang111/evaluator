import ast


class Evaluator(object):
    def __init__(self):
        self.local_namespace = {}

    def evaluate(self, src):
        ast_module = ast.parse(src)
        final_statement = ast_module.body.pop()

        if self._is_expression_statement(final_statement):
            executable = compile(ast_module, '<ast>', mode='exec')
            exec(executable, globals(), self.local_namespace)
            evaluable = compile(ast.Expression(final_statement.value), '<ast>', mode='eval')
            return eval(evaluable, globals(), self.local_namespace)
        else:
            exec(src, globals(), self.local_namespace)

    def _is_expression_statement(self, statement):
        return isinstance(statement, ast.Expr)

