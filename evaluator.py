import ast


class Evaluator(object):
    def __init__(self):
        self.local_namespace = {}

    def evaluate(self, src):
        ast_module = ast.parse(src)
        final_statement = ast_module.body.pop()

        if self._is_evaluable_expression(final_statement):
            executable = compile(ast_module, '<ast>', mode='exec')
            exec(executable, globals(), self.local_namespace)
            evaluable = compile(ast.Expression(final_statement.value), '<ast>', mode='eval')
            return eval(evaluable, globals(), self.local_namespace)
        else:
            exec(src, globals(), self.local_namespace)

    def _is_evaluable_expression(self, statement):
        public_attributes = set(self._get_public_attributes(statement))
        return public_attributes == set(['col_offset', 'lineno', 'value'])

    def _get_public_attributes(self, variable):
        return [x for x in dir(variable) if not x.startswith('_')]

