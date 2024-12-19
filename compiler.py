from typing import Any, Dict, List, Union
import math
import operator as op

class SchemeError(Exception):
    pass

def tokenize(code: str) -> List[str]:
    """Convert a string into a list of tokens."""
    code = code.replace('(', ' ( ').replace(')', ' ) ')
    return code.split()

def parse(tokens: List[str]) -> Any:
    """Convert tokens into a nested list structure."""
    if not tokens:
        raise SchemeError("Unexpected EOF")
    
    token = tokens.pop(0)
    
    if token == '(':
        nested_list = []
        while tokens and tokens[0] != ')':
            nested_list.append(parse(tokens))
        
        if not tokens:
            raise SchemeError("Missing closing parenthesis")
        
        tokens.pop(0)  # Remove ')'
        return nested_list
    elif token == ')':
        raise SchemeError("Unexpected closing parenthesis")
    else:
        # Convert numbers and handle other atoms
        try:
            return int(token)
        except ValueError:
            try:
                return float(token)
            except ValueError:
                return token

class Environment:
    """Environment to store variable and function bindings."""
    def __init__(self, parent=None):
        self.bindings: Dict[str, Any] = {}
        self.parent = parent
    
    def lookup(self, symbol: str) -> Any:
        if symbol in self.bindings:
            return self.bindings[symbol]
        elif self.parent:
            return self.parent.lookup(symbol)
        raise SchemeError(f"Symbol not found: {symbol}")
    
    def define(self, symbol: str, value: Any) -> None:
        self.bindings[symbol] = value

def create_global_env() -> Environment:
    """Create the global environment with basic Scheme procedures."""
    env = Environment()
    
    # Basic arithmetic operations
    env.define('+', lambda *args: sum(args))
    env.define('-', lambda x, *args: x - sum(args) if args else -x)
    env.define('*', lambda *args: math.prod(args))
    env.define('/', lambda x, *args: x / math.prod(args) if args else 1/x)
    
    # Comparison operations
    env.define('=', op.eq)
    env.define('<', op.lt)
    env.define('>', op.gt)
    env.define('<=', op.le)
    env.define('>=', op.ge)
    
    # List operations
    env.define('cons', lambda x, y: [x] + (y if isinstance(y, list) else [y]))
    env.define('car', lambda x: x[0])
    env.define('cdr', lambda x: x[1:])
    env.define('list', lambda *args: list(args))
    
    # Type predicates
    env.define('number?', lambda x: isinstance(x, (int, float)))
    env.define('symbol?', lambda x: isinstance(x, str))
    env.define('null?', lambda x: x == [])
    
    return env

def evaluate(expr: Any, env: Environment) -> Any:
    """Evaluate a Scheme expression in the given environment."""
    # Self-evaluating expressions
    if isinstance(expr, (int, float)):
        return expr
    
    # Symbol lookup
    if isinstance(expr, str):
        return env.lookup(expr)
    
    # Empty list
    if expr == []:
        return []
    
    # Special forms
    if not isinstance(expr, list):
        raise SchemeError(f"Invalid expression: {expr}")
    
    op, *args = expr
    
    if op == 'quote':
        if len(args) != 1:
            raise SchemeError("quote requires exactly one argument")
        return args[0]
    
    elif op == 'define':
        if len(args) != 2:
            raise SchemeError("define requires exactly two arguments")
        symbol, value = args
        if not isinstance(symbol, str):
            raise SchemeError("define requires a symbol as first argument")
        env.define(symbol, evaluate(value, env))
        return None
    
    elif op == 'if':
        if len(args) not in (2, 3):
            raise SchemeError("if requires two or three arguments")
        condition = evaluate(args[0], env)
        if condition:
            return evaluate(args[1], env)
        elif len(args) == 3:
            return evaluate(args[2], env)
        return None
    
    elif op == 'lambda':
        if len(args) < 2:
            raise SchemeError("lambda requires at least two arguments")
        params, *body = args
        if not all(isinstance(p, str) for p in params):
            raise SchemeError("lambda parameters must be symbols")
        
        def lambda_proc(*args):
            if len(args) != len(params):
                raise SchemeError(f"Expected {len(params)} arguments, got {len(args)}")
            new_env = Environment(env)
            for param, arg in zip(params, args):
                new_env.define(param, arg)
            result = None
            for expr in body:
                result = evaluate(expr, new_env)
            return result
        
        return lambda_proc
    
    # Function application
    else:
        proc = evaluate(op, env)
        evaluated_args = [evaluate(arg, env) for arg in args]
        return proc(*evaluated_args)

def repl() -> None:
    """Start a Read-Eval-Print Loop."""
    env = create_global_env()
    while True:
        try:
            code = input("scheme> ")
            if code.lower() in ('exit', 'quit'):
                break
            
            tokens = tokenize(code)
            if not tokens:
                continue
                
            expr = parse(tokens)
            result = evaluate(expr, env)
            if result is not None:
                print(result)
        except SchemeError as e:
            print("Error:", str(e))
        except (KeyboardInterrupt, EOFError):
            break
        except Exception as e:
            print("Internal error:", str(e))

if __name__ == "__main__":
    print("Simple Scheme Interpreter")
    print("Enter 'exit' or 'quit' to exit")
    repl()
