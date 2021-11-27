def evaluateExpression(expression):
    """
    Evaluates a mathematical expression.
    expression: string containing a mathematical expression
    returns: value of the expression
    """
    for e in expression:
        if e not in '+-*/':
            return 'Invalid expression'
        else: