# Simple Scheme Interpreter

A lightweight Scheme interpreter implemented in Python that supports basic Scheme functionality. This interpreter provides a REPL (Read-Eval-Print Loop) environment for executing Scheme expressions and includes support for fundamental Scheme features.

## Features

- Core Scheme data types:
  - Numbers (integers and floating-point)
  - Symbols
  - Lists
  - Functions (including lambda expressions)

- Special forms:
  - `quote`: Quote expressions without evaluation
  - `define`: Define variables and functions
  - `if`: Conditional expressions
  - `lambda`: Create anonymous functions

- Built-in procedures:
  - Arithmetic operations: `+`, `-`, `*`, `/`
  - Comparison operators: `=`, `<`, `>`, `<=`, `>=`
  - List operations: `cons`, `car`, `cdr`, `list`
  - Type predicates: `number?`, `symbol?`, `null?`

## Installation

1. Ensure you have Python 3.6 or later installed
2. Clone or download the interpreter file
3. No additional dependencies are required

## Usage

### Running the REPL

```bash
python scheme_interpreter.py
```

This will start an interactive REPL where you can enter Scheme expressions.

### Example Sessions

```scheme
scheme> (+ 1 2 3)
6

scheme> (define x 42)
scheme> x
42

scheme> (if (> x 0) 'positive 'negative)
positive

scheme> (define square (lambda (x) (* x x)))
scheme> (square 5)
25

scheme> (cons 1 (cons 2 (cons 3 '())))
[1, 2, 3]

scheme> (define factorial
         (lambda (n)
           (if (<= n 1)
               1
               (* n (factorial (- n 1))))))
scheme> (factorial 5)
120
```

### Using as a Library

You can also import the interpreter in your Python code:

```python
from scheme_interpreter import tokenize, parse, evaluate, Environment, create_global_env

# Create a global environment
env = create_global_env()

# Parse and evaluate Scheme expressions
tokens = tokenize("(+ 1 2 3)")
expr = parse(tokens)
result = evaluate(expr, env)
print(result)  # Output: 6
```

## Error Handling

The interpreter includes basic error handling for common Scheme errors:

```scheme
scheme> (+ 1 'a)
Error: Invalid expression

scheme> (undefined-symbol)
Error: Symbol not found: undefined-symbol

scheme> (
Error: Unexpected EOF
```

## Limitations

- No tail-call optimization
- Limited standard library compared to full Scheme implementations
- No support for complex numbers or exact arithmetic
- No macros or continuations
- Basic error reporting

## Implementation Details

The interpreter follows a traditional structure:

1. **Tokenizer**: Converts input strings into tokens
2. **Parser**: Converts tokens into a nested list structure
3. **Evaluator**: Evaluates the parsed expressions in an environment
4. **Environment**: Manages variable and function bindings

## Future Improvements

Potential areas for enhancement:

- Add support for `let`, `cond`, and other special forms
- Implement more standard library functions
- Add proper tail-call optimization
- Improve error messages and debugging features
- Add support for loading Scheme files
- Implement proper number tower (complex numbers, rationals)
- Add macro system

## Contributing

Feel free to contribute by:
1. Reporting bugs
2. Suggesting enhancements
3. Submitting pull requests
4. Improving documentation

## License

This project is open source and available under the MIT License.
