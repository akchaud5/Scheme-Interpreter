# Programming Language Interpreter

A robust programming language interpreter implemented in Python that includes lexical analysis, parsing, and execution capabilities. This interpreter implements a C-style syntax with static scoping and imperative programming features.

## Features

### Language Features
- Variables and assignment
- Control flow statements (if, while)
- Block scoping
- Basic arithmetic and logical operations
- String and numeric literals
- Print statements
- Comments (single-line)

### Implementation Features
- Lexical scanner with comprehensive token recognition
- Recursive descent parser
- Abstract Syntax Tree (AST) generation
- Clear error reporting with line numbers

## Language Syntax

### Variables
```javascript
var x = 10;
var message = "Hello, World!";
```

### Control Flow
```javascript
if (x > 5) {
    print "x is greater than 5";
} else {
    print "x is less than or equal to 5";
}

while (x > 0) {
    print x;
    x = x - 1;
}
```

### Expressions
```javascript
var a = 5 + 3 * 2;
var b = (5 + 3) * 2;
var c = "Hello" + " " + "World";
var isTrue = !false && true;
```

### Blocks and Scope
```javascript
{
    var x = 10;
    {
        var y = 20;
        print x + y;
    }
}
```

## Installation

1. Ensure you have Python 3.8 or later installed
2. Clone the repository or download the interpreter files
3. No additional dependencies are required

## Usage

### Running Programs

```bash
python interpreter.py your_program.txt
```

### Interactive Mode
```bash
python interpreter.py
```

### Using as a Library

```python
from interpreter import Scanner, Parser, Interpreter

# Create scanner
source = "var x = 10; print x;"
scanner = Scanner(source)
tokens = scanner.scan_tokens()

# Parse tokens
parser = Parser(tokens)
statements = parser.parse()

# Execute
interpreter = Interpreter()
interpreter.interpret(statements)
```

## Error Handling

The interpreter provides detailed error messages for:
- Syntax errors
- Runtime errors
- Type errors
- Undefined variables
- Invalid operations

Example error messages:
```
[line 5] Error: Undefined variable 'foo'
[line 7] Error: Expected ';' after expression
[line 10] Error: Cannot add number to string
```

## Implementation Details

### Scanner (Lexical Analysis)
- Handles single and multi-character tokens
- Recognizes keywords and identifiers
- Processes string and number literals
- Tracks line numbers for error reporting

### Parser
- Implements recursive descent parsing
- Builds Abstract Syntax Tree (AST)
- Handles operator precedence
- Provides error recovery through synchronization

### AST Nodes
- Expression nodes (Binary, Unary, Literal, etc.)
- Statement nodes (Print, Var, Block, If, While)
- Clear separation between expressions and statements

## Advanced Usage

### Error Recovery
The interpreter includes error recovery mechanisms to continue parsing after encountering errors:

```javascript
// Even with a syntax error here
var x = ;

// The interpreter can continue with valid code
var y = 10;
print y;
```

### Extending the Language
To add new features, you can:
1. Add new token types in `TokenType`
2. Create new AST node classes
3. Implement corresponding parser methods
4. Add interpretation logic

## Limitations

- No functions or procedures yet
- Limited built-in functions
- No module system
- Single-threaded execution
- No type system or type checking
- No garbage collection (relies on Python's GC)

## Future Improvements

Planned enhancements:
- Function declarations and calls
- For loops
- Break and continue statements
- Arrays and dictionaries
- Standard library
- Type checking
- Better error recovery
- Performance optimizations
- REPL improvements

## Contributing

Contributions are welcome! Some areas that need work:
1. Additional language features
2. Better error messages
3. Performance improvements
4. Documentation improvements
5. Test cases
6. Standard library implementation

## Testing

To run the test suite:
```bash
python -m unittest tests/
```

## License

This project is available under the MIT License.

## Acknowledgments

This interpreter design is inspired by various programming language implementations and compiler theory texts.
