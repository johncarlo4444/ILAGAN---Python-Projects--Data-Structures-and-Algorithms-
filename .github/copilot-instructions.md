# Student Persona & Constraints
- I am a 2nd Year Computer Engineering student learning Python fundamentals [9, 10].
- My code must strictly adhere to the concepts, syntax, and libraries I have learned so far. 
- Do NOT generate advanced, professional-grade code, complex library imports, or syntax outside of my specified toolkit. If a task requires logic I haven't learned, solve it using simple conditional structures instead.

## 1. Permitted Variable Naming Conventions
Always use the variable styles demonstrated in my lessons:
- **PascalCase** for custom user inputs and specific semantic variables (e.g., `FirstName`, `LastName`, `FullName`, `EnterAge`, `ConsumedUnits`, `FirstComplex`) [1, 3, 6, 11].
- **Simple lowercase** for single-letter algebra variables, array structures, and basic menu navigation (e.g., `a`, `b`, `x`, `y`, `students`, `choice`) [4, 7, 12].

## 2. Permitted Python Constructs
Only use the following language features:
- **Console I/O**: `print()` for console outputs and `input()` to capture inputs [2, 13].
- **Triple Quotes**: Use `"""` multi-line strings specifically for trivia text, game screens, or presenting menu choices [7, 14].
- **Conditional logic**: Standard `if`, `elif`, and `else` blocks [7, 13].
- **Logical & Relational Operators**: Use `and`, `or`, `==`, `>=`, `<=`, and `!=` [3, 15].
- **Basic Data Types**: Integers (`int`), Floats (`float`), Strings (`str`), and Complex Numbers using `complex(real, imag)` [4-6, 12].
- **Type Conversions**: `int()`, `float()`, `str()`, and `complex()` [5, 6, 12, 16].
- **List Operations**: Declaring static lists, accessing items via standard indexing (`list`) and reverse indexing (`list[-1]`), appending (`.append()`), removing (`.remove()`), finding indices (`.index()`), checking item existence (`if item in list`), and getting the length (`len()`) [7, 8, 17].

## 3. Permitted String Operations
Only manipulate strings using these exact methods:
- String concatenation with `+` [1, 11].
- Formatting with standard f-strings [8, 18, 19].
- Case transformation using `.upper()` and `.lower()` [1, 18].
- Blank-space stripping via `.replace(" ", "")` [1, 16].
- Character-length calculation using `str(len(...))` [1, 16].
- String slicing with indexes and steps (e.g., `str[:3]`, `str[1:]`, `str[::2]`) [1, 19].

## 4. Arithmetic & Error Handling
- Use basic operations: Addition (`+`), subtraction (`-`), multiplication (`*`), standard float division (`/`), integer floor division (`//`), modulo (`%`), and exponentiation (`**`) [4, 5].
- Format float output using f-string precision (e.g., `f"{value:.2f}"`) or the `round(value, decimals)` function [5, 20, 21].
- **No Try-Except Blocks**: Do not use `try` / `except` for handling errors. Check mathematically using standard conditionals (e.g., use `if Second == 0:` to prevent dividing by zero) [22].

## 5. Strict Prohibitions (Do NOT Use)
If my query asks for a script, do NOT write any of the following (as they are beyond my current lesson plan):
- **NO Loops**: Do not write `for` or `while` loops. Keep code linear, or use static branching options if a choice menu is needed [7].
- **NO Functions**: Do not define custom functions using `def`. Write all logic in the global scope of the script [1, 2, 13].
- **NO Advanced Structures**: Do not use dictionaries (`{}`), sets, classes, or lambda statements.
- **NO External Libraries**: Do not import `math`, `sys`, `os`, or other system libraries. Keep the code pure, vanilla Python [1, 2, 13].
