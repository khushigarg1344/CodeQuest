
PYTHON_FOUNDATIONS = {
    "python-introduction": {
        "id": "python-introduction",
        "title": "Introduction to Python",
        "duration": "25 min",

        "content": """
# 1. What is Python?

Python is a high-level, general-purpose programming language.
It is known for readable syntax and a large ecosystem of libraries.

Python is widely used in:
- Backend development
- Artificial Intelligence and Machine Learning
- Data Science
- Automation and scripting
- Web development
- Data analysis

## 2. Important Features

1. Easy to read: Python uses simple and readable syntax.
2. Interpreted: Python code is executed by the Python interpreter.
3. Dynamically typed: You do not need to declare a variable's type explicitly.
4. Object-oriented: Python supports classes and objects.
5. Cross-platform: Python programs can run on different operating systems.
6. Large standard library: Python provides many built-in modules.

## 3. How Python Executes Code

A simplified view:

1. You write source code in a .py file.
2. Python compiles the source into bytecode.
3. The Python Virtual Machine executes that bytecode.

## 4. Python vs Java vs C++

Python is dynamically typed and generally uses indentation to define blocks.

Java is statically typed and runs on the Java Virtual Machine.

C++ is statically typed and is commonly compiled into native machine code.

## 5. Basic Python Program

print("Hello, World!")

The print() function displays information on the screen.
""",

        "key_concepts": [
            "High-level programming language",
            "Dynamically typed language",
            "Interpreted execution model",
            "Python Virtual Machine",
            "Cross-platform programming"
        ],

        "examples": {
            "python": {
                "code": "print('Hello, World!')\nprint('Welcome to CodeQuest')",
                "output": "Hello, World!\nWelcome to CodeQuest"
            },
            "java": {
                "code": "public class Main {\n    public static void main(String[] args) {\n        System.out.println(\"Hello, World!\");\n        System.out.println(\"Welcome to CodeQuest\");\n    }\n}",
                "output": "Hello, World!\nWelcome to CodeQuest"
            },
            "cpp": {
                "code": "#include <iostream>\nusing namespace std;\n\nint main() {\n    cout << \"Hello, World!\" << endl;\n    cout << \"Welcome to CodeQuest\" << endl;\n    return 0;\n}",
                "output": "Hello, World!\nWelcome to CodeQuest"
            }
        },

        "dry_run": """
Python:
print("Hello, World!")

Step 1: Python encounters the print() function.
Step 2: It evaluates the string "Hello, World!".
Step 3: It displays the string.

Final output:
Hello, World!
""",

        "practice_questions": [
            {
                "level": "Beginner",
                "question": "Write a program to print your name and your college name on separate lines.",
                "sample_input": "No input required",
                "sample_output": "Khushi\nYour College",
                "solutions": {
                    "python": "print('Khushi')\nprint('Your College')",
                    "java": "public class Main {\n    public static void main(String[] args) {\n        System.out.println(\"Khushi\");\n        System.out.println(\"Your College\");\n    }\n}",
                    "cpp": "#include <iostream>\nusing namespace std;\n\nint main() {\n    cout << \"Khushi\" << endl;\n    cout << \"Your College\" << endl;\n    return 0;\n}"
                },
                "explanation": "Each print statement displays its value on a separate line."
            },
            {
                "level": "Beginner",
                "question": "Write a program to print the sum of 25 and 35.",
                "sample_input": "No input required",
                "sample_output": "60",
                "solutions": {
                    "python": "a = 25\nb = 35\nprint(a + b)",
                    "java": "public class Main {\n    public static void main(String[] args) {\n        int a = 25;\n        int b = 35;\n        System.out.println(a + b);\n    }\n}",
                    "cpp": "#include <iostream>\nusing namespace std;\n\nint main() {\n    int a = 25, b = 35;\n    cout << a + b << endl;\n    return 0;\n}"
                },
                "explanation": "The addition operator + adds the two integer values."
            }
        ],

        "interview_questions": [
            {
                "question": "What is Python?",
                "answer": "Python is a high-level, general-purpose programming language known for its readable syntax and extensive libraries."
            },
            {
                "question": "Is Python compiled or interpreted?",
                "answer": "Python commonly compiles source code into bytecode, which is then executed by the Python Virtual Machine. It is generally described as an interpreted language."
            },
            {
                "question": "What is the difference between Python and Java?",
                "answer": "Python is dynamically typed and has concise syntax. Java is statically typed and requires explicit type declarations in most variable definitions."
            }
        ],

        "mcqs": [
            {
                "question": "Which of the following describes Python's typing system?",
                "options": [
                    "Statically typed",
                    "Dynamically typed",
                    "Only strongly typed",
                    "No type system"
                ],
                "answer": "Dynamically typed",
                "explanation": "Python determines variable types at runtime; explicit type declarations are generally not required."
            },
            {
                "question": "Which function displays output in Python?",
                "options": ["input()", "print()", "displayText()", "show()"],
                "answer": "print()",
                "explanation": "The print() function writes values to standard output."
            }
        ]
    },

    "python-variables": {
        "id": "python-variables",
        "title": "Variables and Data Types",
        "duration": "30 min",

        "content": """
# 1. What is a Variable?

A variable is a name that refers to an object or value in a program.

Example:
age = 21

Here:
- age is the variable name.
- 21 is the integer value.
- Python determines the type automatically.

## 2. Rules for Naming Variables

- A variable name can contain letters, digits and underscores.
- It cannot begin with a digit.
- It cannot contain spaces.
- Python keywords cannot be used as variable names.
- Variable names are case-sensitive.

Valid:
student_name = "Aman"
age2 = 21
_total = 500

Invalid:
2age = 21
student name = "Aman"

## 3. Python Data Types

### Numeric types
- int: Whole numbers, such as 10 and -5.
- float: Decimal numbers, such as 3.14.
- complex: Complex numbers, such as 2 + 3j.

### Text type
- str: Text values, such as "Python".

### Boolean type
- bool: True or False.

### Collection types
- list: Ordered, mutable collection.
- tuple: Ordered, immutable collection.
- set: Collection of unique elements.
- dict: Key-value mapping.

### None type
- None represents the absence of a value.

## 4. Checking Data Types

Use type():

x = 10
print(type(x))

Output:
<class 'int'>

## 5. Type Conversion

Converting one type into another is called type conversion.

Examples:
int("25") converts a string to an integer.
float("3.5") converts a string to a float.
str(100) converts an integer to a string.

Some conversions can fail:
int("hello") raises a ValueError.

## 6. Dynamic Typing

Python allows a variable name to refer to values of different types at different times.

x = 10
x = "Hello"

The second assignment makes x refer to a string instead of an integer.
""",

        "key_concepts": [
            "Variable",
            "Dynamic typing",
            "int, float and complex",
            "str and bool",
            "list, tuple, set and dict",
            "None",
            "type()",
            "Type conversion"
        ],

        "examples": {
            "python": {
                "code": "name = 'Aman'\nage = 21\npercentage = 89.5\nis_placed = False\n\nprint(name)\nprint(type(age))\nprint(type(percentage))\nprint(type(is_placed))",
                "output": "Aman\n<class 'int'>\n<class 'float'>\n<class 'bool'>"
            },
            "java": {
                "code": "public class Main {\n    public static void main(String[] args) {\n        String name = \"Aman\";\n        int age = 21;\n        double percentage = 89.5;\n        boolean isPlaced = false;\n\n        System.out.println(name);\n        System.out.println(age);\n        System.out.println(percentage);\n        System.out.println(isPlaced);\n    }\n}",
                "output": "Aman\n21\n89.5\nfalse"
            },
            "cpp": {
                "code": "#include <iostream>\n#include <string>\nusing namespace std;\n\nint main() {\n    string name = \"Aman\";\n    int age = 21;\n    double percentage = 89.5;\n    bool isPlaced = false;\n\n    cout << name << endl;\n    cout << age << endl;\n    cout << percentage << endl;\n    cout << boolalpha << isPlaced << endl;\n    return 0;\n}",
                "output": "Aman\n21\n89.5\nfalse"
            }
        },

        "dry_run": """
Code:
age = 21
age = "Twenty One"
print(age)
print(type(age))

Step 1: age refers to the integer 21.
Step 2: age is reassigned to the string "Twenty One".
Step 3: print(age) displays Twenty One.
Step 4: type(age) returns str.

Output:
Twenty One
<class 'str'>
""",

        "practice_questions": [
            {
                "level": "Beginner",
                "question": "Create variables for name, age and percentage. Print all three values.",
                "sample_input": "No input required",
                "sample_output": "Aman\n21\n89.5",
                "solutions": {
                    "python": "name = 'Aman'\nage = 21\npercentage = 89.5\n\nprint(name)\nprint(age)\nprint(percentage)",
                    "java": "public class Main {\n    public static void main(String[] args) {\n        String name = \"Aman\";\n        int age = 21;\n        double percentage = 89.5;\n        System.out.println(name);\n        System.out.println(age);\n        System.out.println(percentage);\n    }\n}",
                    "cpp": "#include <iostream>\n#include <string>\nusing namespace std;\n\nint main() {\n    string name = \"Aman\";\n    int age = 21;\n    double percentage = 89.5;\n    cout << name << endl;\n    cout << age << endl;\n    cout << percentage << endl;\n    return 0;\n}"
                },
                "explanation": "The program stores values of different types and prints each value."
            },
            {
                "level": "Beginner",
                "question": "Convert the string '150' into an integer and add 50.",
                "sample_input": "No input required",
                "sample_output": "200",
                "solutions": {
                    "python": "number = int('150')\nprint(number + 50)",
                    "java": "public class Main {\n    public static void main(String[] args) {\n        String value = \"150\";\n        int number = Integer.parseInt(value);\n        System.out.println(number + 50);\n    }\n}",
                    "cpp": "#include <iostream>\n#include <string>\nusing namespace std;\n\nint main() {\n    string value = \"150\";\n    int number = stoi(value);\n    cout << number + 50 << endl;\n    return 0;\n}"
                },
                "explanation": "Python int(), Java Integer.parseInt() and C++ stoi() convert numeric strings into integers."
            }
        ],

        "interview_questions": [
            {
                "question": "What is dynamic typing?",
                "answer": "Dynamic typing means a variable does not need an explicit type declaration. Its type is determined from the object it refers to at runtime."
            },
            {
                "question": "What is the difference between a list and a tuple?",
                "answer": "A list is mutable, whereas a tuple is immutable. Both are ordered collections."
            },
            {
                "question": "What is the difference between == and is in Python?",
                "answer": "== compares values for equality. is checks whether two references point to the same object."
            }
        ],

        "mcqs": [
            {
                "question": "Which Python data type is immutable?",
                "options": ["List", "Dictionary", "Tuple", "Set"],
                "answer": "Tuple",
                "explanation": "A tuple cannot be modified after it is created."
            },
            {
                "question": "What is the output of type(10.5)?",
                "options": ["int", "float", "str", "bool"],
                "answer": "float",
                "explanation": "Decimal numeric values such as 10.5 have the float type."
            }
        ]
    }
}


def get_python_lesson(lesson_id: str):
    """Return detailed Python lesson content, or None if not found."""
    return PYTHON_FOUNDATIONS.get(lesson_id)


PYTHON_FOUNDATIONS.update({

    # =========================================================
    # 3. OPERATORS
    # =========================================================

    "python-arithmetic": {
        "id": "python-arithmetic",
        "title": "Python Operators",
        "duration": "30 min",

        "content": """
# Python Operators

Operators are symbols or keywords used to perform operations on values and variables.

## 1. Arithmetic Operators

| Operator | Meaning | Example |
|---|---|---|
| + | Addition | 10 + 5 = 15 |
| - | Subtraction | 10 - 5 = 5 |
| * | Multiplication | 10 * 5 = 50 |
| / | Division | 10 / 5 = 2.0 |
| // | Floor division | 11 // 5 = 2 |
| % | Modulus | 11 % 5 = 1 |
| ** | Exponentiation | 2 ** 3 = 8 |

Important:
- / returns a floating-point result in Python.
- // performs floor division.
- % returns the remainder.
- ** calculates powers.

## 2. Comparison Operators

These operators compare two values and return True or False.

== Equal to
!= Not equal to
> Greater than
< Less than
>= Greater than or equal to
<= Less than or equal to

## 3. Assignment Operators

=, +=, -=, *=, /=, //=, %=, **=

Example:
x = 10
x += 5

This is equivalent to x = x + 5.

## 4. Logical Operators

and: True when both conditions are true.
or: True when at least one condition is true.
not: Reverses a Boolean result.

## 5. Membership Operators

in: Checks whether an element exists in a collection.
not in: Checks whether an element does not exist.

Example:
numbers = [10, 20, 30]
print(20 in numbers)

Output: True

## 6. Identity Operators

is: Checks whether two references point to the same object.
is not: Checks whether they point to different objects.

Do not confuse is with ==.

## 7. Bitwise Operators

&: AND
|: OR
^: XOR
~: NOT
<<: Left shift
>>: Right shift

These operators work on the binary representation of integers.
""",

        "key_concepts": [
            "Arithmetic operators",
            "Comparison operators",
            "Assignment operators",
            "Logical operators",
            "Membership operators",
            "Identity operators",
            "Bitwise operators",
            "Operator precedence"
        ],

        "examples": {
            "python": {
                "code": "a = 10\nb = 3\n\nprint(a + b)\nprint(a // b)\nprint(a % b)\nprint(a ** b)\nprint(a > b)\nprint(a > 5 and b < 5)",
                "output": "13\n3\n1\n1000\nTrue\nTrue"
            },
            "java": {
                "code": "public class Main {\n    public static void main(String[] args) {\n        int a = 10, b = 3;\n\n        System.out.println(a + b);\n        System.out.println(a / b);\n        System.out.println(a % b);\n        System.out.println((int)Math.pow(a, b));\n        System.out.println(a > b);\n        System.out.println(a > 5 && b < 5);\n    }\n}",
                "output": "13\n3\n1\n1000\ntrue\ntrue"
            },
            "cpp": {
                "code": "#include <iostream>\nusing namespace std;\n\nint main() {\n    int a = 10, b = 3;\n\n    cout << a + b << endl;\n    cout << a / b << endl;\n    cout << a % b << endl;\n    cout << (a > b) << endl;\n    cout << (a > 5 && b < 5) << endl;\n    return 0;\n}",
                "output": "13\n3\n1\n1\n1"
            }
        },

        "dry_run": """
a = 10
b = 3

a + b = 13
a // b = 3
a % b = 1
a ** b = 1000

The remainder of 10 divided by 3 is 1.
The floor division result is 3.
""",

        "practice_questions": [
            {
                "level": "Beginner",
                "question": "Take two numbers and print their sum, difference, product and remainder. Use 17 and 5.",
                "sample_input": "17 5",
                "sample_output": "22\n12\n85\n2",
                "solutions": {
                    "python": "a, b = map(int, input().split())\nprint(a + b)\nprint(a - b)\nprint(a * b)\nprint(a % b)",
                    "java": "import java.util.*;\npublic class Main {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int a = sc.nextInt(), b = sc.nextInt();\n        System.out.println(a + b);\n        System.out.println(a - b);\n        System.out.println(a * b);\n        System.out.println(a % b);\n    }\n}",
                    "cpp": "#include <iostream>\nusing namespace std;\nint main() {\n    int a, b;\n    cin >> a >> b;\n    cout << a + b << endl;\n    cout << a - b << endl;\n    cout << a * b << endl;\n    cout << a % b << endl;\n    return 0;\n}"
                },
                "explanation": "Read two integers and apply the four arithmetic operators."
            },
            {
                "level": "Intermediate",
                "question": "Check whether a given number is even using the modulus operator.",
                "sample_input": "14",
                "sample_output": "Even",
                "solutions": {
                    "python": "n = int(input())\nif n % 2 == 0:\n    print('Even')\nelse:\n    print('Odd')",
                    "java": "import java.util.*;\npublic class Main {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int n = sc.nextInt();\n        if (n % 2 == 0) System.out.println(\"Even\");\n        else System.out.println(\"Odd\");\n    }\n}",
                    "cpp": "#include <iostream>\nusing namespace std;\nint main() {\n    int n;\n    cin >> n;\n    if (n % 2 == 0) cout << \"Even\";\n    else cout << \"Odd\";\n    return 0;\n}"
                },
                "explanation": "An even number leaves remainder zero when divided by 2."
            }
        ],

        "interview_questions": [
            {
                "question": "What is the difference between / and // in Python?",
                "answer": "/ performs division and returns a floating-point result. // performs floor division and rounds the result down."
            },
            {
                "question": "What is the difference between == and is?",
                "answer": "== compares values, while is checks object identity."
            },
            {
                "question": "What does the modulus operator do?",
                "answer": "It returns the remainder after division."
            }
        ],

        "mcqs": [
            {
                "question": "What is the output of 17 // 5?",
                "options": ["3.4", "3", "2", "4"],
                "answer": "3",
                "explanation": "Floor division returns the floor of the quotient."
            },
            {
                "question": "What is the output of 2 ** 4?",
                "options": ["6", "8", "16", "24"],
                "answer": "16",
                "explanation": "The exponentiation operator calculates 2 raised to the power 4."
            }
        ]
    },

    # =========================================================
    # 4. CONDITIONAL STATEMENTS
    # =========================================================

    "python-if-else": {
        "id": "python-if-else",
        "title": "Conditional Statements",
        "duration": "35 min",

        "content": """
# Conditional Statements in Python

Conditional statements allow a program to make decisions.

A condition evaluates to True or False.

## 1. if Statement

Executes a block when the condition is true.

age = 20
if age >= 18:
    print("Eligible")

## 2. if-else Statement

Chooses between two alternatives.

if age >= 18:
    print("Adult")
else:
    print("Minor")

## 3. if-elif-else

Used when multiple conditions need to be checked.

marks = 75

if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
elif marks >= 60:
    print("C")
else:
    print("D")

Python checks conditions from top to bottom.
The first true condition's block is executed.

## 4. Nested if

An if statement inside another if statement is called a nested if.

Example:
age = 22
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed")
    else:
        print("ID required")
else:
    print("Not eligible")

## 5. Indentation

Python uses indentation to define code blocks.

Correct:
if True:
    print("Hello")

Incorrect indentation can produce an IndentationError.

## 6. Truthy and Falsy Values

Falsy values include:
- False
- None
- 0
- 0.0
- Empty strings
- Empty lists, tuples, sets and dictionaries

Most other values are truthy.

## 7. Ternary Conditional Expression

Python supports a short conditional expression:

result = "Pass" if marks >= 40 else "Fail"

It is useful for simple decisions.
""",

        "key_concepts": [
            "if statement",
            "if-else",
            "if-elif-else",
            "Nested conditions",
            "Indentation",
            "Truthy and falsy values",
            "Ternary expression"
        ],

        "examples": {
            "python": {
                "code": "marks = 82\n\nif marks >= 90:\n    print('Grade A')\nelif marks >= 75:\n    print('Grade B')\nelif marks >= 60:\n    print('Grade C')\nelse:\n    print('Grade D')",
                "output": "Grade B"
            },
            "java": {
                "code": "public class Main {\n    public static void main(String[] args) {\n        int marks = 82;\n\n        if (marks >= 90) {\n            System.out.println(\"Grade A\");\n        } else if (marks >= 75) {\n            System.out.println(\"Grade B\");\n        } else if (marks >= 60) {\n            System.out.println(\"Grade C\");\n        } else {\n            System.out.println(\"Grade D\");\n        }\n    }\n}",
                "output": "Grade B"
            },
            "cpp": {
                "code": "#include <iostream>\nusing namespace std;\n\nint main() {\n    int marks = 82;\n\n    if (marks >= 90)\n        cout << \"Grade A\";\n    else if (marks >= 75)\n        cout << \"Grade B\";\n    else if (marks >= 60)\n        cout << \"Grade C\";\n    else\n        cout << \"Grade D\";\n\n    return 0;\n}",
                "output": "Grade B"
            }
        },

        "dry_run": """
marks = 82

Check marks >= 90:
82 >= 90 is False.

Check marks >= 75:
82 >= 75 is True.

Print Grade B.
Remaining elif and else blocks are skipped.

Output:
Grade B
""",

        "practice_questions": [
            {
                "level": "Beginner",
                "question": "Write a program to check whether a number is positive, negative or zero.",
                "sample_input": "-5",
                "sample_output": "Negative",
                "solutions": {
                    "python": "n = int(input())\nif n > 0:\n    print('Positive')\nelif n < 0:\n    print('Negative')\nelse:\n    print('Zero')",
                    "java": "import java.util.*;\npublic class Main {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int n = sc.nextInt();\n        if (n > 0) System.out.println(\"Positive\");\n        else if (n < 0) System.out.println(\"Negative\");\n        else System.out.println(\"Zero\");\n    }\n}",
                    "cpp": "#include <iostream>\nusing namespace std;\nint main() {\n    int n;\n    cin >> n;\n    if (n > 0) cout << \"Positive\";\n    else if (n < 0) cout << \"Negative\";\n    else cout << \"Zero\";\n    return 0;\n}"
                },
                "explanation": "Compare the number with zero using if, elif and else."
            },
            {
                "level": "Intermediate",
                "question": "Check whether a year is a leap year. A leap year is divisible by 400, or divisible by 4 but not by 100.",
                "sample_input": "2024",
                "sample_output": "Leap Year",
                "solutions": {
                    "python": "year = int(input())\nif year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):\n    print('Leap Year')\nelse:\n    print('Not a Leap Year')",
                    "java": "import java.util.*;\npublic class Main {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int year = sc.nextInt();\n        if (year % 400 == 0 || (year % 4 == 0 && year % 100 != 0))\n            System.out.println(\"Leap Year\");\n        else\n            System.out.println(\"Not a Leap Year\");\n    }\n}",
                    "cpp": "#include <iostream>\nusing namespace std;\nint main() {\n    int year;\n    cin >> year;\n    if (year % 400 == 0 || (year % 4 == 0 && year % 100 != 0))\n        cout << \"Leap Year\";\n    else\n        cout << \"Not a Leap Year\";\n    return 0;\n}"
                },
                "explanation": "The divisibility rules handle century years correctly. For example, 1900 is not a leap year, but 2000 is."
            }
        ],

        "interview_questions": [
            {
                "question": "What is the difference between if and elif?",
                "answer": "if starts a conditional decision. elif checks another condition when the preceding conditions were false."
            },
            {
                "question": "What is indentation in Python?",
                "answer": "Indentation means leading whitespace used to define blocks of code."
            },
            {
                "question": "What is a nested if?",
                "answer": "A conditional statement placed inside another conditional block."
            }
        ],

        "mcqs": [
            {
                "question": "Which keyword checks another condition after an if?",
                "options": ["elseif", "elif", "otherwise", "then"],
                "answer": "elif",
                "explanation": "Python uses elif for additional conditional branches."
            },
            {
                "question": "Which of these is falsy in Python?",
                "options": ["'Hello'", "[1]", "0", "{1}"],
                "answer": "0",
                "explanation": "Numeric zero is falsy in Python."
            }
        ]
    },

    # =========================================================
    # 5. LOOPS
    # =========================================================

    "python-for-loop": {
        "id": "python-for-loop",
        "title": "For Loops and range()",
        "duration": "35 min",

        "content": """
# Loops in Python

Loops execute a block of code repeatedly.

They are useful when an operation needs to be performed multiple times.

## 1. for Loop

A for loop iterates over a sequence or iterable.

Example:
for number in [1, 2, 3]:
    print(number)

Output:
1
2
3

## 2. range() Function

range() generates a sequence of integers.

range(stop):
Starts at 0 and stops before stop.

range(start, stop):
Starts at start and stops before stop.

range(start, stop, step):
Uses the specified step.

Examples:
range(5) gives 0, 1, 2, 3, 4.
range(2, 6) gives 2, 3, 4, 5.
range(2, 10, 2) gives 2, 4, 6, 8.

## 3. Looping Through Strings

for character in "Python":
    print(character)

Each iteration gives one character.

## 4. break Statement

break immediately terminates the nearest enclosing loop.

## 5. continue Statement

continue skips the rest of the current iteration and proceeds to the next iteration.

## 6. pass Statement

pass is a placeholder statement. It performs no operation.

## 7. Nested Loops

A loop inside another loop is called a nested loop.

Example:
for i in range(1, 3):
    for j in range(1, 3):
        print(i, j)

The inner loop completes its iterations for every outer-loop iteration.

## 8. Loop Complexity

A single loop over n items usually takes O(n) time.

Two nested loops that each run n times usually take O(n^2) time.
""",

        "key_concepts": [
            "for loop",
            "range()",
            "Iteration",
            "break",
            "continue",
            "pass",
            "Nested loops",
            "Loop time complexity"
        ],

        "examples": {
            "python": {
                "code": "for i in range(1, 6):\n    print(i)\n\nfor i in range(2, 11, 2):\n    print(i, end=' ')",
                "output": "1\n2\n3\n4\n5\n2 4 6 8 10"
            },
            "java": {
                "code": "public class Main {\n    public static void main(String[] args) {\n        for (int i = 1; i <= 5; i++) {\n            System.out.println(i);\n        }\n        for (int i = 2; i <= 10; i += 2) {\n            System.out.print(i + \" \");\n        }\n    }\n}",
                "output": "1\n2\n3\n4\n5\n2 4 6 8 10 "
            },
            "cpp": {
                "code": "#include <iostream>\nusing namespace std;\n\nint main() {\n    for (int i = 1; i <= 5; i++) {\n        cout << i << endl;\n    }\n    for (int i = 2; i <= 10; i += 2) {\n        cout << i << \" \";\n    }\n    return 0;\n}",
                "output": "1\n2\n3\n4\n5\n2 4 6 8 10 "
            }
        },

        "dry_run": """
for i in range(1, 4):
    print(i)

range(1, 4) produces 1, 2, 3.

Iteration 1: i = 1, print 1.
Iteration 2: i = 2, print 2.
Iteration 3: i = 3, print 3.

The loop stops because 4 is excluded.

Output:
1
2
3
""",

        "practice_questions": [
            {
                "level": "Beginner",
                "question": "Print the multiplication table of a given number from 1 to 10.",
                "sample_input": "5",
                "sample_output": "5\n10\n15\n20\n25\n30\n35\n40\n45\n50",
                "solutions": {
                    "python": "n = int(input())\nfor i in range(1, 11):\n    print(n * i)",
                    "java": "import java.util.*;\npublic class Main {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int n = sc.nextInt();\n        for (int i = 1; i <= 10; i++) {\n            System.out.println(n * i);\n        }\n    }\n}",
                    "cpp": "#include <iostream>\nusing namespace std;\nint main() {\n    int n;\n    cin >> n;\n    for (int i = 1; i <= 10; i++) {\n        cout << n * i << endl;\n    }\n    return 0;\n}"
                },
                "explanation": "The loop multiplies the given number by each integer from 1 through 10."
            },
            {
                "level": "Intermediate",
                "question": "Calculate the sum of all integers from 1 to n using a loop.",
                "sample_input": "5",
                "sample_output": "15",
                "solutions": {
                    "python": "n = int(input())\ntotal = 0\nfor i in range(1, n + 1):\n    total += i\nprint(total)",
                    "java": "import java.util.*;\npublic class Main {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int n = sc.nextInt();\n        int total = 0;\n        for (int i = 1; i <= n; i++) total += i;\n        System.out.println(total);\n    }\n}",
                    "cpp": "#include <iostream>\nusing namespace std;\nint main() {\n    int n, total = 0;\n    cin >> n;\n    for (int i = 1; i <= n; i++) total += i;\n    cout << total;\n    return 0;\n}"
                },
                "explanation": "Start with total = 0 and add each integer from 1 to n. This loop takes O(n) time."
            }
        ],

        "interview_questions": [
            {
                "question": "What is the difference between break and continue?",
                "answer": "break terminates the loop. continue skips the current iteration and proceeds to the next."
            },
            {
                "question": "What does range(1, 5) generate?",
                "answer": "It generates 1, 2, 3 and 4. The stop value 5 is excluded."
            },
            {
                "question": "What is a nested loop?",
                "answer": "A loop placed inside another loop. Its total number of iterations depends on both loops."
            }
        ],

        "mcqs": [
            {
                "question": "What is the output of list(range(2, 8, 2))?",
                "options": ["[2, 4, 6]", "[2, 4, 6, 8]", "[2, 3, 4, 5, 6, 7]", "[2, 8]"],
                "answer": "[2, 4, 6]",
                "explanation": "The step is 2 and the stop value 8 is excluded."
            },
            {
                "question": "Which statement immediately terminates a loop?",
                "options": ["continue", "pass", "break", "skip"],
                "answer": "break",
                "explanation": "break exits the nearest enclosing loop."
            }
        ]
    },

    "python-while-loop": {
        "id": "python-while-loop",
        "title": "While Loops",
        "duration": "25 min",

        "content": """
# While Loops

A while loop repeatedly executes a block as long as its condition remains true.

## 1. Syntax

while condition:
    statements

Example:
count = 1

while count <= 5:
    print(count)
    count += 1

Output:
1
2
3
4
5

## 2. How It Works

1. The condition is checked.
2. If true, the loop body executes.
3. The condition is checked again.
4. The loop stops when the condition becomes false.

## 3. Infinite Loops

An infinite loop occurs when the condition never becomes false.

Example:
while True:
    print("Running")

Use break when you need a controlled exit.

## 4. break and continue

break exits the loop.

continue skips the remaining statements in the current iteration.

## 5. for vs while

for loop:
- Useful when iterating over a sequence.
- Often used when the number of iterations is known.

while loop:
- Useful when repetition depends on a condition.
- Often used when the number of iterations is not known in advance.

## 6. Common Interview Mistake

Forgetting to update the loop variable can cause an infinite loop.

Always check that your while loop can eventually terminate.
""",

        "key_concepts": [
            "while loop",
            "Loop condition",
            "Infinite loop",
            "Loop termination",
            "break",
            "continue",
            "for vs while"
        ],

        "examples": {
            "python": {
                "code": "count = 1\nwhile count <= 5:\n    print(count)\n    count += 1",
                "output": "1\n2\n3\n4\n5"
            },
            "java": {
                "code": "public class Main {\n    public static void main(String[] args) {\n        int count = 1;\n        while (count <= 5) {\n            System.out.println(count);\n            count++;\n        }\n    }\n}",
                "output": "1\n2\n3\n4\n5"
            },
            "cpp": {
                "code": "#include <iostream>\nusing namespace std;\n\nint main() {\n    int count = 1;\n    while (count <= 5) {\n        cout << count << endl;\n        count++;\n    }\n    return 0;\n}",
                "output": "1\n2\n3\n4\n5"
            }
        },

        "dry_run": """
count = 1

Iteration 1: count = 1, condition true, print 1, increment.
Iteration 2: count = 2, condition true, print 2, increment.
Iteration 3: count = 3, condition true, print 3, increment.
Iteration 4: count = 4, condition true, print 4, increment.
Iteration 5: count = 5, condition true, print 5, increment.
Next: count = 6, condition false, stop.

Output:
1
2
3
4
5
""",

        "practice_questions": [
            {
                "level": "Beginner",
                "question": "Print numbers from 1 to n using a while loop.",
                "sample_input": "4",
                "sample_output": "1\n2\n3\n4",
                "solutions": {
                    "python": "n = int(input())\ni = 1\nwhile i <= n:\n    print(i)\n    i += 1",
                    "java": "import java.util.*;\npublic class Main {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int n = sc.nextInt(), i = 1;\n        while (i <= n) {\n            System.out.println(i);\n            i++;\n        }\n    }\n}",
                    "cpp": "#include <iostream>\nusing namespace std;\nint main() {\n    int n, i = 1;\n    cin >> n;\n    while (i <= n) {\n        cout << i << endl;\n        i++;\n    }\n    return 0;\n}"
                },
                "explanation": "The loop begins at 1 and increments i until it becomes greater than n."
            },
            {
                "level": "Intermediate",
                "question": "Find the sum of the digits of a positive integer using a while loop.",
                "sample_input": "1234",
                "sample_output": "10",
                "solutions": {
                    "python": "n = int(input())\ntotal = 0\nwhile n > 0:\n    digit = n % 10\n    total += digit\n    n //= 10\nprint(total)",
                    "java": "import java.util.*;\npublic class Main {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int n = sc.nextInt(), total = 0;\n        while (n > 0) {\n            int digit = n % 10;\n            total += digit;\n            n /= 10;\n        }\n        System.out.println(total);\n    }\n}",
                    "cpp": "#include <iostream>\nusing namespace std;\nint main() {\n    int n, total = 0;\n    cin >> n;\n    while (n > 0) {\n        int digit = n % 10;\n        total += digit;\n        n /= 10;\n    }\n    cout << total;\n    return 0;\n}"
                },
                "explanation": "The remainder operator extracts the last digit. Integer division removes that digit. Repeat until no digits remain."
            }
        ],

        "interview_questions": [
            {
                "question": "When should you use a while loop?",
                "answer": "Use it when repetition depends on a condition and the number of iterations may not be known in advance."
            },
            {
                "question": "What causes an infinite while loop?",
                "answer": "A loop can run forever when its condition never becomes false, often because the loop variable is not updated."
            }
        ],

        "mcqs": [
            {
                "question": "What happens if a while condition is initially False?",
                "options": ["Runs once", "Runs twice", "Does not execute", "Causes an error"],
                "answer": "Does not execute",
                "explanation": "A while loop checks its condition before executing its body."
            },
            {
                "question": "Which operator is commonly used to remove the last digit of a positive integer?",
                "options": ["%", "//", "**", "=="],
                "answer": "//",
                "explanation": "Integer floor division by 10 removes the last decimal digit of a positive integer."
            }
        ]
    },

    # =========================================================
    # 6. FUNCTIONS
    # =========================================================

    "python-function-basics": {
        "id": "python-function-basics",
        "title": "Functions in Python",
        "duration": "40 min",

        "content": """
# Functions in Python

A function is a reusable block of code designed to perform a specific task.

Functions improve:
- Code reusability
- Readability
- Modularity
- Testing and maintenance

## 1. Defining a Function

Python uses the def keyword.

def greet():
    print("Hello")

## 2. Calling a Function

greet()

Calling a function executes its body.

## 3. Parameters and Arguments

Parameters are variables listed in the function definition.

Arguments are actual values passed during a function call.

def greet(name):
    print("Hello", name)

greet("Aman")

Here name is a parameter and "Aman" is an argument.

## 4. Multiple Parameters

def add(a, b):
    print(a + b)

add(10, 20)

## 5. Types of Arguments

Positional arguments:
Values are assigned based on their position.

Keyword arguments:
Values are assigned using parameter names.

Default arguments:
Parameters can have default values.

Variable-length arguments:
*args collects extra positional arguments into a tuple.
**kwargs collects extra keyword arguments into a dictionary.

## 6. Local and Global Variables

A local variable is created inside a function.

A global variable is defined outside functions.

The global keyword allows a function to reassign a global variable.

Use global variables carefully because they can make code harder to maintain.

## 7. Lambda Functions

A lambda function is a small anonymous function.

square = lambda x: x * x

print(square(5))

Output: 25

## 8. Recursion

Recursion occurs when a function calls itself.

A recursive function needs:
- A base case to stop recursion.
- A recursive case that moves toward the base case.

Recursion will be studied in more detail in the DSA learning path.
""",

        "key_concepts": [
            "def keyword",
            "Function definition and calling",
            "Parameters and arguments",
            "Positional arguments",
            "Keyword arguments",
            "Default arguments",
            "*args and **kwargs",
            "Local and global variables",
            "Lambda functions",
            "Recursion"
        ],

        "examples": {
            "python": {
                "code": "def add(a, b):\n    return a + b\n\nresult = add(10, 20)\nprint(result)",
                "output": "30"
            },
            "java": {
                "code": "public class Main {\n    static int add(int a, int b) {\n        return a + b;\n    }\n\n    public static void main(String[] args) {\n        int result = add(10, 20);\n        System.out.println(result);\n    }\n}",
                "output": "30"
            },
            "cpp": {
                "code": "#include <iostream>\nusing namespace std;\n\nint add(int a, int b) {\n    return a + b;\n}\n\nint main() {\n    int result = add(10, 20);\n    cout << result << endl;\n    return 0;\n}",
                "output": "30"
            }
        },

        "dry_run": """
def add(a, b):
    return a + b

result = add(10, 20)

Step 1: The function is defined.
Step 2: add(10, 20) is called.
Step 3: a receives 10 and b receives 20.
Step 4: a + b evaluates to 30.
Step 5: return sends 30 to the caller.
Step 6: result stores 30.
Step 7: print(result) displays 30.

Output:
30
""",

        "practice_questions": [
            {
                "level": "Beginner",
                "question": "Create a function that accepts two integers and returns their sum.",
                "sample_input": "10 20",
                "sample_output": "30",
                "solutions": {
                    "python": "def add(a, b):\n    return a + b\n\na, b = map(int, input().split())\nprint(add(a, b))",
                    "java": "import java.util.*;\npublic class Main {\n    static int add(int a, int b) {\n        return a + b;\n    }\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int a = sc.nextInt(), b = sc.nextInt();\n        System.out.println(add(a, b));\n    }\n}",
                    "cpp": "#include <iostream>\nusing namespace std;\nint add(int a, int b) {\n    return a + b;\n}\nint main() {\n    int a, b;\n    cin >> a >> b;\n    cout << add(a, b);\n    return 0;\n}"
                },
                "explanation": "The function receives two arguments and returns their sum to the caller."
            },
            {
                "level": "Intermediate",
                "question": "Write a function that returns the factorial of a non-negative integer using iteration.",
                "sample_input": "5",
                "sample_output": "120",
                "solutions": {
                    "python": "def factorial(n):\n    result = 1\n    for i in range(1, n + 1):\n        result *= i\n    return result\n\nn = int(input())\nprint(factorial(n))",
                    "java": "import java.util.*;\npublic class Main {\n    static long factorial(int n) {\n        long result = 1;\n        for (int i = 1; i <= n; i++) result *= i;\n        return result;\n    }\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int n = sc.nextInt();\n        System.out.println(factorial(n));\n    }\n}",
                    "cpp": "#include <iostream>\nusing namespace std;\nlong long factorial(int n) {\n    long long result = 1;\n    for (int i = 1; i <= n; i++) result *= i;\n    return result;\n}\nint main() {\n    int n;\n    cin >> n;\n    cout << factorial(n);\n    return 0;\n}"
                },
                "explanation": "Factorial is the product of all positive integers up to n. By definition, 0! = 1. These implementations use fixed-width integer types in Java and C++, so very large factorials can overflow."
            }
        ],

        "interview_questions": [
            {
                "question": "What is a function?",
                "answer": "A function is a reusable block of code that performs a specific task."
            },
            {
                "question": "What is the difference between print and return?",
                "answer": "print displays a value. return sends a value back to the caller and ends the current function execution."
            },
            {
                "question": "What are *args and **kwargs?",
                "answer": "*args collects additional positional arguments into a tuple. **kwargs collects additional keyword arguments into a dictionary."
            },
            {
                "question": "What is recursion?",
                "answer": "Recursion is a programming technique in which a function calls itself until a base condition is reached."
            }
        ],

        "mcqs": [
            {
                "question": "Which keyword is used to define a function in Python?",
                "options": ["function", "define", "def", "fun"],
                "answer": "def",
                "explanation": "The def keyword begins a function definition."
            },
            {
                "question": "What does a function return if it has no return statement?",
                "options": ["0", "False", "None", "Empty string"],
                "answer": "None",
                "explanation": "A Python function without an explicit return statement returns None."
            },
            {
                "question": "What is the data type of *args inside a Python function?",
                "options": ["List", "Tuple", "Dictionary", "Set"],
                "answer": "Tuple",
                "explanation": "*args collects positional arguments into a tuple."
            }
        ]
    }

})


def get_python_lesson(lesson_id: str):
    """Return detailed Python lesson content, or None if not found."""
    return PYTHON_FOUNDATIONS.get(lesson_id)


PYTHON_FOUNDATIONS.update({

    # =========================================================
    # 8. LISTS
    # =========================================================

    "python-lists": {
        "id": "python-lists",
        "title": "Python Lists",
        "duration": "40 min",

        "content": """
# Python Lists

A list is an ordered and mutable collection of elements.

Mutable means that we can modify a list after creating it.

## 1. Creating Lists

numbers = [10, 20, 30, 40]
names = ["Aman", "Riya", "Khushi"]
mixed = [10, "Python", 3.5, True]

Lists can contain different data types.

## 2. Indexing

Python uses zero-based indexing.

numbers = [10, 20, 30, 40]

numbers[0] gives 10.
numbers[1] gives 20.
numbers[-1] gives 40.

Negative indexing starts from the end.

## 3. Slicing

Syntax:
list[start:stop:step]

Example:
numbers = [10, 20, 30, 40, 50]

numbers[1:4] gives [20, 30, 40].
numbers[:3] gives [10, 20, 30].
numbers[::2] gives [10, 30, 50].

The stop index is excluded.

## 4. Modifying Lists

numbers[0] = 100
Changes the first element.

append(x): Adds one element at the end.
extend(iterable): Adds multiple elements.
insert(i, x): Inserts at a specified index.
remove(x): Removes the first matching value.
pop(): Removes and returns the last element by default.
clear(): Removes all elements.

## 5. Searching and Counting

index(x): Returns the first matching index.
count(x): Counts occurrences.
in: Checks membership.

## 6. Sorting and Reversing

numbers.sort(): Sorts the list in place.
numbers.reverse(): Reverses the list in place.
sorted(numbers): Returns a new sorted list.

## 7. Iterating Through Lists

for value in numbers:
    print(value)

## 8. List Comprehension

A concise way to create lists.

squares = [x * x for x in range(1, 6)]

Output:
[1, 4, 9, 16, 25]

## 9. List vs Array vs Vector

Python list:
- Mutable and dynamically resizable.
- Can store mixed data types.

Java ArrayList:
- Resizable collection.
- Stores objects; primitive values use wrapper classes.

C++ vector:
- Resizable sequence container.
- Commonly stores elements of one declared type.

## 10. Time Complexity

Common list operations:
- Index access: O(1)
- Append: O(1) amortized
- Search: O(n)
- Insert at beginning: O(n)
- Delete from beginning: O(n)
- Sorting: O(n log n) for Python's standard sort.

These complexities are useful in DSA interviews.
""",

        "key_concepts": [
            "List creation",
            "Indexing",
            "Negative indexing",
            "Slicing",
            "append and extend",
            "insert and remove",
            "pop and clear",
            "Sorting",
            "List comprehension",
            "List time complexity"
        ],

        "examples": {
            "python": {
                "code": "numbers = [10, 20, 30, 40]\nnumbers.append(50)\nnumbers[0] = 100\n\nprint(numbers)\nprint(numbers[1:4])\nprint(len(numbers))",
                "output": "[100, 20, 30, 40, 50]\n[20, 30, 40]\n5"
            },
            "java": {
                "code": "import java.util.*;\npublic class Main {\n    public static void main(String[] args) {\n        ArrayList<Integer> numbers = new ArrayList<>(Arrays.asList(10, 20, 30, 40));\n        numbers.add(50);\n        numbers.set(0, 100);\n\n        System.out.println(numbers);\n        System.out.println(numbers.subList(1, 4));\n        System.out.println(numbers.size());\n    }\n}",
                "output": "[100, 20, 30, 40, 50]\n[20, 30, 40]\n5"
            },
            "cpp": {
                "code": "#include <iostream>\n#include <vector>\nusing namespace std;\n\nint main() {\n    vector<int> numbers = {10, 20, 30, 40};\n    numbers.push_back(50);\n    numbers[0] = 100;\n\n    for (int x : numbers) cout << x << \" \";\n    cout << endl;\n    cout << numbers.size();\n    return 0;\n}",
                "output": "100 20 30 40 50\n5"
            }
        },

        "dry_run": """
numbers = [10, 20, 30]

numbers.append(40)
List becomes [10, 20, 30, 40].

numbers[1] = 50
List becomes [10, 50, 30, 40].

numbers.pop()
Removes 40.

Final list:
[10, 50, 30]
""",

        "practice_questions": [
            {
                "level": "Beginner",
                "question": "Read n integers and print their sum.",
                "sample_input": "5\n1 2 3 4 5",
                "sample_output": "15",
                "solutions": {
                    "python": "n = int(input())\narr = list(map(int, input().split()))\nprint(sum(arr[:n]))",
                    "java": "import java.util.*;\npublic class Main {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int n = sc.nextInt();\n        int sum = 0;\n        for (int i = 0; i < n; i++) sum += sc.nextInt();\n        System.out.println(sum);\n    }\n}",
                    "cpp": "#include <iostream>\nusing namespace std;\nint main() {\n    int n, x, sum = 0;\n    cin >> n;\n    for (int i = 0; i < n; i++) {\n        cin >> x;\n        sum += x;\n    }\n    cout << sum;\n    return 0;\n}"
                },
                "explanation": "Read each element and add it to a running sum. Time complexity is O(n)."
            },
            {
                "level": "Intermediate",
                "question": "Find the largest element in an array without using a built-in maximum function.",
                "sample_input": "5\n4 9 2 15 7",
                "sample_output": "15",
                "solutions": {
                    "python": "n = int(input())\narr = list(map(int, input().split()))\nlargest = arr[0]\nfor x in arr[1:n]:\n    if x > largest:\n        largest = x\nprint(largest)",
                    "java": "import java.util.*;\npublic class Main {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int n = sc.nextInt();\n        int largest = sc.nextInt();\n        for (int i = 1; i < n; i++) {\n            int x = sc.nextInt();\n            if (x > largest) largest = x;\n        }\n        System.out.println(largest);\n    }\n}",
                    "cpp": "#include <iostream>\nusing namespace std;\nint main() {\n    int n, x;\n    cin >> n >> x;\n    int largest = x;\n    for (int i = 1; i < n; i++) {\n        cin >> x;\n        if (x > largest) largest = x;\n    }\n    cout << largest;\n    return 0;\n}"
                },
                "explanation": "Initialize the largest value with the first element. Compare every remaining element and update it when a larger value is found. Time complexity is O(n)."
            }
        ],

        "interview_questions": [
            {
                "question": "Are Python lists mutable?",
                "answer": "Yes. Elements can be added, removed or modified after a list is created."
            },
            {
                "question": "What is the difference between append() and extend()?",
                "answer": "append() adds one object as a single element. extend() adds each element from an iterable."
            },
            {
                "question": "What is list comprehension?",
                "answer": "It is a concise syntax for creating a list from an iterable, optionally applying a condition."
            },
            {
                "question": "What is the time complexity of searching an element in a list?",
                "answer": "O(n) in the general case because elements may need to be checked one by one."
            }
        ],

        "mcqs": [
            {
                "question": "What is the output of [10, 20, 30][-1]?",
                "options": ["10", "20", "30", "Error"],
                "answer": "30",
                "explanation": "Index -1 refers to the last element."
            },
            {
                "question": "Which method adds one element at the end of a list?",
                "options": ["extend()", "append()", "insertAll()", "addAll()"],
                "answer": "append()",
                "explanation": "append() adds its argument as one element."
            },
            {
                "question": "What does [x*x for x in range(3)] return?",
                "options": ["[1, 4, 9]", "[0, 1, 4]", "[0, 2, 4]", "[1, 2, 3]"],
                "answer": "[0, 1, 4]",
                "explanation": "range(3) produces 0, 1, 2. Their squares are 0, 1, 4."
            }
        ]
    },

    # =========================================================
    # 9. TUPLES
    # =========================================================

    "python-tuples": {
        "id": "python-tuples",
        "title": "Python Tuples",
        "duration": "30 min",

        "content": """
# Python Tuples

A tuple is an ordered and immutable collection.

Immutable means that the tuple's elements cannot be reassigned after creation.

## 1. Creating Tuples

numbers = (10, 20, 30)
names = ("Aman", "Riya")

A single-element tuple requires a comma:

single = (10,)

Without the comma, (10) is just an integer in parentheses.

## 2. Accessing Elements

Tuples support indexing and slicing.

numbers = (10, 20, 30)

numbers[0] gives 10.
numbers[-1] gives 30.
numbers[0:2] gives (10, 20).

## 3. Immutability

This is invalid:

numbers = (10, 20, 30)
numbers[0] = 100

It raises TypeError.

However, a variable can be reassigned to a completely new tuple.

## 4. Tuple Methods

count(x): Counts occurrences.
index(x): Finds the first index of a value.

Tuples have fewer methods than lists because they cannot be modified.

## 5. Tuple Packing and Unpacking

Packing:
student = ("Aman", 21, 90)

Unpacking:
name, age, marks = student

The number of variables should match the number of unpacked elements.

Extended unpacking:
first, *middle, last = (1, 2, 3, 4)

## 6. Why Use Tuples?

- To represent fixed collections of values.
- To prevent accidental modification.
- To return multiple values from a function.
- To use suitable immutable values as dictionary keys.

A tuple containing mutable objects is not deeply immutable: those contained objects may still be modified.

## 7. List vs Tuple

List:
- Mutable.
- Uses square brackets.
- Supports methods such as append().

Tuple:
- Immutable.
- Uses parentheses commonly.
- Supports indexing and slicing.
""",

        "key_concepts": [
            "Tuple creation",
            "Immutability",
            "Indexing and slicing",
            "count() and index()",
            "Tuple packing",
            "Tuple unpacking",
            "Extended unpacking",
            "List vs tuple"
        ],

        "examples": {
            "python": {
                "code": "student = ('Aman', 21, 90)\nname, age, marks = student\n\nprint(name)\nprint(age)\nprint(marks)\nprint(student[0:2])",
                "output": "Aman\n21\n90\n('Aman', 21)"
            },
            "java": {
                "code": "public class Main {\n    public static void main(String[] args) {\n        String[] student = {\"Aman\", \"21\", \"90\"};\n        String name = student[0];\n        int age = Integer.parseInt(student[1]);\n        int marks = Integer.parseInt(student[2]);\n\n        System.out.println(name);\n        System.out.println(age);\n        System.out.println(marks);\n    }\n}",
                "output": "Aman\n21\n90"
            },
            "cpp": {
                "code": "#include <iostream>\n#include <tuple>\n#include <string>\nusing namespace std;\n\nint main() {\n    tuple<string, int, int> student = {\"Aman\", 21, 90};\n    cout << get<0>(student) << endl;\n    cout << get<1>(student) << endl;\n    cout << get<2>(student) << endl;\n    return 0;\n}",
                "output": "Aman\n21\n90"
            }
        },

        "dry_run": """
student = ("Aman", 21, 90)

name, age, marks = student

name receives "Aman".
age receives 21.
marks receives 90.

print(age) displays 21.

The original tuple remains unchanged.
""",

        "practice_questions": [
            {
                "level": "Beginner",
                "question": "Create a tuple containing three integers and print the first and last elements.",
                "sample_input": "No input required",
                "sample_output": "10\n30",
                "solutions": {
                    "python": "numbers = (10, 20, 30)\nprint(numbers[0])\nprint(numbers[-1])",
                    "java": "public class Main {\n    public static void main(String[] args) {\n        int[] numbers = {10, 20, 30};\n        System.out.println(numbers[0]);\n        System.out.println(numbers[numbers.length - 1]);\n    }\n}",
                    "cpp": "#include <iostream>\n#include <tuple>\nusing namespace std;\nint main() {\n    tuple<int, int, int> numbers = {10, 20, 30};\n    cout << get<0>(numbers) << endl;\n    cout << get<2>(numbers) << endl;\n    return 0;\n}"
                },
                "explanation": "Access the first element with index 0 and the last element with index -1 in Python."
            },
            {
                "level": "Intermediate",
                "question": "Given a tuple of three values, unpack it into three variables and print their sum.",
                "sample_input": "No input required",
                "sample_output": "60",
                "solutions": {
                    "python": "values = (10, 20, 30)\na, b, c = values\nprint(a + b + c)",
                    "java": "public class Main {\n    public static void main(String[] args) {\n        int[] values = {10, 20, 30};\n        int a = values[0], b = values[1], c = values[2];\n        System.out.println(a + b + c);\n    }\n}",
                    "cpp": "#include <iostream>\n#include <tuple>\nusing namespace std;\nint main() {\n    tuple<int, int, int> values = {10, 20, 30};\n    auto [a, b, c] = values;\n    cout << a + b + c;\n    return 0;\n}"
                },
                "explanation": "Python supports direct tuple unpacking. Java arrays and C++ tuples provide comparable ways to store and access fixed groups of values."
            }
        ],

        "interview_questions": [
            {
                "question": "Why are tuples immutable?",
                "answer": "Tuple immutability prevents reassignment of its elements and makes tuples useful for representing fixed collections."
            },
            {
                "question": "Can a tuple contain a list?",
                "answer": "Yes. The tuple cannot have its element reference reassigned, but the contained list can still be modified."
            },
            {
                "question": "How do you create a single-element tuple?",
                "answer": "Use a trailing comma, for example (10,)."
            }
        ],

        "mcqs": [
            {
                "question": "Which is the correct single-element tuple?",
                "options": ["(10)", "(10,)", "[10]", "{10}"],
                "answer": "(10,)",
                "explanation": "The trailing comma makes it a tuple."
            },
            {
                "question": "Which operation is not allowed on a tuple?",
                "options": ["Indexing", "Slicing", "Reassigning an element", "Iteration"],
                "answer": "Reassigning an element",
                "explanation": "Tuples are immutable."
            }
        ]
    },

    # =========================================================
    # 10. SETS
    # =========================================================

    "python-sets": {
        "id": "python-sets",
        "title": "Python Sets",
        "duration": "35 min",

        "content": """
# Python Sets

A set is an unordered collection of unique hashable elements.

The main purpose of a set is to store distinct values and perform mathematical set operations.

## 1. Creating Sets

numbers = {10, 20, 30}

Duplicate values are removed automatically.

numbers = {10, 10, 20, 20}
The resulting set contains 10 and 20.

To create an empty set, use set().

Important:
{} creates an empty dictionary, not an empty set.

## 2. Adding Elements

add(x): Adds one element.
update(iterable): Adds multiple elements.

## 3. Removing Elements

remove(x): Removes an element; raises KeyError if missing.
discard(x): Removes an element if present; does not raise KeyError if missing.
pop(): Removes and returns an arbitrary element.
clear(): Removes all elements.

## 4. Set Operations

Union:
A | B
Contains elements from either set.

Intersection:
A & B
Contains elements common to both.

Difference:
A - B
Contains elements in A but not B.

Symmetric difference:
A ^ B
Contains elements in either set, but not both.

## 5. Membership Testing

x in my_set

Average membership testing is O(1), assuming a good hash distribution.

## 6. Removing Duplicates

numbers = [1, 2, 2, 3, 3]
unique = set(numbers)

This removes duplicate values. Set iteration order should not be relied upon.

## 7. Set vs List

List:
- Allows duplicates.
- Maintains sequence order.
- Supports indexing.

Set:
- Stores unique hashable values.
- Does not support positional indexing.
- Provides efficient average membership testing.
""",

        "key_concepts": [
            "Set creation",
            "Unique elements",
            "add() and update()",
            "remove() and discard()",
            "Union",
            "Intersection",
            "Difference",
            "Symmetric difference",
            "Membership testing",
            "Removing duplicates"
        ],

        "examples": {
            "python": {
                "code": "A = {1, 2, 3, 4}\nB = {3, 4, 5, 6}\n\nprint(A | B)\nprint(A & B)\nprint(A - B)\nprint(A ^ B)",
                "output": "{1, 2, 3, 4, 5, 6}\n{3, 4}\n{1, 2}\n{1, 2, 5, 6}"
            },
            "java": {
                "code": "import java.util.*;\npublic class Main {\n    public static void main(String[] args) {\n        Set<Integer> A = new TreeSet<>(Arrays.asList(1, 2, 3, 4));\n        Set<Integer> B = new TreeSet<>(Arrays.asList(3, 4, 5, 6));\n\n        Set<Integer> union = new TreeSet<>(A);\n        union.addAll(B);\n        System.out.println(union);\n\n        Set<Integer> intersection = new TreeSet<>(A);\n        intersection.retainAll(B);\n        System.out.println(intersection);\n\n        Set<Integer> difference = new TreeSet<>(A);\n        difference.removeAll(B);\n        System.out.println(difference);\n    }\n}",
                "output": "[1, 2, 3, 4, 5, 6]\n[3, 4]\n[1, 2]"
            },
            "cpp": {
                "code": "#include <iostream>\n#include <set>\nusing namespace std;\n\nint main() {\n    set<int> A = {1, 2, 3, 4};\n    set<int> B = {3, 4, 5, 6};\n\n    set<int> result;\n    for (int x : A) result.insert(x);\n    for (int x : B) result.insert(x);\n\n    for (int x : result) cout << x << \" \";\n    return 0;\n}",
                "output": "1 2 3 4 5 6"
            }
        },

        "dry_run": """
A = {1, 2, 3}
B = {3, 4, 5}

A & B:
Only 3 is common.
Result: {3}

A | B:
Combine unique elements.
Result: {1, 2, 3, 4, 5}

A - B:
Keep elements in A but not B.
Result: {1, 2}
""",

        "practice_questions": [
            {
                "level": "Beginner",
                "question": "Remove duplicate elements from a list and print the number of unique elements.",
                "sample_input": "6\n1 2 2 3 3 4",
                "sample_output": "4",
                "solutions": {
                    "python": "n = int(input())\narr = list(map(int, input().split()))\nunique = set(arr[:n])\nprint(len(unique))",
                    "java": "import java.util.*;\npublic class Main {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int n = sc.nextInt();\n        Set<Integer> unique = new HashSet<>();\n        for (int i = 0; i < n; i++) unique.add(sc.nextInt());\n        System.out.println(unique.size());\n    }\n}",
                    "cpp": "#include <iostream>\n#include <unordered_set>\nusing namespace std;\nint main() {\n    int n, x;\n    cin >> n;\n    unordered_set<int> unique;\n    for (int i = 0; i < n; i++) {\n        cin >> x;\n        unique.insert(x);\n    }\n    cout << unique.size();\n    return 0;\n}"
                },
                "explanation": "A set stores each distinct value only once. Its size gives the number of unique values."
            },
            {
                "level": "Intermediate",
                "question": "Find the common elements between two integer collections.",
                "sample_input": "4\n1 2 3 4\n3 4 5 6",
                "sample_output": "3 4",
                "solutions": {
                    "python": "n = int(input())\nA = set(map(int, input().split()))\nB = set(map(int, input().split()))\nprint(*sorted(A & B))",
                    "java": "import java.util.*;\npublic class Main {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int n = sc.nextInt();\n        Set<Integer> A = new TreeSet<>();\n        Set<Integer> B = new TreeSet<>();\n        for (int i = 0; i < n; i++) A.add(sc.nextInt());\n        for (int i = 0; i < n; i++) B.add(sc.nextInt());\n        A.retainAll(B);\n        for (int x : A) System.out.print(x + \" \");\n    }\n}",
                    "cpp": "#include <iostream>\n#include <set>\nusing namespace std;\nint main() {\n    int n, x;\n    cin >> n;\n    set<int> A, B;\n    for (int i = 0; i < n; i++) { cin >> x; A.insert(x); }\n    for (int i = 0; i < n; i++) { cin >> x; B.insert(x); }\n    for (int value : A) {\n        if (B.count(value)) cout << value << \" \";\n    }\n    return 0;\n}"
                },
                "explanation": "Set intersection keeps only values present in both collections. Sorting makes the displayed result predictable."
            }
        ],

        "interview_questions": [
            {
                "question": "Why are sets useful?",
                "answer": "Sets automatically maintain unique hashable values and provide efficient average membership testing."
            },
            {
                "question": "What is the difference between remove() and discard()?",
                "answer": "remove() raises KeyError when an element is absent. discard() does not."
            },
            {
                "question": "Can a list be an element of a Python set?",
                "answer": "No. Lists are mutable and unhashable. A tuple of hashable values can be a set element."
            }
        ],

        "mcqs": [
            {
                "question": "Which creates an empty Python set?",
                "options": ["{}", "[]", "set()", "()"],
                "answer": "set()",
                "explanation": "{} creates an empty dictionary."
            },
            {
                "question": "Which operator performs set intersection?",
                "options": ["|", "&", "-", "^"],
                "answer": "&",
                "explanation": "& returns elements common to both sets."
            },
            {
                "question": "Which set method does not raise an error if the element is absent?",
                "options": ["remove()", "discard()", "pop()", "delete()"],
                "answer": "discard()",
                "explanation": "discard() silently does nothing if the value is not present."
            }
        ]
    },

    # =========================================================
    # 11. DICTIONARIES
    # =========================================================

    "python-dictionaries": {
        "id": "python-dictionaries",
        "title": "Python Dictionaries",
        "duration": "40 min",

        "content": """
# Python Dictionaries

A dictionary stores data as key-value pairs.

Example:
student = {
    "name": "Aman",
    "age": 21,
    "marks": 90
}

Here:
- name, age and marks are keys.
- Aman, 21 and 90 are corresponding values.

## 1. Creating Dictionaries

student = {"name": "Aman", "age": 21}

Keys must be hashable and unique.
Values can be of different types.

## 2. Accessing Values

student["name"]

This returns the value associated with name.

student.get("name")

get() can safely return a default value when the key is absent.

Difference:
- student["city"] raises KeyError if city is missing.
- student.get("city") returns None by default.

## 3. Adding and Updating

student["city"] = "Delhi"

This adds a new key or updates an existing key.

student.update({"age": 22})

## 4. Removing Elements

pop(key): Removes a key and returns its value.
popitem(): Removes and returns the most recently inserted key-value pair.
del: Deletes a key.
clear(): Removes all items.

## 5. Important Dictionary Methods

keys(): Returns a view of keys.
values(): Returns a view of values.
items(): Returns key-value pairs.
get(): Safely retrieves a value.
update(): Adds or updates entries.
setdefault(): Returns a value and inserts a default if the key is absent.

## 6. Iterating Through Dictionaries

for key, value in student.items():
    print(key, value)

## 7. Dictionary Comprehension

squares = {x: x*x for x in range(1, 4)}

Result:
{1: 1, 2: 4, 3: 9}

## 8. Frequency Counting

A very common DSA use case:

arr = [1, 2, 2, 3, 2]
frequency = {}

for x in arr:
    frequency[x] = frequency.get(x, 0) + 1

Result:
{1: 1, 2: 3, 3: 1}

## 9. Time Complexity

Dictionary lookup, insertion and deletion are O(1) on average.

In unusual collision-heavy cases, operations can take longer.

## 10. Dictionary vs List

List:
- Access by numerical index.
- Stores ordered elements.

Dictionary:
- Access by key.
- Stores key-value pairs.
- Keys are unique.
""",

        "key_concepts": [
            "Key-value pairs",
            "Dictionary creation",
            "Accessing values",
            "get()",
            "Adding and updating",
            "pop() and del",
            "keys(), values() and items()",
            "Dictionary iteration",
            "Dictionary comprehension",
            "Frequency counting",
            "Hashing and average O(1) lookup"
        ],

        "examples": {
            "python": {
                "code": "student = {\n    'name': 'Aman',\n    'age': 21,\n    'marks': 90\n}\n\nstudent['city'] = 'Delhi'\nprint(student['name'])\nprint(student.get('city'))\n\nfor key, value in student.items():\n    print(key, value)",
                "output": "Aman\nDelhi\nname Aman\nage 21\nmarks 90\ncity Delhi"
            },
            "java": {
                "code": "import java.util.*;\npublic class Main {\n    public static void main(String[] args) {\n        Map<String, Object> student = new LinkedHashMap<>();\n        student.put(\"name\", \"Aman\");\n        student.put(\"age\", 21);\n        student.put(\"marks\", 90);\n        student.put(\"city\", \"Delhi\");\n\n        System.out.println(student.get(\"name\"));\n        System.out.println(student.get(\"city\"));\n\n        for (Map.Entry<String, Object> entry : student.entrySet()) {\n            System.out.println(entry.getKey() + \" \" + entry.getValue());\n        }\n    }\n}",
                "output": "Aman\nDelhi\nname Aman\nage 21\nmarks 90\ncity Delhi"
            },
            "cpp": {
                "code": "#include <iostream>\n#include <map>\nusing namespace std;\n\nint main() {\n    map<string, string> student;\n    student[\"name\"] = \"Aman\";\n    student[\"city\"] = \"Delhi\";\n\n    cout << student[\"name\"] << endl;\n    cout << student[\"city\"] << endl;\n    return 0;\n}",
                "output": "Aman\nDelhi"
            }
        },

        "dry_run": """
arr = [1, 2, 2, 3]
frequency = {}

First element: 1
frequency[1] = 1

Second element: 2
frequency[2] = 1

Third element: 2
frequency[2] = 2

Fourth element: 3
frequency[3] = 1

Final dictionary:
{1: 1, 2: 2, 3: 1}
""",

        "practice_questions": [
            {
                "level": "Beginner",
                "question": "Create a dictionary containing name and age. Print the name and age.",
                "sample_input": "No input required",
                "sample_output": "Aman\n21",
                "solutions": {
                    "python": "student = {'name': 'Aman', 'age': 21}\nprint(student['name'])\nprint(student['age'])",
                    "java": "import java.util.*;\npublic class Main {\n    public static void main(String[] args) {\n        Map<String, Object> student = new HashMap<>();\n        student.put(\"name\", \"Aman\");\n        student.put(\"age\", 21);\n        System.out.println(student.get(\"name\"));\n        System.out.println(student.get(\"age\"));\n    }\n}",
                    "cpp": "#include <iostream>\n#include <map>\nusing namespace std;\nint main() {\n    map<string, string> student;\n    student[\"name\"] = \"Aman\";\n    student[\"age\"] = \"21\";\n    cout << student[\"name\"] << endl;\n    cout << student[\"age\"] << endl;\n    return 0;\n}"
                },
                "explanation": "Store values using keys and retrieve them using those keys."
            },
            {
                "level": "Intermediate",
                "question": "Count the frequency of every integer in an array.",
                "sample_input": "6\n1 2 2 3 1 2",
                "sample_output": "1: 2\n2: 3\n3: 1",
                "solutions": {
                    "python": "n = int(input())\narr = list(map(int, input().split()))\nfreq = {}\nfor x in arr[:n]:\n    freq[x] = freq.get(x, 0) + 1\nfor key in sorted(freq):\n    print(f'{key}: {freq[key]}')",
                    "java": "import java.util.*;\npublic class Main {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int n = sc.nextInt();\n        Map<Integer, Integer> freq = new TreeMap<>();\n        for (int i = 0; i < n; i++) {\n            int x = sc.nextInt();\n            freq.put(x, freq.getOrDefault(x, 0) + 1);\n        }\n        for (int key : freq.keySet()) {\n            System.out.println(key + \": \" + freq.get(key));\n        }\n    }\n}",
                    "cpp": "#include <iostream>\n#include <map>\nusing namespace std;\nint main() {\n    int n, x;\n    cin >> n;\n    map<int, int> freq;\n    for (int i = 0; i < n; i++) {\n        cin >> x;\n        freq[x]++;\n    }\n    for (auto p : freq) {\n        cout << p.first << \": \" << p.second << endl;\n    }\n    return 0;\n}"
                },
                "explanation": "For each number, increase its frequency by one. get(x, 0) starts a new count at zero. Sorted keys make the output predictable."
            }
        ],

        "interview_questions": [
            {
                "question": "What is a dictionary in Python?",
                "answer": "A dictionary is a mutable mapping that stores key-value pairs. Keys are unique and must be hashable."
            },
            {
                "question": "What is the difference between get() and square-bracket access?",
                "answer": "get() can return a default value for a missing key. Square-bracket access raises KeyError when the key is absent."
            },
            {
                "question": "What is the average lookup complexity of a dictionary?",
                "answer": "O(1) average time, assuming a good hash distribution."
            },
            {
                "question": "What does items() return?",
                "answer": "It returns a view of the dictionary's key-value pairs."
            }
        ],

        "mcqs": [
            {
                "question": "Which data structure stores key-value pairs in Python?",
                "options": ["List", "Tuple", "Dictionary", "Set"],
                "answer": "Dictionary",
                "explanation": "A dictionary maps unique keys to values."
            },
            {
                "question": "What happens when you access a missing dictionary key using d['x']?",
                "options": ["Returns None", "Returns 0", "Raises KeyError", "Creates the key"],
                "answer": "Raises KeyError",
                "explanation": "Direct square-bracket access raises KeyError when the key is absent."
            },
            {
                "question": "Which method returns key-value pairs?",
                "options": ["keys()", "values()", "items()", "pairs()"],
                "answer": "items()",
                "explanation": "items() returns a view containing key-value pairs."
            }
        ]
    }

})


PYTHON_FOUNDATIONS.update({

    # =========================================================
    # 12. CLASSES AND OBJECTS
    # =========================================================

    "python-oops-classes": {
        "id": "python-oops-classes",
        "title": "OOPS: Classes and Objects",
        "duration": "40 min",

        "content": """
# Object-Oriented Programming (OOPS)

OOPS is a programming paradigm based on objects and classes.

It helps organize code into reusable components.

## 1. What is a Class?

A class is a blueprint or template used to create objects.

Example:
class Student:
    pass

Here Student is a class.

## 2. What is an Object?

An object is an instance of a class.

s1 = Student()
s2 = Student()

Here s1 and s2 are two different objects of Student.

## 3. Attributes

Attributes represent the data associated with an object.

class Student:
    name = "Aman"
    age = 21

## 4. Constructor: __init__()

A constructor-like initializer is used to initialize a newly created object.

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Aman", 21)

__init__() is automatically called after an object is created.

Technically, __new__() creates the object, while __init__() initializes it.

## 5. What is self?

self refers to the current instance.

It allows methods to access that object's attributes and other instance methods.

Example:
class Student:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(self.name)

## 6. Instance Methods

Methods that receive self and operate on an object.

## 7. Class Variables

Variables shared by instances through the class.

class Student:
    college = "ABC College"

## 8. Class Methods

Use @classmethod. The first parameter conventionally receives the class as cls.

They can access and modify class-level state.

## 9. Static Methods

Use @staticmethod.

They do not automatically receive self or cls.

They are useful for utility operations related to a class.

## 10. Why OOPS?

- Code reusability
- Modularity
- Maintainability
- Data organization
- Easier modeling of real-world entities

## 11. Class vs Object

Class:
A blueprint.

Object:
A specific instance created using that blueprint.
""",

        "key_concepts": [
            "Object-oriented programming",
            "Class",
            "Object",
            "Attributes",
            "__init__()",
            "self",
            "Instance methods",
            "Class variables",
            "@classmethod",
            "@staticmethod"
        ],

        "examples": {
            "python": {
                "code": "class Student:\n    college = 'ABC College'\n\n    def __init__(self, name, age):\n        self.name = name\n        self.age = age\n\n    def display(self):\n        print(self.name, self.age, Student.college)\n\ns1 = Student('Aman', 21)\ns2 = Student('Riya', 20)\ns1.display()\ns2.display()",
                "output": "Aman 21 ABC College\nRiya 20 ABC College"
            },
            "java": {
                "code": "class Student {\n    static String college = \"ABC College\";\n    String name;\n    int age;\n\n    Student(String name, int age) {\n        this.name = name;\n        this.age = age;\n    }\n\n    void display() {\n        System.out.println(name + \" \" + age + \" \" + college);\n    }\n}\n\npublic class Main {\n    public static void main(String[] args) {\n        Student s1 = new Student(\"Aman\", 21);\n        Student s2 = new Student(\"Riya\", 20);\n        s1.display();\n        s2.display();\n    }\n}",
                "output": "Aman 21 ABC College\nRiya 20 ABC College"
            },
            "cpp": {
                "code": "#include <iostream>\n#include <string>\nusing namespace std;\n\nclass Student {\npublic:\n    static string college;\n    string name;\n    int age;\n\n    Student(string n, int a) {\n        name = n;\n        age = a;\n    }\n\n    void display() {\n        cout << name << \" \" << age << \" \" << college << endl;\n    }\n};\n\nstring Student::college = \"ABC College\";\n\nint main() {\n    Student s1(\"Aman\", 21);\n    Student s2(\"Riya\", 20);\n    s1.display();\n    s2.display();\n    return 0;\n}",
                "output": "Aman 21 ABC College\nRiya 20 ABC College"
            }
        },

        "dry_run": """
s1 = Student("Aman", 21)

1. Python creates a new Student object.
2. __init__() initializes that object.
3. self refers to the new object.
4. self.name stores "Aman".
5. self.age stores 21.
6. s1 refers to the initialized object.

Calling s1.display() prints:
Aman 21 ABC College
""",

        "practice_questions": [
            {
                "level": "Beginner",
                "question": "Create a Rectangle class with length and breadth. Add a method to calculate its area.",
                "sample_input": "10 5",
                "sample_output": "50",
                "solutions": {
                    "python": "class Rectangle:\n    def __init__(self, length, breadth):\n        self.length = length\n        self.breadth = breadth\n\n    def area(self):\n        return self.length * self.breadth\n\nl, b = map(int, input().split())\nr = Rectangle(l, b)\nprint(r.area())",
                    "java": "import java.util.*;\nclass Rectangle {\n    int length, breadth;\n    Rectangle(int l, int b) {\n        length = l;\n        breadth = b;\n    }\n    int area() {\n        return length * breadth;\n    }\n}\npublic class Main {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        Rectangle r = new Rectangle(sc.nextInt(), sc.nextInt());\n        System.out.println(r.area());\n    }\n}",
                    "cpp": "#include <iostream>\nusing namespace std;\nclass Rectangle {\n    int length, breadth;\npublic:\n    Rectangle(int l, int b) : length(l), breadth(b) {}\n    int area() { return length * breadth; }\n};\nint main() {\n    int l, b;\n    cin >> l >> b;\n    Rectangle r(l, b);\n    cout << r.area();\n    return 0;\n}"
                },
                "explanation": "The constructor initializes the rectangle's dimensions. The area method multiplies length by breadth."
            }
        ],

        "interview_questions": [
            {
                "question": "What is a class?",
                "answer": "A class is a blueprint that defines the attributes and methods of its objects."
            },
            {
                "question": "What is an object?",
                "answer": "An object is an instance of a class."
            },
            {
                "question": "What is self?",
                "answer": "self refers to the current instance and is used to access its attributes and methods."
            },
            {
                "question": "What is the difference between a class method and a static method?",
                "answer": "A class method receives the class as cls. A static method receives neither self nor cls automatically."
            }
        ],

        "mcqs": [
            {
                "question": "Which method initializes an instance in Python?",
                "options": ["__start__()", "__init__()", "constructor()", "init()"],
                "answer": "__init__()",
                "explanation": "__init__() initializes an instance after it has been created."
            },
            {
                "question": "What does self represent?",
                "options": ["The parent class", "The current instance", "The module", "The constructor"],
                "answer": "The current instance",
                "explanation": "self refers to the instance on which an instance method is called."
            },
            {
                "question": "Which decorator defines a static method?",
                "options": ["@classmethod", "@staticmethod", "@property", "@abstractmethod"],
                "answer": "@staticmethod",
                "explanation": "@staticmethod creates a method that receives no automatic instance or class argument."
            }
        ]
    },

    # =========================================================
    # 13. ENCAPSULATION AND INHERITANCE
    # =========================================================

    "python-oops-encapsulation": {
        "id": "python-oops-encapsulation",
        "title": "Encapsulation and Access Control",
        "duration": "35 min",

        "content": """
# Encapsulation

Encapsulation means combining data and the methods that operate on that data within a class.

It also involves controlling how internal state is accessed and modified.

## 1. Public Members

Public members can be accessed from outside the class.

Example:
self.name = "Aman"

## 2. Protected Convention

A single leading underscore indicates that an attribute is intended for internal or subclass use.

Example:
self._salary = 50000

Important:
Python does not strictly enforce protected access using a single underscore.

## 3. Private Name Mangling

A double leading underscore triggers name mangling.

Example:
self.__balance = 5000

Python changes the internal attribute name to include the class name.

This helps avoid accidental access and naming conflicts, but it is not absolute security.

## 4. Getters and Setters

Getter: Reads an attribute.
Setter: Updates an attribute after validation.

Python commonly uses @property.

## 5. Inheritance

Inheritance allows a class to derive attributes and methods from another class.

Parent class: Base class.
Child class: Derived class.

Example:
class Animal:
    def eat(self):
        print("Eating")

class Dog(Animal):
    def bark(self):
        print("Barking")

Dog inherits eat() from Animal.

## 6. Types of Inheritance

Single inheritance:
One child inherits from one parent.

Multilevel inheritance:
A child inherits from a class that already inherits from another class.

Hierarchical inheritance:
Multiple child classes inherit from one parent.

Multiple inheritance:
One child inherits from multiple parents.

Hybrid inheritance:
A combination of inheritance patterns.

Python supports all these patterns.

## 7. super()

super() provides access to methods in the next class in the method resolution order.

It is commonly used to call a parent initializer or extend parent behavior.
""",

        "key_concepts": [
            "Encapsulation",
            "Public members",
            "Protected naming convention",
            "Private name mangling",
            "@property",
            "Getter and setter",
            "Inheritance",
            "Single inheritance",
            "Multilevel inheritance",
            "Multiple inheritance",
            "Hierarchical inheritance",
            "super()"
        ],

        "examples": {
            "python": {
                "code": "class BankAccount:\n    def __init__(self, balance):\n        self.__balance = balance\n\n    def deposit(self, amount):\n        if amount > 0:\n            self.__balance += amount\n\n    def get_balance(self):\n        return self.__balance\n\nclass SavingsAccount(BankAccount):\n    def show_type(self):\n        print('Savings Account')\n\naccount = SavingsAccount(1000)\naccount.deposit(500)\naccount.show_type()\nprint(account.get_balance())",
                "output": "Savings Account\n1500"
            },
            "java": {
                "code": "class BankAccount {\n    private int balance;\n\n    BankAccount(int balance) {\n        this.balance = balance;\n    }\n\n    void deposit(int amount) {\n        if (amount > 0) balance += amount;\n    }\n\n    int getBalance() {\n        return balance;\n    }\n}\n\nclass SavingsAccount extends BankAccount {\n    SavingsAccount(int balance) {\n        super(balance);\n    }\n\n    void showType() {\n        System.out.println(\"Savings Account\");\n    }\n}\n\npublic class Main {\n    public static void main(String[] args) {\n        SavingsAccount account = new SavingsAccount(1000);\n        account.deposit(500);\n        account.showType();\n        System.out.println(account.getBalance());\n    }\n}",
                "output": "Savings Account\n1500"
            },
            "cpp": {
                "code": "#include <iostream>\nusing namespace std;\n\nclass BankAccount {\nprivate:\n    int balance;\npublic:\n    BankAccount(int b) : balance(b) {}\n    void deposit(int amount) {\n        if (amount > 0) balance += amount;\n    }\n    int getBalance() { return balance; }\n};\n\nclass SavingsAccount : public BankAccount {\npublic:\n    SavingsAccount(int b) : BankAccount(b) {}\n    void showType() { cout << \"Savings Account\" << endl; }\n};\n\nint main() {\n    SavingsAccount account(1000);\n    account.deposit(500);\n    account.showType();\n    cout << account.getBalance();\n    return 0;\n}",
                "output": "Savings Account\n1500"
            }
        },

        "dry_run": """
account = SavingsAccount(1000)

1. SavingsAccount inherits from BankAccount.
2. The BankAccount initializer stores 1000.
3. deposit(500) checks that the amount is positive.
4. Balance becomes 1500.
5. get_balance() returns 1500.

Output:
Savings Account
1500
""",

        "practice_questions": [
            {
                "level": "Intermediate",
                "question": "Create a BankAccount class with a private balance. Implement deposit and get_balance methods. Reject non-positive deposits.",
                "sample_input": "1000 500",
                "sample_output": "1500",
                "solutions": {
                    "python": "class BankAccount:\n    def __init__(self, balance):\n        self.__balance = balance\n\n    def deposit(self, amount):\n        if amount > 0:\n            self.__balance += amount\n\n    def get_balance(self):\n        return self.__balance\n\nbalance, amount = map(int, input().split())\naccount = BankAccount(balance)\naccount.deposit(amount)\nprint(account.get_balance())",
                    "java": "import java.util.*;\nclass BankAccount {\n    private int balance;\n    BankAccount(int balance) { this.balance = balance; }\n    void deposit(int amount) {\n        if (amount > 0) balance += amount;\n    }\n    int getBalance() { return balance; }\n}\npublic class Main {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        BankAccount account = new BankAccount(sc.nextInt());\n        account.deposit(sc.nextInt());\n        System.out.println(account.getBalance());\n    }\n}",
                    "cpp": "#include <iostream>\nusing namespace std;\nclass BankAccount {\nprivate:\n    int balance;\npublic:\n    BankAccount(int b) : balance(b) {}\n    void deposit(int amount) {\n        if (amount > 0) balance += amount;\n    }\n    int getBalance() { return balance; }\n};\nint main() {\n    int balance, amount;\n    cin >> balance >> amount;\n    BankAccount account(balance);\n    account.deposit(amount);\n    cout << account.getBalance();\n    return 0;\n}"
                },
                "explanation": "The balance is private, so it is modified through the deposit method rather than directly."
            }
        ],

        "interview_questions": [
            {
                "question": "What is encapsulation?",
                "answer": "Encapsulation combines data and related methods in a class and provides controlled access to internal state."
            },
            {
                "question": "Does Python support private variables?",
                "answer": "Python uses double-leading-underscore name mangling. It discourages direct access but does not provide strict private access control."
            },
            {
                "question": "What is inheritance?",
                "answer": "Inheritance allows a child class to reuse or extend functionality from a parent class."
            },
            {
                "question": "What is super()?",
                "answer": "super() provides access to the next class in the method resolution order, commonly for calling inherited methods."
            }
        ],

        "mcqs": [
            {
                "question": "Which naming style triggers name mangling in Python?",
                "options": ["name", "_name", "__name", "name__"],
                "answer": "__name",
                "explanation": "A double leading underscore triggers name mangling."
            },
            {
                "question": "Which keyword is used for inheritance in Java?",
                "options": ["inherits", "extends", "implements", "super"],
                "answer": "extends",
                "explanation": "Java uses extends for class inheritance."
            },
            {
                "question": "Which function is commonly used to access the next class in Python's MRO?",
                "options": ["parent()", "base()", "super()", "this()"],
                "answer": "super()",
                "explanation": "super() follows the method resolution order."
            }
        ]
    },

    # =========================================================
    # 14. POLYMORPHISM
    # =========================================================

    "python-oops-polymorphism": {
        "id": "python-oops-polymorphism",
        "title": "Polymorphism and Method Overriding",
        "duration": "35 min",

        "content": """
# Polymorphism

Polymorphism means one interface or operation can work with different types of objects.

The same method name can produce different behavior depending on the object.

## 1. Method Overriding

A child class provides its own implementation of a method defined by a parent class.

Example:

class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

Dog().sound()

Output:
Bark

## 2. Runtime Polymorphism

When a method call is resolved based on the actual object's class, it is runtime polymorphism.

## 3. Duck Typing in Python

Python focuses on whether an object supports the required behavior rather than its declared type.

If an object has the required method, it can often be used.

Example:
class Dog:
    def sound(self):
        print("Bark")

class Cat:
    def sound(self):
        print("Meow")

def make_sound(animal):
    animal.sound()

make_sound(Dog())
make_sound(Cat())

## 4. Method Overloading

Traditional method overloading means defining multiple methods with the same name but different parameter lists.

Python does not support traditional signature-based method overloading in the same way as Java or C++.

Common alternatives:
- Default arguments
- *args and **kwargs
- Single-dispatch or other dispatch mechanisms

## 5. Operator Overloading

Python lets classes define how operators behave using special methods.

Examples:
__add__(): +
__sub__(): -
__mul__(): *
__eq__(): ==

## 6. Polymorphism Benefits

- Flexible code
- Reusable interfaces
- Easier extension
- Less dependence on specific classes
""",

        "key_concepts": [
            "Polymorphism",
            "Method overriding",
            "Runtime polymorphism",
            "Duck typing",
            "Method overloading",
            "Operator overloading",
            "Special methods"
        ],

        "examples": {
            "python": {
                "code": "class Animal:\n    def sound(self):\n        print('Animal sound')\n\nclass Dog(Animal):\n    def sound(self):\n        print('Bark')\n\nclass Cat(Animal):\n    def sound(self):\n        print('Meow')\n\ndef make_sound(animal):\n    animal.sound()\n\nmake_sound(Dog())\nmake_sound(Cat())",
                "output": "Bark\nMeow"
            },
            "java": {
                "code": "class Animal {\n    void sound() {\n        System.out.println(\"Animal sound\");\n    }\n}\nclass Dog extends Animal {\n    @Override\n    void sound() {\n        System.out.println(\"Bark\");\n    }\n}\nclass Cat extends Animal {\n    @Override\n    void sound() {\n        System.out.println(\"Meow\");\n    }\n}\npublic class Main {\n    public static void main(String[] args) {\n        Animal a = new Dog();\n        a.sound();\n        a = new Cat();\n        a.sound();\n    }\n}",
                "output": "Bark\nMeow"
            },
            "cpp": {
                "code": "#include <iostream>\nusing namespace std;\n\nclass Animal {\npublic:\n    virtual void sound() {\n        cout << \"Animal sound\" << endl;\n    }\n    virtual ~Animal() = default;\n};\nclass Dog : public Animal {\npublic:\n    void sound() override { cout << \"Bark\" << endl; }\n};\nclass Cat : public Animal {\npublic:\n    void sound() override { cout << \"Meow\" << endl; }\n};\nint main() {\n    Dog d;\n    Cat c;\n    Animal* a = &d;\n    a->sound();\n    a = &c;\n    a->sound();\n    return 0;\n}",
                "output": "Bark\nMeow"
            }
        },

        "dry_run": """
make_sound(Dog())

1. A Dog object is created.
2. The object is passed to make_sound().
3. animal refers to the Dog object.
4. animal.sound() invokes Dog.sound().
5. Bark is printed.

Next, Cat is passed.
Cat.sound() prints Meow.

Output:
Bark
Meow
""",

        "practice_questions": [
            {
                "level": "Intermediate",
                "question": "Create a Shape base class and Circle and Rectangle child classes. Override area() in each child class.",
                "sample_input": "Circle radius = 7\nRectangle length = 4 breadth = 5",
                "sample_output": "153.94\n20",
                "solutions": {
                    "python": "class Shape:\n    def area(self):\n        raise NotImplementedError\n\nclass Circle(Shape):\n    def __init__(self, radius):\n        self.radius = radius\n    def area(self):\n        return 3.14 * self.radius * self.radius\n\nclass Rectangle(Shape):\n    def __init__(self, length, breadth):\n        self.length = length\n        self.breadth = breadth\n    def area(self):\n        return self.length * self.breadth\n\nshapes = [Circle(7), Rectangle(4, 5)]\nfor shape in shapes:\n    print(shape.area())",
                    "java": "abstract class Shape {\n    abstract double area();\n}\nclass Circle extends Shape {\n    double radius;\n    Circle(double r) { radius = r; }\n    double area() { return 3.14 * radius * radius; }\n}\nclass Rectangle extends Shape {\n    double length, breadth;\n    Rectangle(double l, double b) { length = l; breadth = b; }\n    double area() { return length * breadth; }\n}\npublic class Main {\n    public static void main(String[] args) {\n        Shape[] shapes = {new Circle(7), new Rectangle(4, 5)};\n        for (Shape s : shapes) System.out.println(s.area());\n    }\n}",
                    "cpp": "#include <iostream>\nusing namespace std;\nclass Shape {\npublic:\n    virtual double area() = 0;\n    virtual ~Shape() = default;\n};\nclass Circle : public Shape {\n    double r;\npublic:\n    Circle(double radius) : r(radius) {}\n    double area() override { return 3.14 * r * r; }\n};\nclass Rectangle : public Shape {\n    double l, b;\npublic:\n    Rectangle(double length, double breadth) : l(length), b(breadth) {}\n    double area() override { return l * b; }\n};\nint main() {\n    Circle c(7);\n    Rectangle r(4, 5);\n    cout << c.area() << endl << r.area();\n    return 0;\n}"
                },
                "explanation": "Each child class supplies its own area() implementation. A common interface lets us work with different shapes."
            }
        ],

        "interview_questions": [
            {
                "question": "What is polymorphism?",
                "answer": "Polymorphism allows the same interface or operation to behave differently for different object types."
            },
            {
                "question": "What is method overriding?",
                "answer": "A child class provides its own implementation of a method inherited from its parent."
            },
            {
                "question": "Does Python support traditional method overloading?",
                "answer": "Python does not support traditional signature-based method overloading directly. Default arguments and variable-length arguments are common alternatives."
            },
            {
                "question": "What is duck typing?",
                "answer": "Duck typing focuses on the operations an object supports rather than its declared class."
            }
        ],

        "mcqs": [
            {
                "question": "Which OOPS concept allows the same method name to behave differently for different objects?",
                "options": ["Encapsulation", "Polymorphism", "Inheritance", "Abstraction"],
                "answer": "Polymorphism",
                "explanation": "Polymorphism allows different implementations behind a common interface."
            },
            {
                "question": "Which Python special method overloads the + operator?",
                "options": ["__sum__()", "__plus__()", "__add__()", "__append__()"],
                "answer": "__add__()",
                "explanation": "__add__() defines behavior for the + operator."
            }
        ]
    },

    # =========================================================
    # 15. ABSTRACTION AND MRO
    # =========================================================

    "python-oops-abstraction": {
        "id": "python-oops-abstraction",
        "title": "Abstraction, Abstract Classes and MRO",
        "duration": "40 min",

        "content": """
# Abstraction

Abstraction means exposing essential functionality while hiding implementation details.

For example, when using an ATM, you choose to withdraw money without needing to understand the internal banking system.

## 1. Abstract Classes

Python provides the abc module for abstract base classes.

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

An abstract class can define methods that subclasses must implement.

## 2. Abstract Methods

An abstract method declares an interface or required behavior.

A concrete child class must implement its inherited abstract methods before it can be instantiated.

## 3. Creating an Abstract Class

from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class UPI(Payment):
    def pay(self, amount):
        print("Paid", amount)

payment = UPI()
payment.pay(500)

## 4. Abstraction vs Encapsulation

Abstraction:
Focuses on what an object does and hides implementation details.

Encapsulation:
Combines data and methods and controls access to internal state.

## 5. Method Resolution Order (MRO)

MRO determines the order in which Python searches classes for an inherited attribute or method.

Use:
ClassName.mro()

Python uses C3 linearization to calculate the MRO.

## 6. Multiple Inheritance

A class can inherit from more than one parent class.

class A:
    def show(self):
        print("A")

class B:
    def show(self):
        print("B")

class C(A, B):
    pass

C().show()

The method resolution order determines which implementation is selected.

## 7. super() and Cooperative Inheritance

super() follows the MRO, not simply the direct parent.

This is important when working with multiple inheritance.

## 8. Four Pillars of OOPS

1. Encapsulation
2. Inheritance
3. Polymorphism
4. Abstraction

Remember these four concepts for placement interviews.
""",

        "key_concepts": [
            "Abstraction",
            "Abstract base class",
            "ABC module",
            "@abstractmethod",
            "Abstract vs concrete class",
            "Abstraction vs encapsulation",
            "Multiple inheritance",
            "Method resolution order",
            "C3 linearization",
            "Cooperative super()"
        ],

        "examples": {
            "python": {
                "code": "from abc import ABC, abstractmethod\n\nclass Payment(ABC):\n    @abstractmethod\n    def pay(self, amount):\n        pass\n\nclass UPI(Payment):\n    def pay(self, amount):\n        print('Paid:', amount)\n\npayment = UPI()\npayment.pay(500)",
                "output": "Paid: 500"
            },
            "java": {
                "code": "abstract class Payment {\n    abstract void pay(int amount);\n}\nclass UPI extends Payment {\n    @Override\n    void pay(int amount) {\n        System.out.println(\"Paid: \" + amount);\n    }\n}\npublic class Main {\n    public static void main(String[] args) {\n        Payment payment = new UPI();\n        payment.pay(500);\n    }\n}",
                "output": "Paid: 500"
            },
            "cpp": {
                "code": "#include <iostream>\nusing namespace std;\n\nclass Payment {\npublic:\n    virtual void pay(int amount) = 0;\n    virtual ~Payment() = default;\n};\nclass UPI : public Payment {\npublic:\n    void pay(int amount) override {\n        cout << \"Paid: \" << amount << endl;\n    }\n};\nint main() {\n    UPI payment;\n    payment.pay(500);\n    return 0;\n}",
                "output": "Paid: 500"
            }
        },

        "dry_run": """
payment = UPI()

1. Payment is an abstract class.
2. UPI inherits from Payment.
3. UPI implements the abstract pay() method.
4. An instance of UPI can now be created.
5. pay(500) is called.
6. The implementation prints Paid: 500.

Output:
Paid: 500
""",

        "practice_questions": [
            {
                "level": "Intermediate",
                "question": "Create an abstract Payment class with a pay() method. Implement it in a UPI class.",
                "sample_input": "500",
                "sample_output": "Paid: 500",
                "solutions": {
                    "python": "from abc import ABC, abstractmethod\n\nclass Payment(ABC):\n    @abstractmethod\n    def pay(self, amount):\n        pass\n\nclass UPI(Payment):\n    def pay(self, amount):\n        print('Paid:', amount)\n\namount = int(input())\npayment = UPI()\npayment.pay(amount)",
                    "java": "import java.util.*;\nabstract class Payment {\n    abstract void pay(int amount);\n}\nclass UPI extends Payment {\n    void pay(int amount) {\n        System.out.println(\"Paid: \" + amount);\n    }\n}\npublic class Main {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        Payment p = new UPI();\n        p.pay(sc.nextInt());\n    }\n}",
                    "cpp": "#include <iostream>\nusing namespace std;\nclass Payment {\npublic:\n    virtual void pay(int amount) = 0;\n    virtual ~Payment() = default;\n};\nclass UPI : public Payment {\npublic:\n    void pay(int amount) override {\n        cout << \"Paid: \" << amount;\n    }\n};\nint main() {\n    int amount;\n    cin >> amount;\n    UPI p;\n    p.pay(amount);\n    return 0;\n}"
                },
                "explanation": "The abstract class defines the required interface. UPI supplies the concrete implementation."
            }
        ],

        "interview_questions": [
            {
                "question": "What is abstraction?",
                "answer": "Abstraction exposes essential operations while hiding implementation details."
            },
            {
                "question": "Can we instantiate an abstract class?",
                "answer": "No. An abstract class containing unimplemented abstract methods cannot be instantiated directly."
            },
            {
                "question": "What is MRO?",
                "answer": "Method Resolution Order is the order in which Python searches classes for inherited attributes and methods."
            },
            {
                "question": "What is the difference between abstraction and encapsulation?",
                "answer": "Abstraction hides implementation complexity. Encapsulation groups data and behavior and controls access to internal state."
            }
        ],

        "mcqs": [
            {
                "question": "Which module provides abstract base classes in Python?",
                "options": ["math", "abc", "os", "sys"],
                "answer": "abc",
                "explanation": "The abc module provides ABC and abstractmethod."
            },
            {
                "question": "Which decorator marks an abstract method?",
                "options": ["@staticmethod", "@classmethod", "@abstractmethod", "@property"],
                "answer": "@abstractmethod",
                "explanation": "@abstractmethod marks a method that concrete subclasses must implement."
            },
            {
                "question": "What does MRO stand for?",
                "options": ["Method Runtime Object", "Method Resolution Order", "Multiple Return Operation", "Module Reference Order"],
                "answer": "Method Resolution Order",
                "explanation": "MRO determines the method lookup order in inheritance."
            }
        ]
    }

})


PYTHON_FOUNDATIONS.update({
    "python-numpy": {
        "id": "python-numpy",
        "title": "NumPy – Numerical Computing in Python",
        "duration": "45 min",

        "content": """
# Introduction to NumPy

NumPy stands for Numerical Python. It is a Python library used for
fast numerical calculations and working with arrays.

It is widely used in Data Science, Machine Learning, scientific
computing and data analysis.

## 1. Why NumPy?

Python lists can store multiple values, but mathematical operations
on large lists can be slow.

NumPy provides:
- Fast numerical operations.
- Multidimensional arrays.
- Mathematical and statistical functions.
- Matrix operations.
- Broadcasting and vectorization.

## 2. Installing and importing NumPy

Install:
pip install numpy

Import:
import numpy as np

Here, np is the commonly used alias for NumPy.

## 3. NumPy Arrays

A NumPy array is a collection of elements of the same data type.

Example:
import numpy as np

arr = np.array([10, 20, 30, 40])

print(arr)

Output:
[10 20 30 40]

Unlike a normal Python list, a NumPy array generally stores
elements of a common data type.

## 4. Creating Arrays

Common functions:

np.array([1, 2, 3])
Creates an array from a list.

np.zeros(4)
Creates an array containing four zeros.

np.ones(3)
Creates an array containing three ones.

np.arange(1, 10, 2)
Creates values from 1 to 9 with a step of 2.

np.linspace(0, 10, 5)
Creates five equally spaced values between 0 and 10.

np.eye(3)
Creates a 3 x 3 identity matrix.

## 5. Array Properties

Important properties:

arr.ndim  -> Number of dimensions.
arr.shape -> Dimensions of the array.
arr.size  -> Total number of elements.
arr.dtype -> Data type of elements.

Example:
arr = np.array([[1, 2, 3], [4, 5, 6]])

print(arr.ndim)
print(arr.shape)
print(arr.size)

Output:
2
(2, 3)
6

## 6. Indexing and Slicing

NumPy indexing starts from zero.

arr = np.array([10, 20, 30, 40, 50])

print(arr[0])    # 10
print(arr[-1])   # 50
print(arr[1:4])  # [20 30 40]

For a two-dimensional array:

matrix = np.array([[1, 2, 3], [4, 5, 6]])

print(matrix[0, 1])  # 2
print(matrix[1, 2])  # 6
print(matrix[0, :])  # First row
print(matrix[:, 1])  # Second column

## 7. Vectorization

Vectorization means performing operations on entire arrays
without explicitly writing a Python loop.

Example:

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)
print(a * b)

Output:
[5 7 9]
[4 10 18]

This makes numerical code concise and efficient.

## 8. Broadcasting

Broadcasting allows NumPy to perform operations on arrays
with compatible shapes.

Example:

arr = np.array([10, 20, 30])
print(arr + 5)

Output:
[15 25 35]

NumPy automatically adds 5 to every element.

## 9. Mathematical Operations

arr = np.array([10, 20, 30, 40])

np.sum(arr)   # 100
np.mean(arr)  # 25.0
np.max(arr)   # 40
np.min(arr)   # 10
np.std(arr)   # Standard deviation

## 10. Axis in NumPy

For a two-dimensional array:

arr = np.array([[1, 2, 3], [4, 5, 6]])

np.sum(arr, axis=0)
Output: [5 7 9]

np.sum(arr, axis=1)
Output: [6 15]

axis=0 performs the operation column-wise.
axis=1 performs the operation row-wise.

## 11. Reshaping Arrays

reshape() changes the dimensions without changing the
number of elements.

arr = np.arange(1, 7)
matrix = arr.reshape(2, 3)

Output:
[[1 2 3]
 [4 5 6]]

The original array has six elements, so a 2 x 3 matrix is valid.

## 12. Filtering Arrays

arr = np.array([10, 25, 30, 45, 50])

result = arr[arr > 30]

print(result)

Output:
[45 50]

This is called Boolean indexing.

## 13. Random Numbers

np.random.randint(1, 10, size=5)

Generates five random integers between 1 and 9.

The output changes each time.

## 14. NumPy in Data Science

NumPy is useful for:
- Numerical data processing.
- Statistical calculations.
- Matrix operations.
- Machine Learning computations.
- Image processing.
- Preparing data for Pandas and Scikit-learn.

## 15. NumPy vs Python Lists

Python List:
- Can contain mixed data types.
- General-purpose collection.
- Mathematical operations often require loops.

NumPy Array:
- Usually contains elements of a common data type.
- Supports multidimensional arrays.
- Supports vectorized mathematical operations.
- Designed for efficient numerical computing.

## 16. NumPy vs Java and C++

NumPy is a Python library, not a Java or C++ library.

Comparable concepts:
- Java: Arrays and multidimensional arrays.
- C++: Arrays and std::vector.
- Python NumPy: ndarray.

NumPy provides convenient vectorized numerical operations
that are not directly available with ordinary arrays in
the same way.
""",

        "key_concepts": [
            "NumPy",
            "ndarray",
            "Array creation",
            "Array dimensions",
            "Indexing and slicing",
            "Vectorization",
            "Broadcasting",
            "Axis",
            "Reshape",
            "Boolean indexing",
            "Statistical functions"
        ],

        "examples": {
            "python": {
                "code": "import numpy as np\n\narr = np.array([[10, 20, 30], [40, 50, 60]])\n\nprint('Array:', arr)\nprint('Dimensions:', arr.ndim)\nprint('Shape:', arr.shape)\nprint('Total elements:', arr.size)\nprint('Column sums:', np.sum(arr, axis=0))\nprint('Row sums:', np.sum(arr, axis=1))",
                "output": "Array: [[10 20 30]\\n [40 50 60]]\\nDimensions: 2\\nShape: (2, 3)\\nTotal elements: 6\\nColumn sums: [50 70 90]\\nRow sums: [60 150]"
            }
        },

        "dry_run": """
arr = np.array([10, 20, 30])

arr + 5

Step 1: Original array = [10, 20, 30]
Step 2: Add 5 to the first element = 15
Step 3: Add 5 to the second element = 25
Step 4: Add 5 to the third element = 35

Final output: [15, 25, 35]
""",

        "practice_questions": [
            {
                "level": "Beginner",
                "question": "Create a NumPy array containing numbers from 1 to 10 and calculate its sum, mean, maximum and minimum.",
                "solutions": {
                    "python": "import numpy as np\narr = np.arange(1, 11)\nprint('Array:', arr)\nprint('Sum:', np.sum(arr))\nprint('Mean:', np.mean(arr))\nprint('Maximum:', np.max(arr))\nprint('Minimum:', np.min(arr))",
                    "java": "public class Main {\n    public static void main(String[] args) {\n        int[] arr = {1,2,3,4,5,6,7,8,9,10};\n        int sum = 0;\n        int min = arr[0], max = arr[0];\n        for (int x : arr) {\n            sum += x;\n            min = Math.min(min, x);\n            max = Math.max(max, x);\n        }\n        System.out.println(\"Sum: \" + sum);\n        System.out.println(\"Mean: \" + (sum / 10.0));\n        System.out.println(\"Maximum: \" + max);\n        System.out.println(\"Minimum: \" + min);\n    }\n}",
                    "cpp": "#include <iostream>\n#include <algorithm>\nusing namespace std;\nint main() {\n    int arr[] = {1,2,3,4,5,6,7,8,9,10};\n    int sum = 0;\n    for (int x : arr) sum += x;\n    cout << \"Sum: \" << sum << endl;\n    cout << \"Mean: \" << sum / 10.0 << endl;\n    cout << \"Maximum: \" << *max_element(arr, arr + 10) << endl;\n    cout << \"Minimum: \" << *min_element(arr, arr + 10) << endl;\n    return 0;\n}"
                },
                "explanation": "NumPy provides built-in aggregation functions. In Java and C++, we can calculate the same results using loops and standard library functions.",
                "sample_input": "Numbers: 1 2 3 4 5 6 7 8 9 10",
                "sample_output": "Sum: 55\nMean: 5.5\nMaximum: 10\nMinimum: 1"
            },
            {
                "level": "Intermediate",
                "question": "Given a NumPy array, select only the even numbers and calculate their sum.",
                "solutions": {
                    "python": "import numpy as np\narr = np.array([1, 2, 3, 4, 5, 6, 7, 8])\neven = arr[arr % 2 == 0]\nprint('Even numbers:', even)\nprint('Sum:', np.sum(even))",
                    "java": "public class Main {\n    public static void main(String[] args) {\n        int[] arr = {1,2,3,4,5,6,7,8};\n        int sum = 0;\n        System.out.print(\"Even numbers: \");\n        for (int x : arr) {\n            if (x % 2 == 0) {\n                System.out.print(x + \" \");\n                sum += x;\n            }\n        }\n        System.out.println(\"\\nSum: \" + sum);\n    }\n}",
                    "cpp": "#include <iostream>\nusing namespace std;\nint main() {\n    int arr[] = {1,2,3,4,5,6,7,8};\n    int sum = 0;\n    cout << \"Even numbers: \";\n    for (int x : arr) {\n        if (x % 2 == 0) {\n            cout << x << \" \";\n            sum += x;\n        }\n    }\n    cout << \"\\nSum: \" << sum;\n    return 0;\n}"
                },
                "explanation": "The NumPy condition arr % 2 == 0 creates a Boolean mask. Using that mask selects only even elements.",
                "sample_input": "[1, 2, 3, 4, 5, 6, 7, 8]",
                "sample_output": "Even numbers: [2 4 6 8]\nSum: 20"
            }
        ],

        "interview_questions": [
            {
                "question": "What is NumPy?",
                "answer": "NumPy is a Python library for efficient numerical computation and multidimensional array processing."
            },
            {
                "question": "What is an ndarray?",
                "answer": "ndarray is NumPy's N-dimensional array object. It stores elements in a structured, usually homogeneous data type."
            },
            {
                "question": "What is vectorization?",
                "answer": "Vectorization performs operations on entire arrays instead of explicitly writing loops for individual elements."
            },
            {
                "question": "What is broadcasting?",
                "answer": "Broadcasting allows NumPy to perform operations on arrays with compatible shapes, sometimes by treating smaller dimensions as if they were expanded."
            },
            {
                "question": "What is the difference between reshape() and resize()?",
                "answer": "reshape() returns an array with a new shape without changing the original number of elements. resize() can change the array's size."
            },
            {
                "question": "What is the difference between axis=0 and axis=1?",
                "answer": "For a 2D array, axis=0 performs aggregation down rows, producing column results. axis=1 performs aggregation across columns, producing row results."
            },
            {
                "question": "What is Boolean indexing?",
                "answer": "Boolean indexing selects elements using a condition that produces a Boolean mask."
            }
        ],

        "mcqs": [
            {
                "question": "Which function creates a NumPy array?",
                "options": ["np.list()", "np.array()", "np.create()", "np.vector()"],
                "answer": "np.array()",
                "explanation": "np.array() creates a NumPy ndarray from array-like data."
            },
            {
                "question": "What is the output of np.arange(1, 6)?",
                "options": ["[1 2 3 4 5]", "[1 2 3 4 5 6]", "[0 1 2 3 4 5]", "[1 6]"],
                "answer": "[1 2 3 4 5]",
                "explanation": "The stop value 6 is excluded."
            },
            {
                "question": "Which property gives the shape of an array?",
                "options": ["size", "ndim", "shape", "dtype"],
                "answer": "shape",
                "explanation": "shape returns the size of each dimension."
            },
            {
                "question": "What does np.zeros(3) return?",
                "options": ["[1 1 1]", "[0 0 0]", "[3 3 3]", "[0 1 2]"],
                "answer": "[0 0 0]",
                "explanation": "np.zeros() creates an array filled with zeros."
            },
            {
                "question": "For a 2D array, what does np.sum(arr, axis=0) calculate?",
                "options": ["Row sums", "Column sums", "Array size", "Array mean"],
                "answer": "Column sums",
                "explanation": "axis=0 aggregates vertically across rows."
            }
        ]
    }
})


PYTHON_FOUNDATIONS.update({
    "python-pandas": {
        "id": "python-pandas",
        "title": "Pandas – Data Analysis in Python",
        "duration": "50 min",

        "content": """
# Introduction to Pandas

Pandas is a Python library used for data manipulation and analysis.

It is widely used in:
- Data Science
- Data Analytics
- Machine Learning
- Data cleaning
- Exploratory Data Analysis (EDA)

## 1. Installing and importing Pandas

Install:
pip install pandas

Import:
import pandas as pd

The alias pd is the standard convention.

## 2. Main Data Structures

Pandas has two important data structures:

### Series
A Series is a one-dimensional labelled array.

Example:
import pandas as pd

marks = pd.Series([85, 90, 78, 92])
print(marks)

Each value has an index.

### DataFrame
A DataFrame is a two-dimensional table containing rows and columns.

Example:
data = {
    "Name": ["Aman", "Riya", "Rahul"],
    "Age": [21, 22, 20],
    "Marks": [85, 92, 78]
}

df = pd.DataFrame(data)
print(df)

A DataFrame is similar to a spreadsheet or SQL table.

## 3. Reading and Writing CSV Files

CSV stands for Comma-Separated Values.

Read a CSV file:
df = pd.read_csv("students.csv")

Save a DataFrame:
df.to_csv("output.csv", index=False)

The index=False argument prevents Pandas from writing
the DataFrame index as an extra column.

Other useful functions:
pd.read_excel("data.xlsx")
df.to_excel("output.xlsx", index=False)

## 4. Inspecting a Dataset

Important functions:

df.head()
Displays the first five rows.

df.head(10)
Displays the first ten rows.

df.tail()
Displays the last five rows.

df.shape
Returns (number of rows, number of columns).

df.columns
Returns column names.

df.info()
Displays column types and non-null counts.

df.describe()
Displays statistical summaries of numerical columns.

df.dtypes
Displays data types of columns.

## 5. Selecting Columns

Select one column:
df["Name"]

Select multiple columns:
df[["Name", "Marks"]]

A single column normally returns a Series.
Multiple columns return a DataFrame.

## 6. Selecting Rows: loc and iloc

loc selects data using index labels.

df.loc[0]
Selects the row with index label 0.

df.loc[0, "Name"]
Selects the Name value for index label 0.

iloc selects data using integer positions.

df.iloc[0]
Selects the first row by position.

df.iloc[0, 1]
Selects the value at first row and second column.

Important:
loc uses labels, while iloc uses integer positions.

## 7. Filtering Data

You can filter rows using conditions.

Example:
df[df["Marks"] > 80]

Multiple conditions:
df[(df["Marks"] > 80) & (df["Age"] < 22)]

Use:
& for AND
| for OR
~ for NOT

Each condition should be enclosed in parentheses.

## 8. Sorting Data

Sort by marks:
df.sort_values("Marks")

Descending order:
df.sort_values("Marks", ascending=False)

Sort by multiple columns:
df.sort_values(["Age", "Marks"])

## 9. Handling Missing Values

Real datasets may contain missing values.

Check missing values:
df.isnull()

Count missing values:
df.isnull().sum()

Remove rows with missing values:
df.dropna()

Fill missing values:
df.fillna(0)

Fill missing marks with their average:
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

Always understand why values are missing before choosing
whether to remove or replace them.

## 10. Adding and Removing Columns

Add a column:
df["Passed"] = df["Marks"] >= 40

Remove a column:
df.drop(columns=["Age"], inplace=True)

The inplace=True argument modifies the existing DataFrame.

## 11. GroupBy

groupby() groups rows based on one or more columns.

Example:
df.groupby("Department")["Salary"].mean()

This calculates the average salary for each department.

Other operations:
sum()
mean()
count()
min()
max()

This is useful for summarizing large datasets.

## 12. Value Counts

df["Department"].value_counts()

Counts how often each department occurs.

## 13. Removing Duplicate Rows

df.duplicated()
Identifies duplicate rows.

df.drop_duplicates()
Removes duplicate rows.

## 14. Combining DataFrames

concat() combines DataFrames along rows or columns.

pd.concat([df1, df2])

merge() combines DataFrames using a common column.

pd.merge(df1, df2, on="StudentID")

This is similar to joining tables in SQL.

## 15. Applying Functions

apply() applies a function to values in a Series or
along an axis of a DataFrame.

Example:
df["Marks"].apply(lambda x: x + 5)

This adds 5 to each mark.

## 16. Pandas vs NumPy

NumPy:
- Mainly focuses on numerical arrays.
- Provides fast mathematical operations.
- Uses ndarray.

Pandas:
- Focuses on labelled tabular data.
- Provides Series and DataFrame.
- Makes missing-value handling and data cleaning easier.
- Uses NumPy internally for many operations.

## 17. Pandas vs Java and C++

Pandas is a Python library.

Comparable concepts:
- Java: Collections, arrays and libraries for tabular data.
- C++: Vectors, maps and external data-processing libraries.
- Python: Pandas Series and DataFrame.

Pandas provides convenient built-in tools for working
with structured datasets.

## 18. Practical Data Science Workflow

A typical workflow:

1. Import Pandas.
2. Load a CSV or Excel dataset.
3. Inspect rows and columns.
4. Check missing values.
5. Clean and transform the data.
6. Filter and group records.
7. Calculate statistics.
8. Export the cleaned dataset.

This workflow is commonly used before training a
Machine Learning model.
""",

        "key_concepts": [
            "Pandas",
            "Series",
            "DataFrame",
            "CSV files",
            "Data inspection",
            "loc and iloc",
            "Filtering",
            "Sorting",
            "Missing values",
            "GroupBy",
            "Merging",
            "Duplicate removal",
            "Data cleaning"
        ],

        "examples": {
            "python": {
                "code": "import pandas as pd\n\ndata = {\n    'Name': ['Aman', 'Riya', 'Rahul', 'Neha'],\n    'Department': ['CS', 'IT', 'CS', 'IT'],\n    'Marks': [85, 92, 78, 88]\n}\n\ndf = pd.DataFrame(data)\n\nprint('Complete dataset:')\nprint(df)\n\nprint('\\nStudents scoring above 80:')\nprint(df[df['Marks'] > 80])\n\nprint('\\nAverage marks by department:')\nprint(df.groupby('Department')['Marks'].mean())",
                "output": "Complete dataset:\n    Name Department  Marks\n0   Aman         CS     85\n1   Riya         IT     92\n2  Rahul         CS     78\n3   Neha         IT     88\n\nStudents scoring above 80:\n   Name Department  Marks\n0  Aman         CS     85\n1  Riya         IT     92\n3  Neha         IT     88\n\nAverage marks by department:\nDepartment\nCS    81.5\nIT    90.0"
            }
        },

        "dry_run": """
Consider this DataFrame:

Name    Marks
Aman    85
Riya    92
Rahul   78

Statement:
df[df["Marks"] > 80]

Step 1: Check Aman's marks: 85 > 80, True.
Step 2: Check Riya's marks: 92 > 80, True.
Step 3: Check Rahul's marks: 78 > 80, False.

Only Aman and Riya remain.

Result:
   Name  Marks
0  Aman     85
1  Riya     92
""",

        "practice_questions": [
            {
                "level": "Beginner",
                "question": "Create a DataFrame containing student names and marks. Display only students who scored more than 75.",
                "solutions": {
                    "python": "import pandas as pd\n\ndata = {'Name': ['Aman', 'Riya', 'Rahul', 'Neha'], 'Marks': [65, 90, 72, 85]}\ndf = pd.DataFrame(data)\nresult = df[df['Marks'] > 75]\nprint(result)",
                    "java": "public class Main {\n    public static void main(String[] args) {\n        String[] names = {\"Aman\", \"Riya\", \"Rahul\", \"Neha\"};\n        int[] marks = {65, 90, 72, 85};\n        for (int i = 0; i < marks.length; i++) {\n            if (marks[i] > 75) {\n                System.out.println(names[i] + \" \" + marks[i]);\n            }\n        }\n    }\n}",
                    "cpp": "#include <iostream>\nusing namespace std;\nint main() {\n    string names[] = {\"Aman\", \"Riya\", \"Rahul\", \"Neha\"};\n    int marks[] = {65, 90, 72, 85};\n    for (int i = 0; i < 4; i++) {\n        if (marks[i] > 75) {\n            cout << names[i] << \" \" << marks[i] << endl;\n        }\n    }\n    return 0;\n}"
                },
                "explanation": "Pandas uses Boolean filtering to select rows that satisfy a condition. Java and C++ can achieve the same result using loops and if statements.",
                "sample_input": "Aman 65, Riya 90, Rahul 72, Neha 85",
                "sample_output": "Riya 90\nNeha 85"
            },
            {
                "level": "Intermediate",
                "question": "Create a DataFrame containing department and salary. Calculate the average salary for each department.",
                "solutions": {
                    "python": "import pandas as pd\n\ndata = {'Department': ['IT', 'HR', 'IT', 'HR', 'IT'], 'Salary': [40000, 30000, 50000, 35000, 45000]}\ndf = pd.DataFrame(data)\nprint(df.groupby('Department')['Salary'].mean())",
                    "java": "import java.util.*;\npublic class Main {\n    public static void main(String[] args) {\n        String[] departments = {\"IT\", \"HR\", \"IT\", \"HR\", \"IT\"};\n        int[] salaries = {40000, 30000, 50000, 35000, 45000};\n        Map<String, int[]> totals = new HashMap<>();\n        for (int i = 0; i < salaries.length; i++) {\n            int[] value = totals.getOrDefault(departments[i], new int[2]);\n            value[0] += salaries[i];\n            value[1]++;\n            totals.put(departments[i], value);\n        }\n        for (String key : totals.keySet()) {\n            int[] value = totals.get(key);\n            System.out.println(key + \": \" + (value[0] / (double)value[1]));\n        }\n    }\n}",
                    "cpp": "#include <iostream>\n#include <map>\nusing namespace std;\nint main() {\n    string departments[] = {\"IT\", \"HR\", \"IT\", \"HR\", \"IT\"};\n    int salaries[] = {40000, 30000, 50000, 35000, 45000};\n    map<string, pair<int, int>> totals;\n    for (int i = 0; i < 5; i++) {\n        totals[departments[i]].first += salaries[i];\n        totals[departments[i]].second++;\n    }\n    for (auto entry : totals) {\n        cout << entry.first << \": \"\n             << entry.second.first / (double)entry.second.second << endl;\n    }\n    return 0;\n}"
                },
                "explanation": "groupby() groups records by department, and mean() calculates the average salary in each group. The Java and C++ versions use maps to store totals and counts.",
                "sample_input": "IT: 40000, HR: 30000, IT: 50000, HR: 35000, IT: 45000",
                "sample_output": "HR: 32500\nIT: 45000"
            }
        ],

        "interview_questions": [
            {
                "question": "What is Pandas?",
                "answer": "Pandas is a Python library used for data manipulation, cleaning and analysis."
            },
            {
                "question": "What is a Series?",
                "answer": "A Series is a one-dimensional labelled data structure in Pandas."
            },
            {
                "question": "What is a DataFrame?",
                "answer": "A DataFrame is a two-dimensional labelled tabular data structure containing rows and columns."
            },
            {
                "question": "What is the difference between loc and iloc?",
                "answer": "loc selects data by index labels, while iloc selects data using integer positions."
            },
            {
                "question": "How do you handle missing values?",
                "answer": "Use isnull() to identify missing values, dropna() to remove them, and fillna() to replace them."
            },
            {
                "question": "What does groupby() do?",
                "answer": "groupby() divides records into groups based on column values so that aggregation and analysis can be performed."
            },
            {
                "question": "What is the difference between merge() and concat()?",
                "answer": "merge() combines DataFrames using common columns or indexes, while concat() joins DataFrames along rows or columns."
            },
            {
                "question": "How do you read a CSV file?",
                "answer": "Use pd.read_csv('filename.csv') to load a CSV file into a DataFrame."
            }
        ],

        "mcqs": [
            {
                "question": "Which function creates a Pandas DataFrame?",
                "options": ["pd.array()", "pd.DataFrame()", "pd.table()", "pd.create()"],
                "answer": "pd.DataFrame()",
                "explanation": "pd.DataFrame() creates a two-dimensional tabular data structure."
            },
            {
                "question": "Which function reads a CSV file?",
                "options": ["pd.open_csv()", "pd.read_csv()", "pd.load()", "pd.csv()"],
                "answer": "pd.read_csv()",
                "explanation": "read_csv() loads CSV data into a DataFrame."
            },
            {
                "question": "Which method displays the first five rows by default?",
                "options": ["tail()", "info()", "head()", "describe()"],
                "answer": "head()",
                "explanation": "head() displays the first five rows by default."
            },
            {
                "question": "Which method removes rows containing missing values by default?",
                "options": ["fillna()", "dropna()", "isnull()", "replace()"],
                "answer": "dropna()",
                "explanation": "dropna() removes missing-value rows by default."
            },
            {
                "question": "Which method groups data based on column values?",
                "options": ["merge()", "sort_values()", "groupby()", "concat()"],
                "answer": "groupby()",
                "explanation": "groupby() creates groups for aggregation and analysis."
            },
            {
                "question": "What does df.shape return?",
                "options": ["Column names", "Number of rows and columns", "Data types", "Missing values"],
                "answer": "Number of rows and columns",
                "explanation": "shape returns a tuple containing the number of rows and columns."
            }
        ]
    }
})


PYTHON_FOUNDATIONS.update({
    "python-rest-api": {
        "id": "python-rest-api",
        "title": "REST API – Backend Communication",
        "duration": "45 min",

        "content": """
# REST API – Backend Communication

## 1. What is an API?

API stands for Application Programming Interface.

An API allows two software applications to communicate
with each other.

Example:
When you log in to CodeQuest:

1. You enter your email and password in the frontend.
2. JavaScript sends an HTTP request to the backend.
3. FastAPI receives the request.
4. Python checks the credentials.
5. The backend sends a response.
6. The frontend displays the result.

The API acts as the communication interface between
the frontend and backend.

## 2. What is REST?

REST stands for Representational State Transfer.

REST is an architectural style used to design web APIs.

A REST API typically:
- Uses HTTP methods.
- Identifies resources using URLs.
- Exchanges data using JSON.
- Is stateless.
- Uses HTTP status codes.

Example resource URLs:

GET /api/users
GET /api/users/10
POST /api/users
PUT /api/users/10
DELETE /api/users/10

## 3. What is HTTP?

HTTP stands for Hypertext Transfer Protocol.

It is a communication protocol used between clients
and servers.

A client sends an HTTP request.
A server processes it and returns an HTTP response.

HTTPS is the secure version of HTTP. It uses TLS
to protect communication.

## 4. HTTP Request Structure

An HTTP request can contain:

1. Method – what action to perform.
2. URL – the resource being accessed.
3. Headers – additional request information.
4. Body – data sent to the server.

Example:

POST /api/users

Content-Type: application/json

{
    "name": "Aman",
    "email": "aman@example.com"
}

Here:
- POST is the HTTP method.
- /api/users is the endpoint.
- Content-Type is a header.
- The JSON object is the request body.

## 5. HTTP Response Structure

A server response can contain:

1. Status code.
2. Response headers.
3. Response body.

Example:

Status: 201 Created

{
    "id": 1,
    "name": "Aman",
    "email": "aman@example.com"
}

The response tells the client whether the operation
succeeded or failed.

## 6. Important HTTP Methods

GET:
Retrieve information.

Example:
GET /api/problems

POST:
Create a new resource.

Example:
POST /api/problems

PUT:
Replace or completely update a resource.

Example:
PUT /api/problems/10

PATCH:
Partially update a resource.

Example:
PATCH /api/users/10

DELETE:
Remove a resource.

Example:
DELETE /api/problems/10

Important:
GET should retrieve data rather than perform operations
that change application state.

## 7. HTTP Status Codes

2xx – Successful requests

200 OK:
Request succeeded.

201 Created:
A new resource was created.

204 No Content:
Request succeeded, but there is no response body.

4xx – Client errors

400 Bad Request:
The request contains invalid data.

401 Unauthorized:
Authentication is missing or invalid.

403 Forbidden:
The user is authenticated but lacks permission.

404 Not Found:
The requested resource does not exist.

422 Unprocessable Content:
The request format may be valid, but its data fails
validation.

5xx – Server errors

500 Internal Server Error:
An unexpected server-side error occurred.

502 Bad Gateway:
A server acting as a gateway received an invalid
response from another server.

## 8. What is JSON?

JSON stands for JavaScript Object Notation.

It is a lightweight data format commonly used for
communication between frontend and backend.

Example:

{
    "name": "Riya",
    "age": 21,
    "skills": ["Python", "Java", "SQL"]
}

Python can convert JSON data into dictionaries and lists.

import json

data = '{"name": "Riya", "age": 21}'
result = json.loads(data)

print(result["name"])

Output:
Riya

Convert Python data into JSON:

json.dumps(result)

## 9. What is an Endpoint?

An endpoint is a specific URL through which a client
accesses an API operation.

Example:

GET /api/users
GET /api/users/5

The first endpoint retrieves users.
The second retrieves a particular user.

## 10. What is Statelessness?

REST APIs are generally stateless.

This means each request must contain the information
required to process that request.

The server does not rely on remembering the previous
request as conversational session state.

For authenticated APIs, a client may send a JWT token
with each protected request.

Example:

Authorization: Bearer your_access_token

## 11. Authentication vs Authorization

Authentication:
Verifies who the user is.

Example:
Logging in using email and password.

Authorization:
Determines what an authenticated user is allowed to do.

Example:
A normal user can solve problems, but only an admin
can delete all problems.

## 12. What is CRUD?

CRUD represents four basic operations:

Create  -> POST
Read    -> GET
Update  -> PUT or PATCH
Delete  -> DELETE

Example for a student resource:

POST   /api/students
GET    /api/students
GET    /api/students/1
PUT    /api/students/1
DELETE /api/students/1

CRUD is used in most database-backed applications.

## 13. Path Parameters and Query Parameters

Path parameter:

GET /api/users/10

Here, 10 identifies a particular user.

Query parameter:

GET /api/problems?difficulty=Easy

Here, difficulty is a query parameter.

Multiple query parameters:

GET /api/problems?difficulty=Easy&topic=Arrays

Path parameters generally identify a resource.
Query parameters commonly filter, sort or paginate results.

## 14. API Validation and Error Handling

A backend should validate incoming data.

Example checks:
- Is the email valid?
- Is the required name present?
- Is the password long enough?
- Does the requested user exist?

Never blindly trust data received from the frontend.

Return appropriate status codes and useful error messages.
Avoid exposing passwords, API keys or internal stack traces.

## 15. API Testing

Common tools:

Postman:
Used to send HTTP requests and inspect responses.

Swagger UI:
Provides interactive API documentation.
FastAPI automatically generates Swagger documentation.

curl:
A command-line tool for sending HTTP requests.

Example:

curl http://127.0.0.1:8000/api/problems

## 16. REST API in CodeQuest

Your CodeQuest application uses REST-style endpoints.

Examples:

POST /api/users/register
Registers a new user.

POST /api/users/login
Authenticates a user.

GET /api/problems
Retrieves coding problems.

POST /api/submissions
Submits code for execution.

POST /api/ai/tutor
Sends a question to the AI Tutor.

GET /api/learning/paths
Retrieves available learning paths.

The frontend sends requests to FastAPI using JavaScript
fetch(). FastAPI processes requests and returns JSON.

## 17. Advantages of REST APIs

- Separates frontend and backend.
- Supports different client applications.
- Uses standard HTTP methods.
- Works with JSON.
- Makes integration easier.
- Supports scalable application architectures.

## 18. REST API vs SOAP

REST:
- Architectural style.
- Commonly uses JSON.
- Uses HTTP methods.
- Generally lightweight.

SOAP:
- Protocol with formal messaging rules.
- Commonly uses XML.
- Defines a structured message format.
- Often used in enterprise integrations.

## 19. REST API vs GraphQL

REST:
Uses multiple resource endpoints.

GraphQL:
Allows clients to request specific fields through
a GraphQL query.

Both approaches can be used to build APIs.
""",

        "key_concepts": [
            "API",
            "REST",
            "HTTP",
            "HTTPS",
            "Request and response",
            "HTTP methods",
            "HTTP status codes",
            "JSON",
            "Endpoints",
            "Statelessness",
            "Authentication",
            "Authorization",
            "CRUD",
            "Path parameters",
            "Query parameters",
            "API testing",
            "Validation"
        ],

        "examples": {
            "python": {
                "code": "import requests\n\nresponse = requests.get('https://jsonplaceholder.typicode.com/users/1')\n\nprint('Status:', response.status_code)\n\nif response.status_code == 200:\n    data = response.json()\n    print('Name:', data['name'])\n    print('Email:', data['email'])",
                "output": "Status: 200\nName: Leanne Graham\nEmail: Sincere@april.biz"
            },
            "java": {
                "code": "import java.net.URI;\nimport java.net.http.HttpClient;\nimport java.net.http.HttpRequest;\nimport java.net.http.HttpResponse;\n\npublic class Main {\n    public static void main(String[] args) throws Exception {\n        HttpClient client = HttpClient.newHttpClient();\n        HttpRequest request = HttpRequest.newBuilder()\n            .uri(URI.create(\"https://jsonplaceholder.typicode.com/users/1\"))\n            .GET()\n            .build();\n\n        HttpResponse<String> response = client.send(\n            request, HttpResponse.BodyHandlers.ofString()\n        );\n        System.out.println(\"Status: \" + response.statusCode());\n        System.out.println(response.body());\n    }\n}",
                "output": "Status: 200\nA JSON response containing user information."
            },
            "cpp": {
                "code": "#include <iostream>\n#include <curl/curl.h>\nusing namespace std;\n\nsize_t writeCallback(void* contents, size_t size, size_t count, void* output) {\n    ((string*)output)->append((char*)contents, size * count);\n    return size * count;\n}\n\nint main() {\n    CURL* curl = curl_easy_init();\n    string response;\n    if (curl) {\n        curl_easy_setopt(curl, CURLOPT_URL,\n            \"https://jsonplaceholder.typicode.com/users/1\");\n        curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, writeCallback);\n        curl_easy_setopt(curl, CURLOPT_WRITEDATA, &response);\n        CURLcode result = curl_easy_perform(curl);\n        if (result == CURLE_OK) cout << response;\n        curl_easy_cleanup(curl);\n    }\n    return 0;\n}",
                "output": "A JSON response containing user information."
            }
        },

        "dry_run": """
Request:
GET /api/users/10

Step 1:
The client sends a GET request.

Step 2:
The server receives the request.

Step 3:
The server searches for user ID 10.

Step 4:
If the user exists, the server returns 200 OK
with the user's JSON information.

If the user does not exist, the server returns
404 Not Found.

Remember:
GET retrieves data. It does not create a new user.
""",

        "practice_questions": [
            {
                "level": "Beginner",
                "question": "You are building a student management API. Identify the correct HTTP methods for creating, retrieving, updating and deleting a student.",
                "solutions": {
                    "python": "operations = {\n    'Create student': 'POST /api/students',\n    'Retrieve students': 'GET /api/students',\n    'Retrieve one student': 'GET /api/students/1',\n    'Update student': 'PUT /api/students/1',\n    'Delete student': 'DELETE /api/students/1'\n}\n\nfor operation, endpoint in operations.items():\n    print(operation + ': ' + endpoint)",
                    "java": "import java.util.*;\npublic class Main {\n    public static void main(String[] args) {\n        Map<String, String> operations = new LinkedHashMap<>();\n        operations.put(\"Create student\", \"POST /api/students\");\n        operations.put(\"Retrieve students\", \"GET /api/students\");\n        operations.put(\"Retrieve one student\", \"GET /api/students/1\");\n        operations.put(\"Update student\", \"PUT /api/students/1\");\n        operations.put(\"Delete student\", \"DELETE /api/students/1\");\n        operations.forEach((key, value) ->\n            System.out.println(key + \": \" + value));\n    }\n}",
                    "cpp": "#include <iostream>\nusing namespace std;\nint main() {\n    string operations[][2] = {\n        {\"Create student\", \"POST /api/students\"},\n        {\"Retrieve students\", \"GET /api/students\"},\n        {\"Retrieve one student\", \"GET /api/students/1\"},\n        {\"Update student\", \"PUT /api/students/1\"},\n        {\"Delete student\", \"DELETE /api/students/1\"}\n    };\n    for (auto &op : operations)\n        cout << op[0] << \": \" << op[1] << endl;\n    return 0;\n}"
                },
                "explanation": "REST uses HTTP methods to represent operations on resources. POST creates, GET retrieves, PUT updates and DELETE removes.",
                "sample_input": "Student resource",
                "sample_output": "Create student: POST /api/students\nRetrieve students: GET /api/students\nRetrieve one student: GET /api/students/1\nUpdate student: PUT /api/students/1\nDelete student: DELETE /api/students/1"
            },
            {
                "level": "Intermediate",
                "question": "Write a Python function that interprets an HTTP status code and returns whether the request succeeded, had a client error or had a server error.",
                "solutions": {
                    "python": "def classify_status(code):\n    if 200 <= code < 300:\n        return 'Success'\n    elif 400 <= code < 500:\n        return 'Client Error'\n    elif 500 <= code < 600:\n        return 'Server Error'\n    return 'Other Status'\n\nfor code in [200, 404, 500, 301]:\n    print(code, classify_status(code))",
                    "java": "public class Main {\n    static String classifyStatus(int code) {\n        if (code >= 200 && code < 300) return \"Success\";\n        if (code >= 400 && code < 500) return \"Client Error\";\n        if (code >= 500 && code < 600) return \"Server Error\";\n        return \"Other Status\";\n    }\n    public static void main(String[] args) {\n        int[] codes = {200, 404, 500, 301};\n        for (int code : codes)\n            System.out.println(code + \" \" + classifyStatus(code));\n    }\n}",
                    "cpp": "#include <iostream>\nusing namespace std;\nstring classifyStatus(int code) {\n    if (code >= 200 && code < 300) return \"Success\";\n    if (code >= 400 && code < 500) return \"Client Error\";\n    if (code >= 500 && code < 600) return \"Server Error\";\n    return \"Other Status\";\n}\nint main() {\n    int codes[] = {200, 404, 500, 301};\n    for (int code : codes)\n        cout << code << \" \" << classifyStatus(code) << endl;\n    return 0;\n}"
                },
                "explanation": "HTTP status codes are grouped into ranges. The first digit indicates the broad category: 2xx success, 4xx client error and 5xx server error.",
                "sample_input": "200, 404, 500, 301",
                "sample_output": "200 Success\n404 Client Error\n500 Server Error\n301 Other Status"
            }
        ],

        "interview_questions": [
            {
                "question": "What is an API?",
                "answer": "An API is an interface that allows different software applications to communicate."
            },
            {
                "question": "What is REST?",
                "answer": "REST is an architectural style for designing network-based applications using resources and standard HTTP operations."
            },
            {
                "question": "What is the difference between PUT and PATCH?",
                "answer": "PUT generally replaces a resource, while PATCH applies a partial update."
            },
            {
                "question": "What is the difference between 401 and 403?",
                "answer": "401 means valid authentication is missing or not provided. 403 means the server understood the request but refuses access."
            },
            {
                "question": "What is statelessness in REST?",
                "answer": "Each request contains the information needed to process it. The server does not depend on conversational session state from previous requests."
            },
            {
                "question": "What is JSON?",
                "answer": "JSON is a lightweight text-based format used to exchange structured data."
            },
            {
                "question": "What is the difference between path and query parameters?",
                "answer": "Path parameters identify a resource, while query parameters commonly filter, sort or paginate results."
            },
            {
                "question": "What is CRUD?",
                "answer": "CRUD stands for Create, Read, Update and Delete."
            },
            {
                "question": "What is the difference between authentication and authorization?",
                "answer": "Authentication verifies identity. Authorization checks permissions."
            },
            {
                "question": "How does the CodeQuest frontend communicate with FastAPI?",
                "answer": "The JavaScript frontend sends HTTP requests using fetch(). FastAPI processes them and returns JSON responses."
            }
        ],

        "mcqs": [
            {
                "question": "What does REST stand for?",
                "options": ["Remote Execution State Transfer", "Representational State Transfer", "Resource Exchange Standard Technology", "Representational Server Transfer"],
                "answer": "Representational State Transfer",
                "explanation": "REST stands for Representational State Transfer."
            },
            {
                "question": "Which HTTP method is normally used to retrieve data?",
                "options": ["POST", "DELETE", "GET", "PATCH"],
                "answer": "GET",
                "explanation": "GET retrieves a resource from the server."
            },
            {
                "question": "Which status code indicates successful resource creation?",
                "options": ["200", "201", "404", "500"],
                "answer": "201",
                "explanation": "201 Created indicates that a resource was successfully created."
            },
            {
                "question": "What does HTTP 404 mean?",
                "options": ["Unauthorized", "Server Error", "Not Found", "Created"],
                "answer": "Not Found",
                "explanation": "404 means the requested resource could not be found."
            },
            {
                "question": "Which format is commonly used for REST API data exchange?",
                "options": ["JSON", "MP3", "EXE", "JPG"],
                "answer": "JSON",
                "explanation": "JSON is commonly used because it is lightweight and easy to process."
            },
            {
                "question": "Which method is generally used for partial updates?",
                "options": ["GET", "POST", "PATCH", "DELETE"],
                "answer": "PATCH",
                "explanation": "PATCH applies partial modifications to a resource."
            },
            {
                "question": "What does HTTP 401 indicate?",
                "options": ["Not Found", "Unauthorized", "Created", "Success"],
                "answer": "Unauthorized",
                "explanation": "401 indicates missing or invalid authentication credentials."
            },
            {
                "question": "What does statelessness mean in REST?",
                "options": ["The server stores every previous request", "Each request contains the information needed to process it", "The API cannot use databases", "The API cannot use authentication"],
                "answer": "Each request contains the information needed to process it",
                "explanation": "REST requests are independent and should contain the information needed for processing."
            }
        ]
    }
})


PYTHON_FOUNDATIONS.update({
    "python-fastapi": {
        "id": "python-fastapi",
        "title": "FastAPI – Modern Python Backend Development",
        "duration": "60 min",

        "content": """
# FastAPI – Modern Python Backend Development

## 1. What is FastAPI?

FastAPI is a modern Python web framework used to build APIs.

It is commonly used for:
- REST API development.
- Backend services.
- Machine Learning APIs.
- AI-powered applications.
- Microservices.
- Database-backed applications.

FastAPI uses Python type hints for validation and automatic
API documentation.

Your CodeQuest backend uses FastAPI.

## 2. Installing FastAPI

Install FastAPI and its development server:

pip install "fastapi[standard]"

The development server is Uvicorn.

## 3. Creating Your First FastAPI Application

Create a file called main.py:

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to FastAPI"}

Explanation:

1. Import FastAPI.
2. Create an application object.
3. Use @app.get("/") to define a GET endpoint.
4. Return a Python dictionary.
5. FastAPI automatically converts the dictionary into JSON.

Run the application:

python -m uvicorn main:app --reload

Here:
- main is the Python filename.
- app is the FastAPI application variable.
- --reload restarts the server when code changes.

Open:
http://127.0.0.1:8000/

## 4. What is a Route?

A route defines how the application responds to a
particular HTTP method and URL.

Example:

@app.get("/users")
def get_users():
    return {"users": ["Aman", "Riya"]}

@app.post("/users")
def create_user():
    return {"message": "User created"}

Common decorators:

@app.get()
@app.post()
@app.put()
@app.patch()
@app.delete()

## 5. Path Parameters

Path parameters are values included directly in a URL.

Example:

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}

Request:
GET /users/10

Response:
{"user_id": 10}

FastAPI uses the type hint int to validate the parameter.

If an invalid integer is provided, FastAPI returns a
validation error.

## 6. Query Parameters

Query parameters are provided after ? in a URL.

Example:

@app.get("/products")
def get_products(category: str, limit: int = 10):
    return {
        "category": category,
        "limit": limit
    }

Request:
GET /products?category=books&limit=5

Response:
{
    "category": "books",
    "limit": 5
}

The limit parameter has a default value of 10.

## 7. Request Body

A request body contains data sent by the client.

FastAPI commonly uses Pydantic models to validate
structured request data.

Example:

from pydantic import BaseModel

class Student(BaseModel):
    name: str
    age: int
    marks: float

@app.post("/students")
def create_student(student: Student):
    return {
        "message": "Student created",
        "student": student
    }

Example JSON request:

{
    "name": "Riya",
    "age": 21,
    "marks": 90.5
}

FastAPI validates the incoming data automatically.

## 8. What is Pydantic?

Pydantic is a Python library for data validation and
data parsing using type annotations.

It is integrated into FastAPI.

Example:

from pydantic import BaseModel, Field

class UserCreate(BaseModel):
    name: str = Field(min_length=2)
    email: str
    age: int = Field(gt=0)

This validates:
- Name must contain at least two characters.
- Email must be a string.
- Age must be greater than zero.

Pydantic models help ensure that incoming data follows
the expected structure.

## 9. Response Models

A response_model defines the structure of an API response.

Example:

from pydantic import BaseModel

class UserResponse(BaseModel):
    id: int
    name: str
    email: str

@app.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int):
    return {
        "id": user_id,
        "name": "Aman",
        "email": "aman@example.com"
    }

Response models help validate and document outgoing data.

They can also prevent internal fields from being exposed
when the response schema intentionally excludes them.

## 10. Automatic API Documentation

FastAPI automatically generates documentation.

Swagger UI:
http://127.0.0.1:8000/docs

ReDoc:
http://127.0.0.1:8000/redoc

You can test endpoints directly from Swagger UI.

This is useful during development and API testing.

## 11. HTTPException

HTTPException is used to return controlled HTTP errors.

Example:

from fastapi import HTTPException

@app.get("/users/{user_id}")
def get_user(user_id: int):
    if user_id != 1:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return {"id": 1, "name": "Aman"}

If the user does not exist, the API returns 404.

Do not expose sensitive internal information in error messages.

## 12. Dependency Injection

Dependency injection allows FastAPI to provide required
objects or services to an endpoint.

It is commonly implemented using Depends().

Example:

from fastapi import Depends

def get_message():
    return "Hello from dependency"

@app.get("/dependency")
def read_message(message: str = Depends(get_message)):
    return {"message": message}

FastAPI calls get_message() and supplies its result.

Common uses:
- Database sessions.
- Current authenticated user.
- Shared services.
- Permission checks.

Your CodeQuest backend uses Depends() to obtain database
sessions and authenticate users.

## 13. APIRouter

APIRouter helps organize a large FastAPI application
into multiple route files.

Example project:

backend/
    main.py
    routes/
        users.py
        problems.py
        submissions.py
        ai.py
        learning.py

In routes/users.py:

from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/")
def get_users():
    return {"message": "Users endpoint"}

In main.py:

from fastapi import FastAPI
from routes.users import router as users_router

app = FastAPI()

app.include_router(users_router, prefix="/api")

The endpoint becomes:

GET /api/users/

This makes the application modular and easier to maintain.

## 14. Middleware

Middleware is code that runs around request processing.

It can execute:
- Before the endpoint handles a request.
- After the endpoint generates a response.

Example:

from fastapi import FastAPI, Request

app = FastAPI()

@app.middleware("http")
async def log_requests(request: Request, call_next):
    print("Request:", request.method, request.url.path)

    response = await call_next(request)

    print("Status:", response.status_code)
    return response

Common uses:
- Request logging.
- Timing measurements.
- Security-related headers.
- Cross-Origin Resource Sharing configuration.

## 15. CORS

CORS stands for Cross-Origin Resource Sharing.

Browsers restrict certain requests made between different
origins.

An origin includes:
- Protocol.
- Hostname.
- Port.

For example:
Frontend: http://localhost:5173
Backend:  http://127.0.0.1:8000

These are different origins.

FastAPI can configure CORS using CORSMiddleware.

Example:

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

In production, configure only the trusted frontend origins
that your application actually needs.

## 16. Async and Await

FastAPI supports both synchronous and asynchronous endpoints.

Synchronous:

@app.get("/sync")
def sync_endpoint():
    return {"message": "Synchronous endpoint"}

Asynchronous:

@app.get("/async")
async def async_endpoint():
    return {"message": "Asynchronous endpoint"}

async and await are used for asynchronous operations.

They are particularly useful for I/O-bound work such as
network requests and supported asynchronous database calls.

An async endpoint does not automatically make CPU-intensive
work faster.

## 17. Database Integration

A real application usually stores information in a database.

FastAPI can integrate with:
- SQLite.
- PostgreSQL.
- MySQL.
- SQLAlchemy.
- Other database libraries.

A common architecture:

Client
  |
FastAPI route
  |
Service or business logic
  |
SQLAlchemy
  |
Database

Your CodeQuest backend uses SQLAlchemy to communicate
with its database.

## 18. Authentication and Authorization

Authentication checks the identity of a user.

Authorization checks the user's permissions.

FastAPI supports authentication patterns through dependencies
and security utilities.

A common token-based workflow:

1. User submits login credentials.
2. Backend verifies the credentials.
3. Backend creates an access token.
4. Frontend stores the token securely according to
   the application's security design.
5. Frontend sends the token with protected requests.
6. Backend verifies the token before returning protected data.

JWT implementation will be covered in a separate lesson.

## 19. Testing FastAPI

FastAPI provides TestClient for testing endpoints.

Example:

from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello"}

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello"}

Testing helps identify problems before deployment.

## 20. FastAPI vs Flask

FastAPI:
- Supports automatic API documentation.
- Uses type hints and Pydantic validation.
- Supports asynchronous endpoints.
- Designed with API development in mind.

Flask:
- Lightweight Python web framework.
- Provides flexible routing.
- Has a simple core.
- Often uses extensions for additional functionality.

Both frameworks can build backend applications.

## 21. FastAPI vs Django

FastAPI:
- Focuses on API development.
- Lightweight and modular.
- Provides automatic API documentation.

Django:
- Full-stack Python web framework.
- Includes an ORM, authentication system and admin interface.
- Provides many built-in application features.

## 22. FastAPI in CodeQuest

Your CodeQuest backend uses:

1. FastAPI to create the backend application.
2. APIRouter to organize endpoints.
3. Pydantic to validate incoming request data.
4. Depends() for dependency injection.
5. SQLAlchemy for database access.
6. JWT authentication for protected endpoints.
7. HTTPException for error handling.
8. CORS middleware to allow frontend communication.
9. Uvicorn to run the backend server.

Example endpoints in your application:

POST /api/users/register
POST /api/users/login
GET /api/problems
POST /api/submissions
POST /api/ai/tutor
GET /api/learning/paths

This is how your frontend communicates with your Python backend.
""",

        "key_concepts": [
            "FastAPI",
            "Uvicorn",
            "Routes",
            "Path parameters",
            "Query parameters",
            "Request body",
            "Pydantic",
            "Response models",
            "Swagger UI",
            "HTTPException",
            "Dependency injection",
            "Depends",
            "APIRouter",
            "Middleware",
            "CORS",
            "Async and await",
            "Database integration",
            "Authentication",
            "TestClient"
        ],

        "examples": {
            "python": {
                "code": "from fastapi import FastAPI, HTTPException\nfrom pydantic import BaseModel, Field\n\napp = FastAPI()\n\nclass Student(BaseModel):\n    name: str = Field(min_length=2)\n    marks: float = Field(ge=0, le=100)\n\n@app.get('/')\ndef home():\n    return {'message': 'Welcome to FastAPI'}\n\n@app.post('/students')\ndef create_student(student: Student):\n    return {\n        'message': 'Student created',\n        'name': student.name,\n        'marks': student.marks\n    }\n\n@app.get('/students/{student_id}')\ndef get_student(student_id: int):\n    if student_id != 1:\n        raise HTTPException(status_code=404, detail='Student not found')\n    return {'id': 1, 'name': 'Riya', 'marks': 90}",
                "output": "GET / -> {\"message\": \"Welcome to FastAPI\"}\n\nPOST /students with {\"name\": \"Riya\", \"marks\": 90} -> {\"message\": \"Student created\", \"name\": \"Riya\", \"marks\": 90}\n\nGET /students/1 -> {\"id\": 1, \"name\": \"Riya\", \"marks\": 90}"
            }
        },

        "dry_run": """
Endpoint:

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}

Request:
GET /users/25

Step 1:
FastAPI matches the GET method and /users/{user_id} route.

Step 2:
It extracts 25 from the URL.

Step 3:
It validates the integer type.

Step 4:
The endpoint receives user_id = 25.

Step 5:
The function returns a Python dictionary.

Step 6:
FastAPI converts it into a JSON response.

Final response:
{"user_id": 25}
""",

        "practice_questions": [
            {
                "level": "Beginner",
                "question": "Create a FastAPI application with a GET endpoint at /welcome that returns a welcome message. Also create a GET endpoint at /square/{number} that returns the square of the given integer.",
                "solutions": {
                    "python": "from fastapi import FastAPI\n\napp = FastAPI()\n\n@app.get('/welcome')\ndef welcome():\n    return {'message': 'Welcome to FastAPI'}\n\n@app.get('/square/{number}')\ndef square(number: int):\n    return {'number': number, 'square': number * number}\n\n# Run using:\n# python -m uvicorn main:app --reload",
                    "java": "import com.sun.net.httpserver.HttpServer;\nimport java.net.InetSocketAddress;\nimport java.io.OutputStream;\n\npublic class Main {\n    public static void main(String[] args) throws Exception {\n        HttpServer server = HttpServer.create(new InetSocketAddress(8080), 0);\n        server.createContext(\"/welcome\", exchange -> {\n            byte[] body = \"{\\\"message\\\":\\\"Welcome\\\"}\".getBytes();\n            exchange.getResponseHeaders().set(\"Content-Type\", \"application/json\");\n            exchange.sendResponseHeaders(200, body.length);\n            try (OutputStream os = exchange.getResponseBody()) {\n                os.write(body);\n            }\n        });\n        server.start();\n        System.out.println(\"Server running on port 8080\");\n    }\n}",
                    "cpp": "#include <iostream>\n#include <string>\n#include <cmath>\nusing namespace std;\n\nint main() {\n    int number = 5;\n    cout << \"Welcome to backend development\" << endl;\n    cout << \"Number: \" << number << endl;\n    cout << \"Square: \" << number * number << endl;\n    return 0;\n}"
                },
                "explanation": "The FastAPI version defines two HTTP GET endpoints. The square endpoint receives a path parameter, validates it as an integer and returns its square. Java and C++ examples demonstrate the underlying logic; they are not FastAPI applications.",
                "sample_input": "GET /square/5",
                "sample_output": "{\"number\": 5, \"square\": 25}"
            },
            {
                "level": "Intermediate",
                "question": "Create a FastAPI POST endpoint that accepts a product name and price. Validate that the name contains at least two characters and the price is greater than zero. Return the product details.",
                "solutions": {
                    "python": "from fastapi import FastAPI\nfrom pydantic import BaseModel, Field\n\napp = FastAPI()\n\nclass Product(BaseModel):\n    name: str = Field(min_length=2)\n    price: float = Field(gt=0)\n\n@app.post('/products')\ndef create_product(product: Product):\n    return {\n        'message': 'Product created',\n        'name': product.name,\n        'price': product.price\n    }\n\n# Example request:\n# {\"name\": \"Laptop\", \"price\": 55000}",
                    "java": "public class Main {\n    static boolean isValidProduct(String name, double price) {\n        return name != null && name.length() >= 2 && price > 0;\n    }\n    public static void main(String[] args) {\n        String name = \"Laptop\";\n        double price = 55000;\n        if (isValidProduct(name, price)) {\n            System.out.println(\"Product created\");\n            System.out.println(\"Name: \" + name);\n            System.out.println(\"Price: \" + price);\n        } else {\n            System.out.println(\"Invalid product\");\n        }\n    }\n}",
                    "cpp": "#include <iostream>\n#include <string>\nusing namespace std;\n\nbool isValidProduct(string name, double price) {\n    return name.length() >= 2 && price > 0;\n}\n\nint main() {\n    string name = \"Laptop\";\n    double price = 55000;\n    if (isValidProduct(name, price)) {\n        cout << \"Product created\" << endl;\n        cout << \"Name: \" << name << endl;\n        cout << \"Price: \" << price << endl;\n    } else {\n        cout << \"Invalid product\" << endl;\n    }\n    return 0;\n}"
                },
                "explanation": "Pydantic validates incoming request data before the endpoint runs. Field constraints enforce the minimum name length and positive price. The Java and C++ versions implement equivalent validation logic, not HTTP APIs.",
                "sample_input": "{\"name\": \"Laptop\", \"price\": 55000}",
                "sample_output": "{\"message\": \"Product created\", \"name\": \"Laptop\", \"price\": 55000}"
            }
        ],

        "interview_questions": [
            {
                "question": "What is FastAPI?",
                "answer": "FastAPI is a modern Python web framework for building APIs using Python type hints and automatic data validation."
            },
            {
                "question": "Why is FastAPI used?",
                "answer": "It provides API routing, validation, automatic documentation, dependency injection and asynchronous endpoint support."
            },
            {
                "question": "What is Uvicorn?",
                "answer": "Uvicorn is an ASGI server commonly used to run FastAPI applications."
            },
            {
                "question": "What is Pydantic?",
                "answer": "Pydantic validates and parses Python data using type annotations and models."
            },
            {
                "question": "What is APIRouter?",
                "answer": "APIRouter organizes related endpoints into separate modules, helping keep a large FastAPI project maintainable."
            },
            {
                "question": "What is Depends()?",
                "answer": "Depends() is FastAPI's dependency injection mechanism. It provides shared dependencies such as database sessions and authenticated users."
            },
            {
                "question": "What is HTTPException?",
                "answer": "HTTPException raises an HTTP error response with a status code and detail message."
            },
            {
                "question": "What is middleware?",
                "answer": "Middleware is code that runs around request processing and can inspect or modify requests and responses."
            },
            {
                "question": "What is CORS?",
                "answer": "CORS is a browser security mechanism that controls which origins are allowed to access resources across origins."
            },
            {
                "question": "What is the difference between async def and def?",
                "answer": "async def defines an asynchronous function that can use await. def defines a regular synchronous function."
            },
            {
                "question": "What is Swagger UI?",
                "answer": "Swagger UI is an interactive interface generated from an API specification. FastAPI provides it at /docs by default."
            },
            {
                "question": "How does FastAPI validate request data?",
                "answer": "It uses type annotations and Pydantic models to validate parameters and request bodies."
            },
            {
                "question": "How is FastAPI used in CodeQuest?",
                "answer": "It powers the backend routes for registration, login, problems, submissions, AI Tutor and learning paths."
            }
        ],

        "mcqs": [
            {
                "question": "Which command starts a FastAPI application using Uvicorn?",
                "options": ["python main.py", "uvicorn main:app --reload", "fastapi start", "python runserver"],
                "answer": "uvicorn main:app --reload",
                "explanation": "Uvicorn runs the ASGI application. main refers to the module and app refers to the application object."
            },
            {
                "question": "Which library is used by FastAPI for data validation?",
                "options": ["NumPy", "Pandas", "Pydantic", "Matplotlib"],
                "answer": "Pydantic",
                "explanation": "Pydantic validates structured data using Python type annotations."
            },
            {
                "question": "Which decorator defines a GET endpoint?",
                "options": ["@app.post()", "@app.get()", "@app.delete()", "@app.put()"],
                "answer": "@app.get()",
                "explanation": "@app.get() registers an endpoint for HTTP GET requests."
            },
            {
                "question": "Which component helps organize routes into separate files?",
                "options": ["APIRouter", "DataFrame", "ndarray", "Series"],
                "answer": "APIRouter",
                "explanation": "APIRouter groups related endpoints into reusable route modules."
            },
            {
                "question": "What is the default Swagger documentation URL?",
                "options": ["/swagger", "/api/docs", "/docs", "/documentation"],
                "answer": "/docs",
                "explanation": "FastAPI provides Swagger UI at /docs by default."
            },
            {
                "question": "Which function is used for dependency injection?",
                "options": ["Field()", "Depends()", "BaseModel()", "Router()"],
                "answer": "Depends()",
                "explanation": "Depends() declares dependencies that FastAPI resolves and provides."
            },
            {
                "question": "Which HTTP error is commonly raised when a resource does not exist?",
                "options": ["200", "201", "404", "500"],
                "answer": "404",
                "explanation": "404 Not Found indicates that the requested resource does not exist."
            },
            {
                "question": "What does CORS control?",
                "options": ["Database passwords", "Cross-origin browser access", "Python package installation", "CPU scheduling"],
                "answer": "Cross-origin browser access",
                "explanation": "CORS controls which origins are permitted to access resources across origins."
            }
        ]
    }
})


PYTHON_FOUNDATIONS.update({
    "python-flask": {
        "id": "python-flask",
        "title": "Flask – Lightweight Python Web Framework",
        "duration": "45 min",

        "content": """
# Flask – Lightweight Python Web Framework

## 1. What is Flask?

Flask is a lightweight Python web framework used to build
web applications and REST APIs.

It is called a microframework because its core provides
essential web development features without forcing a
large application structure.

Flask is commonly used for:
- Small and medium web applications.
- REST API development.
- Backend services.
- Prototypes and proof-of-concept applications.
- Applications requiring flexible architecture.

## 2. Installing Flask

Install using:

pip install flask

Import Flask:

from flask import Flask

## 3. Creating Your First Flask Application

Create app.py:

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return {"message": "Welcome to Flask"}

if __name__ == "__main__":
    app.run(debug=True)

Run:

python app.py

By default, Flask starts its development server at:

http://127.0.0.1:5000

Important:
The built-in Flask development server is for development.
Use a production-ready WSGI server when deploying.

## 4. Understanding Flask(__name__)

Flask(__name__) creates the application object.

__name__ tells Flask the name of the current Python module.

Flask uses this information to locate resources such as
templates and static files.

## 5. Routes in Flask

A route connects a URL to a Python function.

Example:

@app.route("/about")
def about():
    return {"page": "About"}

When a client requests /about, Flask executes about().

## 6. HTTP Methods

Flask supports common HTTP methods.

GET:
Retrieve data.

POST:
Create data.

PUT:
Replace or update data.

PATCH:
Partially update data.

DELETE:
Delete data.

Example:

@app.route("/users", methods=["GET"])
def get_users():
    return {"users": ["Aman", "Riya"]}

@app.route("/users", methods=["POST"])
def create_user():
    return {"message": "User created"}, 201

The second value in the return tuple is the HTTP status code.

## 7. Path Parameters

Path parameters are values included in the URL.

Example:

@app.route("/users/<int:user_id>")
def get_user(user_id):
    return {"user_id": user_id}

Request:

GET /users/10

Response:

{"user_id": 10}

The int converter ensures that the parameter is an integer.

## 8. Query Parameters

Query parameters are values provided after ? in the URL.

Example:

from flask import request

@app.route("/products")
def get_products():
    category = request.args.get("category", "all")
    return {"category": category}

Request:

GET /products?category=books

request.args.get() retrieves a query parameter.

## 9. Request Body and JSON

Flask uses request to access incoming request information.

Example:

from flask import request, jsonify

@app.route("/students", methods=["POST"])
def create_student():
    data = request.get_json()

    if not data or "name" not in data:
        return jsonify({"error": "Name is required"}), 400

    return jsonify({
        "message": "Student created",
        "name": data["name"]
    }), 201

Here:
- request.get_json() reads the JSON body.
- jsonify() creates a JSON response.
- 400 represents a bad request.
- 201 represents successful creation.

## 10. What is jsonify()?

jsonify() converts Python dictionaries and lists into
JSON HTTP responses.

Example:

from flask import jsonify

@app.route("/info")
def info():
    return jsonify({
        "project": "CodeQuest",
        "language": "Python"
    })

## 11. Templates and Jinja2

Flask supports HTML templates using Jinja2.

Project structure:

project/
    app.py
    templates/
        index.html

In app.py:

from flask import render_template

@app.route("/")
def home():
    return render_template("index.html")

Flask searches for HTML templates inside the templates
directory by default.

Templates can receive data:

return render_template("profile.html", name="Aman")

Inside profile.html:

<h1>Hello {{ name }}</h1>

Jinja2 is useful for generating dynamic HTML pages.

## 12. Static Files

CSS, JavaScript and images are commonly stored in
a static directory.

Example:

project/
    app.py
    static/
        style.css
        script.js

Reference a CSS file in a template:

<link rel="stylesheet"
      href="{{ url_for('static', filename='style.css') }}">

## 13. Request and Response

The request object contains information sent by the client.

Examples:
- request.method
- request.args
- request.form
- request.get_json()
- request.headers

A response contains data returned by the server.

Example:

return jsonify({"message": "Success"}), 200

## 14. Sessions and Cookies

A cookie is data stored by the browser.

A session is commonly used to maintain user-related state
between requests.

Flask provides a session object.

Example:

from flask import session

app.secret_key = "replace-with-a-secure-secret"

@app.route("/set")
def set_session():
    session["username"] = "Aman"
    return {"message": "Session saved"}

Flask's default session stores signed session data in
a browser cookie. It is not encrypted by default.

Do not store passwords, API keys or other secrets in it.

Use a strong secret key stored in environment variables.

## 15. Blueprints

Blueprints organize Flask applications into reusable modules.

Example:

from flask import Blueprint

users = Blueprint("users", __name__)

@users.route("/users")
def get_users():
    return {"users": []}

Register in the main application:

app.register_blueprint(users, url_prefix="/api")

The endpoint becomes:

GET /api/users

Blueprints are similar in purpose to FastAPI's APIRouter.

## 16. Error Handling

Flask provides mechanisms to handle HTTP errors.

Example:

from flask import abort

@app.route("/users/<int:user_id>")
def user_detail(user_id):
    if user_id != 1:
        abort(404)

    return {"id": 1, "name": "Aman"}

You can also define custom error handlers:

@app.errorhandler(404)
def not_found(error):
    return {"error": "Resource not found"}, 404

## 17. Flask and Databases

Flask does not force you to use a particular database.

It can work with:
- SQLite.
- PostgreSQL.
- MySQL.
- SQLAlchemy.
- Other database libraries.

SQLAlchemy can be used to manage database models
and queries.

## 18. Flask REST APIs

Flask can be used to build REST APIs.

Typical architecture:

Client
  |
Flask route
  |
Business logic
  |
Database
  |
JSON response

Flask routes receive HTTP requests and return responses.

## 19. Testing Flask

Flask provides a test client.

Example:

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return {"message": "Hello"}

def test_home():
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert response.json == {"message": "Hello"}

Testing helps verify that endpoints work correctly.

## 20. Flask vs FastAPI

Flask:
- Lightweight microframework.
- Flexible application structure.
- Uses extensions for additional functionality.
- Does not automatically provide the same integrated
  request validation and API documentation experience.

FastAPI:
- Designed with API development in mind.
- Uses Python type hints and Pydantic.
- Automatically generates API documentation.
- Supports async endpoints.
- Provides dependency injection.

Both frameworks are useful. The right choice depends
on application requirements.

## 21. Flask vs Django

Flask:
- Lightweight.
- Minimal built-in functionality.
- Flexible architecture.

Django:
- Full-stack framework.
- Built-in ORM and admin panel.
- Includes authentication and other common features.

## 22. When Should You Use Flask?

Choose Flask when:
- You need a lightweight web application.
- You want control over architecture.
- You are building a small API or prototype.
- You prefer choosing your own extensions.

Choose FastAPI when:
- You are primarily building APIs.
- You want automatic request validation.
- You need generated API documentation.
- You want to use asynchronous endpoints.

## 23. Placement Interview Summary

Flask is a lightweight Python microframework.

Important topics:
- Flask application object.
- Routing.
- HTTP methods.
- Path and query parameters.
- Request and response.
- jsonify().
- Templates and Jinja2.
- Sessions and cookies.
- Blueprints.
- Error handling.
- Database integration.
- Flask vs FastAPI.
""",

        "key_concepts": [
            "Flask",
            "Microframework",
            "Flask application",
            "Routing",
            "HTTP methods",
            "Path parameters",
            "Query parameters",
            "Request object",
            "JSON",
            "jsonify",
            "Jinja2",
            "Templates",
            "Static files",
            "Sessions",
            "Cookies",
            "Blueprints",
            "Error handling",
            "Database integration",
            "Flask testing"
        ],

        "examples": {
            "python": {
                "code": "from flask import Flask, request, jsonify\n\napp = Flask(__name__)\n\n@app.route('/')\ndef home():\n    return {'message': 'Welcome to Flask'}\n\n@app.route('/square/<int:number>')\ndef square(number):\n    return jsonify({'number': number, 'square': number * number})\n\n@app.route('/students', methods=['POST'])\ndef create_student():\n    data = request.get_json()\n    if not data or 'name' not in data:\n        return jsonify({'error': 'Name is required'}), 400\n    return jsonify({'message': 'Student created', 'name': data['name']}), 201\n\n# Run with app.run(debug=True) during development.",
                "output": "GET / -> {\"message\": \"Welcome to Flask\"}\n\nGET /square/5 -> {\"number\": 5, \"square\": 25}\n\nPOST /students with {\"name\": \"Riya\"} -> {\"message\": \"Student created\", \"name\": \"Riya\"}"
            },
            "java": {
                "code": "import com.sun.net.httpserver.HttpServer;\nimport java.net.InetSocketAddress;\nimport java.io.OutputStream;\n\npublic class Main {\n    public static void main(String[] args) throws Exception {\n        HttpServer server = HttpServer.create(new InetSocketAddress(8080), 0);\n        server.createContext(\"/\", exchange -> {\n            byte[] body = \"{\\\"message\\\":\\\"Welcome to Java backend\\\"}\".getBytes();\n            exchange.getResponseHeaders().set(\"Content-Type\", \"application/json\");\n            exchange.sendResponseHeaders(200, body.length);\n            try (OutputStream os = exchange.getResponseBody()) {\n                os.write(body);\n            }\n        });\n        server.start();\n    }\n}",
                "output": "GET / -> {\"message\": \"Welcome to Java backend\"}"
            },
            "cpp": {
                "code": "#include <iostream>\nusing namespace std;\n\nint main() {\n    int number = 5;\n    cout << \"Welcome to C++ backend development\" << endl;\n    cout << \"Number: \" << number << endl;\n    cout << \"Square: \" << number * number << endl;\n    return 0;\n}",
                "output": "Welcome to C++ backend development\nNumber: 5\nSquare: 25"
            }
        },

        "dry_run": """
Request:
GET /square/5

Step 1:
Flask matches the URL to the square route.

Step 2:
The <int:number> converter extracts 5 as an integer.

Step 3:
Flask calls square(number=5).

Step 4:
The function calculates 5 * 5 = 25.

Step 5:
jsonify() returns the JSON response.

Final response:
{"number": 5, "square": 25}
""",

        "practice_questions": [
            {
                "level": "Beginner",
                "question": "Create a Flask application with a GET route /welcome that returns a welcome message and a route /add/<int:a>/<int:b> that returns the sum of two numbers.",
                "solutions": {
                    "python": "from flask import Flask, jsonify\n\napp = Flask(__name__)\n\n@app.route('/welcome')\ndef welcome():\n    return jsonify({'message': 'Welcome to Flask'})\n\n@app.route('/add/<int:a>/<int:b>')\ndef add(a, b):\n    return jsonify({'a': a, 'b': b, 'sum': a + b})\n\n# Run using: python app.py\n# Include app.run(debug=True) under the main guard.",
                    "java": "public class Main {\n    public static void main(String[] args) {\n        int a = 10, b = 20;\n        System.out.println(\"Welcome to Java backend\");\n        System.out.println(\"Sum: \" + (a + b));\n    }\n}",
                    "cpp": "#include <iostream>\nusing namespace std;\nint main() {\n    int a = 10, b = 20;\n    cout << \"Welcome to C++ backend\" << endl;\n    cout << \"Sum: \" << a + b << endl;\n    return 0;\n}"
                },
                "explanation": "Flask uses route decorators to connect URLs with Python functions. Integer path converters extract numbers from the URL. Java and C++ versions demonstrate the same calculation but are not Flask servers.",
                "sample_input": "GET /add/10/20",
                "sample_output": "{\"a\": 10, \"b\": 20, \"sum\": 30}"
            },
            {
                "level": "Intermediate",
                "question": "Create a Flask POST endpoint that receives a JSON object containing a person's name and age. Return an error with status 400 if the data is missing or age is negative. Otherwise return the received details.",
                "solutions": {
                    "python": "from flask import Flask, request, jsonify\n\napp = Flask(__name__)\n\n@app.route('/people', methods=['POST'])\ndef create_person():\n    data = request.get_json(silent=True)\n    if not data or 'name' not in data or 'age' not in data:\n        return jsonify({'error': 'Name and age are required'}), 400\n    try:\n        age = int(data['age'])\n    except (ValueError, TypeError):\n        return jsonify({'error': 'Age must be an integer'}), 400\n    if age < 0:\n        return jsonify({'error': 'Age cannot be negative'}), 400\n    return jsonify({'name': data['name'], 'age': age}), 201",
                    "java": "public class Main {\n    public static void main(String[] args) {\n        String name = \"Riya\";\n        int age = 21;\n        if (name == null || name.isBlank() || age < 0) {\n            System.out.println(\"Invalid person data\");\n        } else {\n            System.out.println(\"Name: \" + name);\n            System.out.println(\"Age: \" + age);\n        }\n    }\n}",
                    "cpp": "#include <iostream>\n#include <string>\nusing namespace std;\nint main() {\n    string name = \"Riya\";\n    int age = 21;\n    if (name.empty() || age < 0) {\n        cout << \"Invalid person data\";\n    } else {\n        cout << \"Name: \" << name << endl;\n        cout << \"Age: \" << age << endl;\n    }\n    return 0;\n}"
                },
                "explanation": "request.get_json() reads the incoming JSON body. The endpoint validates required fields and age before returning a successful response. Java and C++ show the equivalent validation logic.",
                "sample_input": "{\"name\": \"Riya\", \"age\": 21}",
                "sample_output": "{\"name\": \"Riya\", \"age\": 21}"
            }
        ],

        "interview_questions": [
            {
                "question": "What is Flask?",
                "answer": "Flask is a lightweight Python microframework used to build web applications and REST APIs."
            },
            {
                "question": "Why is Flask called a microframework?",
                "answer": "Its core provides essential web functionality while leaving many additional features to optional extensions."
            },
            {
                "question": "What is Flask(__name__)?",
                "answer": "It creates a Flask application instance and provides the module name so Flask can locate resources."
            },
            {
                "question": "What is a route in Flask?",
                "answer": "A route maps a URL and HTTP method to a Python function."
            },
            {
                "question": "What is jsonify()?",
                "answer": "jsonify() converts Python data into a JSON HTTP response."
            },
            {
                "question": "How do you access query parameters in Flask?",
                "answer": "Use request.args.get('parameter_name')."
            },
            {
                "question": "How do you access JSON request data?",
                "answer": "Use request.get_json() to parse the JSON body."
            },
            {
                "question": "What is Jinja2?",
                "answer": "Jinja2 is a template engine used by Flask to generate dynamic HTML pages."
            },
            {
                "question": "What is a Flask Blueprint?",
                "answer": "A Blueprint groups related routes and functionality into reusable modules."
            },
            {
                "question": "What is the difference between a cookie and a session?",
                "answer": "A cookie is stored by the browser. A session is a mechanism for maintaining user-related state across requests; Flask's default session uses a signed browser cookie."
            },
            {
                "question": "What is the difference between Flask and FastAPI?",
                "answer": "Flask is a lightweight flexible microframework, while FastAPI is API-focused and provides integrated type-based validation, dependency injection and automatic documentation."
            },
            {
                "question": "Does Flask support REST API development?",
                "answer": "Yes. Flask routes can receive HTTP requests and return JSON responses with appropriate status codes."
            }
        ],

        "mcqs": [
            {
                "question": "Which command installs Flask?",
                "options": ["pip install flask", "pip install fastapi", "npm install flask", "python install flask"],
                "answer": "pip install flask",
                "explanation": "Flask is installed using pip."
            },
            {
                "question": "What is the default Flask development server port?",
                "options": ["3000", "5000", "8000", "8080"],
                "answer": "5000",
                "explanation": "Flask's default development server commonly uses port 5000."
            },
            {
                "question": "Which object is used to access incoming request data?",
                "options": ["response", "request", "session_only", "app"],
                "answer": "request",
                "explanation": "Flask's request object exposes information about the incoming HTTP request."
            },
            {
                "question": "Which function converts Python data into a JSON response?",
                "options": ["render_template()", "jsonify()", "url_for()", "redirect()"],
                "answer": "jsonify()",
                "explanation": "jsonify() creates a JSON response."
            },
            {
                "question": "Which directory stores Flask HTML templates by default?",
                "options": ["static", "views", "templates", "assets"],
                "answer": "templates",
                "explanation": "Flask looks for templates in the templates directory by default."
            },
            {
                "question": "Which Flask feature organizes related routes?",
                "options": ["Blueprint", "DataFrame", "APIRouter", "ndarray"],
                "answer": "Blueprint",
                "explanation": "Blueprints help organize reusable route modules."
            },
            {
                "question": "Which object is used to access query parameters?",
                "options": ["request.args", "request.body", "app.query", "session.args"],
                "answer": "request.args",
                "explanation": "request.args provides access to URL query parameters."
            },
            {
                "question": "Is Flask's built-in development server recommended for production?",
                "options": ["Yes, always", "No", "Only for databases", "Only for HTTPS"],
                "answer": "No",
                "explanation": "Use a production-ready WSGI server or deployment platform instead."
            }
        ]
    }
})


PYTHON_FOUNDATIONS.update({
    "python-sqlalchemy": {
        "id": "python-sqlalchemy",
        "title": "SQLAlchemy – Python ORM and Database Management",
        "duration": "60–75 min",

        "content": """
# 1. What is SQLAlchemy?

SQLAlchemy is a Python library used to communicate with relational databases such as SQLite, PostgreSQL and MySQL.

It provides two major ways to work with databases:

1. SQLAlchemy Core: Work with SQL expressions and database tables.
2. SQLAlchemy ORM: Work with Python classes and objects instead of writing SQL for every operation.

ORM stands for Object Relational Mapping.

An ORM maps:
- Python classes to database tables.
- Python objects to database rows.
- Python attributes to database columns.

For example, instead of writing:

INSERT INTO users (name, email) VALUES ('Aman', 'aman@example.com');

You can create a Python object and save it through SQLAlchemy.

# 2. Why do we use SQLAlchemy?

Without an ORM, developers frequently write SQL queries manually.

SQLAlchemy makes database operations easier by allowing developers to use Python objects.

Benefits:
- Less repetitive SQL code.
- Database operations through Python.
- Supports SQLite, PostgreSQL, MySQL and other databases.
- Provides relationships between tables.
- Supports transactions and connection management.
- Helps write parameterized queries safely.
- Integrates with FastAPI and Flask.

# 3. Important SQLAlchemy components

## Engine

The Engine manages the connection between your Python application and the database.

Example:

from sqlalchemy import create_engine

engine = create_engine("sqlite:///college.db")

For SQLite, the database file is created when a connection is first established if it does not already exist.

For PostgreSQL, a connection URL has a different format.

## Base

Base is the parent class used to define ORM models.

In SQLAlchemy 2.x:

from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

## Model

A model is a Python class representing a database table.

For example, a User model represents a users table.

## Session

A Session manages database operations such as inserting, updating, deleting and querying records.

Example:

from sqlalchemy.orm import sessionmaker

SessionLocal = sessionmaker(bind=engine)

db = SessionLocal()

Always close the session when you finish using it. In web applications, a dependency or context manager can manage this lifecycle.

# 4. Creating a database model

Example using SQLAlchemy 2.x:

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(
        String(150), unique=True, index=True
    )

Explanation:

- __tablename__: Specifies the database table name.
- id: Primary key.
- name: Stores the user's name.
- email: Stores a unique email address.
- mapped_column(): Defines a database column.
- primary_key=True: Uniquely identifies each row.
- unique=True: Prevents duplicate values.

# 5. Creating database tables

Use:

Base.metadata.create_all(bind=engine)

This creates tables for the models registered with Base if they do not already exist.

Important:
create_all() does not automatically update existing tables when you change a model. For production schema changes, use database migrations, commonly with Alembic.

# 6. CRUD operations

CRUD stands for:

- Create: Insert a new record.
- Read: Retrieve existing records.
- Update: Modify a record.
- Delete: Remove a record.

## CREATE

from sqlalchemy.orm import Session

new_user = User(
    name="Aman",
    email="aman@example.com"
)

db.add(new_user)
db.commit()
db.refresh(new_user)

Explanation:
- add(): Adds the object to the session.
- commit(): Saves the transaction.
- refresh(): Reloads database-generated values such as the assigned ID.

## READ

Get all users:

from sqlalchemy import select

users = db.scalars(select(User)).all()

Get one user by ID:

user = db.get(User, 1)

Find a user by email:

user = db.scalar(
    select(User).where(User.email == "aman@example.com")
)

## UPDATE

user = db.get(User, 1)

if user:
    user.name = "Rahul"
    db.commit()
    db.refresh(user)

SQLAlchemy detects the modified attribute and saves the change when the transaction is committed.

## DELETE

user = db.get(User, 1)

if user:
    db.delete(user)
    db.commit()

# 7. Primary keys and foreign keys

A primary key uniquely identifies a row in a table.

A foreign key connects one table to another.

Example:

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Submission(Base):
    __tablename__ = "submissions"

    id: Mapped[int] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id")
    )

    user: Mapped["User"] = relationship(
        back_populates="submissions"
    )

The user_id column references the id column in the users table.

A relationship() creates an ORM-level connection that allows you to navigate between related Python objects.

The corresponding User model would define:

submissions: Mapped[list["Submission"]] = relationship(
    back_populates="user"
)

# 8. One-to-many and many-to-many relationships

One-to-many:
One user can have multiple submissions.

Example:
User -> Submission 1
     -> Submission 2
     -> Submission 3

Many-to-many:
Many students can enroll in many courses.

This is usually implemented using an association table containing foreign keys to both tables.

# 9. Filtering and sorting

Filtering:

users = db.scalars(
    select(User).where(User.name == "Aman")
).all()

Sorting:

users = db.scalars(
    select(User).order_by(User.name)
).all()

Limiting:

users = db.scalars(
    select(User).limit(5)
).all()

Multiple conditions:

from sqlalchemy import and_

users = db.scalars(
    select(User).where(
        and_(
            User.name == "Aman",
            User.email == "aman@example.com"
        )
    )
).all()

# 10. Transactions and error handling

A transaction groups database operations into a unit of work.

commit():
Saves the transaction.

rollback():
Cancels uncommitted changes when an error occurs.

Example:

try:
    db.add(new_user)
    db.commit()
except Exception:
    db.rollback()
    raise

A failed transaction should be rolled back before reusing the session.

# 11. SQLAlchemy in FastAPI

FastAPI commonly uses dependency injection to provide a database session to an endpoint.

Example:

from fastapi import Depends
from sqlalchemy.orm import Session

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

Example endpoint:

@app.get("/users/{user_id}")
def get_user(
    user_id: int,
    db: Session = Depends(get_db)
):
    user = db.get(User, user_id)
    return user

Explanation:

- Depends(): Requests a dependency from FastAPI.
- get_db(): Creates and provides a database session.
- yield: Makes the session available to the endpoint.
- finally: Ensures that the session is closed.

# 12. SQLAlchemy in CodeQuest

CodeQuest uses SQLAlchemy models to represent application data.

Examples include:

User:
- id
- name
- email
- password_hash
- xp
- level
- streak

Problem:
- id
- title
- description
- difficulty
- topic

Submission:
- id
- code
- language
- status
- user_id
- problem_id

UserLessonProgress:
- id
- user_id
- lesson_id
- completed
- completed_at

When a user completes a lesson:
1. FastAPI receives the request.
2. The authentication dependency identifies the user.
3. The database session retrieves the user's progress.
4. SQLAlchemy inserts or updates the progress record.
5. The transaction is committed.
6. The API returns the updated progress and XP information.

# 13. SQLAlchemy and SQL injection

SQL injection occurs when unsafe user input is combined with SQL commands.

Avoid constructing SQL queries by concatenating user-provided strings.

Unsafe example:

query = "SELECT * FROM users WHERE name = '" + name + "'"

Safer SQLAlchemy example:

user = db.scalar(
    select(User).where(User.name == name)
)

SQLAlchemy uses parameterized query handling for normal expression-based queries. This helps protect against SQL injection.

Never assume that using an ORM makes every possible raw SQL query automatically safe.

# 14. Alembic database migrations

Alembic is a database migration tool commonly used with SQLAlchemy.

Suppose your User model originally has:

id
name
email

Later, you add:

phone_number

A migration describes how to change the existing database schema.

Common commands:

alembic init migrations
alembic revision --autogenerate -m "Add phone number"
alembic upgrade head

Important:
- A migration records a schema change.
- upgrade head applies the latest migrations.
- Migrations help maintain existing user data when the schema changes.

# 15. SQLAlchemy vs raw SQL

Raw SQL:
You write SQL statements directly.

SQLAlchemy ORM:
You work with Python classes and objects.

Raw SQL is useful when you need direct control over complex SQL operations.

SQLAlchemy ORM is useful for application development, relationships and routine CRUD operations.

# 16. SQLAlchemy vs Django ORM

SQLAlchemy:
- A flexible database toolkit and ORM.
- Commonly used with FastAPI and Flask.
- Gives developers more control over database design.

Django ORM:
- Built into the Django framework.
- Integrated with Django models and its application ecosystem.

# 17. SQLAlchemy interview summary

Remember these terms:

- Engine: Manages database connectivity.
- Base: Parent class for declarative models.
- Model: Python class mapped to a table.
- Session: Manages database operations.
- Primary key: Uniquely identifies a row.
- Foreign key: Connects related tables.
- relationship(): Defines ORM relationships.
- add(): Adds an object to a session.
- commit(): Saves a transaction.
- rollback(): Cancels uncommitted changes.
- refresh(): Reloads an object's database state.
- Alembic: Manages database schema migrations.
""",

        "key_concepts": [
            "SQLAlchemy",
            "Object Relational Mapping (ORM)",
            "Engine and database connection",
            "Declarative Base",
            "ORM models and mapped_column",
            "Database sessions",
            "CRUD operations",
            "Primary keys and foreign keys",
            "One-to-many and many-to-many relationships",
            "select(), where(), order_by() and limit()",
            "Transactions, commit and rollback",
            "FastAPI dependency injection",
            "SQL injection prevention",
            "Alembic migrations"
        ],

        "examples": {
            "python": """# SQLAlchemy 2.x minimal working example

from sqlalchemy import create_engine, String, select
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    sessionmaker
)

engine = create_engine("sqlite:///college.db")

class Base(DeclarativeBase):
    pass

class Student(Base):
    __tablename__ = "students"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    marks: Mapped[int]

Base.metadata.create_all(engine)

SessionLocal = sessionmaker(bind=engine)

with SessionLocal() as db:
    student = Student(name="Aman", marks=90)

    db.add(student)
    db.commit()
    db.refresh(student)

    students = db.scalars(select(Student)).all()

    for item in students:
        print(item.id, item.name, item.marks)

# Expected output:
# 1 Aman 90""",

            "java": """// Java does not use SQLAlchemy.
// Hibernate is a popular Java ORM.

import jakarta.persistence.*;

@Entity
@Table(name = "students")
public class Student {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String name;
    private int marks;
}

// A repository or EntityManager can save and retrieve
// Student objects using a Java ORM such as Hibernate.""",

            "cpp": """// C++ does not use SQLAlchemy.
// Database libraries such as SQLite C/C++ API can
// execute SQL statements directly.

#include <iostream>
using namespace std;

int main() {
    cout << "Student database application" << endl;
    cout << "SQL operations can be performed using SQLite.";
    return 0;
}

// For C++, SQLite, SOCI and ODB are examples of
// database access tools. They are not SQLAlchemy."""
        },

        "dry_run": """Operation                    Result
------------------------------------------------
Create Student object        Student(name="Aman")
db.add(student)              Object added to session
db.commit()                  INSERT saved to database
db.refresh(student)          Database ID loaded
select(Student)              SELECT query executed
db.scalars(...).all()        Student records returned

Output:
1 Aman 90""",

        "practice_questions": [
            {
                "question": "Create a SQLAlchemy model named Employee with id, name and salary fields. Create the table and insert one employee.",
                "solution": """from sqlalchemy import create_engine, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session

engine = create_engine("sqlite:///company.db")

class Base(DeclarativeBase):
    pass

class Employee(Base):
    __tablename__ = "employees"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    salary: Mapped[int]

Base.metadata.create_all(engine)

with Session(engine) as db:
    employee = Employee(name="Riya", salary=50000)
    db.add(employee)
    db.commit()
    db.refresh(employee)

    print(employee.id, employee.name, employee.salary)

# Expected output:
# 1 Riya 50000"""
            },
            {
                "question": "Retrieve all employees whose salary is greater than 40000.",
                "solution": """from sqlalchemy import select

with Session(engine) as db:
    employees = db.scalars(
        select(Employee).where(Employee.salary > 40000)
    ).all()

    for employee in employees:
        print(employee.name, employee.salary)

# The query returns only employees whose salary
# is greater than 40000."""
            }
        ],

        "interview_questions": [
            {
                "question": "What is SQLAlchemy?",
                "answer": "SQLAlchemy is a Python SQL toolkit and ORM that helps applications communicate with relational databases."
            },
            {
                "question": "What is ORM?",
                "answer": "Object Relational Mapping maps programming-language objects and classes to database rows and tables."
            },
            {
                "question": "What is an Engine?",
                "answer": "The Engine manages database connectivity and provides the interface for connecting to a database."
            },
            {
                "question": "What is a Session?",
                "answer": "A Session manages ORM objects and database transactions, including inserting, querying, updating and deleting records."
            },
            {
                "question": "What is DeclarativeBase?",
                "answer": "DeclarativeBase is the base class used by SQLAlchemy 2.x declarative models."
            },
            {
                "question": "What is the difference between add() and commit()?",
                "answer": "add() places an object in the session. commit() persists the transaction to the database."
            },
            {
                "question": "What is the difference between commit() and flush()?",
                "answer": "flush() sends pending changes to the database within the current transaction. commit() completes and commits that transaction."
            },
            {
                "question": "What is a foreign key?",
                "answer": "A foreign key references a key in another table and establishes a database-level relationship."
            },
            {
                "question": "What is relationship()?",
                "answer": "relationship() defines how related ORM objects can be accessed through Python attributes."
            },
            {
                "question": "What is rollback()?",
                "answer": "rollback() cancels uncommitted changes in the current transaction after an error or when changes should be discarded."
            },
            {
                "question": "How does SQLAlchemy work with FastAPI?",
                "answer": "FastAPI commonly provides a SQLAlchemy Session through Depends(), allowing endpoints to perform database operations."
            },
            {
                "question": "What is Alembic?",
                "answer": "Alembic is a database migration tool used with SQLAlchemy to track and apply schema changes."
            },
            {
                "question": "How does SQLAlchemy help prevent SQL injection?",
                "answer": "SQLAlchemy expression-based queries use parameterized query handling instead of directly concatenating untrusted input into SQL."
            },
            {
                "question": "Which ORM is commonly used in Java?",
                "answer": "Hibernate is a widely used Java ORM. It provides functionality similar in purpose to SQLAlchemy ORM."
            }
        ],

        "mcqs": [
            {
                "question": "What does ORM stand for?",
                "options": [
                    "Object Relational Mapping",
                    "Object Runtime Management",
                    "Operational Resource Mapping",
                    "Online Relational Model"
                ],
                "answer": "Object Relational Mapping",
                "explanation": "ORM maps programming-language objects to relational database tables."
            },
            {
                "question": "Which SQLAlchemy component manages database connectivity?",
                "options": ["Session", "Engine", "Model", "Column"],
                "answer": "Engine",
                "explanation": "The Engine manages connections to the database."
            },
            {
                "question": "Which method adds an object to a SQLAlchemy session?",
                "options": ["insert()", "save()", "add()", "push()"],
                "answer": "add()",
                "explanation": "db.add(object) adds an ORM object to the session."
            },
            {
                "question": "Which method commits a transaction?",
                "options": ["flush()", "commit()", "refresh()", "close()"],
                "answer": "commit()",
                "explanation": "commit() completes the transaction and saves its changes."
            },
            {
                "question": "Which field uniquely identifies a database row?",
                "options": ["Foreign key", "Primary key", "Index", "Relationship"],
                "answer": "Primary key",
                "explanation": "A primary key uniquely identifies each row in a table."
            },
            {
                "question": "Which SQLAlchemy construct defines an ORM relationship?",
                "options": ["relationship()", "connect()", "create_all()", "mapped_column()"],
                "answer": "relationship()",
                "explanation": "relationship() defines how related ORM objects are connected."
            },
            {
                "question": "Which tool manages SQLAlchemy database migrations?",
                "options": ["Uvicorn", "Alembic", "Pydantic", "NumPy"],
                "answer": "Alembic",
                "explanation": "Alembic tracks and applies database schema changes."
            },
            {
                "question": "Which method cancels uncommitted changes in a transaction?",
                "options": ["refresh()", "delete()", "rollback()", "add()"],
                "answer": "rollback()",
                "explanation": "rollback() cancels the current uncommitted transaction."
            }
        ]
    }
})


PYTHON_FOUNDATIONS.update({
    "python-jwt-authentication": {
        "id": "python-jwt-authentication",
        "title": "JWT Authentication – Secure Python Backend APIs",
        "duration": "60–75 min",

        "content": """
# 1. What is Authentication?

Authentication is the process of verifying the identity of a user.

For example, when someone logs into CodeQuest using an email and password, the backend verifies those credentials.

If the credentials are valid, the backend allows the user to access their account.

Examples:
- Login using email and password.
- Login using Google.
- Login using an authentication token.

Authentication answers: Who are you?

# 2. What is Authorization?

Authorization determines what an authenticated user is allowed to access.

For example:
- A normal user can solve coding problems.
- An administrator can manage users and problems.
- A user should not access another user's private submissions.

Authentication and authorization are different.

Authentication verifies identity.
Authorization checks permissions.

# 3. What is JWT?

JWT stands for JSON Web Token.

It is a compact token format commonly used to transfer claims between a client and a server.

JWT is commonly used for:
- User login.
- API authentication.
- Securing backend routes.
- Passing user identity information.
- Stateless authentication.

A JWT commonly looks like three Base64URL-encoded parts separated by dots:

header.payload.signature

Example structure:

xxxxx.yyyyy.zzzzz

A JWT is generally signed, not encrypted. Anyone who obtains a normal signed JWT can decode its header and payload. Therefore, never put passwords, API keys or other secrets inside its payload.

# 4. Three parts of a JWT

## Header

The header describes the token type and signing algorithm.

Example:

{
    "alg": "HS256",
    "typ": "JWT"
}

## Payload

The payload contains claims about the token.

Example:

{
    "sub": "123",
    "role": "user",
    "exp": 1900000000
}

Common claims:

- sub: Subject, often the user identifier.
- exp: Expiration time.
- iat: Issued-at time.
- iss: Issuer.
- aud: Intended audience.

Do not store sensitive information in the payload.

## Signature

The signature is generated using the header, payload and a secret or private key.

It helps the server verify that the token has not been modified.

For an HMAC-based JWT, the signature is calculated using a shared secret.

# 5. How JWT authentication works

Consider a user logging into CodeQuest.

Step 1: The user enters an email and password.

Step 2: The frontend sends the credentials to the login API.

Step 3: FastAPI retrieves the user from the database.

Step 4: The backend verifies the submitted password against the stored password hash.

Step 5: If the credentials are valid, the backend generates an access token.

Step 6: The frontend receives the token and uses it when requesting protected APIs.

Step 7: The backend verifies the token before allowing access.

Flow:

User
  |
  v
Login request
  |
  v
FastAPI backend
  |
  v
Verify password
  |
  v
Generate JWT
  |
  v
Frontend receives token
  |
  v
Request protected API
  |
  v
Verify JWT
  |
  v
Return protected data

# 6. Access tokens

An access token is used to access protected resources.

Example:

Authorization: Bearer <access_token>

The word Bearer means that whoever possesses the token can use it, subject to the token's validity and permissions.

Access tokens should generally have a short expiration time.

For example:
- 15 minutes.
- 30 minutes.
- 1 hour.

The exact duration depends on the application's security requirements.

# 7. Refresh tokens

A refresh token is used to obtain a new access token after the access token expires.

Example flow:

1. User logs in.
2. Backend issues an access token and refresh token.
3. Access token expires.
4. Frontend sends the refresh token to the refresh endpoint.
5. Backend validates the refresh token.
6. Backend issues a new access token.

Refresh tokens usually have a longer lifetime than access tokens.

Important security practices:
- Store refresh tokens securely.
- Validate expiration and revocation.
- Rotate refresh tokens when appropriate.
- Do not accept an access token as a refresh token.
- Consider storing refresh-token identifiers or hashes server-side.

# 8. Password hashing

Passwords should never be stored as plain text.

Bad practice:

password = "mypassword123"

Storing the original password directly in a database creates a serious security risk.

Instead, use password hashing.

Example using bcrypt:

import bcrypt

password = "mypassword123".encode("utf-8")

password_hash = bcrypt.hashpw(
    password,
    bcrypt.gensalt()
)

To verify:

is_valid = bcrypt.checkpw(
    password,
    password_hash
)

A password hash is stored in the database instead of the original password.

Hashing is one-way. You verify a password by checking it against the stored hash.

Use a password-hashing algorithm designed for passwords, such as Argon2id or bcrypt. Do not use ordinary SHA-256 alone for password storage.

# 9. Generating JWT tokens in Python

One library used for JWT handling is PyJWT.

Install:

pip install PyJWT

Example:

import jwt
from datetime import datetime, timedelta, timezone

SECRET_KEY = "replace-with-a-long-random-secret"
ALGORITHM = "HS256"

def create_access_token(user_id: int):
    now = datetime.now(timezone.utc)

    payload = {
        "sub": str(user_id),
        "iat": now,
        "exp": now + timedelta(minutes=30)
    }

    token = jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return token

Important:
- Keep the secret key in environment variables.
- Never commit real secrets to GitHub.
- Use a cryptographically strong random secret.
- Do not accept arbitrary signing algorithms from an untrusted token.

# 10. Verifying JWT tokens

Example:

def verify_access_token(token: str):
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        return payload

    except jwt.ExpiredSignatureError:
        return None

    except jwt.InvalidTokenError:
        return None

The backend verifies the signature and expiration before trusting the claims.

A token can be rejected if:
- Its signature is invalid.
- It has expired.
- Its structure is incorrect.
- Required claims are missing.
- Its issuer or audience is invalid when those checks are required.

# 11. JWT with FastAPI

FastAPI provides OAuth2-related security utilities.

Example:

from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/api/users/login"
)

This tells FastAPI that protected endpoints expect a Bearer token.

Example protected endpoint:

from fastapi import Depends

@app.get("/profile")
def get_profile(
    token: str = Depends(oauth2_scheme)
):
    return {"message": "Token received"}

This example only extracts the token. It does not authenticate the user by itself.

A real application must decode and verify the token, retrieve the user, and check permissions.

# 12. Dependency injection for authenticated users

A typical FastAPI backend uses a reusable dependency.

Example:

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/api/users/login"
)

def get_current_user(
    token: str = Depends(oauth2_scheme)
):
    payload = verify_access_token(token)

    if payload is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired token"
        )

    user_id = payload.get("sub")

    if user_id is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid token payload"
        )

    return user_id

A production implementation should also retrieve the user from the database and verify that the account is active.

# 13. Protecting backend routes

Example:

@app.get("/my-submissions")
def my_submissions(
    user_id: int = Depends(get_current_user)
):
    return {
        "message": "Protected submissions",
        "user_id": user_id
    }

The route depends on get_current_user.

If the token is invalid or missing, the request is rejected.

If valid, the endpoint receives the authenticated user's identifier.

This prevents the application from blindly trusting a user ID supplied by the frontend.

# 14. HTTP status codes for authentication

401 Unauthorized:
The request does not contain valid authentication credentials.

403 Forbidden:
The user is authenticated but does not have permission to perform the requested action.

400 Bad Request:
The request has invalid input.

404 Not Found:
The requested resource does not exist.

# 15. JWT security best practices

1. Never store plain-text passwords.
2. Use Argon2id or bcrypt for password hashing.
3. Keep signing secrets in environment variables.
4. Never expose secrets in frontend JavaScript.
5. Set token expiration.
6. Validate the signature and claims.
7. Use HTTPS in production.
8. Never place sensitive information in JWT payloads.
9. Validate authorization on the backend.
10. Use refresh-token rotation and revocation where appropriate.
11. Do not log complete tokens or passwords.
12. Choose token storage carefully.

Browser storage considerations:

- localStorage is accessible to JavaScript and can be exposed by cross-site scripting (XSS).
- HttpOnly cookies cannot be read by JavaScript, but cookie-based authentication needs appropriate CSRF protection.
- Secure cookies should only be sent over HTTPS.
- SameSite settings should be configured according to the application's requirements.

# 16. JWT in CodeQuest

CodeQuest uses JWT authentication to protect backend APIs.

Typical flow:

1. A user registers.
2. The password is hashed before storage.
3. The user logs in.
4. FastAPI verifies the password.
5. The backend generates an access token.
6. The frontend sends the token with protected API requests.
7. The backend uses get_current_user to identify the logged-in user.

Examples of protected CodeQuest functionality:

- Viewing personal progress.
- Accessing learning paths.
- Completing lessons.
- Viewing personal submissions.
- Using authenticated AI Tutor functionality.

The backend should always identify the user from verified authentication credentials, not from an untrusted user ID in the request body.

# 17. JWT vs Session-based authentication

Session-based authentication:

- Server maintains session state.
- Client typically stores a session identifier in a cookie.
- Server looks up the session for incoming requests.

JWT-based authentication:

- Client sends a signed token.
- Server validates the token and its claims.
- The server does not necessarily need a session record for every request.

JWT can support stateless authentication, but revocation and refresh-token management may still require server-side state.

# 18. Interview revision

Remember:

- JWT: JSON Web Token.
- Authentication: Verifying identity.
- Authorization: Checking permissions.
- Header: Token metadata.
- Payload: Token claims.
- Signature: Protects token integrity.
- Access token: Used to access protected APIs.
- Refresh token: Used to obtain new access tokens.
- Bearer token: Token sent in the Authorization header.
- OAuth2PasswordBearer: FastAPI utility for extracting Bearer tokens.
- Password hashing: Secure one-way password transformation.
- 401: Invalid or missing authentication.
- 403: Insufficient permission.
""",

        "key_concepts": [
            "Authentication and authorization",
            "JSON Web Token (JWT)",
            "JWT header, payload and signature",
            "JWT claims: sub, exp, iat, iss and aud",
            "Access tokens",
            "Refresh tokens",
            "Password hashing with bcrypt and Argon2id",
            "PyJWT token generation and verification",
            "HS256 signing algorithm",
            "OAuth2PasswordBearer",
            "FastAPI dependency injection",
            "Protected API routes",
            "401 Unauthorized and 403 Forbidden",
            "Token expiration and revocation",
            "JWT security best practices",
            "Session-based versus token-based authentication"
        ],

        "examples": {
            "python": """# Generate and verify a JWT using PyJWT.
# Install: pip install PyJWT

import jwt
from datetime import datetime, timedelta, timezone

SECRET_KEY = "replace-with-a-long-random-secret"
ALGORITHM = "HS256"

def create_token(user_id):
    now = datetime.now(timezone.utc)

    payload = {
        "sub": str(user_id),
        "iat": now,
        "exp": now + timedelta(minutes=30)
    }

    return jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

def verify_token(token):
    try:
        return jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )
    except jwt.InvalidTokenError:
        return None

token = create_token(101)
print("Token generated:", bool(token))

decoded = verify_token(token)
print("User ID:", decoded["sub"])

# Expected output:
# Token generated: True
# User ID: 101

# Demonstration only: use environment variables for
# the secret in an actual application.""",

            "java": """// Java commonly uses the JJWT library for JWT handling.
// This is an equivalent concept, not SQLAlchemy or PyJWT.

import io.jsonwebtoken.Jwts;
import io.jsonwebtoken.security.Keys;
import java.security.Key;
import java.util.Date;

public class JwtExample {
    public static void main(String[] args) {
        Key key = Keys.secretKeyFor(
            io.jsonwebtoken.SignatureAlgorithm.HS256
        );

        String token = Jwts.builder()
            .subject("101")
            .issuedAt(new Date())
            .expiration(
                new Date(System.currentTimeMillis() + 1800000)
            )
            .signWith(key)
            .compact();

        System.out.println("JWT generated: " + !token.isEmpty());
    }
}

// In real applications, securely manage and persist
// signing keys rather than generating a new one per process.""",

            "cpp": """// C++ does not provide a standard built-in JWT library.
// Libraries such as jwt-cpp can be used.

#include <iostream>
using namespace std;

int main() {
    string userId = "101";

    cout << "Authenticated user: " << userId << endl;

    return 0;
}

// This illustrates the identity concept only.
// A real C++ backend must use a JWT library to
// sign and verify tokens securely."""
        },

        "dry_run": """JWT authentication flow:

User ID: 101
        |
        v
Create payload:
sub = "101"
exp = 30 minutes from now
        |
        v
Sign payload using secret key
        |
        v
JWT generated
        |
        v
Client sends:
Authorization: Bearer <token>
        |
        v
Backend verifies signature and expiration
        |
        v
Extract subject: 101
        |
        v
Retrieve user and authorize request

Result:
Authenticated user ID = 101""",

        "practice_questions": [
            {
                "question": "Write a Python function that creates a JWT containing a user ID and a 15-minute expiration time.",
                "solution": """import jwt
from datetime import datetime, timedelta, timezone

SECRET_KEY = "replace-with-a-long-random-secret"

def create_access_token(user_id):
    now = datetime.now(timezone.utc)

    payload = {
        "sub": str(user_id),
        "iat": now,
        "exp": now + timedelta(minutes=15)
    }

    return jwt.encode(
        payload,
        SECRET_KEY,
        algorithm="HS256"
    )

token = create_access_token(25)
print(bool(token))

# Expected output:
# True

# Install PyJWT using:
# pip install PyJWT"""
            },
            {
                "question": "Write a Python function that verifies a JWT and extracts the user ID. Handle invalid or expired tokens.",
                "solution": """import jwt

SECRET_KEY = "replace-with-a-long-random-secret"

def get_user_id(token):
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=["HS256"]
        )

        user_id = payload.get("sub")

        if user_id is None:
            return None

        return int(user_id)

    except (jwt.InvalidTokenError, ValueError, TypeError):
        return None

# For a valid token containing sub="25":
# get_user_id(token) returns 25.
#
# For an invalid or expired token:
# get_user_id(token) returns None."""
            }
        ],

        "interview_questions": [
            {
                "question": "What is JWT?",
                "answer": "JWT stands for JSON Web Token. It is a compact token format commonly used to transmit signed claims between a client and server."
            },
            {
                "question": "What are the three parts of a JWT?",
                "answer": "Header, payload and signature. They are separated by dots."
            },
            {
                "question": "Is JWT encrypted?",
                "answer": "A normal signed JWT is not encrypted. Its payload can be decoded, so sensitive information must not be stored in it."
            },
            {
                "question": "What is the difference between authentication and authorization?",
                "answer": "Authentication verifies identity, whereas authorization determines which resources or operations that identity is allowed to access."
            },
            {
                "question": "What is an access token?",
                "answer": "An access token is a credential sent with requests to access protected APIs. It normally has a relatively short lifetime."
            },
            {
                "question": "What is a refresh token?",
                "answer": "A refresh token is used to obtain a new access token without asking the user to log in again, subject to server-side validation."
            },
            {
                "question": "What does Bearer mean in an Authorization header?",
                "answer": "Bearer indicates that the request is presenting a token as its authentication credential, commonly using Authorization: Bearer <token>."
            },
            {
                "question": "What is OAuth2PasswordBearer in FastAPI?",
                "answer": "It is a FastAPI security utility that extracts a Bearer token from the Authorization header and integrates with OAuth2 security documentation."
            },
            {
                "question": "What is the purpose of the JWT signature?",
                "answer": "The signature allows the server to verify the token's integrity and that it was signed using a trusted key."
            },
            {
                "question": "Why should passwords be hashed?",
                "answer": "Hashing prevents the original passwords from being stored directly. Passwords should be hashed using dedicated algorithms such as Argon2id or bcrypt."
            },
            {
                "question": "What is the difference between HTTP 401 and 403?",
                "answer": "401 means valid authentication credentials are missing or invalid. 403 means the authenticated user is not permitted to perform the requested operation."
            },
            {
                "question": "What is the exp claim?",
                "answer": "The exp claim specifies the token's expiration time. A token must not be accepted after its expiration."
            },
            {
                "question": "Where should the JWT secret key be stored?",
                "answer": "It should be stored securely on the backend, typically in environment variables or a secrets manager, and never exposed in frontend code or committed to Git."
            },
            {
                "question": "How does CodeQuest use JWT?",
                "answer": "After login, CodeQuest issues an access token. The frontend sends it with protected API requests, and FastAPI verifies it through an authentication dependency before accessing user-specific data."
            }
        ],

        "mcqs": [
            {
                "question": "What is the full form of JWT?",
                "options": [
                    "Java Web Technology",
                    "JSON Web Token",
                    "JavaScript Web Transfer",
                    "JSON Web Table"
                ],
                "answer": "JSON Web Token",
                "explanation": "JWT stands for JSON Web Token."
            },
            {
                "question": "Which are the three parts of a JWT?",
                "options": [
                    "Header, Payload, Signature",
                    "Username, Password, Token",
                    "Request, Response, Server",
                    "Key, Database, Session"
                ],
                "answer": "Header, Payload, Signature",
                "explanation": "A JWT contains three dot-separated components."
            },
            {
                "question": "Which JWT claim specifies expiration?",
                "options": ["sub", "iat", "exp", "iss"],
                "answer": "exp",
                "explanation": "The exp claim represents the token expiration time."
            },
            {
                "question": "Which HTTP header commonly carries a JWT access token?",
                "options": [
                    "Content-Type",
                    "Authorization",
                    "Accept-Language",
                    "Host"
                ],
                "answer": "Authorization",
                "explanation": "The common format is Authorization: Bearer <token>."
            },
            {
                "question": "Which status code commonly indicates missing or invalid authentication?",
                "options": ["200", "301", "401", "500"],
                "answer": "401",
                "explanation": "401 indicates that valid authentication credentials are missing or invalid."
            },
            {
                "question": "Which FastAPI utility extracts an OAuth2 Bearer token?",
                "options": [
                    "OAuth2PasswordBearer",
                    "BaseModel",
                    "SQLAlchemy",
                    "BackgroundTasks"
                ],
                "answer": "OAuth2PasswordBearer",
                "explanation": "OAuth2PasswordBearer extracts the Bearer token from the Authorization header."
            },
            {
                "question": "Should a normal signed JWT payload contain a user's plain-text password?",
                "options": [
                    "Yes",
                    "No",
                    "Only for admins",
                    "Only when using HS256"
                ],
                "answer": "No",
                "explanation": "A signed JWT is not necessarily encrypted. Its payload can be decoded."
            },
            {
                "question": "Which is a suitable password-hashing algorithm?",
                "options": [
                    "Base64",
                    "Plain SHA-256 alone",
                    "Argon2id",
                    "UTF-8"
                ],
                "answer": "Argon2id",
                "explanation": "Argon2id is designed for password hashing and is a suitable modern choice."
            }
        ]
    }
})


PYTHON_FOUNDATIONS.update({
    "python-sql-database-fundamentals": {
        "id": "python-sql-database-fundamentals",
        "title": "SQL and Database Fundamentals",
        "duration": "75–90 min",

        "content": """
# 1. What is a Database?

A database is an organized collection of information that can be stored, accessed, managed and updated.

Examples:
- College student records.
- Banking transactions.
- E-commerce products and orders.
- CodeQuest users, problems and submissions.

A Database Management System (DBMS) is software used to manage databases.

Examples:
- MySQL
- PostgreSQL
- SQLite
- Oracle Database
- Microsoft SQL Server

# 2. What is SQL?

SQL stands for Structured Query Language.

It is used to communicate with relational databases.

SQL can be used to:
- Create databases and tables.
- Insert records.
- Retrieve information.
- Update records.
- Delete records.
- Control access.
- Manage transactions.

# 3. Relational Database Concepts

A relational database stores information in tables.

A table consists of:
- Rows: Individual records.
- Columns: Attributes of records.
- Primary key: Uniquely identifies each row.
- Foreign key: Connects one table to another.

Example Students table:

| id | name | age | marks |
|----|------|-----|-------|
| 1 | Aman | 21 | 85 |
| 2 | Riya | 22 | 92 |
| 3 | Rahul | 20 | 75 |

Here:
- id, name, age and marks are columns.
- Each student is a row.
- id can be the primary key.

# 4. Types of SQL Commands

SQL commands are commonly grouped into five categories.

## DDL – Data Definition Language

Used to define database structures.

Commands:
- CREATE
- ALTER
- DROP
- TRUNCATE

Example:

CREATE TABLE Students (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    marks INT
);

## DML – Data Manipulation Language

Used to modify table data.

Commands:
- INSERT
- UPDATE
- DELETE

Example:

INSERT INTO Students (id, name, marks)
VALUES (1, 'Aman', 85);

## DQL – Data Query Language

Used to retrieve data.

Command:
- SELECT

Example:

SELECT * FROM Students;

## DCL – Data Control Language

Used to manage database permissions.

Commands:
- GRANT
- REVOKE

## TCL – Transaction Control Language

Used to manage transactions.

Commands:
- COMMIT
- ROLLBACK
- SAVEPOINT

# 5. Creating a Table

Example:

CREATE TABLE Employees (
    id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE,
    salary DECIMAL(10, 2),
    department VARCHAR(50)
);

Explanation:

- INT: Integer values.
- VARCHAR: Variable-length text.
- DECIMAL: Exact numeric values, useful for monetary amounts.
- PRIMARY KEY: Unique row identifier.
- NOT NULL: Value cannot be NULL.
- UNIQUE: Prevents duplicate values.

# 6. INSERT – Adding Records

INSERT INTO Employees
(id, name, email, salary, department)
VALUES
(1, 'Aman', 'aman@example.com', 50000, 'IT');

Insert multiple records:

INSERT INTO Employees
(id, name, email, salary, department)
VALUES
(2, 'Riya', 'riya@example.com', 60000, 'HR'),
(3, 'Rahul', 'rahul@example.com', 45000, 'IT');

# 7. SELECT – Retrieving Records

Retrieve all columns:

SELECT * FROM Employees;

Retrieve selected columns:

SELECT name, salary FROM Employees;

Retrieve unique departments:

SELECT DISTINCT department FROM Employees;

Limit the number of records:

SELECT * FROM Employees LIMIT 5;

LIMIT syntax is supported by databases such as MySQL, PostgreSQL and SQLite. Other database systems may use different syntax.

# 8. WHERE – Filtering Records

WHERE filters records according to a condition.

Example:

SELECT * FROM Employees
WHERE salary > 45000;

Other operators:

- = : Equal to
- != or <> : Not equal to
- > : Greater than
- < : Less than
- >= : Greater than or equal to
- <= : Less than or equal to

Multiple conditions:

SELECT * FROM Employees
WHERE department = 'IT'
AND salary > 40000;

OR example:

SELECT * FROM Employees
WHERE department = 'IT'
OR department = 'HR';

NOT example:

SELECT * FROM Employees
WHERE NOT department = 'HR';

# 9. UPDATE – Modifying Records

UPDATE Employees
SET salary = 55000
WHERE id = 1;

Important:
Always understand the WHERE condition before running UPDATE.

Without WHERE, every row may be updated.

# 10. DELETE – Removing Records

DELETE FROM Employees
WHERE id = 3;

Without WHERE, all rows in the table may be deleted.

DELETE removes rows but does not remove the table structure.

# 11. ORDER BY – Sorting Records

Ascending order:

SELECT * FROM Employees
ORDER BY salary ASC;

Descending order:

SELECT * FROM Employees
ORDER BY salary DESC;

You can sort using multiple columns:

SELECT * FROM Employees
ORDER BY department ASC, salary DESC;

# 12. Aggregate Functions

Aggregate functions calculate values from multiple rows.

COUNT():

SELECT COUNT(*) FROM Employees;

SUM():

SELECT SUM(salary) FROM Employees;

AVG():

SELECT AVG(salary) FROM Employees;

MIN():

SELECT MIN(salary) FROM Employees;

MAX():

SELECT MAX(salary) FROM Employees;

Common uses:
- Number of employees.
- Total salary expenditure.
- Average marks.
- Highest salary.
- Lowest salary.

# 13. GROUP BY

GROUP BY groups rows that have the same values.

Example:

SELECT department, COUNT(*)
FROM Employees
GROUP BY department;

This returns the number of employees in each department.

Another example:

SELECT department, AVG(salary)
FROM Employees
GROUP BY department;

# 14. HAVING

HAVING filters groups created by GROUP BY.

Example:

SELECT department, AVG(salary)
FROM Employees
GROUP BY department
HAVING AVG(salary) > 45000;

Difference:

WHERE filters individual rows before grouping.

HAVING filters groups after grouping.

# 15. SQL Joins

Joins combine related information from multiple tables.

Suppose we have:

Employees:

| id | name | department_id |
|----|------|---------------|
| 1 | Aman | 10 |
| 2 | Riya | 20 |
| 3 | Rahul | 10 |

Departments:

| id | department_name |
|----|-----------------|
| 10 | IT |
| 20 | HR |
| 30 | Finance |

## INNER JOIN

Returns matching records from both tables.

SELECT e.name, d.department_name
FROM Employees e
INNER JOIN Departments d
ON e.department_id = d.id;

## LEFT JOIN

Returns all rows from the left table and matching rows from the right table.

If no match exists, right-side columns contain NULL.

SELECT e.name, d.department_name
FROM Employees e
LEFT JOIN Departments d
ON e.department_id = d.id;

## RIGHT JOIN

Returns all rows from the right table and matching rows from the left table.

Support varies by database. SQLite versions commonly used in modern applications support RIGHT JOIN.

## FULL OUTER JOIN

Returns matching and non-matching rows from both tables.

Non-matching columns are filled with NULL.

Support varies across database systems. SQLite supports FULL OUTER JOIN in modern versions.

## CROSS JOIN

Returns the Cartesian product of two tables.

If the first table has 3 rows and the second has 4 rows, the result contains 12 combinations.

# 16. Subqueries

A subquery is a query inside another query.

Example:

SELECT name, salary
FROM Employees
WHERE salary > (
    SELECT AVG(salary)
    FROM Employees
);

This retrieves employees earning more than the average salary.

Subqueries can appear in:
- WHERE
- FROM
- SELECT
- HAVING

# 17. Constraints

Constraints enforce rules on database columns.

Important constraints:

PRIMARY KEY:
Uniquely identifies each record.

FOREIGN KEY:
References a key in another table.

NOT NULL:
Prevents NULL values.

UNIQUE:
Prevents duplicate values.

CHECK:
Ensures values satisfy a condition.

DEFAULT:
Provides a default value when one is not supplied.

Example:

CREATE TABLE Students (
    id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT CHECK (age >= 18),
    city VARCHAR(50) DEFAULT 'Unknown'
);

# 18. NULL Values

NULL represents missing or unknown information.

It is not the same as:
- Zero.
- Empty string.
- False.

Correct NULL check:

SELECT * FROM Employees
WHERE email IS NULL;

To check non-NULL values:

SELECT * FROM Employees
WHERE email IS NOT NULL;

Do not use:

WHERE email = NULL;

# 19. Database Normalization

Normalization organizes database tables to reduce unnecessary duplication and update problems.

## First Normal Form (1NF)

Each cell should contain a single atomic value.

Avoid storing multiple phone numbers in one column as a comma-separated list.

## Second Normal Form (2NF)

The table must be in 1NF, and every non-key attribute must depend on the whole candidate key, not just part of a composite candidate key.

This removes partial dependencies.

## Third Normal Form (3NF)

The table must be in 2NF and have no transitive dependency of non-key attributes on a candidate key.

This removes transitive dependencies.

Example:

Instead of repeatedly storing department details with every employee, create a separate Departments table and reference it using department_id.

Benefits:
- Less duplicate data.
- Easier updates.
- Better consistency.
- Reduced insertion and deletion anomalies.

# 20. Database Indexing

An index helps the database find records more efficiently.

Example:

CREATE INDEX idx_employee_email
ON Employees(email);

Without an index, the database may need to examine many rows.

With a suitable index, it can locate matching records more efficiently.

Advantages:
- Faster lookups in suitable queries.
- Faster filtering and joins in many cases.

Disadvantages:
- Requires additional storage.
- Inserts, updates and deletes may become more expensive because indexes also need maintenance.

Do not create indexes on every column automatically.

# 21. Transactions and ACID Properties

A transaction is a group of database operations treated as one logical unit.

Example: Bank transfer.

1. Deduct money from account A.
2. Add money to account B.
3. Commit both operations.

If the operation fails, roll back the transaction.

ACID properties:

Atomicity:
All operations succeed together or fail together.

Consistency:
A transaction preserves database rules and constraints.

Isolation:
Concurrent transactions should not interfere in an invalid way.

Durability:
Committed changes survive failures according to the database's durability guarantees.

# 22. COMMIT and ROLLBACK

COMMIT saves transaction changes.

ROLLBACK cancels uncommitted transaction changes.

Example:

BEGIN;

UPDATE Accounts
SET balance = balance - 1000
WHERE id = 1;

UPDATE Accounts
SET balance = balance + 1000
WHERE id = 2;

COMMIT;

If an error occurs before committing:

ROLLBACK;

Transaction syntax and behavior can vary slightly between database systems.

# 23. SQL Views

A view is a virtual table based on a query.

Example:

CREATE VIEW IT_Employees AS
SELECT name, salary
FROM Employees
WHERE department = 'IT';

Retrieve from the view:

SELECT * FROM IT_Employees;

Views can simplify complex queries and restrict which columns are exposed to users.

# 24. Stored Procedures and Triggers

Stored Procedure:
A stored routine containing SQL operations. Availability and syntax vary across database systems.

Trigger:
A database operation that automatically executes when a specified event occurs, such as INSERT, UPDATE or DELETE.

Triggers are useful for auditing and enforcing certain database rules, but should be used carefully.

# 25. SQL Window Functions

Window functions calculate values across related rows without combining them into a single grouped row.

Example:

SELECT
    name,
    salary,
    RANK() OVER (ORDER BY salary DESC) AS salary_rank
FROM Employees;

Common window functions:

- ROW_NUMBER()
- RANK()
- DENSE_RANK()
- LAG()
- LEAD()

These are useful in reporting, analytics and interview questions.

# 26. SQL in Python Backend Development

Python backend applications commonly use SQL databases.

A typical application flow:

Frontend
   |
   v
FastAPI endpoint
   |
   v
Business logic
   |
   v
SQLAlchemy ORM
   |
   v
SQL database
   |
   v
Return response

SQLAlchemy can generate SQL queries from Python expressions.

Example:

from sqlalchemy import select

users = db.scalars(
    select(User).where(User.xp >= 100)
).all()

This is conceptually equivalent to:

SELECT * FROM users WHERE xp >= 100;

# 27. SQL in CodeQuest

CodeQuest stores several types of data:

Users:
Stores registration information, password hashes, XP and levels.

Problems:
Stores coding problem descriptions and test cases.

Submissions:
Stores submitted code, language, result and user relationship.

UserLessonProgress:
Stores completed lesson IDs and completion timestamps.

Examples of useful queries:

Retrieve a user's submissions:

SELECT *
FROM submissions
WHERE user_id = 1;

Retrieve completed lessons:

SELECT *
FROM user_lesson_progress
WHERE user_id = 1
AND completed = TRUE;

Count solved problems:

SELECT COUNT(DISTINCT problem_id)
FROM submissions
WHERE user_id = 1
AND passed = TRUE;

# 28. SQL Interview Revision

Remember these differences:

- DBMS vs RDBMS: RDBMS is a relational database management system.
- Primary key vs Foreign key: Unique row identifier vs reference to another table.
- DELETE vs TRUNCATE vs DROP: Remove selected rows, remove all rows, remove the table structure.
- WHERE vs HAVING: Filter rows vs filter groups.
- UNION vs UNION ALL: Combine results with duplicate elimination vs retain duplicates.
- INNER JOIN vs LEFT JOIN: Matching records vs all left-side records plus matches.
- Primary key vs UNIQUE: Both enforce uniqueness, but primary keys identify rows and cannot be NULL.
- Normalization: Reduces redundancy and anomalies.
- Indexing: Improves suitable lookup queries at the cost of storage and write overhead.
- ACID: Atomicity, Consistency, Isolation and Durability.
- COMMIT vs ROLLBACK: Save vs cancel uncommitted changes.
""",

        "key_concepts": [
            "Database and DBMS",
            "Relational database and tables",
            "SQL command categories: DDL, DML, DQL, DCL and TCL",
            "CREATE, INSERT, SELECT, UPDATE and DELETE",
            "WHERE, DISTINCT, ORDER BY and LIMIT",
            "Aggregate functions: COUNT, SUM, AVG, MIN and MAX",
            "GROUP BY and HAVING",
            "INNER, LEFT, RIGHT, FULL OUTER and CROSS JOIN",
            "Subqueries",
            "Primary key and foreign key",
            "NOT NULL, UNIQUE, CHECK and DEFAULT",
            "NULL handling",
            "Normalization: 1NF, 2NF and 3NF",
            "Database indexes",
            "Transactions and ACID properties",
            "COMMIT and ROLLBACK",
            "Views, stored procedures and triggers",
            "Window functions",
            "SQLAlchemy integration with Python backend"
        ],

        "examples": {
            "python": """# Python example using sqlite3.
# sqlite3 is included with standard Python installations.

import sqlite3

connection = sqlite3.connect(":memory:")
cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE students (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        marks INTEGER
    )
''')

cursor.execute(
    "INSERT INTO students (name, marks) VALUES (?, ?)",
    ("Aman", 85)
)

cursor.execute(
    "INSERT INTO students (name, marks) VALUES (?, ?)",
    ("Riya", 92)
)

connection.commit()

cursor.execute(
    "SELECT name, marks FROM students WHERE marks > ?",
    (80,)
)

for row in cursor.fetchall():
    print(row)

connection.close()

# Expected output:
# ('Aman', 85)
# ('Riya', 92)

# The ? placeholders safely bind values to the query.""",

            "java": """// Java can communicate with relational databases
// using JDBC (Java Database Connectivity).

import java.sql.*;

public class Main {
    public static void main(String[] args) throws Exception {
        Connection con = DriverManager.getConnection(
            "jdbc:sqlite:college.db"
        );

        PreparedStatement ps = con.prepareStatement(
            "SELECT name, marks FROM students WHERE marks > ?"
        );

        ps.setInt(1, 80);

        ResultSet rs = ps.executeQuery();

        while (rs.next()) {
            System.out.println(
                rs.getString("name") + " " +
                rs.getInt("marks")
            );
        }

        rs.close();
        ps.close();
        con.close();
    }
}

// Add an appropriate SQLite JDBC driver to the project.
// PreparedStatement supports parameterized queries.""",

            "cpp": """// C++ can communicate with SQLite using
// the SQLite C/C++ API.

#include <iostream>
#include <sqlite3.h>
using namespace std;

int main() {
    sqlite3* db = nullptr;

    int result = sqlite3_open("college.db", &db);

    if (result != SQLITE_OK) {
        cout << "Database connection failed";
        return 1;
    }

    cout << "Database connected successfully";

    sqlite3_close(db);
    return 0;
}

// Compile with the SQLite development library installed.
// This demonstrates connection setup, not a complete query."""
        },

        "dry_run": """Students table:

id    name     marks
1     Aman     85
2     Riya     92
3     Rahul    70
4     Neha     88

Query:

SELECT name, marks
FROM Students
WHERE marks > 80
ORDER BY marks DESC;

Execution:
1. WHERE removes Rahul because 70 is not greater than 80.
2. Aman, Riya and Neha remain.
3. ORDER BY sorts marks in descending order.

Result:

Riya     92
Neha     88
Aman     85""",

        "practice_questions": [
            {
                "question": "Write an SQL query to find the second-highest distinct salary from an Employees table.",
                "solution": """SELECT MAX(salary) AS second_highest_salary
FROM Employees
WHERE salary < (
    SELECT MAX(salary)
    FROM Employees
);

Explanation:
1. The inner query finds the highest salary.
2. The outer WHERE removes salaries equal to the highest.
3. MAX() returns the next-highest distinct salary.

If no second distinct salary exists, the result is NULL."""
            },
            {
                "question": "Write an SQL query to find departments having more than 3 employees.",
                "solution": """SELECT department, COUNT(*) AS employee_count
FROM Employees
GROUP BY department
HAVING COUNT(*) > 3;

Explanation:
1. GROUP BY groups employees by department.
2. COUNT(*) counts employees in each department.
3. HAVING filters groups with more than 3 employees."""
            },
            {
                "question": "Write an SQL query to display employee names with their department names using INNER JOIN.",
                "solution": """SELECT e.name, d.department_name
FROM Employees e
INNER JOIN Departments d
ON e.department_id = d.id;

Explanation:
The query matches department_id in Employees
with id in Departments and returns matching records."""
            }
        ],

        "interview_questions": [
            {
                "question": "What is SQL?",
                "answer": "SQL stands for Structured Query Language. It is used to create, retrieve, modify and manage data in relational databases."
            },
            {
                "question": "What is the difference between DBMS and RDBMS?",
                "answer": "DBMS is a general system for managing databases. RDBMS organizes data primarily into related tables and supports relational concepts such as keys and constraints."
            },
            {
                "question": "What are DDL, DML, DQL, DCL and TCL?",
                "answer": "DDL defines structures, DML modifies records, DQL retrieves data, DCL manages permissions and TCL manages transactions."
            },
            {
                "question": "What is a primary key?",
                "answer": "A primary key uniquely identifies every row in a table. It cannot contain NULL values."
            },
            {
                "question": "What is a foreign key?",
                "answer": "A foreign key references a key in another or the same table and helps maintain referential integrity."
            },
            {
                "question": "What is the difference between WHERE and HAVING?",
                "answer": "WHERE filters individual rows before grouping. HAVING filters groups after GROUP BY."
            },
            {
                "question": "What is the difference between DELETE, TRUNCATE and DROP?",
                "answer": "DELETE removes selected rows or all rows, TRUNCATE removes all rows while retaining the table structure, and DROP removes the table itself. Exact transactional and identity-reset behavior varies by database."
            },
            {
                "question": "What is the difference between INNER JOIN and LEFT JOIN?",
                "answer": "INNER JOIN returns matching records from both tables. LEFT JOIN returns all rows from the left table and matching rows from the right table."
            },
            {
                "question": "What is normalization?",
                "answer": "Normalization organizes database tables to reduce redundant data and prevent insertion, update and deletion anomalies."
            },
            {
                "question": "Explain 1NF, 2NF and 3NF.",
                "answer": "1NF requires atomic values, 2NF removes partial dependencies on composite candidate keys, and 3NF removes transitive dependencies of non-key attributes."
            },
            {
                "question": "What is an index?",
                "answer": "An index is a data structure that helps the database locate records efficiently, often improving reads but adding storage and write overhead."
            },
            {
                "question": "What are ACID properties?",
                "answer": "Atomicity, Consistency, Isolation and Durability are properties that help ensure reliable database transactions."
            },
            {
                "question": "What is a subquery?",
                "answer": "A subquery is a query nested inside another SQL query."
            },
            {
                "question": "What is the difference between UNION and UNION ALL?",
                "answer": "UNION combines query results and removes duplicates. UNION ALL combines results while retaining duplicates."
            },
            {
                "question": "What is a view?",
                "answer": "A view is a virtual table defined by a query. It can simplify complex queries and restrict access to selected data."
            },
            {
                "question": "What is a transaction?",
                "answer": "A transaction is a logical group of database operations that should be completed or rolled back according to the application's requirements."
            },
            {
                "question": "What is a window function?",
                "answer": "A window function calculates a value across related rows without collapsing them into one row per group. Examples include ROW_NUMBER(), RANK() and DENSE_RANK()."
            },
            {
                "question": "How does Python connect to a database?",
                "answer": "Python can use sqlite3 for SQLite, database-specific drivers for other systems, or an ORM such as SQLAlchemy."
            },
            {
                "question": "What is SQL injection?",
                "answer": "SQL injection is a security vulnerability in which untrusted input changes the meaning of a SQL query. Parameterized queries help prevent it."
            }
        ],

        "mcqs": [
            {
                "question": "What does SQL stand for?",
                "options": [
                    "Structured Query Language",
                    "Simple Question Language",
                    "System Query Logic",
                    "Standard Queue Language"
                ],
                "answer": "Structured Query Language",
                "explanation": "SQL is used to communicate with relational databases."
            },
            {
                "question": "Which command retrieves data from a table?",
                "options": ["INSERT", "SELECT", "UPDATE", "DROP"],
                "answer": "SELECT",
                "explanation": "SELECT retrieves records from database tables."
            },
            {
                "question": "Which clause filters groups after GROUP BY?",
                "options": ["WHERE", "ORDER BY", "HAVING", "LIMIT"],
                "answer": "HAVING",
                "explanation": "HAVING applies conditions to grouped results."
            },
            {
                "question": "Which JOIN returns all rows from the left table and matching rows from the right table?",
                "options": ["INNER JOIN", "LEFT JOIN", "CROSS JOIN", "SELF JOIN"],
                "answer": "LEFT JOIN",
                "explanation": "LEFT JOIN preserves every row from the left-side table."
            },
            {
                "question": "Which constraint uniquely identifies each row?",
                "options": ["DEFAULT", "CHECK", "PRIMARY KEY", "FOREIGN KEY"],
                "answer": "PRIMARY KEY",
                "explanation": "A primary key uniquely identifies each record."
            },
            {
                "question": "Which ACID property ensures all operations in a transaction succeed together or fail together?",
                "options": ["Consistency", "Atomicity", "Isolation", "Durability"],
                "answer": "Atomicity",
                "explanation": "Atomicity treats a transaction as an indivisible unit."
            },
            {
                "question": "Which command removes a table structure?",
                "options": ["DELETE", "TRUNCATE", "DROP", "UPDATE"],
                "answer": "DROP",
                "explanation": "DROP removes the database object itself."
            },
            {
                "question": "Which SQL function counts records?",
                "options": ["SUM()", "AVG()", "COUNT()", "MAX()"],
                "answer": "COUNT()",
                "explanation": "COUNT() returns the number of rows or non-NULL values depending on the expression."
            },
            {
                "question": "Which normal form removes partial dependencies?",
                "options": ["1NF", "2NF", "3NF", "4NF"],
                "answer": "2NF",
                "explanation": "Second Normal Form eliminates partial dependencies on a composite candidate key."
            },
            {
                "question": "Which command cancels uncommitted transaction changes?",
                "options": ["COMMIT", "ROLLBACK", "GRANT", "SELECT"],
                "answer": "ROLLBACK",
                "explanation": "ROLLBACK cancels the current uncommitted transaction."
            }
        ]
    }
})
# dsa


# DSA lesson catalog
DSA_TRACK = {}

DSA_TRACK.update({
    "dsa-time-complexity": {
        "id": "dsa-time-complexity",
        "title": "Time Complexity – Analyze Algorithm Efficiency",
        "duration": "60–75 min",

        "content": """
# 1. What is an Algorithm?

An algorithm is a finite sequence of steps used to solve a problem.

Example: Finding the largest number in an array.

Input:
[10, 25, 7, 40, 15]

Steps:
1. Assume the first element is the largest.
2. Compare it with every remaining element.
3. Update the largest value whenever a bigger element is found.
4. Return the largest value.

Output: 40

Different algorithms can solve the same problem with different amounts of time and memory.

This is why we analyze algorithm efficiency.

# 2. What is Time Complexity?

Time complexity describes how the number of operations performed by an algorithm grows as the input size increases.

Input size is commonly represented by n.

For example:
- n = 10 means 10 input elements.
- n = 100 means 100 input elements.
- n = 1000 means 1000 input elements.

Time complexity helps us understand how an algorithm scales.

Important:
Time complexity does not directly represent execution time in seconds. It describes the growth of computational work as input size increases.

# 3. What is Big O Notation?

Big O notation describes an asymptotic upper bound on an algorithm's growth rate.

It is commonly used to express worst-case time complexity.

Examples:

O(1)       Constant
O(log n)   Logarithmic
O(n)       Linear
O(n log n) Linearithmic
O(n²)      Quadratic
O(n³)      Cubic
O(2ⁿ)      Exponential
O(n!)      Factorial

For large inputs, the growth rate matters more than small constant factors.

# 4. O(1) – Constant Time

An operation takes approximately the same amount of work regardless of input size.

Example:

arr = [10, 20, 30, 40]

print(arr[2])

Accessing an array element by index takes constant time.

Python:

def get_first(arr):
    return arr[0]

Java:

static int getFirst(int[] arr) {
    return arr[0];
}

C++:

int getFirst(vector<int>& arr) {
    return arr[0];
}

Time Complexity: O(1)

# 5. O(n) – Linear Time

The amount of work grows proportionally to the input size.

Example:

def print_elements(arr):
    for value in arr:
        print(value)

If there are 5 elements, approximately 5 iterations occur.

If there are 100 elements, approximately 100 iterations occur.

Java:

static void printElements(int[] arr) {
    for (int value : arr) {
        System.out.println(value);
    }
}

C++:

void printElements(vector<int>& arr) {
    for (int value : arr) {
        cout << value << endl;
    }
}

Time Complexity: O(n)

# 6. O(n²) – Quadratic Time

A nested loop often results in quadratic complexity.

Example:

def print_pairs(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            print(arr[i], arr[j])

For n elements:
- Outer loop runs n times.
- Inner loop runs n times for each outer iteration.
- Total iterations = n × n.

Time Complexity: O(n²)

Java:

static void printPairs(int[] arr) {
    for (int i = 0; i < arr.length; i++) {
        for (int j = 0; j < arr.length; j++) {
            System.out.println(arr[i] + " " + arr[j]);
        }
    }
}

C++:

void printPairs(vector<int>& arr) {
    for (int i = 0; i < arr.size(); i++) {
        for (int j = 0; j < arr.size(); j++) {
            cout << arr[i] << " " << arr[j] << endl;
        }
    }
}

Time Complexity: O(n²)

# 7. O(log n) – Logarithmic Time

Logarithmic complexity commonly appears when the search space is repeatedly divided.

Example: Binary Search.

Suppose the sorted array is:

[10, 20, 30, 40, 50, 60, 70]

We want to find 60.

Steps:
1. Check the middle element: 40.
2. Since 60 is greater, discard the left half.
3. Check the middle of the remaining section.
4. Continue until the element is found.

The search space becomes approximately half after each iteration.

Time Complexity: O(log n)

Binary search requires sorted data and an efficient way to access the middle element.

Python:

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

Java:

static int binarySearch(int[] arr, int target) {
    int left = 0;
    int right = arr.length - 1;

    while (left <= right) {
        int mid = left + (right - left) / 2;

        if (arr[mid] == target) {
            return mid;
        } else if (arr[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }

    return -1;
}

C++:

int binarySearch(vector<int>& arr, int target) {
    int left = 0;
    int right = arr.size() - 1;

    while (left <= right) {
        int mid = left + (right - left) / 2;

        if (arr[mid] == target) {
            return mid;
        } else if (arr[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }

    return -1;
}

# 8. O(n log n) – Linearithmic Time

This complexity commonly appears in efficient sorting algorithms.

Examples:
- Merge Sort
- Heap Sort
- Average-case Quick Sort

Merge Sort divides the array into smaller parts and merges the sorted parts.

It performs approximately log n levels of division, with O(n) work at each level.

Time Complexity: O(n log n)

# 9. O(2ⁿ) – Exponential Time

Exponential complexity often appears in recursive algorithms that explore two possibilities at every step.

Example: Generating all subsets of an array.

For an array containing n elements, the number of subsets is 2ⁿ.

Python:

def generate_subsets(index, arr, current):
    if index == len(arr):
        print(current)
        return

    generate_subsets(index + 1, arr, current)

    generate_subsets(
        index + 1,
        arr,
        current + [arr[index]]
    )

For n elements, the number of subsets is 2ⁿ.

Time Complexity: O(2ⁿ), excluding the additional cost of copying or printing each subset.

# 10. O(n!) – Factorial Time

Factorial complexity can occur when generating all permutations.

For n distinct elements, there are n! possible permutations.

Example:

[1, 2, 3]

Permutations:
[1, 2, 3]
[1, 3, 2]
[2, 1, 3]
[2, 3, 1]
[3, 1, 2]
[3, 2, 1]

The number of permutations is:

3! = 3 × 2 × 1 = 6

Factorial algorithms become extremely expensive even for relatively small inputs.

# 11. Best Case, Average Case and Worst Case

Consider Linear Search.

Array:
[10, 20, 30, 40, 50]

Target: 10

Best case:
The target is at the first position.
Only one comparison is needed.
Complexity: O(1)

Average case:
The target is somewhere in the middle on average.
Complexity: O(n)

Worst case:
The target is at the last position or absent.
Complexity: O(n)

When discussing Big O in interviews, clearly mention which case you are analyzing.

# 12. Rules for Calculating Time Complexity

Rule 1: Ignore constants.

O(2n) becomes O(n).

Rule 2: Keep the dominant term.

O(n² + n + 10) becomes O(n²).

Rule 3: Sequential loops are added.

Loop 1: O(n)
Loop 2: O(n)

Total: O(n + n) = O(n).

Rule 4: Nested loops are multiplied.

Outer loop: O(n)
Inner loop: O(n)

Total: O(n²).

Rule 5: Repeatedly dividing the input often produces logarithmic complexity.

Example: n, n/2, n/4, n/8.

Total complexity: O(log n).

Rule 6: Different input sizes should use different variables.

For example, if one loop processes n elements and another processes m elements, total complexity may be O(n + m), not O(n).

# 13. Common Complexity Comparison

For n = 1000, approximate growth:

O(1)       = 1
O(log n)   ≈ 10
O(n)       = 1,000
O(n log n) ≈ 10,000
O(n²)      = 1,000,000
O(n³)      = 1,000,000,000

These are illustrative growth values, not exact execution times.

# 14. What is Space Complexity?

Space complexity describes how memory requirements grow as the input size increases.

It can include:
- Extra arrays.
- Variables and data structures.
- Recursion call stack.
- Auxiliary storage.

Auxiliary space means the extra memory used by an algorithm, excluding the input itself.

Example:

def get_sum(arr):
    total = 0

    for value in arr:
        total += value

    return total

The algorithm uses only a constant number of extra variables.

Auxiliary Space: O(1)

# 15. O(n) Space Complexity

Example:

def create_copy(arr):
    result = []

    for value in arr:
        result.append(value)

    return result

The result array grows with the input size.

Auxiliary Space: O(n)

# 16. Recursion and Space Complexity

Recursive functions use the call stack.

Example:

def countdown(n):
    if n == 0:
        return

    countdown(n - 1)

For n recursive calls:
- Each call occupies a stack frame.
- The maximum recursion depth is proportional to n.

Time Complexity: O(n)
Auxiliary Space: O(n)

# 17. Time and Space Trade-off

Sometimes an algorithm uses extra memory to improve execution time.

Example: Two Sum.

Approach 1: Brute force
- Check every pair.
- Time: O(n²).
- Auxiliary space: O(1).

Approach 2: Hash Map
- Store previously seen numbers.
- Time: O(n) average-case.
- Auxiliary space: O(n).

The hash map uses additional memory but reduces repeated searching.

# 18. Complexity of Common Data Structures

Array:
- Access by index: O(1).
- Linear search: O(n).
- Insert/delete at the beginning: O(n).

Hash Map:
- Lookup: O(1) average-case.
- Insert: O(1) average-case.
- Worst-case lookup can be O(n), depending on collisions and implementation.

Stack:
- Push: O(1).
- Pop: O(1).
- Peek: O(1).

Queue:
- Enqueue: O(1) with a suitable queue implementation.
- Dequeue: O(1) with a suitable queue implementation.

Binary Search Tree:
- Search: O(log n) average-case when reasonably balanced.
- Search: O(n) worst-case when skewed.

Heap:
- Insert: O(log n).
- Remove minimum/maximum: O(log n).
- Peek: O(1).

# 19. Interview Approach

When asked to analyze an algorithm:

1. Identify the input size.
2. Count the number of operations or loop iterations.
3. Analyze nested loops.
4. Analyze recursive calls.
5. Identify the dominant growth term.
6. Remove constants and lower-order terms.
7. Analyze auxiliary memory separately.
8. State best, average or worst case when relevant.

# 20. Key Takeaways

- Time complexity measures growth in computational work.
- Space complexity measures growth in memory requirements.
- Big O describes an asymptotic upper bound.
- O(1) is constant.
- O(log n) is logarithmic.
- O(n) is linear.
- O(n²) is quadratic.
- Binary Search is O(log n).
- Merge Sort is O(n log n).
- Hash Map lookup is O(1) on average.
- Recursion can consume stack memory.
- Optimizing an algorithm often involves balancing time and space.
""",

        "key_concepts": [
            "Algorithm analysis",
            "Input size n",
            "Big O notation",
            "Constant time O(1)",
            "Logarithmic time O(log n)",
            "Linear time O(n)",
            "Linearithmic time O(n log n)",
            "Quadratic time O(n²)",
            "Exponential time O(2ⁿ)",
            "Factorial time O(n!)",
            "Best, average and worst cases",
            "Nested loops and sequential loops",
            "Recursion complexity",
            "Space complexity",
            "Auxiliary space",
            "Time-space trade-off",
            "Data structure operation complexity"
        ],

        "examples": {
            "python": """# Example 1: O(1)
def get_first(arr):
    return arr[0]


# Example 2: O(n)
def find_max(arr):
    maximum = arr[0]

    for value in arr:
        if value > maximum:
            maximum = value

    return maximum


# Example 3: O(n^2)
def print_pairs(arr):
    for x in arr:
        for y in arr:
            print(x, y)


# Example 4: O(log n)
def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# Example 5: O(n) auxiliary space
def copy_array(arr):
    return [x for x in arr]


arr = [10, 20, 30, 40, 50]

print(get_first(arr))
print(find_max(arr))
print(binary_search(arr, 30))
print(copy_array(arr))

# Output:
# 10
# 50
# 2
# [10, 20, 30, 40, 50]""",

            "java": """public class Main {

    // O(1)
    static int getFirst(int[] arr) {
        return arr[0];
    }

    // O(n)
    static int findMax(int[] arr) {
        int maximum = arr[0];

        for (int value : arr) {
            maximum = Math.max(maximum, value);
        }

        return maximum;
    }

    // O(log n), requires sorted array
    static int binarySearch(int[] arr, int target) {
        int left = 0;
        int right = arr.length - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2;

            if (arr[mid] == target) {
                return mid;
            } else if (arr[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        return -1;
    }

    public static void main(String[] args) {
        int[] arr = {10, 20, 30, 40, 50};

        System.out.println(getFirst(arr));
        System.out.println(findMax(arr));
        System.out.println(binarySearch(arr, 30));
    }
}

// Output:
// 10
// 50
// 2""",

            "cpp": """#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// O(1)
int getFirst(vector<int>& arr) {
    return arr[0];
}

// O(n)
int findMax(vector<int>& arr) {
    int maximum = arr[0];

    for (int value : arr) {
        maximum = max(maximum, value);
    }

    return maximum;
}

// O(log n), requires sorted array
int binarySearch(vector<int>& arr, int target) {
    int left = 0;
    int right = arr.size() - 1;

    while (left <= right) {
        int mid = left + (right - left) / 2;

        if (arr[mid] == target) {
            return mid;
        } else if (arr[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }

    return -1;
}

int main() {
    vector<int> arr = {10, 20, 30, 40, 50};

    cout << getFirst(arr) << endl;
    cout << findMax(arr) << endl;
    cout << binarySearch(arr, 30) << endl;

    return 0;
}

// Output:
// 10
// 50
// 2"""
        },

        "dry_run": """Analyze the following code:

for i in range(n):
    for j in range(n):
        print(i, j)

Let n = 3.

i = 0: j = 0, 1, 2  -> 3 operations
i = 1: j = 0, 1, 2  -> 3 operations
i = 2: j = 0, 1, 2  -> 3 operations

Total operations = 3 × 3 = 9.

For general n:
Total operations = n × n = n².

Time Complexity: O(n²)
Auxiliary Space: O(1)

Now consider:

i = 1
while i < n:
    i = i * 2

Values of i:
1, 2, 4, 8, 16, ...

The value doubles in every iteration.

Time Complexity: O(log n)
Auxiliary Space: O(1)""",

        "practice_questions": [
            {
                "question": "Find the time and auxiliary space complexity of the following code. Explain your answer.",
                "solution": """def calculate_sum(arr):
    total = 0

    for i in range(len(arr)):
        total += arr[i]

    return total

Time Complexity: O(n)
Reason: The loop executes n times.

Auxiliary Space: O(1)
Reason: Only the total and loop index use extra memory."""
            },
            {
                "question": "Analyze the time complexity of this code:",
                "solution": """def example(n):
    i = 1

    while i < n:
        print(i)
        i *= 2

The values are:
1, 2, 4, 8, 16, ...

The input doubles in each iteration.

If there are k iterations:
2^k is approximately n.

Therefore:
k = log2(n)

Time Complexity: O(log n)
Auxiliary Space: O(1)"""
            },
            {
                "question": "Given an array of n elements, explain the time and space complexity difference between finding a pair using nested loops and using a hash set.",
                "solution": """Brute-force approach:

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] + arr[j] == target:
            return True

Time: O(n^2)
Auxiliary Space: O(1)

Hash-set approach:

seen = set()

for value in arr:
    if target - value in seen:
        return True

    seen.add(value)

Time: O(n) average-case
Auxiliary Space: O(n)

The hash-set approach uses extra memory to reduce
the amount of searching."""
            }
        ],

        "interview_questions": [
            {
                "question": "What is time complexity?",
                "answer": "Time complexity describes how the amount of computational work grows with the input size."
            },
            {
                "question": "What is space complexity?",
                "answer": "Space complexity describes how memory requirements grow with input size. Auxiliary space refers specifically to extra memory used by the algorithm."
            },
            {
                "question": "What is Big O notation?",
                "answer": "Big O notation expresses an asymptotic upper bound on growth and is commonly used to discuss worst-case algorithm complexity."
            },
            {
                "question": "What is the complexity of accessing an array element by index?",
                "answer": "O(1), because direct indexing takes constant time under the usual array model."
            },
            {
                "question": "What is the time complexity of Linear Search?",
                "answer": "Best case O(1), average case O(n), and worst case O(n)."
            },
            {
                "question": "What is the time complexity of Binary Search?",
                "answer": "O(log n) because the search interval is approximately halved in each iteration. The data must be sorted."
            },
            {
                "question": "What is the time complexity of two nested loops, each running n times?",
                "answer": "O(n²), because the inner loop executes n times for each of n outer iterations."
            },
            {
                "question": "What is the time complexity of Merge Sort?",
                "answer": "O(n log n) in its best, average and worst cases."
            },
            {
                "question": "What is the difference between O(n) and O(log n)?",
                "answer": "O(n) grows proportionally to input size, whereas O(log n) grows much more slowly because the problem size is repeatedly reduced by a constant factor."
            },
            {
                "question": "What is auxiliary space?",
                "answer": "Auxiliary space is the extra memory an algorithm uses, excluding the input storage itself."
            },
            {
                "question": "Why can recursion require O(n) space?",
                "answer": "A recursive algorithm may create up to n simultaneously active function calls, each using a stack frame."
            },
            {
                "question": "What is the average-case lookup complexity of a hash map?",
                "answer": "O(1) average-case lookup, although worst-case behavior can be O(n)."
            },
            {
                "question": "What is a time-space trade-off?",
                "answer": "It is a design choice in which an algorithm uses more memory to reduce computation time, or saves memory at the cost of additional computation."
            },
            {
                "question": "What is the complexity of generating all permutations of n distinct elements?",
                "answer": "There are n! permutations. Generating and outputting them requires at least O(n × n!) total work because each permutation contains n elements."
            },
            {
                "question": "What is the complexity of O(n + n²)?",
                "answer": "O(n²), because the quadratic term dominates for sufficiently large n."
            }
        ],

        "mcqs": [
            {
                "question": "What is the time complexity of accessing arr[5] in an array?",
                "options": ["O(n)", "O(log n)", "O(1)", "O(n²)"],
                "answer": "O(1)",
                "explanation": "Array index access takes constant time under the usual array model."
            },
            {
                "question": "What is the worst-case time complexity of Linear Search?",
                "options": ["O(1)", "O(log n)", "O(n)", "O(n²)"],
                "answer": "O(n)",
                "explanation": "The algorithm may examine every element."
            },
            {
                "question": "Binary Search requires which condition?",
                "options": [
                    "The array must be sorted",
                    "The array must contain duplicates",
                    "The array must contain only positive numbers",
                    "The array must have even length"
                ],
                "answer": "The array must be sorted",
                "explanation": "Binary Search uses ordering to discard half of the search space."
            },
            {
                "question": "What is the complexity of two nested loops, each running n times?",
                "options": ["O(n)", "O(log n)", "O(n²)", "O(1)"],
                "answer": "O(n²)",
                "explanation": "The total number of iterations is n multiplied by n."
            },
            {
                "question": "Which complexity grows the slowest for large n?",
                "options": ["O(n²)", "O(n)", "O(log n)", "O(2ⁿ)"],
                "answer": "O(log n)",
                "explanation": "Logarithmic growth is slower than linear, quadratic and exponential growth."
            },
            {
                "question": "What is the time complexity of Merge Sort?",
                "options": ["O(n²)", "O(n log n)", "O(log n)", "O(2ⁿ)"],
                "answer": "O(n log n)",
                "explanation": "Merge Sort performs O(n) work over O(log n) levels."
            },
            {
                "question": "What is the auxiliary space complexity of an iterative algorithm using only a fixed number of variables?",
                "options": ["O(n)", "O(n²)", "O(1)", "O(log n)"],
                "answer": "O(1)",
                "explanation": "A fixed number of extra variables requires constant auxiliary space."
            },
            {
                "question": "Which data structure commonly provides O(1) average-case lookup?",
                "options": ["Linked List", "Hash Map", "Unsorted Array", "Stack"],
                "answer": "Hash Map",
                "explanation": "Hash maps use hashing to provide average constant-time lookup."
            },
            {
                "question": "What is the time complexity of O(n² + 5n + 10)?",
                "options": ["O(n)", "O(n²)", "O(5n)", "O(1)"],
                "answer": "O(n²)",
                "explanation": "The highest-order term dominates the growth rate."
            },
            {
                "question": "Why can recursive algorithms consume additional space?",
                "options": [
                    "They always create arrays",
                    "They use the call stack",
                    "They always use a database",
                    "They cannot use variables"
                ],
                "answer": "They use the call stack",
                "explanation": "Each active recursive call occupies a stack frame."
            }
        ]
    }
})



DSA_TRACK.update({
    "dsa-space-complexity": {
        "id": "dsa-space-complexity",
        "title": "Space Complexity and Recursion Analysis",
        "description": "Understand how algorithms use memory, analyze auxiliary space, and calculate recursion stack complexity.",
        "duration": "35 min",
        "difficulty": "Beginner",

        "content": """
# 1. What is Space Complexity?

Space complexity measures how much memory an algorithm requires
as the input size increases.

It includes memory used for:
- Variables
- Arrays and other data structures
- Function calls
- Recursion call stack
- Temporary objects

If an algorithm uses more memory as the input grows, its space
complexity increases.

For example:

    int sum = 0;

This uses a fixed amount of extra memory, regardless of input size.
Its auxiliary space complexity is O(1).

# 2. Total Space vs Auxiliary Space

Total space complexity includes all memory used by an algorithm,
including the memory occupied by the input.

Auxiliary space means the extra memory used by the algorithm,
excluding the input itself.

Example:

    int findSum(int arr[], int n) {
        int sum = 0;

        for (int i = 0; i < n; i++) {
            sum += arr[i];
        }

        return sum;
    }

The input array occupies O(n) memory.
The variables sum and i use O(1) extra memory.

Therefore:
- Total space: O(n)
- Auxiliary space: O(1)

In coding interviews, always clarify whether the question asks
for total space or auxiliary space.

# 3. Common Space Complexities

O(1) – Constant Space:
The algorithm uses a fixed amount of extra memory.

O(log n) – Logarithmic Space:
The memory grows logarithmically, often because of recursion
that repeatedly divides the problem.

O(n) – Linear Space:
The algorithm creates an additional array or uses a recursion
stack proportional to input size.

O(n²) – Quadratic Space:
The algorithm stores a two-dimensional structure such as an
n × n matrix.

# 4. Understanding the Recursion Call Stack

Whenever a function calls itself, a new function call is placed
on the call stack.

Each call stores information such as:
- Parameters
- Local variables
- Return address
- Execution state

Consider:

    void countDown(int n) {
        if (n == 0) return;

        countDown(n - 1);
    }

For countDown(3), the calls are:

    countDown(3)
        countDown(2)
            countDown(1)
                countDown(0)

There are four active calls at the deepest point.

For input n, the maximum recursion depth is approximately n.

Therefore:
- Time complexity: O(n)
- Auxiliary space: O(n), because of the call stack.

# 5. Recursion with Logarithmic Space

Consider binary search:

    binarySearch(arr, low, high)

At each recursive call, the search range becomes half.

For an array of size n, the maximum recursion depth is:

    log2(n)

Therefore:
- Time complexity: O(log n)
- Auxiliary space: O(log n) for recursive binary search.

An iterative binary search uses O(1) auxiliary space because
it uses a fixed number of variables instead of recursive calls.

# 6. In-place Algorithms

An in-place algorithm modifies the input directly and uses
constant or very little extra memory.

Example: reversing an array using two pointers.

    [1, 2, 3, 4]
    [4, 2, 3, 1]
    [4, 3, 2, 1]

Only a temporary variable is needed for swapping.

Auxiliary space: O(1).

Important: In-place does not necessarily mean that absolutely
no extra memory is used. It generally means that the extra
memory requirement is constant or very small.

# 7. Space Complexity of Common Algorithms

- Iterative array traversal: O(1) auxiliary space.
- Creating a copy of an array: O(n).
- Recursive factorial: O(n) call stack.
- Recursive binary search: O(log n) call stack.
- Iterative binary search: O(1).
- Merge sort: O(n) auxiliary array space.
- Quick sort: typically O(log n) average recursion stack,
  but O(n) in the worst case.
- BFS: O(V) auxiliary space for its queue and visited structure.
- DFS: O(V) worst-case auxiliary space for its stack or recursion.

Here, V represents the number of vertices in a graph.

# 8. Merge Sort vs Quick Sort: Memory

Merge Sort:
- Divides the array into smaller parts.
- Uses temporary arrays while merging.
- Requires O(n) auxiliary array space.

Quick Sort:
- Partitions the array around a pivot.
- Usually sorts in place.
- Uses recursion stack space.
- Average stack space: O(log n).
- Worst-case stack space: O(n).

# 9. Recursion and Stack Overflow

Every recursive call consumes stack memory.

If recursion continues too deeply, the call stack may run out
of available memory. This is called stack overflow.

Common causes:
- Missing base condition.
- Incorrect recursive progress.
- Extremely deep recursion.

Always ensure:
1. A valid base condition exists.
2. Every recursive call moves toward that condition.
3. The recursion depth is reasonable.

# 10. How to Analyze Space Complexity in Interviews

Follow these steps:

1. Identify the input memory.
2. Identify additional variables.
3. Check whether new arrays, lists, maps, or matrices are created.
4. Check whether recursion is used.
5. Calculate maximum recursion depth.
6. Ignore constant factors and lower-order terms.
7. State auxiliary space separately from total space when useful.

For example, O(3n + 5) becomes O(n).
""",

        "key_concepts": [
            {
                "term": "Space Complexity",
                "definition": "The amount of memory an algorithm requires as input size grows."
            },
            {
                "term": "Auxiliary Space",
                "definition": "Extra memory used by an algorithm, excluding the input storage."
            },
            {
                "term": "Call Stack",
                "definition": "Memory area that stores active function calls and their execution information."
            },
            {
                "term": "Recursion Depth",
                "definition": "The maximum number of simultaneously active recursive calls."
            },
            {
                "term": "In-place Algorithm",
                "definition": "An algorithm that modifies input directly and uses constant or very little extra memory."
            },
            {
                "term": "Stack Overflow",
                "definition": "An error caused when function calls consume more stack memory than is available."
            }
        ],

        "examples": {
            "python": """# O(1) auxiliary space
def find_sum(arr):
    total = 0

    for number in arr:
        total += number

    return total


# O(n) auxiliary space
def create_copy(arr):
    copied = []

    for number in arr:
        copied.append(number)

    return copied


# O(n) recursion stack
def factorial(n):
    if n <= 1:
        return 1

    return n * factorial(n - 1)


# O(log n) recursion stack
def binary_search(arr, target, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid

    if target < arr[mid]:
        return binary_search(arr, target, low, mid - 1)

    return binary_search(arr, target, mid + 1, high)


numbers = [1, 3, 5, 7, 9]

print(find_sum(numbers))
print(create_copy(numbers))
print(factorial(5))
print(binary_search(numbers, 7, 0, len(numbers) - 1))""",

            "java": """import java.util.*;

public class Main {

    // O(1) auxiliary space
    static int findSum(int[] arr) {
        int total = 0;

        for (int number : arr) {
            total += number;
        }

        return total;
    }

    // O(n) auxiliary space
    static int[] createCopy(int[] arr) {
        int[] copy = new int[arr.length];

        for (int i = 0; i < arr.length; i++) {
            copy[i] = arr[i];
        }

        return copy;
    }

    // O(n) recursion stack
    static int factorial(int n) {
        if (n <= 1) return 1;

        return n * factorial(n - 1);
    }

    // O(log n) recursion stack
    static int binarySearch(int[] arr, int low, int high, int target) {
        if (low > high) return -1;

        int mid = low + (high - low) / 2;

        if (arr[mid] == target) return mid;

        if (target < arr[mid]) {
            return binarySearch(arr, low, mid - 1, target);
        }

        return binarySearch(arr, mid + 1, high, target);
    }

    public static void main(String[] args) {
        int[] numbers = {1, 3, 5, 7, 9};

        System.out.println(findSum(numbers));
        System.out.println(Arrays.toString(createCopy(numbers)));
        System.out.println(factorial(5));
        System.out.println(binarySearch(numbers, 0, 4, 7));
    }
}""",

            "cpp": """#include <iostream>
#include <vector>
using namespace std;

// O(1) auxiliary space
int findSum(vector<int>& arr) {
    int total = 0;

    for (int number : arr) {
        total += number;
    }

    return total;
}

// O(n) auxiliary space
vector<int> createCopy(vector<int>& arr) {
    vector<int> copy;

    for (int number : arr) {
        copy.push_back(number);
    }

    return copy;
}

// O(n) recursion stack
int factorial(int n) {
    if (n <= 1) return 1;

    return n * factorial(n - 1);
}

// O(log n) recursion stack
int binarySearch(vector<int>& arr, int low, int high, int target) {
    if (low > high) return -1;

    int mid = low + (high - low) / 2;

    if (arr[mid] == target) return mid;

    if (target < arr[mid]) {
        return binarySearch(arr, low, mid - 1, target);
    }

    return binarySearch(arr, mid + 1, high, target);
}

int main() {
    vector<int> numbers = {1, 3, 5, 7, 9};

    cout << findSum(numbers) << endl;

    vector<int> copy = createCopy(numbers);

    for (int x : copy) cout << x << " ";
    cout << endl;

    cout << factorial(5) << endl;
    cout << binarySearch(numbers, 0, 4, 7) << endl;

    return 0;
}"""
        },

        "dry_run": [
            {
                "title": "Tracing recursive factorial",
                "input": "factorial(4)",
                "steps": [
                    "factorial(4) calls factorial(3)",
                    "factorial(3) calls factorial(2)",
                    "factorial(2) calls factorial(1)",
                    "factorial(1) returns 1",
                    "factorial(2) returns 2",
                    "factorial(3) returns 6",
                    "factorial(4) returns 24"
                ],
                "output": "24",
                "complexity": "Time: O(n), Auxiliary space: O(n)"
            },
            {
                "title": "Tracing recursive binary search",
                "input": "Array = [1, 3, 5, 7, 9], target = 7",
                "steps": [
                    "low = 0, high = 4, mid = 2, value = 5",
                    "Target is greater than 5, search right half",
                    "low = 3, high = 4, mid = 3, value = 7",
                    "Target found at index 3"
                ],
                "output": "3",
                "complexity": "Time: O(log n), Auxiliary space: O(log n)"
            }
        ],

        "practice_questions": [
            {
                "question": "Write a function that calculates the sum of an array without creating another array. State its auxiliary space complexity.",
                "difficulty": "Easy",
                "solution": {
                    "python": """def array_sum(arr):
    total = 0

    for value in arr:
        total += value

    return total

print(array_sum([10, 20, 30, 40]))""",
                    "java": """static int arraySum(int[] arr) {
    int total = 0;

    for (int value : arr) {
        total += value;
    }

    return total;
}""",
                    "cpp": """int arraySum(vector<int>& arr) {
    int total = 0;

    for (int value : arr) {
        total += value;
    }

    return total;
}""",
                    "output": "100",
                    "explanation": "Only one additional variable is used. Auxiliary space is O(1), and time complexity is O(n)."
                }
            },
            {
                "question": "Write a recursive function to calculate the sum of numbers from 1 to n. State its space complexity.",
                "difficulty": "Easy",
                "solution": {
                    "python": """def sum_n(n):
    if n <= 0:
        return 0

    return n + sum_n(n - 1)

print(sum_n(5))""",
                    "java": """static int sumN(int n) {
    if (n <= 0) return 0;

    return n + sumN(n - 1);
}""",
                    "cpp": """int sumN(int n) {
    if (n <= 0) return 0;

    return n + sumN(n - 1);
}""",
                    "output": "15",
                    "explanation": "There are n recursive calls in the deepest call chain. Auxiliary space is O(n). Time complexity is O(n)."
                }
            },
            {
                "question": "Reverse an array in-place using two pointers. State its auxiliary space complexity.",
                "difficulty": "Medium",
                "solution": {
                    "python": """def reverse_array(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    return arr

print(reverse_array([1, 2, 3, 4, 5]))""",
                    "java": """static void reverseArray(int[] arr) {
    int left = 0;
    int right = arr.length - 1;

    while (left < right) {
        int temp = arr[left];
        arr[left] = arr[right];
        arr[right] = temp;

        left++;
        right--;
    }
}""",
                    "cpp": """void reverseArray(vector<int>& arr) {
    int left = 0;
    int right = arr.size() - 1;

    while (left < right) {
        swap(arr[left], arr[right]);
        left++;
        right--;
    }
}""",
                    "output": "[5, 4, 3, 2, 1]",
                    "explanation": "The input is modified directly. Only a fixed number of variables are used. Auxiliary space is O(1). Time complexity is O(n)."
                }
            }
        ],

        "interview_questions": [
            {
                "question": "What is space complexity?",
                "answer": "Space complexity measures the memory required by an algorithm as input size increases."
            },
            {
                "question": "What is auxiliary space?",
                "answer": "Auxiliary space is the extra memory used by an algorithm, excluding the input storage."
            },
            {
                "question": "Differentiate total space and auxiliary space.",
                "answer": "Total space includes input memory and extra memory. Auxiliary space counts only the extra memory used by the algorithm."
            },
            {
                "question": "What is a recursion call stack?",
                "answer": "It is a memory structure that stores information about active function calls, including parameters, local variables and return addresses."
            },
            {
                "question": "What is the space complexity of iterative array traversal?",
                "answer": "O(1) auxiliary space if only a fixed number of variables are used."
            },
            {
                "question": "What is the space complexity of recursive factorial?",
                "answer": "O(n), because there can be n active recursive calls."
            },
            {
                "question": "What is the space complexity of recursive binary search?",
                "answer": "O(log n), because the search range is halved at each recursive call."
            },
            {
                "question": "How does iterative binary search differ in space complexity?",
                "answer": "Iterative binary search uses O(1) auxiliary space because it uses a fixed number of variables."
            },
            {
                "question": "What is an in-place algorithm?",
                "answer": "An algorithm that modifies the input directly and uses constant or very little extra memory."
            },
            {
                "question": "Can an in-place algorithm use extra memory?",
                "answer": "Yes. It may use a few variables or a temporary value. In-place generally means constant or very little auxiliary space."
            },
            {
                "question": "What causes stack overflow?",
                "answer": "Excessive function calls can exhaust available call-stack memory. Deep or incorrectly terminating recursion can cause it."
            },
            {
                "question": "What is the auxiliary space complexity of Merge Sort?",
                "answer": "O(n) for the temporary arrays used during merging."
            },
            {
                "question": "What is the average recursion stack space of Quick Sort?",
                "answer": "Typically O(log n) with reasonably balanced partitions. It can reach O(n) in the worst case."
            },
            {
                "question": "What is the difference between iterative and recursive solutions in terms of memory?",
                "answer": "Recursive solutions use call-stack memory for active calls. Iterative solutions often use a fixed set of variables, although some iterations may use explicit data structures."
            },
            {
                "question": "Why should we consider space complexity during optimization?",
                "answer": "An algorithm that uses less memory can be more suitable for large inputs and memory-constrained environments. Sometimes time and memory must be traded off."
            }
        ],

        "mcqs": [
            {
                "question": "What does space complexity measure?",
                "options": [
                    "Execution time only",
                    "Memory requirement as input grows",
                    "Number of lines of code",
                    "Number of functions"
                ],
                "answer": "Memory requirement as input grows",
                "explanation": "Space complexity describes memory usage in relation to input size."
            },
            {
                "question": "What is auxiliary space?",
                "options": [
                    "Input memory only",
                    "Extra memory used by the algorithm",
                    "Disk storage",
                    "Program execution time"
                ],
                "answer": "Extra memory used by the algorithm",
                "explanation": "Auxiliary space excludes the memory occupied by the input."
            },
            {
                "question": "What is the auxiliary space complexity of a simple iterative sum using two variables?",
                "options": ["O(n)", "O(n²)", "O(1)", "O(log n)"],
                "answer": "O(1)",
                "explanation": "The number of extra variables remains constant."
            },
            {
                "question": "What is the auxiliary space complexity of recursive factorial?",
                "options": ["O(1)", "O(log n)", "O(n)", "O(n²)"],
                "answer": "O(n)",
                "explanation": "The recursion stack can contain n active calls."
            },
            {
                "question": "What is the recursion stack space of recursive binary search?",
                "options": ["O(n²)", "O(n)", "O(log n)", "O(1)"],
                "answer": "O(log n)",
                "explanation": "Each call halves the search range."
            },
            {
                "question": "Which algorithm generally requires O(n) auxiliary array space?",
                "options": ["Binary Search", "Merge Sort", "Linear Search", "Selection Sort"],
                "answer": "Merge Sort",
                "explanation": "Merge Sort uses temporary storage while merging."
            },
            {
                "question": "What can cause stack overflow?",
                "options": [
                    "Using a loop",
                    "Too many active recursive calls",
                    "Using an integer",
                    "Declaring a constant"
                ],
                "answer": "Too many active recursive calls",
                "explanation": "Every active function call consumes stack memory."
            },
            {
                "question": "Which approach typically uses O(1) auxiliary space for binary search?",
                "options": [
                    "Recursive binary search",
                    "Iterative binary search",
                    "Merge Sort",
                    "Recursive factorial"
                ],
                "answer": "Iterative binary search",
                "explanation": "It uses a fixed number of variables and no recursive call stack."
            },
            {
                "question": "What does an in-place algorithm generally mean?",
                "options": [
                    "It uses O(n²) memory",
                    "It uses no CPU",
                    "It uses constant or very little extra memory",
                    "It always uses recursion"
                ],
                "answer": "It uses constant or very little extra memory",
                "explanation": "In-place algorithms usually modify the input directly."
            },
            {
                "question": "What is the worst-case recursion stack space of Quick Sort?",
                "options": ["O(1)", "O(log n)", "O(n)", "O(n²)"],
                "answer": "O(n)",
                "explanation": "Highly unbalanced partitions can produce recursion depth proportional to n."
            }
        ]
    }
})


DSA_TRACK.update({
    "dsa-recursion": {
        "id": "dsa-recursion",
        "title": "Recursion Fundamentals and Backtracking Basics",
        "description": "Learn recursive problem-solving, call stacks, base cases, recursion trees, and the fundamentals of backtracking.",
        "duration": "45 min",
        "difficulty": "Beginner",

        "content": """
# 1. What is Recursion?

Recursion is a programming technique in which a function calls itself
to solve a smaller version of the same problem.

Instead of solving the entire problem at once, recursion divides it
into smaller subproblems until a stopping condition is reached.

Example:
To calculate factorial of 5:

5! = 5 × 4 × 3 × 2 × 1

We can define:

factorial(n) = n × factorial(n - 1)

# 2. Two Essential Parts of Recursion

Every correct recursive solution needs:

1. Base case:
   The condition that stops further recursive calls.

2. Recursive case:
   The part where the function calls itself with a smaller or simpler input.

Example:

def countdown(n):
    if n == 0:
        return

    print(n)
    countdown(n - 1)

The base case is n == 0.
The recursive case is countdown(n - 1).

Without a valid base case, recursion may continue indefinitely
until the call stack runs out of memory.

# 3. How Recursion Works Internally

Consider:

def print_numbers(n):
    if n == 0:
        return

    print(n)
    print_numbers(n - 1)

print_numbers(3)

Execution:

print_numbers(3)
    prints 3
    calls print_numbers(2)
        prints 2
        calls print_numbers(1)
            prints 1
            calls print_numbers(0)
                returns

Output:
3
2
1

Each function call is stored on the call stack.

When a function finishes, its call is removed from the stack.

# 4. Understanding the Call Stack

For factorial(4):

factorial(4)
    factorial(3)
        factorial(2)
            factorial(1)

The calls are made in this order:

factorial(4)
factorial(3)
factorial(2)
factorial(1)

They return in reverse order:

factorial(1) = 1
factorial(2) = 2
factorial(3) = 6
factorial(4) = 24

This behavior is called Last In, First Out (LIFO).

# 5. Types of Recursion

Direct recursion:
A function directly calls itself.

Indirect recursion:
One function calls another function, which eventually calls the first.

Tail recursion:
The recursive call is the final operation performed by the function.

Non-tail recursion:
Some operation remains after the recursive call returns.

Example of tail recursion:

def countdown(n):
    if n == 0:
        return

    print(n)
    countdown(n - 1)

Example of non-tail recursion:

def factorial(n):
    if n <= 1:
        return 1

    return n * factorial(n - 1)

Python does not automatically optimize tail recursion.

# 6. Recursion Tree

A recursion tree represents recursive calls as a tree.

Consider Fibonacci:

fib(n) = fib(n - 1) + fib(n - 2)

For fib(4):

                fib(4)
               /      \\
          fib(3)       fib(2)
          /   \\        /   \\
       fib(2) fib(1) fib(1) fib(0)

Notice that fib(2) is calculated more than once.

This repeated work makes simple recursive Fibonacci inefficient.

Its time complexity is O(2^n), approximately, and its
maximum call stack depth is O(n).

# 7. Recursion vs Iteration

Recursion:
- Uses function calls.
- Uses call-stack memory.
- Often produces shorter code for tree and divide-and-conquer problems.
- Can cause stack overflow for very deep recursion.

Iteration:
- Uses loops such as for and while.
- Often uses O(1) extra space.
- Can be more memory-efficient.
- May require more manual state management.

Choose the approach that makes the solution correct, understandable,
and efficient.

# 8. What is Backtracking?

Backtracking is a problem-solving technique that builds a solution
step by step.

If a choice leads to an invalid or unsuccessful solution,
we undo that choice and try another option.

The general process is:

1. Choose an option.
2. Explore the resulting state.
3. Check whether the state is valid.
4. Continue recursively if valid.
5. Undo the choice.
6. Try another option.

This is commonly called choose, explore, unchoose.

# 9. Backtracking Example: Generate Subsets

For array [1, 2], possible subsets are:

[]
[1]
[2]
[1, 2]

For each element, we have two choices:

- Include the element.
- Exclude the element.

This creates a decision tree.

For n elements, there are 2^n possible subsets.

Therefore:
- Time complexity: O(2^n) output combinations, ignoring copying costs.
- Auxiliary recursion space: O(n), excluding stored results.

# 10. Backtracking Example: Permutations

For [1, 2, 3], possible permutations include:

[1, 2, 3]
[1, 3, 2]
[2, 1, 3]
[2, 3, 1]
[3, 1, 2]
[3, 2, 1]

The number of permutations is n!.

Backtracking selects one unused element at a time and explores
the remaining choices.

# 11. Where Recursion and Backtracking Are Used

Recursion:
- Factorial
- Fibonacci
- Binary search
- Tree traversal
- Graph DFS
- Merge Sort
- Quick Sort

Backtracking:
- N-Queens
- Sudoku solver
- Rat in a Maze
- Subset generation
- Permutations
- Combination Sum
- Word Search

# 12. Common Interview Mistakes

- Forgetting the base case.
- Not moving toward the base case.
- Returning the wrong value.
- Confusing printing with returning.
- Not understanding the order of recursive calls.
- Forgetting that recursive calls consume stack memory.
- Not undoing a choice during backtracking.
- Recalculating the same subproblem unnecessarily.

# 13. How to Solve a Recursive Problem

Follow this checklist:

1. Identify the smaller version of the problem.
2. Define the function parameters.
3. Write the base case.
4. Write the recursive relationship.
5. Determine what each call returns.
6. Trace a small example manually.
7. Analyze time and auxiliary space.
8. Check for repeated work.
""",

        "key_concepts": [
            {
                "term": "Recursion",
                "definition": "A technique in which a function calls itself to solve smaller versions of a problem."
            },
            {
                "term": "Base Case",
                "definition": "The stopping condition that prevents further recursive calls."
            },
            {
                "term": "Recursive Case",
                "definition": "The part of a function that calls itself with a smaller or simpler input."
            },
            {
                "term": "Call Stack",
                "definition": "Memory structure that stores information about active function calls."
            },
            {
                "term": "Tail Recursion",
                "definition": "Recursion in which the recursive call is the final operation."
            },
            {
                "term": "Backtracking",
                "definition": "A technique that explores choices and reverses unsuccessful choices to explore alternatives."
            },
            {
                "term": "Recursion Tree",
                "definition": "A tree representation of recursive calls and their subproblems."
            }
        ],

        "examples": {
            "python": """# 1. Factorial
def factorial(n):
    if n <= 1:
        return 1

    return n * factorial(n - 1)


# 2. Sum of first n natural numbers
def sum_n(n):
    if n <= 0:
        return 0

    return n + sum_n(n - 1)


# 3. Fibonacci
def fibonacci(n):
    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


# 4. Generate all subsets using backtracking
def generate_subsets(arr):
    result = []
    current = []

    def backtrack(index):
        if index == len(arr):
            result.append(current.copy())
            return

        # Choose the current element
        current.append(arr[index])
        backtrack(index + 1)

        # Undo the choice
        current.pop()

        # Explore without the current element
        backtrack(index + 1)

    backtrack(0)
    return result


print(factorial(5))
print(sum_n(5))
print(fibonacci(6))
print(generate_subsets([1, 2]))""",

            "java": """import java.util.*;

public class Main {

    static int factorial(int n) {
        if (n <= 1) return 1;

        return n * factorial(n - 1);
    }

    static int sumN(int n) {
        if (n <= 0) return 0;

        return n + sumN(n - 1);
    }

    static int fibonacci(int n) {
        if (n <= 1) return n;

        return fibonacci(n - 1) + fibonacci(n - 2);
    }

    static void backtrack(
        int[] arr,
        int index,
        List<Integer> current,
        List<List<Integer>> result
    ) {
        if (index == arr.length) {
            result.add(new ArrayList<>(current));
            return;
        }

        // Include the current element
        current.add(arr[index]);
        backtrack(arr, index + 1, current, result);

        // Undo the choice
        current.remove(current.size() - 1);

        // Exclude the current element
        backtrack(arr, index + 1, current, result);
    }

    static List<List<Integer>> subsets(int[] arr) {
        List<List<Integer>> result = new ArrayList<>();

        backtrack(
            arr,
            0,
            new ArrayList<>(),
            result
        );

        return result;
    }

    public static void main(String[] args) {
        int[] arr = {1, 2};

        System.out.println(factorial(5));
        System.out.println(sumN(5));
        System.out.println(fibonacci(6));
        System.out.println(subsets(arr));
    }
}""",

            "cpp": """#include <iostream>
#include <vector>
using namespace std;

int factorial(int n) {
    if (n <= 1) return 1;

    return n * factorial(n - 1);
}

int sumN(int n) {
    if (n <= 0) return 0;

    return n + sumN(n - 1);
}

int fibonacci(int n) {
    if (n <= 1) return n;

    return fibonacci(n - 1) + fibonacci(n - 2);
}

void backtrack(
    vector<int>& arr,
    int index,
    vector<int>& current,
    vector<vector<int>>& result
) {
    if (index == arr.size()) {
        result.push_back(current);
        return;
    }

    // Include current element
    current.push_back(arr[index]);
    backtrack(arr, index + 1, current, result);

    // Undo the choice
    current.pop_back();

    // Exclude current element
    backtrack(arr, index + 1, current, result);
}

vector<vector<int>> subsets(vector<int>& arr) {
    vector<vector<int>> result;
    vector<int> current;

    backtrack(arr, 0, current, result);

    return result;
}

int main() {
    vector<int> arr = {1, 2};

    cout << factorial(5) << endl;
    cout << sumN(5) << endl;
    cout << fibonacci(6) << endl;

    vector<vector<int>> result = subsets(arr);

    for (auto& subset : result) {
        cout << "[ ";

        for (int x : subset) {
            cout << x << " ";
        }

        cout << "]" << endl;
    }

    return 0;
}"""
        },

        "dry_run": [
            {
                "title": "Factorial recursion",
                "input": "factorial(4)",
                "steps": [
                    "factorial(4) = 4 * factorial(3)",
                    "factorial(3) = 3 * factorial(2)",
                    "factorial(2) = 2 * factorial(1)",
                    "factorial(1) returns 1",
                    "factorial(2) returns 2",
                    "factorial(3) returns 6",
                    "factorial(4) returns 24"
                ],
                "output": "24",
                "complexity": "Time: O(n), Auxiliary space: O(n)"
            },
            {
                "title": "Backtracking subset generation",
                "input": "[1, 2]",
                "steps": [
                    "Start with an empty subset.",
                    "Choose 1.",
                    "Choose 2. Record [1, 2].",
                    "Undo the choice of 2. Record [1].",
                    "Undo the choice of 1.",
                    "Choose 2. Record [2].",
                    "Undo the choice of 2. Record []."
                ],
                "output": "[[1, 2], [1], [2], []]",
                "complexity": "Time: O(n * 2^n) including copying subsets; Auxiliary recursion space: O(n), excluding results."
            }
        ],

        "practice_questions": [
            {
                "question": "Write a recursive function to calculate the factorial of a number.",
                "difficulty": "Easy",
                "solution": {
                    "python": """def factorial(n):
    if n < 0:
        raise ValueError("Negative input")

    if n <= 1:
        return 1

    return n * factorial(n - 1)

print(factorial(5))""",
                    "java": """static int factorial(int n) {
    if (n < 0) throw new IllegalArgumentException();

    if (n <= 1) return 1;

    return n * factorial(n - 1);
}""",
                    "cpp": """int factorial(int n) {
    if (n < 0) return -1;

    if (n <= 1) return 1;

    return n * factorial(n - 1);
}""",
                    "output": "120",
                    "explanation": "The base case returns 1. Each recursive call multiplies n by factorial(n-1). Time and auxiliary space are O(n)."
                }
            },
            {
                "question": "Write a recursive function to reverse a string.",
                "difficulty": "Medium",
                "solution": {
                    "python": """def reverse_string(s):
    if len(s) <= 1:
        return s

    return reverse_string(s[1:]) + s[0]

print(reverse_string("code"))""",
                    "java": """static String reverseString(String s) {
    if (s.length() <= 1) return s;

    return reverseString(s.substring(1)) + s.charAt(0);
}""",
                    "cpp": """string reverseString(string s) {
    if (s.length() <= 1) return s;

    return reverseString(s.substr(1)) + s[0];
}""",
                    "output": "edoc",
                    "explanation": "Each call processes a smaller string. The simple slicing/substrings version can create additional string copies, so its total time and memory may exceed the O(n) call-stack estimate."
                }
            },
            {
                "question": "Generate all subsets of an array using backtracking.",
                "difficulty": "Medium",
                "solution": {
                    "python": """def subsets(arr):
    result = []
    current = []

    def backtrack(index):
        if index == len(arr):
            result.append(current.copy())
            return

        current.append(arr[index])
        backtrack(index + 1)

        current.pop()
        backtrack(index + 1)

    backtrack(0)
    return result

print(subsets([1, 2]))""",
                    "java": """static void solve(
    int[] arr, int index,
    List<Integer> current,
    List<List<Integer>> result
) {
    if (index == arr.length) {
        result.add(new ArrayList<>(current));
        return;
    }

    current.add(arr[index]);
    solve(arr, index + 1, current, result);

    current.remove(current.size() - 1);
    solve(arr, index + 1, current, result);
}""",
                    "cpp": """void solve(
    vector<int>& arr, int index,
    vector<int>& current,
    vector<vector<int>>& result
) {
    if (index == arr.size()) {
        result.push_back(current);
        return;
    }

    current.push_back(arr[index]);
    solve(arr, index + 1, current, result);

    current.pop_back();
    solve(arr, index + 1, current, result);
}""",
                    "output": "[[1, 2], [1], [2], []]",
                    "explanation": "Each element creates two choices: include or exclude. There are 2^n subsets. Copying each subset requires up to O(n) work, giving O(n * 2^n) total time."
                }
            }
        ],

        "interview_questions": [
            {
                "question": "What is recursion?",
                "answer": "Recursion is a technique in which a function calls itself to solve smaller instances of a problem."
            },
            {
                "question": "What are the two essential parts of recursion?",
                "answer": "A base case that stops recursion and a recursive case that makes progress toward the base case."
            },
            {
                "question": "What happens if a recursive function has no base case?",
                "answer": "It may continue calling itself until the call stack runs out of memory, causing stack overflow."
            },
            {
                "question": "What is a call stack?",
                "answer": "It stores information about active function calls and follows Last In, First Out behavior."
            },
            {
                "question": "What is the difference between direct and indirect recursion?",
                "answer": "Direct recursion occurs when a function calls itself. Indirect recursion occurs when functions call one another in a cycle."
            },
            {
                "question": "What is tail recursion?",
                "answer": "A recursive function is tail recursive when its recursive call is the final operation."
            },
            {
                "question": "Does Python optimize tail recursion automatically?",
                "answer": "No. Python does not provide automatic tail-call optimization."
            },
            {
                "question": "What is a recursion tree?",
                "answer": "A tree that shows how a recursive problem divides into smaller recursive calls."
            },
            {
                "question": "What is the time complexity of recursive Fibonacci without memoization?",
                "answer": "O(2^n) as a common upper-bound analysis; the same subproblems are recalculated repeatedly."
            },
            {
                "question": "What is backtracking?",
                "answer": "A technique that explores possible choices and reverses a choice when that path cannot produce a valid solution."
            },
            {
                "question": "Explain choose, explore, unchoose.",
                "answer": "Choose an option, recursively explore the resulting state, then undo the choice to try another option."
            },
            {
                "question": "What is the difference between recursion and backtracking?",
                "answer": "Recursion is a function-calling technique. Backtracking is an algorithmic strategy that often uses recursion to explore choices."
            },
            {
                "question": "How many subsets can an array of n elements have?",
                "answer": "2^n, because each element has two choices: include or exclude."
            },
            {
                "question": "What is the time complexity of generating all permutations of n distinct elements?",
                "answer": "There are n! permutations. If each permutation is copied or output, total work is O(n * n!)."
            },
            {
                "question": "Name some common backtracking problems.",
                "answer": "N-Queens, Sudoku Solver, Rat in a Maze, Subsets, Permutations, Combination Sum, and Word Search."
            }
        ],

        "mcqs": [
            {
                "question": "Which condition stops recursive calls?",
                "options": ["Loop", "Base case", "Class", "Import"],
                "answer": "Base case",
                "explanation": "The base case terminates the recursive process."
            },
            {
                "question": "Which data structure manages recursive function calls?",
                "options": ["Queue", "Heap", "Stack", "Graph"],
                "answer": "Stack",
                "explanation": "Function calls are stored on the call stack."
            },
            {
                "question": "What does LIFO mean?",
                "options": [
                    "Last In First Out",
                    "Last In Final Output",
                    "Least Input First Output",
                    "Linear Input First Output"
                ],
                "answer": "Last In First Out",
                "explanation": "The most recently added function call returns first."
            },
            {
                "question": "What is the time complexity of recursive factorial?",
                "options": ["O(1)", "O(log n)", "O(n)", "O(n²)"],
                "answer": "O(n)",
                "explanation": "There are n recursive calls."
            },
            {
                "question": "What is the maximum recursion stack space of factorial(n)?",
                "options": ["O(1)", "O(log n)", "O(n)", "O(n²)"],
                "answer": "O(n)",
                "explanation": "The deepest call chain contains O(n) calls."
            },
            {
                "question": "Which technique explores a choice and then undoes it?",
                "options": ["Sorting", "Backtracking", "Hashing", "Binary Search"],
                "answer": "Backtracking",
                "explanation": "Backtracking explores alternatives by undoing previous choices."
            },
            {
                "question": "How many subsets can be generated from 4 distinct elements?",
                "options": ["4", "8", "12", "16"],
                "answer": "16",
                "explanation": "There are 2^4 = 16 subsets."
            },
            {
                "question": "What is the main problem with naive recursive Fibonacci?",
                "options": [
                    "It cannot return integers",
                    "It repeats calculations",
                    "It never uses recursion",
                    "It always uses O(1) time"
                ],
                "answer": "It repeats calculations",
                "explanation": "The same Fibonacci subproblems are evaluated multiple times."
            },
            {
                "question": "Which is a classic backtracking problem?",
                "options": ["Binary Search", "N-Queens", "Linear Search", "Bubble Sort"],
                "answer": "N-Queens",
                "explanation": "N-Queens explores queen placements and backtracks when constraints are violated."
            },
            {
                "question": "What is the purpose of current.pop() in subset backtracking?",
                "options": [
                    "Sort the subset",
                    "Undo the previous choice",
                    "End the program",
                    "Create a new array"
                ],
                "answer": "Undo the previous choice",
                "explanation": "It restores the previous state before exploring another branch."
            }
        ]
    }
})


DSA_TRACK.update({
    "dsa-array-basics": {
        "id": "dsa-array-basics",
        "title": "Arrays and Array Manipulation",
        "description": "Learn array fundamentals, traversal, insertion, deletion, searching, reversing, rotation, and common interview patterns.",
        "duration": "45 min",
        "difficulty": "Beginner",

        "content": """
# 1. What is an Array?

An array is a data structure that stores multiple elements
of the same type in a sequence.

Each element is accessed using an index.

Example:

    arr = [10, 20, 30, 40, 50]

Indexes:

    Value:  10  20  30  40  50
    Index:   0   1   2   3   4

Most programming languages use zero-based indexing.

Accessing arr[2] returns 30.

# 2. Array Characteristics

- Elements are stored in an ordered sequence.
- Elements can be accessed using indexes.
- Array traversal takes O(n) time.
- Accessing an element by index takes O(1) time.
- Inserting or deleting in the middle generally requires shifting elements.
- Fixed-size arrays have a predefined capacity.
- Dynamic arrays can grow when required.

Python lists and Java ArrayLists are dynamic-array-like structures.
C++ vector is also a dynamic array.

# 3. Array Operations and Complexity

Access by index: O(1)

Traversal: O(n)

Searching in an unsorted array: O(n)

Binary search in a sorted array: O(log n)

Updating by index: O(1)

Insertion at the end of a dynamic array: O(1) amortized

Insertion at the beginning or middle: O(n)

Deletion at the beginning or middle: O(n)

The shifting of elements is the reason insertion and deletion
at arbitrary positions can take linear time.

# 4. Array Traversal

Traversal means visiting every element of an array.

Example:

    arr = [10, 20, 30]

    for value in arr:
        print(value)

Output:

    10
    20
    30

Time complexity: O(n)
Auxiliary space: O(1)

# 5. Finding Maximum and Minimum

We can find the largest and smallest elements by traversing
the array once.

Example:

    arr = [12, 5, 30, 8]

    maximum = 30
    minimum = 5

Time complexity: O(n)
Auxiliary space: O(1)

# 6. Reversing an Array

Two-pointer technique:

- Start one pointer at index 0.
- Start another pointer at the last index.
- Swap the elements.
- Move the left pointer forward.
- Move the right pointer backward.
- Stop when left is no longer smaller than right.

Example:

    [1, 2, 3, 4, 5]
    [5, 2, 3, 4, 1]
    [5, 4, 3, 2, 1]

Time complexity: O(n)
Auxiliary space: O(1)

# 7. Array Rotation

Left rotation by one position:

    [1, 2, 3, 4, 5]
    [2, 3, 4, 5, 1]

Right rotation by one position:

    [1, 2, 3, 4, 5]
    [5, 1, 2, 3, 4]

For rotation by k positions, first reduce k:

    k = k % n

This handles cases where k is larger than the array length.

An efficient approach is the reversal algorithm.

For left rotation by k:
1. Reverse the first k elements.
2. Reverse the remaining elements.
3. Reverse the entire array.

Time complexity: O(n)
Auxiliary space: O(1) when reversing in place.

# 8. Removing Duplicates from a Sorted Array

A sorted array can be processed using two pointers.

One pointer tracks the position of the last unique element.
The other scans the array.

When a new unique value is found, move the unique pointer
and overwrite the next position.

Time complexity: O(n)
Auxiliary space: O(1)

# 9. Second Largest Element

Maintain two variables:
- largest
- second_largest

Traverse the array and update these values carefully.

Do not simply sort the array if the question expects an
efficient one-pass solution.

Time complexity: O(n)
Auxiliary space: O(1)

# 10. Prefix Sum Preview

A prefix sum stores cumulative sums.

For:

    [2, 4, 6, 8]

Prefix sum:

    [2, 6, 12, 20]

It can answer range-sum queries efficiently after preprocessing.
We will study this as a separate lesson.

# 11. Common Array Interview Problems

- Two Sum
- Maximum Subarray
- Best Time to Buy and Sell Stock
- Move Zeroes
- Contains Duplicate
- Remove Duplicates from Sorted Array
- Rotate Array
- Merge Sorted Arrays
- Product of Array Except Self
- Find the Missing Number

# 12. How to Approach Array Problems

1. Understand the input and expected output.
2. Check whether the array is sorted.
3. Consider edge cases: empty array, one element, duplicates.
4. Think about a brute-force solution first.
5. Optimize using two pointers, hashing, or prefix sums.
6. Analyze time and auxiliary space complexity.
7. Test the solution on a small example.
""",

        "key_concepts": [
            {
                "term": "Array",
                "definition": "An ordered collection of elements accessed using indexes."
            },
            {
                "term": "Index",
                "definition": "The position of an element in an array, commonly starting at zero."
            },
            {
                "term": "Traversal",
                "definition": "Visiting array elements one by one."
            },
            {
                "term": "Two Pointers",
                "definition": "Using two indexes to process an array efficiently."
            },
            {
                "term": "In-place Operation",
                "definition": "Modifying the original array without creating a proportional-size extra array."
            },
            {
                "term": "Rotation",
                "definition": "Moving elements circularly to the left or right."
            },
            {
                "term": "Prefix Sum",
                "definition": "An array storing cumulative sums of elements."
            }
        ],

        "examples": {
            "python": """# 1. Traverse an array
arr = [10, 20, 30, 40]

for value in arr:
    print(value)


# 2. Find maximum and minimum
def find_max_min(arr):
    maximum = arr[0]
    minimum = arr[0]

    for value in arr:
        maximum = max(maximum, value)
        minimum = min(minimum, value)

    return maximum, minimum


# 3. Reverse an array in-place
def reverse_array(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    return arr


# 4. Left rotate by k positions
def left_rotate(arr, k):
    n = len(arr)

    if n == 0:
        return arr

    k %= n

    return arr[k:] + arr[:k]


# 5. Find second largest distinct element
def second_largest(arr):
    largest = None
    second = None

    for value in arr:
        if largest is None or value > largest:
            second = largest
            largest = value
        elif value != largest and (second is None or value > second):
            second = value

    return second


# 6. Move zeroes to the end
def move_zeroes(arr):
    position = 0

    for value in arr:
        if value != 0:
            arr[position] = value
            position += 1

    while position < len(arr):
        arr[position] = 0
        position += 1

    return arr


print(find_max_min([12, 5, 30, 8]))
print(reverse_array([1, 2, 3, 4, 5]))
print(left_rotate([1, 2, 3, 4, 5], 2))
print(second_largest([10, 5, 20, 8, 20]))
print(move_zeroes([0, 1, 0, 3, 12]))""",

            "java": """import java.util.*;

public class Main {

    static int[] findMaxMin(int[] arr) {
        int maximum = arr[0];
        int minimum = arr[0];

        for (int value : arr) {
            maximum = Math.max(maximum, value);
            minimum = Math.min(minimum, value);
        }

        return new int[]{maximum, minimum};
    }

    static void reverseArray(int[] arr) {
        int left = 0;
        int right = arr.length - 1;

        while (left < right) {
            int temp = arr[left];
            arr[left] = arr[right];
            arr[right] = temp;

            left++;
            right--;
        }
    }

    static void leftRotate(int[] arr, int k) {
        int n = arr.length;

        if (n == 0) return;

        k %= n;

        reverse(arr, 0, k - 1);
        reverse(arr, k, n - 1);
        reverse(arr, 0, n - 1);
    }

    static void reverse(int[] arr, int left, int right) {
        while (left < right) {
            int temp = arr[left];
            arr[left] = arr[right];
            arr[right] = temp;

            left++;
            right--;
        }
    }

    static Integer secondLargest(int[] arr) {
        Integer largest = null;
        Integer second = null;

        for (int value : arr) {
            if (largest == null || value > largest) {
                second = largest;
                largest = value;
            } else if (value != largest &&
                       (second == null || value > second)) {
                second = value;
            }
        }

        return second;
    }

    static void moveZeroes(int[] arr) {
        int position = 0;

        for (int value : arr) {
            if (value != 0) {
                arr[position++] = value;
            }
        }

        while (position < arr.length) {
            arr[position++] = 0;
        }
    }

    public static void main(String[] args) {
        int[] arr = {12, 5, 30, 8};

        System.out.println(Arrays.toString(findMaxMin(arr)));

        int[] reversed = {1, 2, 3, 4, 5};
        reverseArray(reversed);
        System.out.println(Arrays.toString(reversed));

        int[] rotated = {1, 2, 3, 4, 5};
        leftRotate(rotated, 2);
        System.out.println(Arrays.toString(rotated));

        System.out.println(secondLargest(
            new int[]{10, 5, 20, 8, 20}
        ));

        int[] zeroes = {0, 1, 0, 3, 12};
        moveZeroes(zeroes);
        System.out.println(Arrays.toString(zeroes));
    }
}""",

            "cpp": """#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

pair<int, int> findMaxMin(vector<int>& arr) {
    int maximum = arr[0];
    int minimum = arr[0];

    for (int value : arr) {
        maximum = max(maximum, value);
        minimum = min(minimum, value);
    }

    return {maximum, minimum};
}

void reverseArray(vector<int>& arr) {
    int left = 0;
    int right = arr.size() - 1;

    while (left < right) {
        swap(arr[left], arr[right]);
        left++;
        right--;
    }
}

void leftRotate(vector<int>& arr, int k) {
    int n = arr.size();

    if (n == 0) return;

    k %= n;

    reverse(arr.begin(), arr.begin() + k);
    reverse(arr.begin() + k, arr.end());
    reverse(arr.begin(), arr.end());
}

int secondLargest(vector<int>& arr) {
    int largest = 0, second = 0;
    bool hasLargest = false, hasSecond = false;

    for (int value : arr) {
        if (!hasLargest || value > largest) {
            if (hasLargest) {
                second = largest;
                hasSecond = true;
            }

            largest = value;
            hasLargest = true;
        } else if (value != largest &&
                   (!hasSecond || value > second)) {
            second = value;
            hasSecond = true;
        }
    }

    return hasSecond ? second : -1;
}

void moveZeroes(vector<int>& arr) {
    int position = 0;

    for (int value : arr) {
        if (value != 0) {
            arr[position++] = value;
        }
    }

    while (position < arr.size()) {
        arr[position++] = 0;
    }
}

int main() {
    vector<int> arr = {12, 5, 30, 8};

    auto result = findMaxMin(arr);
    cout << result.first << " " << result.second << endl;

    vector<int> reversed = {1, 2, 3, 4, 5};
    reverseArray(reversed);

    for (int x : reversed) cout << x << " ";
    cout << endl;

    vector<int> rotated = {1, 2, 3, 4, 5};
    leftRotate(rotated, 2);

    for (int x : rotated) cout << x << " ";
    cout << endl;

    vector<int> values = {10, 5, 20, 8, 20};
    cout << secondLargest(values) << endl;

    vector<int> zeroes = {0, 1, 0, 3, 12};
    moveZeroes(zeroes);

    for (int x : zeroes) cout << x << " ";

    return 0;
}"""
        },

        "dry_run": [
            {
                "title": "Reverse an array using two pointers",
                "input": "[1, 2, 3, 4, 5]",
                "steps": [
                    "left = 0, right = 4; swap 1 and 5",
                    "Array becomes [5, 2, 3, 4, 1]",
                    "left = 1, right = 3; swap 2 and 4",
                    "Array becomes [5, 4, 3, 2, 1]",
                    "Pointers meet or cross; stop"
                ],
                "output": "[5, 4, 3, 2, 1]",
                "complexity": "Time: O(n), Auxiliary space: O(1)"
            },
            {
                "title": "Find second largest distinct element",
                "input": "[10, 5, 20, 8, 20]",
                "steps": [
                    "Read 10: largest = 10",
                    "Read 5: second largest = 5",
                    "Read 20: largest = 20, second largest = 10",
                    "Read 8: no change",
                    "Read 20: duplicate largest, ignore"
                ],
                "output": "10",
                "complexity": "Time: O(n), Auxiliary space: O(1)"
            },
            {
                "title": "Move zeroes to the end",
                "input": "[0, 1, 0, 3, 12]",
                "steps": [
                    "Read 0: skip",
                    "Read 1: place at index 0",
                    "Read 0: skip",
                    "Read 3: place at index 1",
                    "Read 12: place at index 2",
                    "Fill remaining positions with zero"
                ],
                "output": "[1, 3, 12, 0, 0]",
                "complexity": "Time: O(n), Auxiliary space: O(1)"
            }
        ],

        "practice_questions": [
            {
                "question": "Find the largest and smallest elements in an array in one traversal.",
                "difficulty": "Easy",
                "solution": {
                    "python": """def find_max_min(arr):
    if not arr:
        return None

    maximum = minimum = arr[0]

    for value in arr:
        maximum = max(maximum, value)
        minimum = min(minimum, value)

    return maximum, minimum

print(find_max_min([12, 5, 30, 8]))""",
                    "java": """static int[] findMaxMin(int[] arr) {
    if (arr.length == 0) return new int[0];

    int maximum = arr[0];
    int minimum = arr[0];

    for (int value : arr) {
        maximum = Math.max(maximum, value);
        minimum = Math.min(minimum, value);
    }

    return new int[]{maximum, minimum};
}""",
                    "cpp": """pair<int, int> findMaxMin(vector<int>& arr) {
    int maximum = arr[0];
    int minimum = arr[0];

    for (int value : arr) {
        maximum = max(maximum, value);
        minimum = min(minimum, value);
    }

    return {maximum, minimum};
}""",
                    "output": "(30, 5)",
                    "explanation": "One traversal checks every element. Time complexity is O(n), and auxiliary space is O(1)."
                }
            },
            {
                "question": "Rotate an array to the left by k positions using the reversal algorithm.",
                "difficulty": "Medium",
                "solution": {
                    "python": """def rotate_left(arr, k):
    n = len(arr)

    if n == 0:
        return arr

    k %= n
    return arr[k:] + arr[:k]

print(rotate_left([1, 2, 3, 4, 5], 2))""",
                    "java": """static void rotateLeft(int[] arr, int k) {
    int n = arr.length;
    if (n == 0) return;

    k %= n;

    reverse(arr, 0, k - 1);
    reverse(arr, k, n - 1);
    reverse(arr, 0, n - 1);
}

static void reverse(int[] arr, int left, int right) {
    while (left < right) {
        int temp = arr[left];
        arr[left] = arr[right];
        arr[right] = temp;
        left++;
        right--;
    }
}""",
                    "cpp": """void rotateLeft(vector<int>& arr, int k) {
    int n = arr.size();
    if (n == 0) return;

    k %= n;

    reverse(arr.begin(), arr.begin() + k);
    reverse(arr.begin() + k, arr.end());
    reverse(arr.begin(), arr.end());
}""",
                    "output": "[3, 4, 5, 1, 2]",
                    "explanation": "The Python slicing version creates a new list and uses O(n) auxiliary space. The Java and C++ reversal implementations modify the original array in O(1) auxiliary space. All take O(n) time."
                }
            },
            {
                "question": "Move all zeroes to the end while maintaining the order of non-zero elements.",
                "difficulty": "Easy",
                "solution": {
                    "python": """def move_zeroes(arr):
    position = 0

    for value in arr:
        if value != 0:
            arr[position] = value
            position += 1

    while position < len(arr):
        arr[position] = 0
        position += 1

    return arr

print(move_zeroes([0, 1, 0, 3, 12]))""",
                    "java": """static void moveZeroes(int[] arr) {
    int position = 0;

    for (int value : arr) {
        if (value != 0) {
            arr[position++] = value;
        }
    }

    while (position < arr.length) {
        arr[position++] = 0;
    }
}""",
                    "cpp": """void moveZeroes(vector<int>& arr) {
    int position = 0;

    for (int value : arr) {
        if (value != 0) {
            arr[position++] = value;
        }
    }

    while (position < arr.size()) {
        arr[position++] = 0;
    }
}""",
                    "output": "[1, 3, 12, 0, 0]",
                    "explanation": "The write pointer places non-zero values in order, then fills the remaining positions with zeroes. Time O(n), auxiliary space O(1)."
                }
            }
        ],

        "interview_questions": [
            {
                "question": "What is an array?",
                "answer": "An array is an ordered collection of elements accessed using indexes."
            },
            {
                "question": "Why does array indexing take O(1) time?",
                "answer": "The address of an element can be calculated directly using its index and the element size."
            },
            {
                "question": "What is the time complexity of traversing an array?",
                "answer": "O(n), because every element is visited once."
            },
            {
                "question": "What is the time complexity of searching an unsorted array?",
                "answer": "O(n) in the worst case using linear search."
            },
            {
                "question": "What is the time complexity of binary search on a sorted array?",
                "answer": "O(log n)."
            },
            {
                "question": "Why can insertion in the middle of an array take O(n)?",
                "answer": "Elements after the insertion position may need to be shifted."
            },
            {
                "question": "What is a dynamic array?",
                "answer": "A resizable array that can allocate a larger storage area when its current capacity is insufficient."
            },
            {
                "question": "What is the difference between an array and a linked list?",
                "answer": "Arrays provide O(1) indexed access, while linked lists require traversal for indexed access. Linked-list insertion can be efficient when the relevant node is already known."
            },
            {
                "question": "How can an array be reversed in O(1) auxiliary space?",
                "answer": "Use two pointers at opposite ends and swap elements while moving inward."
            },
            {
                "question": "How do you rotate an array efficiently?",
                "answer": "The reversal algorithm rotates an array in O(n) time and O(1) auxiliary space."
            },
            {
                "question": "How do you find the second largest distinct element in one traversal?",
                "answer": "Maintain largest and second-largest values, updating them as each element is processed."
            },
            {
                "question": "How can you move zeroes to the end of an array?",
                "answer": "Use a write pointer to compact non-zero values, then fill the remaining positions with zeroes."
            },
            {
                "question": "What is a prefix sum array?",
                "answer": "An array containing cumulative sums, where each position stores the sum of elements up to that position."
            },
            {
                "question": "What is the difference between static and dynamic arrays?",
                "answer": "A static array has a fixed size, while a dynamic array can resize when necessary."
            },
            {
                "question": "Name common array interview problems.",
                "answer": "Two Sum, Maximum Subarray, Move Zeroes, Rotate Array, Best Time to Buy and Sell Stock, and Product of Array Except Self."
            }
        ],

        "mcqs": [
            {
                "question": "What is the time complexity of accessing arr[5]?",
                "options": ["O(n)", "O(log n)", "O(1)", "O(n²)"],
                "answer": "O(1)",
                "explanation": "Array indexing provides direct access."
            },
            {
                "question": "What is the worst-case time complexity of linear search?",
                "options": ["O(1)", "O(log n)", "O(n)", "O(n²)"],
                "answer": "O(n)",
                "explanation": "The target may be at the last position or absent."
            },
            {
                "question": "Binary search requires which condition?",
                "options": [
                    "Array must be sorted",
                    "Array must contain duplicates",
                    "Array must have even length",
                    "Array must contain only positive values"
                ],
                "answer": "Array must be sorted",
                "explanation": "Binary search relies on sorted order to eliminate half the search space."
            },
            {
                "question": "What is the auxiliary space of reversing an array using two pointers?",
                "options": ["O(n)", "O(n²)", "O(log n)", "O(1)"],
                "answer": "O(1)",
                "explanation": "Only a fixed number of variables are used."
            },
            {
                "question": "What is the time complexity of traversing an array of n elements?",
                "options": ["O(1)", "O(log n)", "O(n)", "O(n²)"],
                "answer": "O(n)",
                "explanation": "Every element is visited once."
            },
            {
                "question": "What is the time complexity of inserting an element at the beginning of an array with n elements?",
                "options": ["O(1)", "O(log n)", "O(n)", "O(n²)"],
                "answer": "O(n)",
                "explanation": "Existing elements generally need to be shifted."
            },
            {
                "question": "What does k %= n achieve during array rotation?",
                "options": [
                    "Sorts the array",
                    "Reduces rotations to the equivalent range",
                    "Deletes duplicate elements",
                    "Reverses the array"
                ],
                "answer": "Reduces rotations to the equivalent range",
                "explanation": "Rotating by n positions returns the array to its original arrangement."
            },
            {
                "question": "Which technique is useful for reversing an array in place?",
                "options": ["Binary Search", "Two Pointers", "Hashing", "DFS"],
                "answer": "Two Pointers",
                "explanation": "Two pointers swap elements from opposite ends."
            },
            {
                "question": "What is the prefix sum of [2, 4, 6]?",
                "options": [
                    "[2, 4, 6]",
                    "[2, 6, 12]",
                    "[12, 6, 2]",
                    "[4, 10, 16]"
                ],
                "answer": "[2, 6, 12]",
                "explanation": "Each prefix position stores the cumulative sum up to that index."
            },
            {
                "question": "Which data structure is a dynamic-array-like collection in Java?",
                "options": ["HashMap", "ArrayList", "TreeSet", "Queue"],
                "answer": "ArrayList",
                "explanation": "ArrayList supports a resizable array-backed collection."
            }
        ]
    }
})


DSA_TRACK.update({
    "dsa-prefix-sum": {
        "id": "dsa-prefix-sum",
        "title": "Prefix Sum Technique",
        "description": "Learn cumulative sums, range-sum queries, prefix sum with hashing, and subarray sum problems.",
        "duration": "40 min",
        "difficulty": "Beginner",

        "content": """
# 1. What is Prefix Sum?

Prefix Sum is a technique that stores the cumulative sum of
array elements.

For an array:

    arr = [2, 4, 6, 8, 10]

Its prefix sum array is:

    prefix = [2, 6, 12, 20, 30]

Each position stores the sum of all elements from index 0
to that position.

Formula:

    prefix[i] = prefix[i - 1] + arr[i]

For the first element:

    prefix[0] = arr[0]

# 2. Why Do We Use Prefix Sum?

Suppose we have an array and need to answer many questions
about the sum of elements between two indexes.

Without prefix sums, we may traverse the range every time.

If there are q queries and each query takes O(n), the total
time can be O(n * q).

With prefix sums:
- Preprocessing takes O(n).
- Each range-sum query takes O(1).

This is especially useful when the array does not change
between queries.

# 3. Range Sum Query

Suppose:

    arr = [2, 4, 6, 8, 10]
    prefix = [2, 6, 12, 20, 30]

Find the sum from index 1 to index 3.

The answer is:

    prefix[3] - prefix[0]

    20 - 2 = 18

General formula for an inclusive range [L, R]:

    if L == 0:
        sum = prefix[R]
    else:
        sum = prefix[R] - prefix[L - 1]

# 4. Prefix Sum with a Leading Zero

A useful alternative is to create a prefix array of size n + 1.

For:

    arr = [2, 4, 6, 8]

Create:

    prefix = [0, 2, 6, 12, 20]

Now the sum of elements from L to R, inclusive, is:

    prefix[R + 1] - prefix[L]

This formula works even when L is zero.

# 5. Prefix Sum of Negative Numbers

Prefix sums also work with negative values.

Example:

    arr = [3, -2, 5, -1]

    prefix = [3, 1, 6, 5]

The sum from index 1 to index 3:

    prefix[3] - prefix[0]
    = 5 - 3
    = 2

Negative values do not change the formula.

# 6. Two-Dimensional Prefix Sum

Prefix sums can also be used for matrices.

A 2D prefix sum stores the sum of all matrix elements
inside the rectangle from the top-left corner to a given cell.

For a matrix, the formula is:

    prefix[i][j] =
        matrix[i][j]
        + prefix[i - 1][j]
        + prefix[i][j - 1]
        - prefix[i - 1][j - 1]

The overlapping top-left region is subtracted once
because it was counted twice.

2D prefix sums are useful for rectangular region-sum queries.

# 7. Prefix Sum with Hashing

Prefix sum can be combined with a HashMap to solve
subarray problems.

Important problem:

Find the number of subarrays whose sum equals k.

Let current prefix sum be S.

We need an earlier prefix sum equal to:

    S - k

If that prefix sum exists, the difference between the two
prefix sums is k.

Algorithm:
1. Start prefix sum at 0.
2. Store the frequency of prefix sum 0 as 1.
3. Traverse the array.
4. Add the current value to prefix sum.
5. Add frequency[prefix_sum - k] to the answer.
6. Increase frequency[prefix_sum].

Average time complexity: O(n).
Auxiliary space: O(n).

This technique also works when the array contains negative values.

# 8. Difference Array: A Related Technique

A difference array is useful when we need to perform many
range increment operations.

For example, adding 5 to every element from index 1 to 3:

    diff[L] += 5
    diff[R + 1] -= 5

After all updates, calculate the prefix sum of the difference
array to recover the final values.

Difference arrays are useful for range updates.

# 9. Complexity Analysis

Building a one-dimensional prefix array:
- Time: O(n)
- Auxiliary space: O(n)

Range-sum query:
- Time: O(1)
- Additional query space: O(1)

Counting subarrays with sum k using a hash map:
- Average time: O(n)
- Auxiliary space: O(n)

Building a 2D prefix sum:
- Time: O(rows * columns)
- Auxiliary space: O(rows * columns)

# 10. Common Prefix Sum Interview Problems

- Range Sum Query
- Find Pivot Index
- Subarray Sum Equals K
- Product of Array Except Self (related prefix/suffix idea)
- Continuous Subarray Sum
- Maximum Size Subarray Sum Equals K
- Count Subarrays with Given Sum
- 2D Matrix Range Sum Query

# 11. When Should You Use Prefix Sum?

Use prefix sums when:
- You need many range-sum queries.
- You need cumulative totals.
- You need to count subarrays with a target sum.
- You need efficient matrix region-sum queries.
- You need to process range updates using difference arrays.

Important:
Prefix sums are most useful when the input is not changing
between queries. If elements are frequently updated, data
structures such as Fenwick Trees or Segment Trees may be better.
""",

        "key_concepts": [
            {
                "term": "Prefix Sum",
                "definition": "An array storing cumulative sums from the beginning of the original array."
            },
            {
                "term": "Range Sum Query",
                "definition": "Finding the sum of elements between two indexes."
            },
            {
                "term": "Leading Zero Prefix",
                "definition": "A prefix array beginning with zero, making range-sum formulas simpler."
            },
            {
                "term": "Subarray",
                "definition": "A contiguous sequence of elements from an array."
            },
            {
                "term": "Prefix Sum Hashing",
                "definition": "Combining cumulative sums with a hash map to efficiently find subarrays with a target sum."
            },
            {
                "term": "Difference Array",
                "definition": "A technique for applying multiple range updates efficiently."
            },
            {
                "term": "2D Prefix Sum",
                "definition": "A cumulative-sum structure used to answer rectangular matrix-sum queries."
            }
        ],

        "examples": {
            "python": """# 1. Build prefix sum
def build_prefix(arr):
    prefix = [0]

    for value in arr:
        prefix.append(prefix[-1] + value)

    return prefix


# 2. Range sum query: inclusive indexes L and R
def range_sum(prefix, left, right):
    return prefix[right + 1] - prefix[left]


# 3. Count subarrays with sum k
def subarray_sum_count(nums, k):
    frequency = {0: 1}
    prefix = 0
    count = 0

    for value in nums:
        prefix += value

        count += frequency.get(prefix - k, 0)

        frequency[prefix] = frequency.get(prefix, 0) + 1

    return count


# 4. Pivot index
def pivot_index(nums):
    total = sum(nums)
    left_sum = 0

    for i, value in enumerate(nums):
        right_sum = total - left_sum - value

        if left_sum == right_sum:
            return i

        left_sum += value

    return -1


arr = [2, 4, 6, 8, 10]
prefix = build_prefix(arr)

print(prefix)
print(range_sum(prefix, 1, 3))
print(subarray_sum_count([1, 2, 3], 3))
print(pivot_index([1, 7, 3, 6, 5, 6]))""",

            "java": """import java.util.*;

public class Main {

    static int[] buildPrefix(int[] arr) {
        int[] prefix = new int[arr.length + 1];

        for (int i = 0; i < arr.length; i++) {
            prefix[i + 1] = prefix[i] + arr[i];
        }

        return prefix;
    }

    static int rangeSum(int[] prefix, int left, int right) {
        return prefix[right + 1] - prefix[left];
    }

    static int subarraySumCount(int[] nums, int k) {
        Map<Integer, Integer> frequency = new HashMap<>();
        frequency.put(0, 1);

        int prefix = 0;
        int count = 0;

        for (int value : nums) {
            prefix += value;

            count += frequency.getOrDefault(prefix - k, 0);

            frequency.put(
                prefix,
                frequency.getOrDefault(prefix, 0) + 1
            );
        }

        return count;
    }

    static int pivotIndex(int[] nums) {
        int total = 0;

        for (int value : nums) {
            total += value;
        }

        int leftSum = 0;

        for (int i = 0; i < nums.length; i++) {
            int rightSum = total - leftSum - nums[i];

            if (leftSum == rightSum) return i;

            leftSum += nums[i];
        }

        return -1;
    }

    public static void main(String[] args) {
        int[] arr = {2, 4, 6, 8, 10};

        int[] prefix = buildPrefix(arr);

        System.out.println(Arrays.toString(prefix));
        System.out.println(rangeSum(prefix, 1, 3));

        System.out.println(
            subarraySumCount(new int[]{1, 2, 3}, 3)
        );

        System.out.println(
            pivotIndex(new int[]{1, 7, 3, 6, 5, 6})
        );
    }
}""",

            "cpp": """#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

vector<int> buildPrefix(vector<int>& arr) {
    vector<int> prefix(arr.size() + 1, 0);

    for (int i = 0; i < arr.size(); i++) {
        prefix[i + 1] = prefix[i] + arr[i];
    }

    return prefix;
}

int rangeSum(vector<int>& prefix, int left, int right) {
    return prefix[right + 1] - prefix[left];
}

int subarraySumCount(vector<int>& nums, int k) {
    unordered_map<int, int> frequency;
    frequency[0] = 1;

    int prefix = 0;
    int count = 0;

    for (int value : nums) {
        prefix += value;

        count += frequency[prefix - k];

        frequency[prefix]++;
    }

    return count;
}

int pivotIndex(vector<int>& nums) {
    int total = 0;

    for (int value : nums) {
        total += value;
    }

    int leftSum = 0;

    for (int i = 0; i < nums.size(); i++) {
        int rightSum = total - leftSum - nums[i];

        if (leftSum == rightSum) return i;

        leftSum += nums[i];
    }

    return -1;
}

int main() {
    vector<int> arr = {2, 4, 6, 8, 10};

    vector<int> prefix = buildPrefix(arr);

    for (int x : prefix) cout << x << " ";
    cout << endl;

    cout << rangeSum(prefix, 1, 3) << endl;

    vector<int> nums = {1, 2, 3};
    cout << subarraySumCount(nums, 3) << endl;

    vector<int> pivot = {1, 7, 3, 6, 5, 6};
    cout << pivotIndex(pivot) << endl;

    return 0;
}"""
        },

        "dry_run": [
            {
                "title": "Building a prefix sum",
                "input": "[2, 4, 6, 8]",
                "steps": [
                    "Start prefix = [0]",
                    "Read 2: prefix = [0, 2]",
                    "Read 4: prefix = [0, 2, 6]",
                    "Read 6: prefix = [0, 2, 6, 12]",
                    "Read 8: prefix = [0, 2, 6, 12, 20]"
                ],
                "output": "[0, 2, 6, 12, 20]",
                "complexity": "Time: O(n), Auxiliary space: O(n)"
            },
            {
                "title": "Range sum query",
                "input": "Array = [2, 4, 6, 8, 10], L = 1, R = 3",
                "steps": [
                    "Build prefix = [0, 2, 6, 12, 20, 30]",
                    "Use prefix[R + 1] - prefix[L]",
                    "Calculate prefix[4] - prefix[1]",
                    "Calculate 20 - 2"
                ],
                "output": "18",
                "complexity": "Preprocessing: O(n), each query: O(1)"
            },
            {
                "title": "Count subarrays with sum k",
                "input": "Array = [1, 2, 3], k = 3",
                "steps": [
                    "Start frequency = {0: 1}, prefix = 0",
                    "Read 1: prefix = 1, no previous prefix of -2",
                    "Read 2: prefix = 3, previous prefix 0 exists once; count = 1",
                    "Read 3: prefix = 6, previous prefix 3 exists once; count = 2"
                ],
                "output": "2",
                "complexity": "Average time: O(n), Auxiliary space: O(n)"
            }
        ],

        "practice_questions": [
            {
                "question": "Build a prefix sum array and answer the sum query from index L to R, inclusive.",
                "difficulty": "Easy",
                "solution": {
                    "python": """def range_sum_queries(arr, queries):
    prefix = [0]

    for value in arr:
        prefix.append(prefix[-1] + value)

    answers = []

    for left, right in queries:
        answers.append(prefix[right + 1] - prefix[left])

    return answers

print(range_sum_queries(
    [2, 4, 6, 8, 10],
    [(1, 3), (0, 2)]
))""",
                    "java": """static int[] rangeSumQueries(
    int[] arr, int[][] queries
) {
    int[] prefix = new int[arr.length + 1];

    for (int i = 0; i < arr.length; i++) {
        prefix[i + 1] = prefix[i] + arr[i];
    }

    int[] answers = new int[queries.length];

    for (int i = 0; i < queries.length; i++) {
        int left = queries[i][0];
        int right = queries[i][1];

        answers[i] = prefix[right + 1] - prefix[left];
    }

    return answers;
}""",
                    "cpp": """vector<int> rangeSumQueries(
    vector<int>& arr, vector<pair<int, int>>& queries
) {
    vector<int> prefix(arr.size() + 1, 0);

    for (int i = 0; i < arr.size(); i++) {
        prefix[i + 1] = prefix[i] + arr[i];
    }

    vector<int> answers;

    for (auto [left, right] : queries) {
        answers.push_back(prefix[right + 1] - prefix[left]);
    }

    return answers;
}""",
                    "output": "[18, 12]",
                    "explanation": "Build the prefix array once. Each query is answered in O(1). Preprocessing is O(n), and auxiliary space is O(n)."
                }
            },
            {
                "question": "Find the pivot index where the sum of elements on the left equals the sum on the right.",
                "difficulty": "Easy",
                "solution": {
                    "python": """def pivot_index(nums):
    total = sum(nums)
    left_sum = 0

    for i, value in enumerate(nums):
        right_sum = total - left_sum - value

        if left_sum == right_sum:
            return i

        left_sum += value

    return -1

print(pivot_index([1, 7, 3, 6, 5, 6]))""",
                    "java": """static int pivotIndex(int[] nums) {
    int total = 0;

    for (int value : nums) total += value;

    int leftSum = 0;

    for (int i = 0; i < nums.length; i++) {
        int rightSum = total - leftSum - nums[i];

        if (leftSum == rightSum) return i;

        leftSum += nums[i];
    }

    return -1;
}""",
                    "cpp": """int pivotIndex(vector<int>& nums) {
    int total = 0;

    for (int value : nums) total += value;

    int leftSum = 0;

    for (int i = 0; i < nums.size(); i++) {
        int rightSum = total - leftSum - nums[i];

        if (leftSum == rightSum) return i;

        leftSum += nums[i];
    }

    return -1;
}""",
                    "output": "3",
                    "explanation": "At index 3, the left sum is 1 + 7 + 3 = 11 and the right sum is 5 + 6 = 11. Time O(n), auxiliary space O(1)."
                }
            },
            {
                "question": "Count the number of continuous subarrays whose sum equals k.",
                "difficulty": "Medium",
                "solution": {
                    "python": """def subarray_sum(nums, k):
    frequency = {0: 1}
    prefix = 0
    count = 0

    for value in nums:
        prefix += value
        count += frequency.get(prefix - k, 0)
        frequency[prefix] = frequency.get(prefix, 0) + 1

    return count

print(subarray_sum([1, 2, 3], 3))""",
                    "java": """static int subarraySum(int[] nums, int k) {
    Map<Integer, Integer> frequency = new HashMap<>();
    frequency.put(0, 1);

    int prefix = 0;
    int count = 0;

    for (int value : nums) {
        prefix += value;
        count += frequency.getOrDefault(prefix - k, 0);

        frequency.put(
            prefix,
            frequency.getOrDefault(prefix, 0) + 1
        );
    }

    return count;
}""",
                    "cpp": """int subarraySum(vector<int>& nums, int k) {
    unordered_map<int, int> frequency;
    frequency[0] = 1;

    int prefix = 0;
    int count = 0;

    for (int value : nums) {
        prefix += value;
        count += frequency[prefix - k];
        frequency[prefix]++;
    }

    return count;
}""",
                    "output": "2",
                    "explanation": "The qualifying subarrays are [1, 2] and [3]. The hash map stores earlier prefix sums and their frequencies. Average time O(n), auxiliary space O(n)."
                }
            }
        ],

        "interview_questions": [
            {
                "question": "What is prefix sum?",
                "answer": "Prefix sum stores cumulative sums of array elements."
            },
            {
                "question": "How do you build a prefix sum array?",
                "answer": "Set prefix[0] to the first element, then calculate each next value using prefix[i] = prefix[i-1] + arr[i]. A leading-zero representation is also common."
            },
            {
                "question": "How do you answer a range sum query using prefix sums?",
                "answer": "With a leading-zero prefix array, sum(L, R) = prefix[R+1] - prefix[L]."
            },
            {
                "question": "What is the preprocessing time complexity of prefix sums?",
                "answer": "O(n), because every element is processed once."
            },
            {
                "question": "What is the time complexity of an individual range-sum query after preprocessing?",
                "answer": "O(1)."
            },
            {
                "question": "Can prefix sums handle negative numbers?",
                "answer": "Yes. The cumulative-sum formula works with both positive and negative numbers."
            },
            {
                "question": "What is the advantage of a leading-zero prefix array?",
                "answer": "It simplifies range queries into prefix[R+1] - prefix[L], including ranges starting at index zero."
            },
            {
                "question": "How can prefix sums be combined with a HashMap?",
                "answer": "Store frequencies of previous prefix sums. To find subarrays with sum k, look for an earlier prefix equal to currentPrefix - k."
            },
            {
                "question": "Why is frequency[0] initialized to 1 in the subarray-sum problem?",
                "answer": "It accounts for a subarray starting at index zero whose cumulative sum equals k."
            },
            {
                "question": "What is the average time complexity of counting subarrays with sum k using hashing?",
                "answer": "O(n), assuming average O(1) hash-map operations."
            },
            {
                "question": "What is a 2D prefix sum?",
                "answer": "It stores cumulative sums for rectangular regions of a matrix."
            },
            {
                "question": "What is a difference array?",
                "answer": "It represents changes between adjacent elements and helps perform range updates efficiently."
            },
            {
                "question": "When are prefix sums less suitable?",
                "answer": "When elements are frequently updated, because a normal prefix array may require O(n) rebuilding or updating work."
            },
            {
                "question": "What data structures can support dynamic range-sum queries?",
                "answer": "Fenwick Trees (Binary Indexed Trees) and Segment Trees."
            },
            {
                "question": "Name common prefix sum interview problems.",
                "answer": "Range Sum Query, Pivot Index, Subarray Sum Equals K, and Continuous Subarray Sum."
            }
        ],

        "mcqs": [
            {
                "question": "What is the prefix sum array of [2, 3, 4] using a leading zero?",
                "options": [
                    "[2, 5, 9]",
                    "[0, 2, 5, 9]",
                    "[0, 3, 7, 9]",
                    "[9, 7, 4]"
                ],
                "answer": "[0, 2, 5, 9]",
                "explanation": "Each position stores the sum of all previous elements, starting from zero."
            },
            {
                "question": "What is the preprocessing time complexity of a prefix sum array?",
                "options": ["O(1)", "O(log n)", "O(n)", "O(n²)"],
                "answer": "O(n)",
                "explanation": "Each array element is processed once."
            },
            {
                "question": "Using a leading-zero prefix array, how do you calculate the sum from L to R?",
                "options": [
                    "prefix[R] - prefix[L]",
                    "prefix[R+1] - prefix[L]",
                    "prefix[L] + prefix[R]",
                    "prefix[R+1] + prefix[L]"
                ],
                "answer": "prefix[R+1] - prefix[L]",
                "explanation": "The leading-zero representation makes this formula work for all valid ranges."
            },
            {
                "question": "What is the time complexity of one range-sum query after prefix preprocessing?",
                "options": ["O(n)", "O(log n)", "O(1)", "O(n²)"],
                "answer": "O(1)",
                "explanation": "Only two prefix values need to be subtracted."
            },
            {
                "question": "Can prefix sums work with negative numbers?",
                "options": ["No", "Yes", "Only with sorting", "Only with positive indexes"],
                "answer": "Yes",
                "explanation": "Cumulative sums and range subtraction work with negative values too."
            },
            {
                "question": "Why is frequency[0] initialized to 1 in Subarray Sum Equals K?",
                "options": [
                    "To count an empty input",
                    "To handle subarrays beginning at index zero",
                    "To sort the hash map",
                    "To avoid negative values"
                ],
                "answer": "To handle subarrays beginning at index zero",
                "explanation": "It allows the current prefix itself to equal k."
            },
            {
                "question": "What is the average time complexity of Subarray Sum Equals K using hashing?",
                "options": ["O(n²)", "O(n log n)", "O(n)", "O(1)"],
                "answer": "O(n)",
                "explanation": "Each element is processed once with average constant-time hash operations."
            },
            {
                "question": "Which technique is useful for multiple range increment operations?",
                "options": ["Binary Search", "Difference Array", "Merge Sort", "DFS"],
                "answer": "Difference Array",
                "explanation": "Difference arrays represent range updates with two boundary changes."
            },
            {
                "question": "What is the preprocessing space complexity of a standard leading-zero prefix array?",
                "options": ["O(1)", "O(log n)", "O(n)", "O(n²)"],
                "answer": "O(n)",
                "explanation": "The prefix array stores n+1 values."
            },
            {
                "question": "Which data structure is suitable for dynamic range-sum queries?",
                "options": ["Stack only", "Fenwick Tree", "Simple prefix array only", "Queue only"],
                "answer": "Fenwick Tree",
                "explanation": "A Fenwick Tree supports efficient updates and prefix-sum queries."
            }
        ]
    }
})


DSA_TRACK.update({
    "dsa-sliding-window": {
        "title": "Sliding Window Technique",
        "description": "Learn how to solve array and string problems efficiently using fixed-size and variable-size sliding windows.",

        "content": """
# 1. What is the Sliding Window Technique?

Sliding Window is an algorithmic technique used to solve problems involving
contiguous parts of an array or string.

A window represents a continuous section of elements.

Instead of recalculating the result for every possible subarray,
we maintain a window and update its result as it moves.

This often reduces time complexity from O(n*k) or O(n²) to O(n).

## 2. Why do we need Sliding Window?

Consider this problem:

Given an array [2, 1, 5, 1, 3, 2], find the maximum sum of any
contiguous subarray of size 3.

A brute-force approach calculates every group of 3 elements separately.

A better approach:
1. Calculate the sum of the first 3 elements.
2. Remove the element leaving the window.
3. Add the new element entering the window.
4. Update the maximum sum.

This avoids repeatedly adding elements.

## 3. Types of Sliding Window

### A. Fixed-size Sliding Window

The window size remains constant.

Examples:
- Maximum sum of a subarray of size K.
- Average of every subarray of size K.
- First negative number in every window of size K.

Typical process:
1. Add the next element.
2. If the window becomes larger than K, remove its leftmost element.
3. Process the window when its size is K.

### B. Variable-size Sliding Window

The window size changes depending on a condition.

Examples:
- Longest substring without repeating characters.
- Smallest subarray with sum greater than or equal to a target.
- Longest subarray containing at most K distinct elements.

Typical process:
1. Expand the window by moving the right pointer.
2. Check whether the current window satisfies the condition.
3. If it violates the condition, move the left pointer.
4. Update the answer.

## 4. Fixed-size Window Algorithm

For an array and window size K:

- Initialize window_sum = 0.
- Add elements while moving the right pointer.
- When the window reaches size K, update the answer.
- Remove the leftmost element before moving to the next window.

Time Complexity: O(n)
Space Complexity: O(1)

## 5. Variable-size Window Algorithm

Use two pointers:

- left: beginning of the window.
- right: end of the window.

Expand right to include new elements.
Shrink left whenever the window violates the required condition.

For many problems, each pointer moves at most n times.

Time Complexity: O(n)
Space Complexity: O(1) for simple numeric windows.

Important: The usual sum-based variable window requires non-negative
array elements for problems such as finding the smallest subarray
with sum at least a target. Negative values can break the logic.

## 6. When should you use Sliding Window?

Look for problem statements containing:
- Contiguous subarray
- Continuous substring
- Subarray of size K
- Longest substring
- Maximum or minimum sum of K consecutive elements
- Smallest or longest valid window

Sliding Window is generally useful when a problem asks about
a continuous range of elements.
""",

        "key_concepts": [
            {
                "concept": "Window",
                "explanation": "A continuous section of an array or string being considered at a particular time."
            },
            {
                "concept": "Left Pointer",
                "explanation": "Represents the starting index of the current window."
            },
            {
                "concept": "Right Pointer",
                "explanation": "Represents the ending index of the current window and expands the window."
            },
            {
                "concept": "Fixed-size Window",
                "explanation": "A window whose number of elements remains constant."
            },
            {
                "concept": "Variable-size Window",
                "explanation": "A window that expands or shrinks according to a condition."
            },
            {
                "concept": "Window Update",
                "explanation": "Update the current result by adding incoming elements and removing outgoing elements instead of recalculating everything."
            }
        ],

        "examples": {
            "python": """# Maximum sum of a subarray of size k

def max_sum_subarray(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum

    for right in range(k, len(arr)):
        window_sum += arr[right]
        window_sum -= arr[right - k]
        max_sum = max(max_sum, window_sum)

    return max_sum


arr = [2, 1, 5, 1, 3, 2]
print(max_sum_subarray(arr, 3))

# Output: 9""",

            "java": """import java.util.*;

public class Main {
    public static int maxSumSubarray(int[] arr, int k) {
        int windowSum = 0;

        for (int i = 0; i < k; i++) {
            windowSum += arr[i];
        }

        int maxSum = windowSum;

        for (int right = k; right < arr.length; right++) {
            windowSum += arr[right];
            windowSum -= arr[right - k];

            maxSum = Math.max(maxSum, windowSum);
        }

        return maxSum;
    }

    public static void main(String[] args) {
        int[] arr = {2, 1, 5, 1, 3, 2};

        System.out.println(maxSumSubarray(arr, 3));
    }
}

// Output: 9""",

            "cpp": """#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int maxSumSubarray(vector<int>& arr, int k) {
    int windowSum = 0;

    for (int i = 0; i < k; i++) {
        windowSum += arr[i];
    }

    int maxSum = windowSum;

    for (int right = k; right < arr.size(); right++) {
        windowSum += arr[right];
        windowSum -= arr[right - k];

        maxSum = max(maxSum, windowSum);
    }

    return maxSum;
}

int main() {
    vector<int> arr = {2, 1, 5, 1, 3, 2};

    cout << maxSumSubarray(arr, 3);

    return 0;
}

// Output: 9"""
        },

        "dry_run": [
            {
                "step": 1,
                "operation": "Initial window",
                "window": "[2, 1, 5]",
                "window_sum": 8,
                "max_sum": 8
            },
            {
                "step": 2,
                "operation": "Remove 2 and add 1",
                "window": "[1, 5, 1]",
                "window_sum": 7,
                "max_sum": 8
            },
            {
                "step": 3,
                "operation": "Remove 1 and add 3",
                "window": "[5, 1, 3]",
                "window_sum": 9,
                "max_sum": 9
            },
            {
                "step": 4,
                "operation": "Remove 5 and add 2",
                "window": "[1, 3, 2]",
                "window_sum": 6,
                "max_sum": 9
            }
        ],

        "practice_questions": [
            {
                "title": "Maximum Sum Subarray of Size K",
                "difficulty": "Easy",
                "problem": "Given an integer array and an integer K, find the maximum sum among all contiguous subarrays of size K.",
                "example": "Input: arr = [2, 1, 5, 1, 3, 2], K = 3. Output: 9",
                "solution": {
                    "python": """def maximum_sum(arr, k):
    if k <= 0 or k > len(arr):
        return None

    window_sum = sum(arr[:k])
    answer = window_sum

    for right in range(k, len(arr)):
        window_sum += arr[right]
        window_sum -= arr[right - k]
        answer = max(answer, window_sum)

    return answer


print(maximum_sum([2, 1, 5, 1, 3, 2], 3))""",
                    "java": """public static int maximumSum(int[] arr, int k) {
    if (k <= 0 || k > arr.length) {
        return -1;
    }

    int windowSum = 0;

    for (int i = 0; i < k; i++) {
        windowSum += arr[i];
    }

    int answer = windowSum;

    for (int right = k; right < arr.length; right++) {
        windowSum += arr[right] - arr[right - k];
        answer = Math.max(answer, windowSum);
    }

    return answer;
}""",
                    "cpp": """int maximumSum(vector<int>& arr, int k) {
    if (k <= 0 || k > arr.size()) return -1;

    int windowSum = 0;

    for (int i = 0; i < k; i++) {
        windowSum += arr[i];
    }

    int answer = windowSum;

    for (int right = k; right < arr.size(); right++) {
        windowSum += arr[right] - arr[right - k];
        answer = max(answer, windowSum);
    }

    return answer;
}"""
                },
                "explanation": "Calculate the first window once. For every next window, subtract the outgoing element and add the incoming element.",
                "time_complexity": "O(n)",
                "space_complexity": "O(1)"
            },
            {
                "title": "Longest Substring Without Repeating Characters",
                "difficulty": "Medium",
                "problem": "Given a string, find the length of the longest substring that contains no repeated characters.",
                "example": "Input: s = 'abcabcbb'. Output: 3. The longest substring is 'abc'.",
                "solution": {
                    "python": """def longest_unique_substring(s):
    seen = set()
    left = 0
    answer = 0

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1

        seen.add(s[right])
        answer = max(answer, right - left + 1)

    return answer


print(longest_unique_substring("abcabcbb"))""",
                    "java": """import java.util.*;

public static int longestUniqueSubstring(String s) {
    Set<Character> seen = new HashSet<>();
    int left = 0;
    int answer = 0;

    for (int right = 0; right < s.length(); right++) {
        while (seen.contains(s.charAt(right))) {
            seen.remove(s.charAt(left));
            left++;
        }

        seen.add(s.charAt(right));
        answer = Math.max(answer, right - left + 1);
    }

    return answer;
}""",
                    "cpp": """#include <unordered_set>
#include <string>
#include <algorithm>
using namespace std;

int longestUniqueSubstring(string s) {
    unordered_set<char> seen;
    int left = 0;
    int answer = 0;

    for (int right = 0; right < s.size(); right++) {
        while (seen.count(s[right])) {
            seen.erase(s[left]);
            left++;
        }

        seen.insert(s[right]);
        answer = max(answer, right - left + 1);
    }

    return answer;
}"""
                },
                "explanation": "Expand the right pointer. When a duplicate appears, shrink the window from the left until the duplicate is removed.",
                "time_complexity": "O(n) average",
                "space_complexity": "O(min(n, character set size))"
            },
            {
                "title": "Minimum Size Subarray Sum",
                "difficulty": "Medium",
                "problem": "Given an array of positive integers and a target, find the minimum length of a contiguous subarray whose sum is greater than or equal to the target. Return 0 if no such subarray exists.",
                "example": "Input: target = 7, nums = [2, 3, 1, 2, 4, 3]. Output: 2. The subarray [4, 3] has sum 7.",
                "solution": {
                    "python": """def min_subarray_length(target, nums):
    left = 0
    window_sum = 0
    answer = float('inf')

    for right in range(len(nums)):
        window_sum += nums[right]

        while window_sum >= target:
            answer = min(answer, right - left + 1)
            window_sum -= nums[left]
            left += 1

    return 0 if answer == float('inf') else answer


print(min_subarray_length(7, [2, 3, 1, 2, 4, 3]))""",
                    "java": """public static int minSubarrayLength(int target, int[] nums) {
    int left = 0;
    int windowSum = 0;
    int answer = Integer.MAX_VALUE;

    for (int right = 0; right < nums.length; right++) {
        windowSum += nums[right];

        while (windowSum >= target) {
            answer = Math.min(answer, right - left + 1);
            windowSum -= nums[left];
            left++;
        }
    }

    return answer == Integer.MAX_VALUE ? 0 : answer;
}""",
                    "cpp": """#include <vector>
#include <algorithm>
#include <climits>
using namespace std;

int minSubarrayLength(int target, vector<int>& nums) {
    int left = 0;
    int windowSum = 0;
    int answer = INT_MAX;

    for (int right = 0; right < nums.size(); right++) {
        windowSum += nums[right];

        while (windowSum >= target) {
            answer = min(answer, right - left + 1);
            windowSum -= nums[left];
            left++;
        }
    }

    return answer == INT_MAX ? 0 : answer;
}"""
                },
                "explanation": "Expand the window until its sum reaches the target. Then shrink it from the left while it remains valid, recording the smallest length.",
                "time_complexity": "O(n)",
                "space_complexity": "O(1)"
            }
        ],

        "interview_questions": [
            {
                "question": "What is the Sliding Window technique?",
                "answer": "It is an algorithmic technique that maintains a continuous range of elements and moves that range through an array or string."
            },
            {
                "question": "What are the two types of Sliding Window?",
                "answer": "Fixed-size Sliding Window and Variable-size Sliding Window."
            },
            {
                "question": "When should you use Sliding Window?",
                "answer": "When a problem involves contiguous subarrays or substrings and asks for a maximum, minimum, length, sum, or count."
            },
            {
                "question": "What is the difference between Sliding Window and Two Pointers?",
                "answer": "Two Pointers is a general technique using two indices. Sliding Window is a related technique that uses pointers to maintain a continuous range."
            },
            {
                "question": "What is the time complexity of a typical Sliding Window algorithm?",
                "answer": "Usually O(n), because each pointer moves through the input at most a constant number of times."
            },
            {
                "question": "How does a fixed-size window work?",
                "answer": "It maintains exactly K elements by adding a new element and removing the element that leaves the window."
            },
            {
                "question": "How does a variable-size window work?",
                "answer": "It expands and shrinks according to a condition, such as a sum limit or the presence of duplicate characters."
            },
            {
                "question": "Why is Sliding Window more efficient than brute force?",
                "answer": "It reuses the previous window's calculation instead of repeatedly processing all elements."
            },
            {
                "question": "What is the role of the left pointer?",
                "answer": "It identifies the starting position of the current window and moves forward when the window needs to shrink."
            },
            {
                "question": "What is the role of the right pointer?",
                "answer": "It expands the current window by including new elements."
            },
            {
                "question": "Can Sliding Window solve the maximum sum subarray of size K problem?",
                "answer": "Yes. Maintain the sum of K consecutive elements and update it by adding the incoming element and subtracting the outgoing element."
            },
            {
                "question": "Can a variable-size sum window always work with negative numbers?",
                "answer": "No. The common expand-and-shrink sum approach relies on non-negative numbers. Negative values can make the sum unpredictable when the window changes."
            },
            {
                "question": "What is the difference between a subarray and a subsequence?",
                "answer": "A subarray must contain consecutive elements. A subsequence can skip elements while preserving their relative order."
            },
            {
                "question": "How can you find the longest substring without repeating characters?",
                "answer": "Use a variable-size window and a set or map to track characters. Shrink the window when a repeated character appears."
            },
            {
                "question": "What is the space complexity of a Sliding Window algorithm?",
                "answer": "It can be O(1) when only a few variables are maintained, or O(n) when a set or map stores elements from the window."
            }
        ],

        "mcqs": [
            {
                "question": "Sliding Window is mainly used for problems involving:",
                "options": [
                    "Contiguous subarrays or substrings",
                    "Only binary trees",
                    "Only graph traversal",
                    "Only sorting"
                ],
                "answer": "Contiguous subarrays or substrings",
                "explanation": "Sliding Window maintains a continuous range of elements."
            },
            {
                "question": "How many main types of Sliding Window are commonly used?",
                "options": ["1", "2", "3", "4"],
                "answer": "2",
                "explanation": "The two common types are fixed-size and variable-size."
            },
            {
                "question": "What is the typical time complexity of a basic Sliding Window algorithm?",
                "options": ["O(n²)", "O(n log n)", "O(n)", "O(2ⁿ)"],
                "answer": "O(n)",
                "explanation": "Each pointer usually moves through the input at most once."
            },
            {
                "question": "In a fixed-size window of size K, how many elements should the window contain?",
                "options": ["K", "K + 1", "K - 1", "Any number"],
                "answer": "K",
                "explanation": "A fixed-size window always contains exactly K elements."
            },
            {
                "question": "For the array [1, 2, 3, 4, 5], what is the sum of the first window of size 3?",
                "options": ["5", "6", "9", "12"],
                "answer": "6",
                "explanation": "1 + 2 + 3 = 6."
            },
            {
                "question": "If the current window sum is 10, the outgoing element is 3, and the incoming element is 5, what is the new sum?",
                "options": ["12", "15", "8", "18"],
                "answer": "12",
                "explanation": "New sum = 10 - 3 + 5 = 12."
            },
            {
                "question": "Which pointers are commonly used in Sliding Window?",
                "options": [
                    "Left and Right",
                    "Top and Bottom",
                    "Parent and Child",
                    "Front and Middle"
                ],
                "answer": "Left and Right",
                "explanation": "The left and right pointers represent the boundaries of the window."
            },
            {
                "question": "Which data structure can help find duplicate characters in a window?",
                "options": ["Stack only", "Set", "Queue only", "Tree only"],
                "answer": "Set",
                "explanation": "A set can track characters currently present in the window."
            },
            {
                "question": "Which problem is a common Sliding Window application?",
                "options": [
                    "Longest substring without repeating characters",
                    "Binary tree traversal",
                    "Merge sort",
                    "Finding a graph cycle using DFS"
                ],
                "answer": "Longest substring without repeating characters",
                "explanation": "It uses a variable-size window to maintain unique characters."
            },
            {
                "question": "The common variable-size window algorithm for minimum subarray sum at least a target assumes:",
                "options": [
                    "All elements are negative",
                    "All elements are non-negative",
                    "The array is sorted",
                    "The array has unique elements"
                ],
                "answer": "All elements are non-negative",
                "explanation": "Non-negative values allow the sum-based window to shrink predictably."
            }
        ]
    }
})


DSA_TRACK.update({
    "dsa-greedy": {
        "title": "Greedy Algorithms",
        "description": "Learn to solve optimization problems by making locally optimal choices at each step.",

        "content": """
# 1. What is a Greedy Algorithm?

A Greedy Algorithm is an approach in which we make the best-looking
choice at the current step, hoping that these choices produce
the globally optimal solution.

A greedy algorithm does not normally reconsider its previous choices.

Example:
Suppose you need to select the maximum number of non-overlapping
meetings. A useful strategy is to always select the meeting
that finishes earliest.

## 2. How Greedy Algorithms Work

1. Identify the available choices.
2. Decide which choice is best at the current step.
3. Select that choice.
4. Update the problem state.
5. Repeat until the problem is complete.

## 3. Important Properties

### Greedy Choice Property

A globally optimal solution can be obtained by making a locally
optimal choice at each step.

### Optimal Substructure

An optimal solution to a problem contains optimal solutions
to its smaller subproblems.

Many greedy problems have both properties.

## 4. Greedy vs Dynamic Programming

Greedy:
- Makes a choice and moves forward.
- Usually does not reconsider earlier decisions.
- Often uses sorting or priority queues.
- Can be faster and simpler.

Dynamic Programming:
- Solves and combines overlapping subproblems.
- Stores results to avoid repeated calculations.
- Considers multiple possibilities when necessary.

## 5. Example: Activity Selection

Suppose meetings have these intervals:

(1, 3), (2, 5), (4, 6), (6, 8)

We want to attend the maximum number of non-overlapping meetings.

Greedy strategy:
1. Sort meetings by finishing time.
2. Select the meeting that finishes earliest.
3. Select the next meeting whose start time is greater than
   or equal to the finish time of the last selected meeting.

Selected meetings:
(1, 3), (4, 6), (6, 8)

Answer: 3 meetings.

## 6. Common Greedy Problems

- Activity Selection
- Fractional Knapsack
- Minimum Number of Coins (for suitable coin systems)
- Job Sequencing with Deadlines
- Huffman Coding
- Minimum Platforms
- Interval Scheduling

## 7. When Does Greedy Work?

Greedy is not correct for every optimization problem.

You must prove that the local choice is safe.

For example, choosing the largest coin first does not always
produce the minimum number of coins for arbitrary denominations.

For coins [1, 3, 4] and amount 6:
Greedy chooses 4 + 1 + 1 = 3 coins.
The optimal solution is 3 + 3 = 2 coins.

This is why understanding the greedy choice property is important.
""",

        "key_concepts": [
            {
                "concept": "Greedy Choice",
                "explanation": "Choosing the best available option at the current step."
            },
            {
                "concept": "Greedy Choice Property",
                "explanation": "A locally optimal choice can be part of a globally optimal solution."
            },
            {
                "concept": "Optimal Substructure",
                "explanation": "An optimal solution contains optimal solutions to smaller subproblems."
            },
            {
                "concept": "Activity Selection",
                "explanation": "Select the maximum number of mutually compatible activities, commonly by sorting by finish time."
            },
            {
                "concept": "Fractional Knapsack",
                "explanation": "Select items in descending order of value-to-weight ratio. Fractions of items are allowed."
            },
            {
                "concept": "Greedy Limitation",
                "explanation": "A locally optimal choice does not always produce a globally optimal answer."
            }
        ],

        "examples": {
            "python": """# Activity Selection Problem

def activity_selection(start, finish):
    activities = sorted(zip(start, finish), key=lambda x: x[1])

    selected = []
    last_finish = float('-inf')

    for s, f in activities:
        if s >= last_finish:
            selected.append((s, f))
            last_finish = f

    return selected


start = [1, 2, 4, 6]
finish = [3, 5, 6, 8]

print(activity_selection(start, finish))

# Output: [(1, 3), (4, 6), (6, 8)]""",

            "java": """import java.util.*;

public class Main {
    static int activitySelection(int[] start, int[] finish) {
        int n = start.length;
        int[][] activities = new int[n][2];

        for (int i = 0; i < n; i++) {
            activities[i][0] = start[i];
            activities[i][1] = finish[i];
        }

        Arrays.sort(activities, Comparator.comparingInt(a -> a[1]));

        int count = 0;
        int lastFinish = Integer.MIN_VALUE;

        for (int[] activity : activities) {
            if (activity[0] >= lastFinish) {
                count++;
                lastFinish = activity[1];
            }
        }

        return count;
    }

    public static void main(String[] args) {
        int[] start = {1, 2, 4, 6};
        int[] finish = {3, 5, 6, 8};

        System.out.println(activitySelection(start, finish));
    }
}

// Output: 3""",

            "cpp": """#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int activitySelection(vector<int>& start, vector<int>& finish) {
    vector<pair<int, int>> activities;

    for (int i = 0; i < start.size(); i++) {
        activities.push_back({finish[i], start[i]});
    }

    sort(activities.begin(), activities.end());

    int count = 0;
    int lastFinish = -1;

    for (auto activity : activities) {
        int finishTime = activity.first;
        int startTime = activity.second;

        if (startTime >= lastFinish) {
            count++;
            lastFinish = finishTime;
        }
    }

    return count;
}

int main() {
    vector<int> start = {1, 2, 4, 6};
    vector<int> finish = {3, 5, 6, 8};

    cout << activitySelection(start, finish);

    return 0;
}

// Output: 3"""
        },

        "dry_run": [
            {
                "step": 1,
                "operation": "Sort activities by finish time",
                "selected": "None",
                "explanation": "Activities are ordered by their finishing times: (1,3), (2,5), (4,6), (6,8)."
            },
            {
                "step": 2,
                "operation": "Select (1,3)",
                "selected": "(1,3)",
                "explanation": "This activity finishes earliest."
            },
            {
                "step": 3,
                "operation": "Check (2,5)",
                "selected": "(1,3)",
                "explanation": "Reject because it starts before the previous activity finishes."
            },
            {
                "step": 4,
                "operation": "Select (4,6)",
                "selected": "(1,3), (4,6)",
                "explanation": "It starts after the previous selected activity finishes."
            },
            {
                "step": 5,
                "operation": "Select (6,8)",
                "selected": "(1,3), (4,6), (6,8)",
                "explanation": "It starts exactly when the previous selected activity finishes."
            }
        ],

        "practice_questions": [
            {
                "title": "Activity Selection",
                "difficulty": "Easy",
                "problem": "Given start and finish times of activities, select the maximum number of non-overlapping activities. An activity can start when the previous selected activity finishes.",
                "example": "Input: start = [1, 2, 4, 6], finish = [3, 5, 6, 8]. Output: 3",
                "solution": {
                    "python": """def activity_selection(start, finish):
    activities = sorted(zip(start, finish), key=lambda x: x[1])

    count = 0
    last_finish = float('-inf')

    for s, f in activities:
        if s >= last_finish:
            count += 1
            last_finish = f

    return count


print(activity_selection([1, 2, 4, 6], [3, 5, 6, 8]))""",
                    "java": """import java.util.*;

public static int activitySelection(int[] start, int[] finish) {
    int[][] activities = new int[start.length][2];

    for (int i = 0; i < start.length; i++) {
        activities[i][0] = start[i];
        activities[i][1] = finish[i];
    }

    Arrays.sort(activities, Comparator.comparingInt(a -> a[1]));

    int count = 0;
    int lastFinish = Integer.MIN_VALUE;

    for (int[] activity : activities) {
        if (activity[0] >= lastFinish) {
            count++;
            lastFinish = activity[1];
        }
    }

    return count;
}""",
                    "cpp": """int activitySelection(vector<int>& start, vector<int>& finish) {
    vector<pair<int, int>> activities;

    for (int i = 0; i < start.size(); i++) {
        activities.push_back({finish[i], start[i]});
    }

    sort(activities.begin(), activities.end());

    int count = 0;
    int lastFinish = -1;

    for (auto activity : activities) {
        if (activity.second >= lastFinish) {
            count++;
            lastFinish = activity.first;
        }
    }

    return count;
}"""
                },
                "explanation": "Sorting by finishing time allows us to choose the earliest finishing compatible activity at every step.",
                "time_complexity": "O(n log n)",
                "space_complexity": "O(n)"
            },
            {
                "title": "Fractional Knapsack",
                "difficulty": "Medium",
                "problem": "Given values and weights of items and a knapsack capacity, maximize the total value. You are allowed to take fractions of items.",
                "example": "Input: values = [60, 100, 120], weights = [10, 20, 30], capacity = 50. Output: 240.0",
                "solution": {
                    "python": """def fractional_knapsack(values, weights, capacity):
    items = sorted(
        zip(values, weights),
        key=lambda item: item[0] / item[1],
        reverse=True
    )

    total_value = 0.0

    for value, weight in items:
        if capacity == 0:
            break

        take = min(weight, capacity)
        total_value += take * (value / weight)
        capacity -= take

    return total_value


print(fractional_knapsack([60, 100, 120], [10, 20, 30], 50))""",
                    "java": """import java.util.*;

public static double fractionalKnapsack(int[] values, int[] weights, int capacity) {
    int n = values.length;
    double[][] items = new double[n][3];

    for (int i = 0; i < n; i++) {
        items[i][0] = values[i];
        items[i][1] = weights[i];
        items[i][2] = (double) values[i] / weights[i];
    }

    Arrays.sort(items, (a, b) -> Double.compare(b[2], a[2]));

    double totalValue = 0;

    for (double[] item : items) {
        if (capacity == 0) break;

        double take = Math.min(item[1], capacity);
        totalValue += take * item[2];
        capacity -= (int) take;
    }

    return totalValue;
}""",
                    "cpp": """double fractionalKnapsack(vector<int>& values,
                         vector<int>& weights, int capacity) {
    vector<pair<double, int>> items;

    for (int i = 0; i < values.size(); i++) {
        double ratio = (double) values[i] / weights[i];
        items.push_back({ratio, i});
    }

    sort(items.rbegin(), items.rend());

    double totalValue = 0;

    for (auto item : items) {
        if (capacity == 0) break;

        int i = item.second;
        int take = min(weights[i], capacity);

        totalValue += take * item.first;
        capacity -= take;
    }

    return totalValue;
}"""
                },
                "explanation": "Choose items with the highest value-to-weight ratio first. Take a fraction when the remaining capacity is insufficient for the whole item.",
                "time_complexity": "O(n log n)",
                "space_complexity": "O(n)"
            },
            {
                "title": "Minimum Number of Platforms",
                "difficulty": "Medium",
                "problem": "Given train arrival and departure times, find the minimum number of platforms required so that no train has to wait.",
                "example": "Input: arrival = [900, 940, 950, 1100, 1500, 1800], departure = [910, 1200, 1120, 1130, 1900, 2000]. Output: 3",
                "solution": {
                    "python": """def minimum_platforms(arrival, departure):
    arrival.sort()
    departure.sort()

    platforms = 0
    maximum = 0
    i = j = 0

    while i < len(arrival):
        if i < len(arrival) and (
            j >= len(departure) or arrival[i] <= departure[j]
        ):
            platforms += 1
            maximum = max(maximum, platforms)
            i += 1
        else:
            platforms -= 1
            j += 1

    return maximum


print(minimum_platforms(
    [900, 940, 950, 1100, 1500, 1800],
    [910, 1200, 1120, 1130, 1900, 2000]
))""",
                    "java": """import java.util.*;

public static int minimumPlatforms(int[] arrival, int[] departure) {
    Arrays.sort(arrival);
    Arrays.sort(departure);

    int i = 0, j = 0;
    int platforms = 0, maximum = 0;

    while (i < arrival.length) {
        if (j >= departure.length || arrival[i] <= departure[j]) {
            platforms++;
            maximum = Math.max(maximum, platforms);
            i++;
        } else {
            platforms--;
            j++;
        }
    }

    return maximum;
}""",
                    "cpp": """int minimumPlatforms(vector<int>& arrival, vector<int>& departure) {
    sort(arrival.begin(), arrival.end());
    sort(departure.begin(), departure.end());

    int i = 0, j = 0;
    int platforms = 0, maximum = 0;

    while (i < arrival.size()) {
        if (j >= departure.size() || arrival[i] <= departure[j]) {
            platforms++;
            maximum = max(maximum, platforms);
            i++;
        } else {
            platforms--;
            j++;
        }
    }

    return maximum;
}"""
                },
                "explanation": "Sort arrival and departure times separately. Track how many trains are present at the same time. The maximum overlap is the required number of platforms.",
                "time_complexity": "O(n log n)",
                "space_complexity": "O(1) auxiliary space when sorting in place"
            }
        ],

        "interview_questions": [
            {
                "question": "What is a Greedy Algorithm?",
                "answer": "An algorithm that repeatedly makes a locally optimal choice to try to obtain a globally optimal solution."
            },
            {
                "question": "What is the Greedy Choice Property?",
                "answer": "It means a globally optimal solution can be reached by making locally optimal choices."
            },
            {
                "question": "What is Optimal Substructure?",
                "answer": "A problem has optimal substructure when an optimal solution can be built from optimal solutions to its smaller subproblems."
            },
            {
                "question": "Does Greedy always produce an optimal solution?",
                "answer": "No. A greedy strategy works only when the problem has the required properties and the chosen greedy rule is correct."
            },
            {
                "question": "What is the difference between Greedy and Dynamic Programming?",
                "answer": "Greedy commits to a locally optimal choice, while Dynamic Programming compares and combines solutions to subproblems."
            },
            {
                "question": "What is the Activity Selection problem?",
                "answer": "It asks for the maximum number of mutually compatible activities. Sorting by finishing time gives a greedy solution."
            },
            {
                "question": "Why do we sort activities by finish time?",
                "answer": "Choosing the activity that finishes earliest leaves as much time as possible for the remaining activities."
            },
            {
                "question": "What is Fractional Knapsack?",
                "answer": "A knapsack optimization problem where fractions of items are allowed. Sorting by value-to-weight ratio gives an optimal greedy solution."
            },
            {
                "question": "Does the greedy approach solve 0/1 Knapsack optimally?",
                "answer": "No. The standard value-to-weight greedy strategy is not guaranteed to solve 0/1 Knapsack optimally."
            },
            {
                "question": "What is Job Sequencing with Deadlines?",
                "answer": "A problem where jobs have deadlines and profits, and we schedule jobs to maximize profit while meeting deadlines."
            },
            {
                "question": "What is Huffman Coding?",
                "answer": "A greedy compression algorithm that repeatedly combines the two least frequent symbols to build an optimal prefix code."
            },
            {
                "question": "Why is the standard coin-change greedy method not always correct?",
                "answer": "Arbitrary coin denominations may require a combination of smaller coins that is better than choosing the largest coin first."
            },
            {
                "question": "Which data structures are commonly used in Greedy Algorithms?",
                "answer": "Sorting, arrays, priority queues, heaps, and sets are commonly used depending on the problem."
            },
            {
                "question": "What is the time complexity of Activity Selection?",
                "answer": "O(n log n) when sorting is required, followed by an O(n) scan."
            },
            {
                "question": "Give examples of Greedy Algorithms.",
                "answer": "Activity Selection, Fractional Knapsack, Huffman Coding, Job Sequencing, and Minimum Spanning Tree algorithms such as Kruskal's and Prim's."
            }
        ],

        "mcqs": [
            {
                "question": "A Greedy Algorithm makes which type of choice?",
                "options": [
                    "Locally optimal choice",
                    "Random choice",
                    "Always maximum choice",
                    "Always minimum choice"
                ],
                "answer": "Locally optimal choice",
                "explanation": "A greedy algorithm chooses the best available option at the current step according to its strategy."
            },
            {
                "question": "Which property means a global optimum can be built using local greedy choices?",
                "options": [
                    "Greedy Choice Property",
                    "Binary Search Property",
                    "Hashing Property",
                    "Recursion Property"
                ],
                "answer": "Greedy Choice Property",
                "explanation": "This property justifies the greedy decision."
            },
            {
                "question": "Which problem is optimally solved by the standard greedy ratio strategy?",
                "options": [
                    "0/1 Knapsack",
                    "Fractional Knapsack",
                    "Matrix Chain Multiplication",
                    "Longest Common Subsequence"
                ],
                "answer": "Fractional Knapsack",
                "explanation": "Fractions of items can be selected in descending value-to-weight ratio."
            },
            {
                "question": "For Activity Selection, activities are usually sorted by:",
                "options": [
                    "Starting time",
                    "Finishing time",
                    "Activity length only",
                    "Random order"
                ],
                "answer": "Finishing time",
                "explanation": "The earliest finishing activity leaves the most room for future activities."
            },
            {
                "question": "Does Greedy always give the optimal answer?",
                "options": ["Yes", "No", "Only for arrays", "Only for strings"],
                "answer": "No",
                "explanation": "The greedy choice must be proven correct for the particular problem."
            },
            {
                "question": "Which algorithm uses a greedy strategy to build prefix codes?",
                "options": ["Merge Sort", "Huffman Coding", "Binary Search", "DFS"],
                "answer": "Huffman Coding",
                "explanation": "Huffman Coding repeatedly combines the two least frequent nodes."
            },
            {
                "question": "The standard greedy strategy for Fractional Knapsack sorts items by:",
                "options": [
                    "Weight",
                    "Value",
                    "Value / Weight",
                    "Weight / Value"
                ],
                "answer": "Value / Weight",
                "explanation": "A higher value-to-weight ratio provides more value per unit of capacity."
            },
            {
                "question": "Which technique is more suitable when all relevant choices must be compared across overlapping subproblems?",
                "options": [
                    "Dynamic Programming",
                    "Simple Greedy",
                    "Linear Search",
                    "Binary Search"
                ],
                "answer": "Dynamic Programming",
                "explanation": "Dynamic Programming stores and combines solutions to subproblems."
            },
            {
                "question": "For coins [1, 3, 4] and amount 6, what does the largest-coin-first greedy method produce?",
                "options": [
                    "3 + 3",
                    "4 + 1 + 1",
                    "1 + 1 + 1 + 1 + 1 + 1",
                    "4 + 3"
                ],
                "answer": "4 + 1 + 1",
                "explanation": "The greedy method uses 3 coins, while the optimal solution uses 2 coins: 3 + 3."
            },
            {
                "question": "Which of these is a common application of Greedy Algorithms?",
                "options": [
                    "Activity Selection",
                    "Matrix Chain Multiplication",
                    "Floyd-Warshall",
                    "All of the above"
                ],
                "answer": "Activity Selection",
                "explanation": "Activity Selection is a classic greedy problem. Matrix Chain Multiplication and Floyd-Warshall are commonly solved using Dynamic Programming."
            }
        ]
    }
})


DSA_TRACK.update({
    "dsa-backtracking": {
        "title": "Backtracking Algorithms",
        "description": "Learn how to explore possible solutions, make decisions, and undo choices when they lead to invalid paths.",

        "content": """
# 1. What is Backtracking?

Backtracking is an algorithmic technique that solves problems by
building a solution step by step.

Whenever a choice leads to an invalid or unpromising state,
the algorithm goes back and tries another choice.

This process is called backtracking.

Think of solving a maze:
1. Move in one direction.
2. If you reach a dead end, go back.
3. Try another direction.
4. Continue until you reach the destination.

## 2. How Backtracking Works

A typical backtracking algorithm follows these steps:

1. Start with an empty or partial solution.
2. Check whether the current solution is complete.
3. If complete, record the solution.
4. Otherwise, try each possible choice.
5. Make a choice.
6. Explore recursively.
7. Undo the choice before trying another option.

The undo operation is also called restoring the state.

## 3. General Backtracking Template

function backtrack(state):
    if solution is complete:
        save solution
        return

    for each possible choice:
        if choice is valid:
            make choice
            backtrack(updated state)
            undo choice

## 4. Backtracking vs Recursion

Recursion is a programming technique where a function calls itself.

Backtracking is an algorithmic problem-solving technique that
often uses recursion to explore choices and undo them.

Not every recursive algorithm is backtracking.

## 5. Backtracking vs Brute Force

Brute force may generate every possible candidate and check it.

Backtracking can stop exploring a branch as soon as it knows
that the branch cannot produce a valid solution.

This is called pruning.

## 6. Common Backtracking Problems

- Generate all subsets.
- Generate all permutations.
- N-Queens problem.
- Sudoku Solver.
- Rat in a Maze.
- Combination Sum.
- Word Search.

## 7. Example: Generate All Subsets

For array [1, 2], possible subsets are:

[]
[1]
[2]
[1, 2]

For each element, we have two choices:
- Include the element.
- Exclude the element.

The algorithm explores both possibilities recursively.

## 8. Complexity

Backtracking often has exponential time complexity because
it explores combinations of choices.

For generating all subsets of n elements:
- Number of subsets = 2^n.
- Time complexity = O(n * 2^n) when copying each subset.
- Auxiliary recursion space = O(n), excluding stored answers.

The actual complexity depends on the problem and pruning strategy.
""",

        "key_concepts": [
            {
                "concept": "Backtracking",
                "explanation": "Explore a choice, recursively search its possibilities, and undo the choice when returning."
            },
            {
                "concept": "State Space Tree",
                "explanation": "A tree representing the different possible states and choices of a problem."
            },
            {
                "concept": "Pruning",
                "explanation": "Stop exploring a branch when it cannot lead to a valid or useful solution."
            },
            {
                "concept": "Base Case",
                "explanation": "The condition that identifies a complete solution or stops recursion."
            },
            {
                "concept": "Undo Choice",
                "explanation": "Restore the previous state after recursive exploration so another choice can be attempted."
            },
            {
                "concept": "Constraint Checking",
                "explanation": "Check whether a candidate choice satisfies the problem's rules before exploring it."
            }
        ],

        "examples": {
            "python": """# Generate all subsets using backtracking

def subsets(nums):
    result = []
    current = []

    def backtrack(index):
        if index == len(nums):
            result.append(current.copy())
            return

        # Choice 1: Include the current element
        current.append(nums[index])
        backtrack(index + 1)

        # Undo the choice
        current.pop()

        # Choice 2: Exclude the current element
        backtrack(index + 1)

    backtrack(0)
    return result


print(subsets([1, 2]))

# Output:
# [[1, 2], [1], [2], []]""",

            "java": """import java.util.*;

public class Main {
    static List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        List<Integer> current = new ArrayList<>();

        backtrack(0, nums, current, result);
        return result;
    }

    static void backtrack(int index, int[] nums,
                          List<Integer> current,
                          List<List<Integer>> result) {

        if (index == nums.length) {
            result.add(new ArrayList<>(current));
            return;
        }

        // Include current element
        current.add(nums[index]);
        backtrack(index + 1, nums, current, result);

        // Undo the choice
        current.remove(current.size() - 1);

        // Exclude current element
        backtrack(index + 1, nums, current, result);
    }

    public static void main(String[] args) {
        System.out.println(subsets(new int[]{1, 2}));
    }
}

// Output: [[1, 2], [1], [2], []]""",

            "cpp": """#include <iostream>
#include <vector>
using namespace std;

void backtrack(int index, vector<int>& nums,
               vector<int>& current,
               vector<vector<int>>& result) {

    if (index == nums.size()) {
        result.push_back(current);
        return;
    }

    // Include current element
    current.push_back(nums[index]);
    backtrack(index + 1, nums, current, result);

    // Undo the choice
    current.pop_back();

    // Exclude current element
    backtrack(index + 1, nums, current, result);
}

vector<vector<int>> subsets(vector<int>& nums) {
    vector<vector<int>> result;
    vector<int> current;

    backtrack(0, nums, current, result);
    return result;
}

int main() {
    vector<int> nums = {1, 2};
    vector<vector<int>> result = subsets(nums);

    for (auto subset : result) {
        cout << "[";
        for (int x : subset) cout << x << " ";
        cout << "] ";
    }

    return 0;
}

// Output: [1 2] [1] [2] []"""
        },

        "dry_run": [
            {
                "step": 1,
                "operation": "Start recursion",
                "current": "[]",
                "explanation": "Begin with an empty subset and index 0."
            },
            {
                "step": 2,
                "operation": "Include 1",
                "current": "[1]",
                "explanation": "Add the first element and move to index 1."
            },
            {
                "step": 3,
                "operation": "Include 2",
                "current": "[1, 2]",
                "explanation": "Add 2. All elements have been considered, so save the subset."
            },
            {
                "step": 4,
                "operation": "Undo 2 and exclude it",
                "current": "[1]",
                "explanation": "Remove 2 and explore the branch where it is excluded. Save [1]."
            },
            {
                "step": 5,
                "operation": "Undo 1",
                "current": "[]",
                "explanation": "Remove 1 so the algorithm can explore subsets that do not contain 1."
            },
            {
                "step": 6,
                "operation": "Explore remaining choices",
                "current": "[2] and []",
                "explanation": "Generate the remaining subsets by including or excluding 2."
            }
        ],

        "practice_questions": [
            {
                "title": "Generate All Subsets",
                "difficulty": "Medium",
                "problem": "Given an array of distinct integers, return all possible subsets (the power set).",
                "example": "Input: [1, 2]. Output: [[], [1], [2], [1, 2]]",
                "solution": {
                    "python": """def subsets(nums):
    result = []
    current = []

    def backtrack(index):
        if index == len(nums):
            result.append(current.copy())
            return

        current.append(nums[index])
        backtrack(index + 1)

        current.pop()
        backtrack(index + 1)

    backtrack(0)
    return result


print(subsets([1, 2]))""",
                    "java": """import java.util.*;

public static List<List<Integer>> subsets(int[] nums) {
    List<List<Integer>> result = new ArrayList<>();
    backtrack(0, nums, new ArrayList<>(), result);
    return result;
}

static void backtrack(int index, int[] nums,
                      List<Integer> current,
                      List<List<Integer>> result) {
    if (index == nums.length) {
        result.add(new ArrayList<>(current));
        return;
    }

    current.add(nums[index]);
    backtrack(index + 1, nums, current, result);

    current.remove(current.size() - 1);
    backtrack(index + 1, nums, current, result);
}""",
                    "cpp": """void backtrack(int index, vector<int>& nums,
               vector<int>& current,
               vector<vector<int>>& result) {
    if (index == nums.size()) {
        result.push_back(current);
        return;
    }

    current.push_back(nums[index]);
    backtrack(index + 1, nums, current, result);

    current.pop_back();
    backtrack(index + 1, nums, current, result);
}

vector<vector<int>> subsets(vector<int>& nums) {
    vector<vector<int>> result;
    vector<int> current;
    backtrack(0, nums, current, result);
    return result;
}"""
                },
                "explanation": "For every element, explore two possibilities: include it or exclude it. Copy the current subset whenever all elements have been considered.",
                "time_complexity": "O(n * 2^n)",
                "space_complexity": "O(n) auxiliary recursion space, excluding output"
            },
            {
                "title": "Generate All Permutations",
                "difficulty": "Medium",
                "problem": "Given an array of distinct integers, generate every possible ordering of its elements.",
                "example": "Input: [1, 2, 3]. Output contains 6 permutations.",
                "solution": {
                    "python": """def permutations(nums):
    result = []
    current = []
    used = [False] * len(nums)

    def backtrack():
        if len(current) == len(nums):
            result.append(current.copy())
            return

        for i in range(len(nums)):
            if used[i]:
                continue

            used[i] = True
            current.append(nums[i])

            backtrack()

            current.pop()
            used[i] = False

    backtrack()
    return result


print(permutations([1, 2, 3]))""",
                    "java": """import java.util.*;

public static List<List<Integer>> permutations(int[] nums) {
    List<List<Integer>> result = new ArrayList<>();
    boolean[] used = new boolean[nums.length];

    permute(nums, used, new ArrayList<>(), result);
    return result;
}

static void permute(int[] nums, boolean[] used,
                    List<Integer> current,
                    List<List<Integer>> result) {
    if (current.size() == nums.length) {
        result.add(new ArrayList<>(current));
        return;
    }

    for (int i = 0; i < nums.length; i++) {
        if (used[i]) continue;

        used[i] = true;
        current.add(nums[i]);

        permute(nums, used, current, result);

        current.remove(current.size() - 1);
        used[i] = false;
    }
}""",
                    "cpp": """void permute(vector<int>& nums, vector<bool>& used,
             vector<int>& current,
             vector<vector<int>>& result) {
    if (current.size() == nums.size()) {
        result.push_back(current);
        return;
    }

    for (int i = 0; i < nums.size(); i++) {
        if (used[i]) continue;

        used[i] = true;
        current.push_back(nums[i]);

        permute(nums, used, current, result);

        current.pop_back();
        used[i] = false;
    }
}

vector<vector<int>> permutations(vector<int>& nums) {
    vector<vector<int>> result;
    vector<bool> used(nums.size(), false);
    vector<int> current;

    permute(nums, used, current, result);
    return result;
}"""
                },
                "explanation": "At each position, choose one unused element. After exploring its branch, remove it and mark it unused so another permutation can be generated.",
                "time_complexity": "O(n * n!)",
                "space_complexity": "O(n) auxiliary space, excluding output"
            },
            {
                "title": "Combination Sum",
                "difficulty": "Medium",
                "problem": "Given an array of distinct positive integers and a target, return all unique combinations whose sum equals the target. Each number may be used unlimited times.",
                "example": "Input: candidates = [2, 3, 6, 7], target = 7. Output: [[2, 2, 3], [7]]",
                "solution": {
                    "python": """def combination_sum(candidates, target):
    result = []
    current = []

    def backtrack(start, remaining):
        if remaining == 0:
            result.append(current.copy())
            return

        for i in range(start, len(candidates)):
            value = candidates[i]

            if value > remaining:
                continue

            current.append(value)
            backtrack(i, remaining - value)
            current.pop()

    candidates.sort()
    backtrack(0, target)
    return result


print(combination_sum([2, 3, 6, 7], 7))""",
                    "java": """import java.util.*;

public static List<List<Integer>> combinationSum(int[] candidates, int target) {
    Arrays.sort(candidates);
    List<List<Integer>> result = new ArrayList<>();

    combinationBacktrack(0, target, candidates,
                         new ArrayList<>(), result);
    return result;
}

static void combinationBacktrack(int start, int remaining,
                                 int[] candidates,
                                 List<Integer> current,
                                 List<List<Integer>> result) {
    if (remaining == 0) {
        result.add(new ArrayList<>(current));
        return;
    }

    for (int i = start; i < candidates.length; i++) {
        if (candidates[i] > remaining) break;

        current.add(candidates[i]);
        combinationBacktrack(i, remaining - candidates[i],
                             candidates, current, result);
        current.remove(current.size() - 1);
    }
}""",
                    "cpp": """void combinationBacktrack(int start, int remaining,
                          vector<int>& candidates,
                          vector<int>& current,
                          vector<vector<int>>& result) {
    if (remaining == 0) {
        result.push_back(current);
        return;
    }

    for (int i = start; i < candidates.size(); i++) {
        if (candidates[i] > remaining) break;

        current.push_back(candidates[i]);

        combinationBacktrack(i, remaining - candidates[i],
                             candidates, current, result);

        current.pop_back();
    }
}

vector<vector<int>> combinationSum(vector<int>& candidates,
                                   int target) {
    sort(candidates.begin(), candidates.end());

    vector<vector<int>> result;
    vector<int> current;

    combinationBacktrack(0, target, candidates, current, result);
    return result;
}"""
                },
                "explanation": "Choose a candidate, subtract its value from the remaining target, and recurse using the same index because the number can be reused. Undo the choice before trying another candidate.",
                "time_complexity": "Exponential in the worst case; depends on the candidate values and target.",
                "space_complexity": "O(target / smallest candidate) recursion depth, excluding output"
            }
        ],

        "interview_questions": [
            {
                "question": "What is Backtracking?",
                "answer": "It is a problem-solving technique that explores possible choices and undoes a choice when it cannot lead to a valid solution."
            },
            {
                "question": "How is Backtracking related to Recursion?",
                "answer": "Backtracking commonly uses recursion to explore different choices, but it also restores the previous state after each recursive call."
            },
            {
                "question": "What is pruning?",
                "answer": "Pruning means stopping the exploration of a branch when it cannot produce a valid solution."
            },
            {
                "question": "What is a state space tree?",
                "answer": "A tree that represents all possible states or choices in a search problem."
            },
            {
                "question": "What is the role of the base case?",
                "answer": "It identifies when a solution is complete or when recursion should stop."
            },
            {
                "question": "Why do we undo a choice?",
                "answer": "To restore the original state so other possible choices can be explored independently."
            },
            {
                "question": "What is the difference between Backtracking and Brute Force?",
                "answer": "Brute force may examine all candidates, while backtracking can prune invalid or unpromising branches early."
            },
            {
                "question": "What is the time complexity of generating all subsets?",
                "answer": "There are 2^n subsets. Copying each subset can require O(n * 2^n) total time."
            },
            {
                "question": "How many permutations are possible for n distinct elements?",
                "answer": "n factorial, written as n!."
            },
            {
                "question": "What is the N-Queens problem?",
                "answer": "Place N queens on an N by N chessboard so that no two queens attack each other."
            },
            {
                "question": "Name some common Backtracking problems.",
                "answer": "N-Queens, Sudoku Solver, Rat in a Maze, permutations, subsets, and Combination Sum."
            },
            {
                "question": "Can Backtracking be implemented without recursion?",
                "answer": "Yes. An explicit stack can be used to simulate recursive exploration."
            },
            {
                "question": "What is the difference between a subset and a permutation?",
                "answer": "A subset selects elements without considering order, while a permutation considers different arrangements."
            },
            {
                "question": "What is the difference between Combination Sum and Permutations?",
                "answer": "Combination Sum searches for selections meeting a target condition, while permutations generate different orderings of elements."
            },
            {
                "question": "What is the auxiliary space complexity of subset generation?",
                "answer": "O(n) for the recursion stack and current subset, excluding the stored output."
            }
        ],

        "mcqs": [
            {
                "question": "Backtracking is mainly used to:",
                "options": [
                    "Explore choices and undo invalid choices",
                    "Sort an array only",
                    "Perform binary search only",
                    "Calculate hashes only"
                ],
                "answer": "Explore choices and undo invalid choices",
                "explanation": "Backtracking explores possible solution paths and restores state when returning."
            },
            {
                "question": "Which programming technique is commonly used to implement Backtracking?",
                "options": ["Recursion", "Binary Search", "Hashing", "Merge Sort"],
                "answer": "Recursion",
                "explanation": "Recursion naturally represents the repeated exploration of choices."
            },
            {
                "question": "What is pruning?",
                "options": [
                    "Stopping an invalid or unpromising branch",
                    "Sorting all branches",
                    "Repeating every choice",
                    "Deleting the input"
                ],
                "answer": "Stopping an invalid or unpromising branch",
                "explanation": "Pruning avoids unnecessary exploration."
            },
            {
                "question": "How many subsets can an array of 3 distinct elements have?",
                "options": ["3", "6", "8", "9"],
                "answer": "8",
                "explanation": "The number of subsets is 2^n, so 2^3 = 8."
            },
            {
                "question": "How many permutations can be formed from 3 distinct elements?",
                "options": ["3", "6", "8", "9"],
                "answer": "6",
                "explanation": "The number of permutations is 3! = 6."
            },
            {
                "question": "Which operation restores the previous state in subset backtracking?",
                "options": [
                    "Removing the last chosen element",
                    "Sorting the array",
                    "Reversing the array",
                    "Deleting the recursion function"
                ],
                "answer": "Removing the last chosen element",
                "explanation": "Undoing the choice lets another branch start from the correct state."
            },
            {
                "question": "Which is a classic Backtracking problem?",
                "options": ["N-Queens", "Binary Search", "Counting Sort", "Prefix Sum"],
                "answer": "N-Queens",
                "explanation": "N-Queens explores queen placements and rejects positions that violate constraints."
            },
            {
                "question": "What is the number of possible subsets of n elements?",
                "options": ["n!", "2^n", "n²", "n log n"],
                "answer": "2^n",
                "explanation": "Every element has two independent choices: include or exclude."
            },
            {
                "question": "What does a base case do in Backtracking?",
                "options": [
                    "Identifies a completed solution or stops recursion",
                    "Always sorts the choices",
                    "Always removes the first element",
                    "Creates a new input array"
                ],
                "answer": "Identifies a completed solution or stops recursion",
                "explanation": "The base case prevents recursion from continuing indefinitely."
            },
            {
                "question": "Which problem asks for all combinations that sum to a target?",
                "options": [
                    "Combination Sum",
                    "Binary Tree Traversal",
                    "Merge Intervals",
                    "Two Sum"
                ],
                "answer": "Combination Sum",
                "explanation": "Combination Sum uses backtracking to explore candidate combinations."
            }
        ]
    }
})


DSA_TRACK.update({
    "dsa-dynamic-programming": {
        "title": "Dynamic Programming (DP)",
        "description": "Learn memoization, tabulation, state transitions, and optimization techniques for problems with overlapping subproblems.",

        "content": """
# 1. What is Dynamic Programming?

Dynamic Programming (DP) is an algorithmic technique used to solve
complex problems by breaking them into smaller overlapping subproblems.

Instead of solving the same subproblem repeatedly, DP stores its
result and reuses it whenever needed.

This avoids unnecessary calculations.

## 2. Why do we need DP?

Consider the Fibonacci sequence:

F(0) = 0
F(1) = 1
F(n) = F(n-1) + F(n-2)

A simple recursive solution repeatedly calculates the same values.

For example:
F(5) requires F(4) and F(3).
F(4) also requires F(3) and F(2).

F(3) is calculated multiple times.

DP stores previously calculated results.

## 3. Two Important Properties of DP

### A. Overlapping Subproblems

A problem has overlapping subproblems when the same smaller
problems are solved multiple times.

DP saves their results to avoid repeated work.

### B. Optimal Substructure

A problem has optimal substructure when its optimal solution
can be constructed from optimal solutions to smaller subproblems.

These properties commonly indicate that DP may be useful.

## 4. Two Approaches to DP

### A. Memoization (Top-Down)

Memoization uses recursion and stores previously calculated results.

Steps:
1. Write a recursive solution.
2. Create a cache or DP array.
3. Check whether the answer is already stored.
4. If stored, return it.
5. Otherwise calculate, store, and return the answer.

### B. Tabulation (Bottom-Up)

Tabulation uses iteration and builds answers from smaller
subproblems.

Steps:
1. Initialize the base cases.
2. Create a DP array or table.
3. Calculate states in the correct order.
4. Return the final state.

## 5. Fibonacci Example

Recurrence:

dp[n] = dp[n-1] + dp[n-2]

Base cases:

dp[0] = 0
dp[1] = 1

For n = 5:

dp[0] = 0
dp[1] = 1
dp[2] = 1
dp[3] = 2
dp[4] = 3
dp[5] = 5

Answer = 5.

## 6. Space Optimization

If a state only depends on the previous two states, we do not
need to store the entire DP array.

We can maintain two variables:

previous2 = 0
previous1 = 1

Then calculate the next value using their sum.

This reduces auxiliary space from O(n) to O(1).

## 7. Steps to Solve a DP Problem

1. Define the state: What does dp[i] or dp[i][j] represent?
2. Identify the transition: How is the current state calculated?
3. Define base cases.
4. Decide memoization or tabulation.
5. Determine the correct calculation order.
6. Analyze time and space complexity.
7. Optimize space if possible.

## 8. Common DP Problems

- Fibonacci Number
- Climbing Stairs
- House Robber
- 0/1 Knapsack
- Coin Change
- Longest Common Subsequence
- Longest Increasing Subsequence
- Matrix Chain Multiplication
- Edit Distance
- Grid Unique Paths

## 9. DP vs Greedy

Greedy makes a locally optimal choice and generally does not
reconsider it.

DP compares solutions to subproblems and combines them.

Greedy is usually simpler, but it is not correct for every
optimization problem. DP can solve problems where multiple
choices must be considered.

## 10. When should you think about DP?

Look for:
- Maximum or minimum possible value.
- Number of ways to achieve something.
- Can a target be achieved?
- Longest or shortest subsequence.
- Repeated recursive calculations.
- Decisions that affect future choices.
""",

        "key_concepts": [
            {
                "concept": "Dynamic Programming",
                "explanation": "A technique that stores results of overlapping subproblems and reuses them."
            },
            {
                "concept": "Overlapping Subproblems",
                "explanation": "The same smaller problem is solved repeatedly in a recursive solution."
            },
            {
                "concept": "Optimal Substructure",
                "explanation": "An optimal solution can be constructed from optimal solutions to smaller subproblems."
            },
            {
                "concept": "Memoization",
                "explanation": "A top-down approach using recursion and caching."
            },
            {
                "concept": "Tabulation",
                "explanation": "A bottom-up approach that calculates DP states iteratively."
            },
            {
                "concept": "DP State",
                "explanation": "A definition of what a DP entry represents, such as dp[i] being the number of ways to reach step i."
            },
            {
                "concept": "State Transition",
                "explanation": "The recurrence relation used to calculate one DP state from previously solved states."
            },
            {
                "concept": "Base Case",
                "explanation": "The smallest states whose answers are known directly."
            },
            {
                "concept": "Space Optimization",
                "explanation": "Reducing memory usage by keeping only the previous states needed for the next calculation."
            }
        ],

        "examples": {
            "python": """# Fibonacci using Memoization

def fibonacci(n, memo=None):
    if memo is None:
        memo = {}

    if n <= 1:
        return n

    if n in memo:
        return memo[n]

    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)

    return memo[n]


print(fibonacci(5))


# Fibonacci using Tabulation

def fibonacci_tabulation(n):
    if n <= 1:
        return n

    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


print(fibonacci_tabulation(5))


# Output:
# 5
# 5""",

            "java": """public class Main {

    // Memoization
    static int fibonacci(int n, int[] memo) {
        if (n <= 1) return n;

        if (memo[n] != -1) {
            return memo[n];
        }

        memo[n] = fibonacci(n - 1, memo)
                + fibonacci(n - 2, memo);

        return memo[n];
    }

    // Tabulation
    static int fibonacciTabulation(int n) {
        if (n <= 1) return n;

        int[] dp = new int[n + 1];

        dp[0] = 0;
        dp[1] = 1;

        for (int i = 2; i <= n; i++) {
            dp[i] = dp[i - 1] + dp[i - 2];
        }

        return dp[n];
    }

    public static void main(String[] args) {
        int n = 5;

        int[] memo = new int[n + 1];
        java.util.Arrays.fill(memo, -1);

        System.out.println(fibonacci(n, memo));
        System.out.println(fibonacciTabulation(n));
    }
}

// Output:
// 5
// 5""",

            "cpp": """#include <iostream>
#include <vector>
using namespace std;

// Memoization
int fibonacci(int n, vector<int>& memo) {
    if (n <= 1) return n;

    if (memo[n] != -1) {
        return memo[n];
    }

    memo[n] = fibonacci(n - 1, memo)
            + fibonacci(n - 2, memo);

    return memo[n];
}

// Tabulation
int fibonacciTabulation(int n) {
    if (n <= 1) return n;

    vector<int> dp(n + 1);

    dp[0] = 0;
    dp[1] = 1;

    for (int i = 2; i <= n; i++) {
        dp[i] = dp[i - 1] + dp[i - 2];
    }

    return dp[n];
}

int main() {
    int n = 5;

    vector<int> memo(n + 1, -1);

    cout << fibonacci(n, memo) << endl;
    cout << fibonacciTabulation(n);

    return 0;
}

// Output:
// 5
// 5"""
        },

        "dry_run": [
            {
                "step": 1,
                "operation": "Initialize base cases",
                "dp": "[0, 1, _, _, _, _]",
                "explanation": "The first two Fibonacci values are 0 and 1."
            },
            {
                "step": 2,
                "operation": "Calculate dp[2]",
                "dp": "[0, 1, 1, _, _, _]",
                "explanation": "dp[2] = dp[1] + dp[0] = 1."
            },
            {
                "step": 3,
                "operation": "Calculate dp[3]",
                "dp": "[0, 1, 1, 2, _, _]",
                "explanation": "dp[3] = dp[2] + dp[1] = 2."
            },
            {
                "step": 4,
                "operation": "Calculate dp[4]",
                "dp": "[0, 1, 1, 2, 3, _]",
                "explanation": "dp[4] = dp[3] + dp[2] = 3."
            },
            {
                "step": 5,
                "operation": "Calculate dp[5]",
                "dp": "[0, 1, 1, 2, 3, 5]",
                "explanation": "dp[5] = dp[4] + dp[3] = 5. The final answer is 5."
            }
        ],

        "practice_questions": [
            {
                "title": "Climbing Stairs",
                "difficulty": "Easy",
                "problem": "You are climbing a staircase with n steps. You can climb either 1 or 2 steps at a time. Find the number of distinct ways to reach the top.",
                "example": "Input: n = 3. Output: 3. Ways: 1+1+1, 1+2, 2+1.",
                "solution": {
                    "python": """def climb_stairs(n):
    if n <= 2:
        return n

    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


print(climb_stairs(3))""",
                    "java": """public static int climbStairs(int n) {
    if (n <= 2) return n;

    int[] dp = new int[n + 1];
    dp[1] = 1;
    dp[2] = 2;

    for (int i = 3; i <= n; i++) {
        dp[i] = dp[i - 1] + dp[i - 2];
    }

    return dp[n];
}""",
                    "cpp": """int climbStairs(int n) {
    if (n <= 2) return n;

    vector<int> dp(n + 1);
    dp[1] = 1;
    dp[2] = 2;

    for (int i = 3; i <= n; i++) {
        dp[i] = dp[i - 1] + dp[i - 2];
    }

    return dp[n];
}"""
                },
                "explanation": "To reach step i, you must come from step i-1 or i-2. Therefore dp[i] = dp[i-1] + dp[i-2].",
                "time_complexity": "O(n)",
                "space_complexity": "O(n), reducible to O(1)"
            },
            {
                "title": "House Robber",
                "difficulty": "Medium",
                "problem": "You are given an array where each value represents money in a house. You cannot rob two adjacent houses. Find the maximum amount you can rob.",
                "example": "Input: [2, 7, 9, 3, 1]. Output: 12. Rob houses containing 2, 9, and 1.",
                "solution": {
                    "python": """def rob(nums):
    previous_two = 0
    previous_one = 0

    for money in nums:
        current = max(previous_one, previous_two + money)

        previous_two = previous_one
        previous_one = current

    return previous_one


print(rob([2, 7, 9, 3, 1]))""",
                    "java": """public static int rob(int[] nums) {
    int previousTwo = 0;
    int previousOne = 0;

    for (int money : nums) {
        int current = Math.max(previousOne, previousTwo + money);

        previousTwo = previousOne;
        previousOne = current;
    }

    return previousOne;
}""",
                    "cpp": """int rob(vector<int>& nums) {
    int previousTwo = 0;
    int previousOne = 0;

    for (int money : nums) {
        int current = max(previousOne, previousTwo + money);

        previousTwo = previousOne;
        previousOne = current;
    }

    return previousOne;
}"""
                },
                "explanation": "For every house, choose between skipping it and taking its money plus the best result from two houses earlier. Maintain only the previous two results.",
                "time_complexity": "O(n)",
                "space_complexity": "O(1)"
            },
            {
                "title": "Coin Change",
                "difficulty": "Medium",
                "problem": "Given coin denominations and an amount, return the minimum number of coins needed to make that amount. Return -1 if it is impossible. Each coin can be used unlimited times.",
                "example": "Input: coins = [1, 2, 5], amount = 11. Output: 3. Use 5 + 5 + 1.",
                "solution": {
                    "python": """def coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for value in range(1, amount + 1):
        for coin in coins:
            if coin <= value:
                dp[value] = min(
                    dp[value],
                    dp[value - coin] + 1
                )

    return -1 if dp[amount] == float('inf') else dp[amount]


print(coin_change([1, 2, 5], 11))""",
                    "java": """import java.util.*;

public static int coinChange(int[] coins, int amount) {
    int[] dp = new int[amount + 1];
    Arrays.fill(dp, amount + 1);
    dp[0] = 0;

    for (int value = 1; value <= amount; value++) {
        for (int coin : coins) {
            if (coin <= value) {
                dp[value] = Math.min(
                    dp[value],
                    dp[value - coin] + 1
                );
            }
        }
    }

    return dp[amount] > amount ? -1 : dp[amount];
}""",
                    "cpp": """int coinChange(vector<int>& coins, int amount) {
    vector<int> dp(amount + 1, amount + 1);
    dp[0] = 0;

    for (int value = 1; value <= amount; value++) {
        for (int coin : coins) {
            if (coin <= value) {
                dp[value] = min(
                    dp[value],
                    dp[value - coin] + 1
                );
            }
        }
    }

    return dp[amount] > amount ? -1 : dp[amount];
}"""
                },
                "explanation": "Define dp[value] as the minimum coins needed to make that value. Try every coin and use the best result for value - coin.",
                "time_complexity": "O(amount * number of coin denominations)",
                "space_complexity": "O(amount)"
            }
        ],

        "interview_questions": [
            {
                "question": "What is Dynamic Programming?",
                "answer": "A technique that solves problems by storing results of overlapping subproblems and reusing them."
            },
            {
                "question": "What are the two important properties of DP?",
                "answer": "Overlapping subproblems and optimal substructure."
            },
            {
                "question": "What is memoization?",
                "answer": "A top-down DP approach that uses recursion and caching."
            },
            {
                "question": "What is tabulation?",
                "answer": "A bottom-up DP approach that calculates states iteratively."
            },
            {
                "question": "What is the difference between memoization and tabulation?",
                "answer": "Memoization starts from the requested state and recursively calculates dependencies. Tabulation starts from base cases and builds toward the required answer."
            },
            {
                "question": "What is a DP state?",
                "answer": "A definition of what a DP array or table entry represents."
            },
            {
                "question": "What is a state transition?",
                "answer": "A recurrence relation that explains how to calculate a state from other states."
            },
            {
                "question": "What is the time complexity of Fibonacci using naive recursion?",
                "answer": "O(2^n) as a common upper-bound description of the recursive work."
            },
            {
                "question": "What is the time complexity of Fibonacci using tabulation?",
                "answer": "O(n), because each state is calculated once."
            },
            {
                "question": "How can Fibonacci space complexity be optimized?",
                "answer": "Maintain only the previous two Fibonacci values, reducing auxiliary space to O(1)."
            },
            {
                "question": "Does every recursive problem require DP?",
                "answer": "No. DP is especially useful when subproblems overlap and storing their results avoids repeated work."
            },
            {
                "question": "What is the difference between Greedy and DP?",
                "answer": "Greedy commits to a local choice, while DP combines results from multiple relevant subproblems."
            },
            {
                "question": "What is the 0/1 Knapsack problem?",
                "answer": "Choose items with given weights and values to maximize value within a capacity, taking each item either completely or not at all."
            },
            {
                "question": "What is the Longest Common Subsequence problem?",
                "answer": "Find the longest sequence that appears in two strings in the same relative order, not necessarily contiguously."
            },
            {
                "question": "How do you approach an unfamiliar DP problem?",
                "answer": "Define the state, identify transitions, establish base cases, select memoization or tabulation, determine complexity, and look for space optimization."
            }
        ],

        "mcqs": [
            {
                "question": "Which two properties are commonly associated with Dynamic Programming?",
                "options": [
                    "Overlapping subproblems and optimal substructure",
                    "Sorting and searching",
                    "Hashing and collision",
                    "Stack and queue"
                ],
                "answer": "Overlapping subproblems and optimal substructure",
                "explanation": "These properties indicate that DP may help avoid repeated work and build optimal solutions."
            },
            {
                "question": "Memoization is which approach?",
                "options": [
                    "Top-Down",
                    "Bottom-Up",
                    "Greedy",
                    "Divide and Conquer without caching"
                ],
                "answer": "Top-Down",
                "explanation": "Memoization begins with a requested state and recursively solves its dependencies."
            },
            {
                "question": "Tabulation is which approach?",
                "options": [
                    "Top-Down",
                    "Bottom-Up",
                    "Randomized",
                    "Backtracking only"
                ],
                "answer": "Bottom-Up",
                "explanation": "Tabulation starts with base cases and builds larger states iteratively."
            },
            {
                "question": "What is the time complexity of Fibonacci using tabulation?",
                "options": ["O(1)", "O(log n)", "O(n)", "O(2^n)"],
                "answer": "O(n)",
                "explanation": "Each Fibonacci state is calculated once."
            },
            {
                "question": "What is the value of Fibonacci(5) when F(0)=0 and F(1)=1?",
                "options": ["3", "5", "8", "13"],
                "answer": "5",
                "explanation": "The sequence is 0, 1, 1, 2, 3, 5."
            },
            {
                "question": "What does dp[i] represent?",
                "options": [
                    "A problem-specific state",
                    "Always an array index",
                    "Always the maximum value",
                    "Always the minimum value"
                ],
                "answer": "A problem-specific state",
                "explanation": "The meaning of a DP state must be defined for each problem."
            },
            {
                "question": "Which problem is a classic DP problem?",
                "options": [
                    "Coin Change",
                    "Linear Search",
                    "Selection Sort",
                    "Printing an array"
                ],
                "answer": "Coin Change",
                "explanation": "Coin Change can be solved by storing the best answer for smaller amounts."
            },
            {
                "question": "Which technique can reduce Fibonacci's auxiliary space to O(1)?",
                "options": [
                    "Store only the previous two values",
                    "Use a two-dimensional table",
                    "Sort the sequence",
                    "Use a hash set of all values"
                ],
                "answer": "Store only the previous two values",
                "explanation": "The next Fibonacci value depends only on the previous two."
            },
            {
                "question": "What is a state transition?",
                "options": [
                    "A formula relating DP states",
                    "A sorting operation",
                    "A database transaction",
                    "A function call only"
                ],
                "answer": "A formula relating DP states",
                "explanation": "The transition explains how the answer for one state is derived from other states."
            },
            {
                "question": "Which of the following is not a typical DP problem?",
                "options": [
                    "Longest Common Subsequence",
                    "0/1 Knapsack",
                    "Coin Change",
                    "Binary Search in a sorted array"
                ],
                "answer": "Binary Search in a sorted array",
                "explanation": "Binary Search is generally solved using divide and conquer, not Dynamic Programming."
            }
        ]
    }
})


DSA_TRACK.update({
    "dsa-bit-manipulation": {
        "title": "Bit Manipulation",
        "subtitle": "Solve problems efficiently using binary operations",
        "content": """
# 1. What is Bit Manipulation?

Bit manipulation is a technique used to perform operations directly on the binary representation of numbers.

Computers represent integers using bits:
- 0 represents an off bit.
- 1 represents an on bit.

For example, decimal number 5 is represented as 101 in binary.

Bit manipulation is useful in:
- Optimizing algorithms.
- Checking whether a number is even or odd.
- Finding unique elements.
- Managing sets of flags.
- Solving competitive programming problems.

# 2. Binary Number System

The binary number system uses only two digits: 0 and 1.

Each position represents a power of 2.

Example:
Binary 1011

= (1 × 8) + (0 × 4) + (1 × 2) + (1 × 1)
= 11

Therefore, binary 1011 represents decimal 11.

# 3. Bitwise Operators

## AND (&)

A bit becomes 1 only when both corresponding bits are 1.

Example:
  5 = 0101
  3 = 0011
5 & 3 = 0001 = 1

## OR (|)

A bit becomes 1 when at least one corresponding bit is 1.

5 | 3 = 0111 = 7

## XOR (^)

A bit becomes 1 when the corresponding bits are different.

5 ^ 3 = 0110 = 6

Important XOR properties:
- a ^ a = 0
- a ^ 0 = a
- a ^ b = b ^ a
- (a ^ b) ^ c = a ^ (b ^ c)

## NOT (~)

Flips every bit.

In Python, ~5 evaluates to -6 because Python uses signed integer representation with an effectively unlimited number of bits.

## Left Shift (<<)

Shifts bits to the left.

Example:
5 << 1

0101 becomes 1010

Result = 10

For non-negative integers, shifting left by k positions is equivalent to multiplying by 2^k, provided the result fits the relevant integer representation.

## Right Shift (>>)

Shifts bits to the right.

Example:
10 >> 1

1010 becomes 0101

Result = 5

For non-negative integers, shifting right by k positions is equivalent to integer division by 2^k.

# 4. Important Bit Manipulation Techniques

## Check whether a number is even or odd

Use n & 1.

If the result is 1, the number is odd.
If the result is 0, the number is even.

## Check whether the kth bit is set

Use:

(n & (1 << k)) != 0

Bit positions are counted from 0, starting from the rightmost bit.

## Set the kth bit

Use:

n | (1 << k)

## Clear the kth bit

Use:

n & ~(1 << k)

## Toggle the kth bit

Use:

n ^ (1 << k)

## Check whether a number is a power of two

A positive power of two contains exactly one set bit.

Use:

n > 0 and (n & (n - 1)) == 0

Examples:
1, 2, 4, 8, 16 are powers of two.

6 is not a power of two.

## Remove the rightmost set bit

Use:

n & (n - 1)

Example:
12 = 1100
11 = 1011

12 & 11 = 1000 = 8

# 5. Counting Set Bits

A set bit is a bit whose value is 1.

Example:
Binary 1011 contains three set bits.

Brian Kernighan's algorithm:

Repeatedly execute:

n = n & (n - 1)

Each operation removes one set bit.

The algorithm runs in O(number of set bits) time.

# 6. Common Interview Applications

1. Find the number that appears once when every other number appears twice.
2. Check whether a number is a power of two.
3. Count set bits.
4. Find the missing number using XOR.
5. Generate subsets using bitmasks.
6. Use bits to represent multiple boolean states.

# 7. Complexity

Most individual bitwise operations take O(1) time on fixed-width machine integers.

Counting set bits using Brian Kernighan's algorithm takes O(k), where k is the number of set bits.

Space complexity is generally O(1) for these basic operations.
""",

        "key_concepts": [
            {
                "name": "AND (&)",
                "description": "Sets a bit to 1 only if both corresponding bits are 1."
            },
            {
                "name": "OR (|)",
                "description": "Sets a bit to 1 if either corresponding bit is 1."
            },
            {
                "name": "XOR (^)",
                "description": "Sets a bit to 1 when corresponding bits are different."
            },
            {
                "name": "Left Shift (<<)",
                "description": "Moves bits toward higher positions."
            },
            {
                "name": "Right Shift (>>)",
                "description": "Moves bits toward lower positions."
            },
            {
                "name": "Set Bit",
                "description": "Changes a selected bit to 1 using OR."
            },
            {
                "name": "Clear Bit",
                "description": "Changes a selected bit to 0 using AND and NOT."
            },
            {
                "name": "Toggle Bit",
                "description": "Changes a selected bit from 0 to 1 or 1 to 0 using XOR."
            },
            {
                "name": "Bitmask",
                "description": "Uses individual bits to represent multiple boolean values."
            }
        ],

        "examples": {
            "python": {
                "title": "Bitwise Operators in Python",
                "code": """a = 5
b = 3

print("AND:", a & b)
print("OR:", a | b)
print("XOR:", a ^ b)
print("Left shift:", a << 1)
print("Right shift:", a >> 1)

n = 12
print("Is even:", (n & 1) == 0)

# Check whether n is a power of two
n = 16
print("Power of two:", n > 0 and (n & (n - 1)) == 0)

# Count set bits
n = 11
count = 0

while n:
    n = n & (n - 1)
    count += 1

print("Set bits:", count)""",
                "output": """AND: 1
OR: 7
XOR: 6
Left shift: 10
Right shift: 2
Is even: True
Power of two: True
Set bits: 3"""
            },
            "java": {
                "title": "Bitwise Operators in Java",
                "code": """public class Main {
    public static void main(String[] args) {
        int a = 5;
        int b = 3;

        System.out.println("AND: " + (a & b));
        System.out.println("OR: " + (a | b));
        System.out.println("XOR: " + (a ^ b));
        System.out.println("Left shift: " + (a << 1));
        System.out.println("Right shift: " + (a >> 1));

        int n = 16;

        boolean powerOfTwo =
            n > 0 && (n & (n - 1)) == 0;

        System.out.println("Power of two: " + powerOfTwo);

        n = 11;
        int count = 0;

        while (n != 0) {
            n = n & (n - 1);
            count++;
        }

        System.out.println("Set bits: " + count);
    }
}""",
                "output": """AND: 1
OR: 7
XOR: 6
Left shift: 10
Right shift: 2
Power of two: true
Set bits: 3"""
            },
            "cpp": {
                "title": "Bitwise Operators in C++",
                "code": """#include <iostream>
using namespace std;

int main() {
    int a = 5;
    int b = 3;

    cout << "AND: " << (a & b) << endl;
    cout << "OR: " << (a | b) << endl;
    cout << "XOR: " << (a ^ b) << endl;
    cout << "Left shift: " << (a << 1) << endl;
    cout << "Right shift: " << (a >> 1) << endl;

    int n = 16;

    bool powerOfTwo =
        n > 0 && (n & (n - 1)) == 0;

    cout << "Power of two: " << powerOfTwo << endl;

    n = 11;
    int count = 0;

    while (n != 0) {
        n = n & (n - 1);
        count++;
    }

    cout << "Set bits: " << count << endl;

    return 0;
}""",
                "output": """AND: 1
OR: 7
XOR: 6
Left shift: 10
Right shift: 2
Power of two: 1
Set bits: 3"""
            }
        },

        "dry_run": {
            "title": "Dry Run: Count Set Bits",
            "code": "n = 11",
            "steps": [
                {
                    "step": 1,
                    "value": "11 = 1011",
                    "explanation": "The number 11 has three set bits."
                },
                {
                    "step": 2,
                    "value": "1011 & 1010 = 1010",
                    "explanation": "Remove the rightmost set bit. Count becomes 1."
                },
                {
                    "step": 3,
                    "value": "1010 & 1001 = 1000",
                    "explanation": "Remove another set bit. Count becomes 2."
                },
                {
                    "step": 4,
                    "value": "1000 & 0111 = 0000",
                    "explanation": "Remove the final set bit. Count becomes 3."
                },
                {
                    "step": 5,
                    "value": "n = 0",
                    "explanation": "The loop ends. The answer is 3."
                }
            ],
            "result": "Number of set bits = 3"
        },

        "practice_questions": [
            {
                "question": "Check whether a number is odd or even using bit manipulation.",
                "difficulty": "Easy",
                "hint": "Check the rightmost bit using n & 1.",
                "solution": {
                    "python": """n = 17
if n & 1:
    print("Odd")
else:
    print("Even")""",
                    "java": """public class Main {
    public static void main(String[] args) {
        int n = 17;

        if ((n & 1) == 1) {
            System.out.println("Odd");
        } else {
            System.out.println("Even");
        }
    }
}""",
                    "cpp": """#include <iostream>
using namespace std;

int main() {
    int n = 17;

    if (n & 1)
        cout << "Odd";
    else
        cout << "Even";

    return 0;
}"""
                },
                "expected_output": "Odd",
                "explanation": "The rightmost bit of an odd number is always 1."
            },
            {
                "question": "Given an integer n, count the number of set bits in its binary representation.",
                "difficulty": "Easy",
                "hint": "Use n & (n - 1) to remove one set bit in every iteration.",
                "solution": {
                    "python": """def count_bits(n):
    count = 0

    while n:
        n = n & (n - 1)
        count += 1

    return count

print(count_bits(13))""",
                    "java": """public class Main {
    static int countBits(int n) {
        int count = 0;

        while (n != 0) {
            n = n & (n - 1);
            count++;
        }

        return count;
    }

    public static void main(String[] args) {
        System.out.println(countBits(13));
    }
}""",
                    "cpp": """#include <iostream>
using namespace std;

int countBits(int n) {
    int count = 0;

    while (n != 0) {
        n = n & (n - 1);
        count++;
    }

    return count;
}

int main() {
    cout << countBits(13);
    return 0;
}"""
                },
                "expected_output": "3",
                "explanation": "13 in binary is 1101, which contains three set bits."
            },
            {
                "question": "Given an array where every element appears twice except one element, find the unique element.",
                "difficulty": "Medium",
                "hint": "XOR of two equal numbers is zero. XOR of a number with zero is the number itself.",
                "solution": {
                    "python": """def single_number(nums):
    answer = 0

    for num in nums:
        answer ^= num

    return answer

print(single_number([4, 1, 2, 1, 2]))""",
                    "java": """public class Main {
    static int singleNumber(int[] nums) {
        int answer = 0;

        for (int num : nums) {
            answer ^= num;
        }

        return answer;
    }

    public static void main(String[] args) {
        int[] nums = {4, 1, 2, 1, 2};
        System.out.println(singleNumber(nums));
    }
}""",
                    "cpp": """#include <iostream>
using namespace std;

int singleNumber(int nums[], int size) {
    int answer = 0;

    for (int i = 0; i < size; i++) {
        answer ^= nums[i];
    }

    return answer;
}

int main() {
    int nums[] = {4, 1, 2, 1, 2};
    cout << singleNumber(nums, 5);
    return 0;
}"""
                },
                "expected_output": "4",
                "explanation": "The duplicate values cancel each other because a ^ a = 0. Only 4 remains.",
                "complexity": "O(n) time and O(1) auxiliary space."
            }
        ],

        "interview_questions": [
            {
                "question": "What is bit manipulation?",
                "answer": "It is a technique that directly operates on the binary bits of integers using operators such as AND, OR, XOR, NOT and shifts."
            },
            {
                "question": "What is the difference between AND and OR?",
                "answer": "AND returns 1 only when both bits are 1. OR returns 1 when at least one bit is 1."
            },
            {
                "question": "What is XOR?",
                "answer": "XOR returns 1 when two corresponding bits are different and 0 when they are equal."
            },
            {
                "question": "Why is XOR useful for finding a unique number?",
                "answer": "Because equal numbers cancel out using a ^ a = 0, leaving the unique number."
            },
            {
                "question": "How do you check whether a number is odd using bits?",
                "answer": "Use n & 1. A result of 1 means odd; a result of 0 means even."
            },
            {
                "question": "How do you check whether a number is a power of two?",
                "answer": "For a positive integer n, check n > 0 and (n & (n - 1)) == 0."
            },
            {
                "question": "What does n & (n - 1) do?",
                "answer": "It removes the rightmost set bit from a non-negative integer."
            },
            {
                "question": "What is a set bit?",
                "answer": "A bit whose binary value is 1."
            },
            {
                "question": "What is a bitmask?",
                "answer": "A number whose bits represent multiple boolean states or selections."
            },
            {
                "question": "How do you set the kth bit?",
                "answer": "Use n | (1 << k), where bit positions start at zero from the right."
            },
            {
                "question": "How do you clear the kth bit?",
                "answer": "Use n & ~(1 << k)."
            },
            {
                "question": "How do you toggle the kth bit?",
                "answer": "Use n ^ (1 << k)."
            },
            {
                "question": "What is Brian Kernighan's algorithm?",
                "answer": "It counts set bits by repeatedly removing the rightmost set bit using n & (n - 1)."
            },
            {
                "question": "What is the time complexity of counting set bits using Brian Kernighan's algorithm?",
                "answer": "O(k), where k is the number of set bits. In the worst case for a fixed-width integer, this is O(number of bits)."
            },
            {
                "question": "How can bitmasks be used to generate subsets?",
                "answer": "For an array of n elements, each integer from 0 to 2^n - 1 represents a subset. A set bit indicates that the corresponding element is selected."
            }
        ],

        "mcqs": [
            {
                "question": "What is the result of 5 & 3?",
                "options": ["1", "2", "7", "6"],
                "answer": "1",
                "explanation": "0101 & 0011 = 0001."
            },
            {
                "question": "What is the result of 5 | 3?",
                "options": ["1", "6", "7", "8"],
                "answer": "7",
                "explanation": "0101 | 0011 = 0111."
            },
            {
                "question": "What is the result of 5 ^ 3?",
                "options": ["1", "6", "7", "8"],
                "answer": "6",
                "explanation": "0101 ^ 0011 = 0110."
            },
            {
                "question": "Which expression checks whether n is odd?",
                "options": ["n % 2 == 0", "n & 1", "n | 1", "n ^ 1"],
                "answer": "n & 1",
                "explanation": "The rightmost bit is 1 for odd numbers."
            },
            {
                "question": "Which expression checks whether a positive integer is a power of two?",
                "options": ["n & (n + 1)", "n | (n - 1)", "n & (n - 1) == 0", "n ^ (n - 1)"],
                "answer": "n & (n - 1) == 0",
                "explanation": "A power of two has exactly one set bit. Also ensure n > 0."
            },
            {
                "question": "What is 4 << 1?",
                "options": ["2", "4", "8", "16"],
                "answer": "8",
                "explanation": "Left shifting by one multiplies a non-negative integer by two."
            },
            {
                "question": "What is 16 >> 2?",
                "options": ["2", "4", "8", "16"],
                "answer": "4",
                "explanation": "Right shifting by two divides 16 by four."
            },
            {
                "question": "What is the result of 7 & (7 - 1)?",
                "options": ["0", "1", "3", "7"],
                "answer": "6",
                "explanation": "0111 & 0110 = 0110. The rightmost set bit is removed."
            },
            {
                "question": "What is the XOR of a number with itself?",
                "options": ["The same number", "1", "0", "Undefined"],
                "answer": "0",
                "explanation": "a ^ a = 0."
            },
            {
                "question": "How many set bits are present in binary 1010?",
                "options": ["1", "2", "3", "4"],
                "answer": "2",
                "explanation": "The binary representation contains two 1s."
            }
        ]
    }
})


DSA_TRACK.update({
    "dsa-tries": {
        "title": "Tries (Prefix Trees)",
        "subtitle": "Efficient string storage, prefix searching and autocomplete",

        "content": """
# 1. What is a Trie?

A Trie (pronounced try) is a tree-based data structure used to store and search strings.

It is also called a Prefix Tree because strings with common prefixes share the same path.

Example words:
- cat
- car
- care
- dog

The words cat, car and care share the prefix "ca", so they share the same initial nodes.

Each node represents a character. A special end-of-word marker indicates that a complete word finishes at that node.

# 2. Structure of a Trie

A Trie node generally contains:

1. Children: references to child nodes.
2. is_end: indicates whether a complete word ends here.

For example, inserting "cat" creates a path:

root -> c -> a -> t

The node containing t is marked as the end of a word.

# 3. Main Trie Operations

## Insertion

To insert a word:
1. Start from the root.
2. Visit each character.
3. If the character's node does not exist, create it.
4. Move to that node.
5. Mark the last node as the end of a word.

## Search

To search for a complete word:
1. Start from the root.
2. Follow the characters one by one.
3. If a required character does not exist, return false.
4. After processing all characters, return true only if the final node marks the end of a word.

## Prefix Search

Prefix search checks whether any inserted word starts with a given prefix.

Unlike complete-word search, it does not require the final node to be marked as the end of a word.

# 4. Time and Space Complexity

Let L be the length of the input word.

Insertion: O(L)

Search: O(L)

Prefix search: O(L)

Space complexity: O(total characters stored), with additional node and child-reference overhead.

For a fixed alphabet, each node may have a fixed-size array of child references. A dictionary or map can be used when the character set is flexible.

# 5. Applications of Tries

1. Autocomplete suggestions.
2. Search engine query suggestions.
3. Dictionary implementation.
4. Spell checking.
5. Prefix-based searching.
6. Word games.
7. IP routing using binary tries.
8. Efficient storage of words with shared prefixes.

# 6. Trie vs HashMap

A HashMap can provide efficient exact-key lookup.

A Trie is especially useful when we need:
- Prefix searches.
- Autocomplete.
- Listing words with a common prefix.
- Character-by-character traversal.

A Trie may consume more memory because it stores nodes and links between characters.

# 7. Important Interview Points

- Every Trie starts with a root node.
- The root normally does not represent a character.
- A word can be a prefix of another word.
- The end-of-word marker distinguishes a complete word from a prefix.
- Multiple words can share nodes.
- Search and insertion depend on word length rather than the total number of stored words.
""",

        "key_concepts": [
            {
                "name": "Trie Node",
                "description": "A node containing character links and an end-of-word marker."
            },
            {
                "name": "Root Node",
                "description": "The starting node of a Trie, usually representing no character."
            },
            {
                "name": "Children",
                "description": "References to nodes representing the next characters."
            },
            {
                "name": "End of Word",
                "description": "A boolean marker indicating that a complete word ends at a node."
            },
            {
                "name": "Prefix Search",
                "description": "Checks whether one or more stored words begin with a given prefix."
            },
            {
                "name": "Autocomplete",
                "description": "Uses a prefix to find and suggest matching words."
            }
        ],

        "examples": {
            "python": {
                "title": "Trie Implementation in Python",
                "code": """class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()

            node = node.children[char]

        node.is_end = True

    def search(self, word):
        node = self.root

        for char in word:
            if char not in node.children:
                return False

            node = node.children[char]

        return node.is_end

    def starts_with(self, prefix):
        node = self.root

        for char in prefix:
            if char not in node.children:
                return False

            node = node.children[char]

        return True


trie = Trie()

trie.insert("cat")
trie.insert("car")
trie.insert("care")

print(trie.search("cat"))
print(trie.search("ca"))
print(trie.starts_with("ca"))
print(trie.starts_with("dog"))""",
                "output": """True
False
True
False"""
            },

            "java": {
                "title": "Trie Implementation in Java",
                "code": """import java.util.HashMap;
import java.util.Map;

class TrieNode {
    Map<Character, TrieNode> children = new HashMap<>();
    boolean isEnd = false;
}

class Trie {
    private TrieNode root = new TrieNode();

    public void insert(String word) {
        TrieNode node = root;

        for (char ch : word.toCharArray()) {
            node.children.putIfAbsent(ch, new TrieNode());
            node = node.children.get(ch);
        }

        node.isEnd = true;
    }

    public boolean search(String word) {
        TrieNode node = root;

        for (char ch : word.toCharArray()) {
            if (!node.children.containsKey(ch)) {
                return false;
            }

            node = node.children.get(ch);
        }

        return node.isEnd;
    }

    public boolean startsWith(String prefix) {
        TrieNode node = root;

        for (char ch : prefix.toCharArray()) {
            if (!node.children.containsKey(ch)) {
                return false;
            }

            node = node.children.get(ch);
        }

        return true;
    }
}

public class Main {
    public static void main(String[] args) {
        Trie trie = new Trie();

        trie.insert("cat");
        trie.insert("car");
        trie.insert("care");

        System.out.println(trie.search("cat"));
        System.out.println(trie.search("ca"));
        System.out.println(trie.startsWith("ca"));
        System.out.println(trie.startsWith("dog"));
    }
}""",
                "output": """true
false
true
false"""
            },

            "cpp": {
                "title": "Trie Implementation in C++",
                "code": """#include <iostream>
#include <unordered_map>
using namespace std;

class TrieNode {
public:
    unordered_map<char, TrieNode*> children;
    bool isEnd = false;
};

class Trie {
private:
    TrieNode* root;

public:
    Trie() {
        root = new TrieNode();
    }

    void insert(string word) {
        TrieNode* node = root;

        for (char ch : word) {
            if (node->children.find(ch) == node->children.end()) {
                node->children[ch] = new TrieNode();
            }

            node = node->children[ch];
        }

        node->isEnd = true;
    }

    bool search(string word) {
        TrieNode* node = root;

        for (char ch : word) {
            if (node->children.find(ch) == node->children.end()) {
                return false;
            }

            node = node->children[ch];
        }

        return node->isEnd;
    }

    bool startsWith(string prefix) {
        TrieNode* node = root;

        for (char ch : prefix) {
            if (node->children.find(ch) == node->children.end()) {
                return false;
            }

            node = node->children[ch];
        }

        return true;
    }
};

int main() {
    Trie trie;

    trie.insert("cat");
    trie.insert("car");
    trie.insert("care");

    cout << boolalpha;
    cout << trie.search("cat") << endl;
    cout << trie.search("ca") << endl;
    cout << trie.startsWith("ca") << endl;
    cout << trie.startsWith("dog") << endl;

    return 0;
}""",
                "output": """true
false
true
false"""
            }
        },

        "dry_run": {
            "title": "Dry Run: Insert and Search Words",
            "code": "Insert: cat, car. Search: cat, can",
            "steps": [
                {
                    "step": 1,
                    "value": "Insert cat",
                    "explanation": "Create the path root -> c -> a -> t. Mark t as the end of a word."
                },
                {
                    "step": 2,
                    "value": "Insert car",
                    "explanation": "Reuse the existing c and a nodes. Create a new r node and mark it as the end of a word."
                },
                {
                    "step": 3,
                    "value": "Search cat",
                    "explanation": "All three characters exist and the t node is marked as the end of a word. Return true."
                },
                {
                    "step": 4,
                    "value": "Search ca",
                    "explanation": "The path exists, but the a node is not marked as the end of a word. Return false."
                },
                {
                    "step": 5,
                    "value": "Search can",
                    "explanation": "The path for c and a exists, but n does not. Return false."
                }
            ],
            "result": "search(cat) = true, search(ca) = false, search(can) = false"
        },

        "practice_questions": [
            {
                "question": "Implement a Trie with insert, search and startsWith operations.",
                "difficulty": "Medium",
                "hint": "Create a node with a children map and an is_end flag.",
                "solution": {
                    "python": """class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root

        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]

        node.is_end = True

    def search(self, word):
        node = self.root

        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]

        return node.is_end

    def startsWith(self, prefix):
        node = self.root

        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]

        return True


trie = Trie()
trie.insert("apple")
print(trie.search("apple"))
print(trie.search("app"))
print(trie.startsWith("app"))""",
                    "java": """import java.util.*;

class TrieNode {
    Map<Character, TrieNode> children = new HashMap<>();
    boolean end = false;
}

class Trie {
    TrieNode root = new TrieNode();

    void insert(String word) {
        TrieNode node = root;

        for (char ch : word.toCharArray()) {
            node.children.putIfAbsent(ch, new TrieNode());
            node = node.children.get(ch);
        }

        node.end = true;
    }

    boolean search(String word) {
        TrieNode node = root;

        for (char ch : word.toCharArray()) {
            if (!node.children.containsKey(ch)) return false;
            node = node.children.get(ch);
        }

        return node.end;
    }

    boolean startsWith(String prefix) {
        TrieNode node = root;

        for (char ch : prefix.toCharArray()) {
            if (!node.children.containsKey(ch)) return false;
            node = node.children.get(ch);
        }

        return true;
    }
}""",
                    "cpp": """#include <bits/stdc++.h>
using namespace std;

class Node {
public:
    unordered_map<char, Node*> children;
    bool end = false;
};

class Trie {
    Node* root = new Node();

public:
    void insert(string word) {
        Node* node = root;

        for (char ch : word) {
            if (!node->children.count(ch))
                node->children[ch] = new Node();

            node = node->children[ch];
        }

        node->end = true;
    }

    bool search(string word) {
        Node* node = root;

        for (char ch : word) {
            if (!node->children.count(ch)) return false;
            node = node->children[ch];
        }

        return node->end;
    }

    bool startsWith(string prefix) {
        Node* node = root;

        for (char ch : prefix) {
            if (!node->children.count(ch)) return false;
            node = node->children[ch];
        }

        return true;
    }
};"""
                },
                "expected_output": """True
False
True""",
                "explanation": "The word apple is present. The string app is a prefix but is not a complete word. startsWith therefore returns true."
            },
            {
                "question": "Given a list of words, find all words that start with a given prefix.",
                "difficulty": "Medium",
                "hint": "First locate the prefix node. Then use DFS to collect complete words below it.",
                "solution": {
                    "python": """class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root

        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]

        node.is_end = True

    def autocomplete(self, prefix):
        node = self.root

        for ch in prefix:
            if ch not in node.children:
                return []
            node = node.children[ch]

        result = []

        def dfs(current, path):
            if current.is_end:
                result.append(path)

            for ch in sorted(current.children):
                dfs(current.children[ch], path + ch)

        dfs(node, prefix)
        return result


trie = Trie()

for word in ["cat", "car", "care", "dog"]:
    trie.insert(word)

print(trie.autocomplete("ca"))""",
                    "java": """import java.util.*;

class TrieNode {
    Map<Character, TrieNode> children = new TreeMap<>();
    boolean end = false;
}

class Trie {
    TrieNode root = new TrieNode();

    void insert(String word) {
        TrieNode node = root;

        for (char ch : word.toCharArray()) {
            node.children.putIfAbsent(ch, new TrieNode());
            node = node.children.get(ch);
        }

        node.end = true;
    }

    List<String> autocomplete(String prefix) {
        TrieNode node = root;

        for (char ch : prefix.toCharArray()) {
            if (!node.children.containsKey(ch))
                return new ArrayList<>();

            node = node.children.get(ch);
        }

        List<String> result = new ArrayList<>();
        dfs(node, prefix, result);
        return result;
    }

    void dfs(TrieNode node, String path, List<String> result) {
        if (node.end) result.add(path);

        for (char ch : node.children.keySet()) {
            dfs(node.children.get(ch), path + ch, result);
        }
    }
}""",
                    "cpp": """#include <bits/stdc++.h>
using namespace std;

class Node {
public:
    map<char, Node*> children;
    bool end = false;
};

class Trie {
    Node* root = new Node();

    void dfs(Node* node, string path, vector<string>& result) {
        if (node->end) result.push_back(path);

        for (auto& item : node->children) {
            dfs(item.second, path + item.first, result);
        }
    }

public:
    void insert(string word) {
        Node* node = root;

        for (char ch : word) {
            if (!node->children.count(ch))
                node->children[ch] = new Node();

            node = node->children[ch];
        }

        node->end = true;
    }

    vector<string> autocomplete(string prefix) {
        Node* node = root;

        for (char ch : prefix) {
            if (!node->children.count(ch)) return {};
            node = node->children[ch];
        }

        vector<string> result;
        dfs(node, prefix, result);
        return result;
    }
};"""
                },
                "expected_output": """['car', 'care', 'cat']""",
                "explanation": "The Trie finds the prefix node for ca and traverses its descendants to collect complete words."
            },
            {
                "question": "Implement a function that checks whether a list contains a word with a given prefix.",
                "difficulty": "Easy",
                "hint": "Insert the words into a Trie and use the prefix search operation.",
                "solution": {
                    "python": """def has_prefix(words, prefix):
    trie = Trie()

    for word in words:
        trie.insert(word)

    return trie.startsWith(prefix)


words = ["apple", "banana", "application"]
print(has_prefix(words, "app"))
print(has_prefix(words, "cat"))""",
                    "java": """import java.util.*;

class Main {
    public static boolean hasPrefix(String[] words, String prefix) {
        Trie trie = new Trie();

        for (String word : words) {
            trie.insert(word);
        }

        return trie.startsWith(prefix);
    }

    public static void main(String[] args) {
        String[] words = {"apple", "banana", "application"};

        System.out.println(hasPrefix(words, "app"));
        System.out.println(hasPrefix(words, "cat"));
    }
}""",
                    "cpp": """#include <bits/stdc++.h>
using namespace std;

bool hasPrefix(vector<string>& words, string prefix) {
    Trie trie;

    for (string word : words) {
        trie.insert(word);
    }

    return trie.startsWith(prefix);
}

int main() {
    vector<string> words = {
        "apple", "banana", "application"
    };

    cout << boolalpha;
    cout << hasPrefix(words, "app") << endl;
    cout << hasPrefix(words, "cat") << endl;

    return 0;
}"""
                },
                "expected_output": """True
False""",
                "explanation": "At least one word starts with app, but no word starts with cat."
            }
        ],

        "interview_questions": [
            {
                "question": "What is a Trie?",
                "answer": "A Trie is a tree-based data structure used to store strings and efficiently perform prefix-based operations."
            },
            {
                "question": "Why is a Trie called a Prefix Tree?",
                "answer": "Because words sharing common prefixes share the same initial path in the tree."
            },
            {
                "question": "What is the root node?",
                "answer": "The starting node of a Trie. It normally does not represent a character."
            },
            {
                "question": "What does the end-of-word flag represent?",
                "answer": "It indicates that a complete word ends at a particular Trie node."
            },
            {
                "question": "What is the time complexity of Trie insertion?",
                "answer": "O(L), where L is the length of the inserted word."
            },
            {
                "question": "What is the time complexity of searching a word in a Trie?",
                "answer": "O(L), where L is the length of the word."
            },
            {
                "question": "What is the difference between search and startsWith?",
                "answer": "search checks whether a complete word exists. startsWith checks whether the prefix path exists."
            },
            {
                "question": "Can a word be a prefix of another word?",
                "answer": "Yes. For example, app is a prefix of apple. Both can be stored by marking the app node as an end of a word."
            },
            {
                "question": "How are Tries used in autocomplete?",
                "answer": "The prefix is traversed first, then DFS or another traversal collects complete words below that node."
            },
            {
                "question": "What is the space complexity of a Trie?",
                "answer": "It depends on the total number of nodes and child references. In the worst case, it is proportional to the total number of characters inserted."
            },
            {
                "question": "What is the difference between a Trie and a HashMap?",
                "answer": "A HashMap is useful for exact-key lookup, while a Trie naturally supports prefix searches and autocomplete."
            },
            {
                "question": "What happens when a word is inserted more than once?",
                "answer": "The existing path is reused and its final node remains marked as an end of a word."
            },
            {
                "question": "Can a Trie store numbers?",
                "answer": "Yes. Binary Tries store bits and can support operations such as maximum XOR queries."
            },
            {
                "question": "How can you implement a Trie using an array?",
                "answer": "For a fixed alphabet such as lowercase English letters, each node can contain an array of 26 child references."
            },
            {
                "question": "What are the disadvantages of a Trie?",
                "answer": "Tries can consume significant memory because they create nodes and child references for stored characters."
            }
        ],

        "mcqs": [
            {
                "question": "What is another name for a Trie?",
                "options": ["Binary Heap", "Prefix Tree", "Hash Table", "Graph"],
                "answer": "Prefix Tree",
                "explanation": "A Trie stores strings using shared prefix paths."
            },
            {
                "question": "What does a Trie node usually store?",
                "options": ["Only an integer", "Child references and an end marker", "Only an array index", "A sorting algorithm"],
                "answer": "Child references and an end marker",
                "explanation": "Children represent the next characters, and the marker identifies complete words."
            },
            {
                "question": "What is the time complexity of searching a word of length L?",
                "options": ["O(1)", "O(log L)", "O(L)", "O(L squared)"],
                "answer": "O(L)",
                "explanation": "The algorithm follows one node per character."
            },
            {
                "question": "What is the main purpose of the end-of-word flag?",
                "options": ["To sort words", "To mark a complete word", "To delete nodes", "To count characters"],
                "answer": "To mark a complete word",
                "explanation": "It distinguishes a complete word from a prefix."
            },
            {
                "question": "If app is inserted, what should search(app) return?",
                "options": ["True", "False", "Null", "Error"],
                "answer": "True",
                "explanation": "The final node for app is marked as a complete word."
            },
            {
                "question": "If apple is inserted but app is not separately inserted, what does search(app) return?",
                "options": ["True", "False", "Null", "Error"],
                "answer": "False",
                "explanation": "The prefix path exists, but app is not marked as a complete word."
            },
            {
                "question": "Which operation checks whether any stored word starts with a prefix?",
                "options": ["delete", "startsWith", "sort", "reverse"],
                "answer": "startsWith",
                "explanation": "Prefix search checks whether the path for the prefix exists."
            },
            {
                "question": "Which application commonly uses a Trie?",
                "options": ["Autocomplete", "Matrix multiplication", "Heap sorting", "Binary search on integers"],
                "answer": "Autocomplete",
                "explanation": "Tries efficiently locate words sharing a prefix."
            },
            {
                "question": "What is the usual role of the root node?",
                "options": ["Stores the last character", "Stores the first complete word", "Acts as the starting node", "Stores the word count only"],
                "answer": "Acts as the starting node",
                "explanation": "All inserted words begin their traversal from the root."
            },
            {
                "question": "What is a major disadvantage of a Trie?",
                "options": ["Cannot store strings", "High memory usage in some implementations", "Cannot search prefixes", "Insertion is always O(n squared)"],
                "answer": "High memory usage in some implementations",
                "explanation": "Trie nodes and child references can consume substantial memory."
            }
        ]
    }
})


DSA_TRACK.update({
    "dsa-two-pointers": {
        "title": "Two Pointers Technique",
        "subtitle": "Solve array and string problems efficiently using two indices",

        "content": """
# 1. What is the Two Pointers Technique?

Two Pointers is an algorithmic technique in which two variables (pointers or indices) are used to traverse an array or string.

Instead of checking every possible pair using nested loops, we move two pointers strategically to reduce unnecessary comparisons.

It is commonly used for:
- Finding pairs with a target sum in sorted arrays.
- Reversing arrays and strings.
- Removing duplicates.
- Checking palindromes.
- Partitioning arrays.

# 2. Types of Two Pointers

## A. Opposite Direction Pointers

One pointer starts at the beginning and the other at the end.

Example:
arr = [1, 2, 3, 4, 6]
target = 6

left = 0
right = 4

Calculate arr[left] + arr[right].

If the sum is too small, move left forward.
If the sum is too large, move right backward.
If the sum matches, we found the answer.

This approach is particularly useful for sorted arrays.

## B. Same Direction Pointers

Both pointers move from left to right, usually at different speeds.

Common applications:
- Removing duplicates from sorted arrays.
- Moving zeroes.
- Partitioning arrays.
- Detecting certain patterns.

## C. Fast and Slow Pointers

One pointer moves faster than the other.

Common applications:
- Detecting cycles in linked lists.
- Finding the middle of a linked list.
- Finding the starting point of a cycle.

# 3. Example: Pair Sum in a Sorted Array

Array = [1, 2, 3, 4, 6]
Target = 6

Initially:
left = 0, right = 4

Step 1:
1 + 6 = 7
7 > 6, so move right left.

Step 2:
1 + 4 = 5
5 < 6, so move left right.

Step 3:
2 + 4 = 6
Target found.

Answer: [2, 4]

# 4. Remove Duplicates from a Sorted Array

Use two pointers:
- i identifies the last unique element.
- j scans the remaining array.

When arr[j] differs from arr[i], increase i and copy arr[j].

The first i + 1 elements contain the unique values.

# 5. Reverse an Array

Initialize:
left = 0
right = n - 1

Swap the elements and move both pointers inward until left >= right.

# 6. Complexity Analysis

For the pair sum problem:
- Time Complexity: O(n)
- Auxiliary Space: O(1)

For reversing an array:
- Time Complexity: O(n)
- Auxiliary Space: O(1)

For removing duplicates:
- Time Complexity: O(n)
- Auxiliary Space: O(1), if modification is performed in place.

# 7. Important Conditions

The pair-sum approach described above requires a sorted array.

If the array is unsorted, sorting first generally takes O(n log n), and the two-pointer scan takes O(n).

Sorting may change the original element positions, so preserve indices separately if the problem requires original indices.
""",

        "key_concepts": [
            {
                "name": "Left Pointer",
                "description": "Usually starts at the beginning of the array."
            },
            {
                "name": "Right Pointer",
                "description": "Usually starts at the end of the array."
            },
            {
                "name": "Opposite Direction",
                "description": "Two pointers move toward each other."
            },
            {
                "name": "Same Direction",
                "description": "Two pointers move forward through an array."
            },
            {
                "name": "Fast and Slow Pointers",
                "description": "Two pointers move at different speeds, commonly in linked lists."
            },
            {
                "name": "In-place Algorithm",
                "description": "Modifies data without requiring an additional array."
            }
        ],

        "examples": {
            "python": {
                "title": "Pair Sum Using Two Pointers",
                "code": """def two_sum_sorted(arr, target):
    left = 0
    right = len(arr) - 1

    while left < right:
        total = arr[left] + arr[right]

        if total == target:
            return [arr[left], arr[right]]
        elif total < target:
            left += 1
        else:
            right -= 1

    return []

arr = [1, 2, 3, 4, 6]
print(two_sum_sorted(arr, 6))""",
                "output": "[2, 4]"
            },
            "java": {
                "title": "Pair Sum Using Two Pointers in Java",
                "code": """public class Main {
    static int[] twoSumSorted(int[] arr, int target) {
        int left = 0;
        int right = arr.length - 1;

        while (left < right) {
            int sum = arr[left] + arr[right];

            if (sum == target) {
                return new int[]{arr[left], arr[right]};
            } else if (sum < target) {
                left++;
            } else {
                right--;
            }
        }

        return new int[]{};
    }

    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 6};
        int[] result = twoSumSorted(arr, 6);

        for (int value : result) {
            System.out.print(value + " ");
        }
    }
}""",
                "output": "2 4"
            },
            "cpp": {
                "title": "Pair Sum Using Two Pointers in C++",
                "code": """#include <iostream>
#include <vector>
using namespace std;

vector<int> twoSumSorted(vector<int>& arr, int target) {
    int left = 0;
    int right = arr.size() - 1;

    while (left < right) {
        int sum = arr[left] + arr[right];

        if (sum == target) {
            return {arr[left], arr[right]};
        } else if (sum < target) {
            left++;
        } else {
            right--;
        }
    }

    return {};
}

int main() {
    vector<int> arr = {1, 2, 3, 4, 6};
    vector<int> result = twoSumSorted(arr, 6);

    for (int value : result) {
        cout << value << " ";
    }

    return 0;
}""",
                "output": "2 4"
            }
        },

        "dry_run": {
            "title": "Dry Run: Find Pair With Target Sum",
            "code": "arr = [1, 2, 3, 4, 6], target = 6",
            "steps": [
                {
                    "step": 1,
                    "value": "left = 0, right = 4",
                    "explanation": "Compare 1 + 6 = 7. Since 7 is greater than 6, move right left."
                },
                {
                    "step": 2,
                    "value": "left = 0, right = 3",
                    "explanation": "Compare 1 + 4 = 5. Since 5 is smaller than 6, move left right."
                },
                {
                    "step": 3,
                    "value": "left = 1, right = 3",
                    "explanation": "Compare 2 + 4 = 6. The target is found."
                }
            ],
            "result": "Pair found: [2, 4]"
        },

        "practice_questions": [
            {
                "question": "Reverse an array in place using two pointers.",
                "difficulty": "Easy",
                "hint": "Swap the first and last elements, then move both pointers inward.",
                "solution": {
                    "python": """def reverse_array(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    return arr

print(reverse_array([1, 2, 3, 4, 5]))""",
                    "java": """import java.util.Arrays;

public class Main {
    static void reverse(int[] arr) {
        int left = 0;
        int right = arr.length - 1;

        while (left < right) {
            int temp = arr[left];
            arr[left] = arr[right];
            arr[right] = temp;

            left++;
            right--;
        }
    }

    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};
        reverse(arr);
        System.out.println(Arrays.toString(arr));
    }
}""",
                    "cpp": """#include <iostream>
#include <vector>
using namespace std;

void reverseArray(vector<int>& arr) {
    int left = 0;
    int right = arr.size() - 1;

    while (left < right) {
        swap(arr[left], arr[right]);
        left++;
        right--;
    }
}

int main() {
    vector<int> arr = {1, 2, 3, 4, 5};
    reverseArray(arr);

    for (int x : arr) cout << x << " ";
    return 0;
}"""
                },
                "expected_output": "[5, 4, 3, 2, 1]",
                "explanation": "Each iteration swaps two elements at opposite ends."
            },
            {
                "question": "Determine whether a string is a palindrome using two pointers.",
                "difficulty": "Easy",
                "hint": "Compare characters from both ends and move toward the center.",
                "solution": {
                    "python": """def is_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False

        left += 1
        right -= 1

    return True

print(is_palindrome("madam"))""",
                    "java": """public class Main {
    static boolean isPalindrome(String s) {
        int left = 0;
        int right = s.length() - 1;

        while (left < right) {
            if (s.charAt(left) != s.charAt(right)) {
                return false;
            }

            left++;
            right--;
        }

        return true;
    }

    public static void main(String[] args) {
        System.out.println(isPalindrome("madam"));
    }
}""",
                    "cpp": """#include <iostream>
#include <string>
using namespace std;

bool isPalindrome(string s) {
    int left = 0;
    int right = s.size() - 1;

    while (left < right) {
        if (s[left] != s[right]) return false;

        left++;
        right--;
    }

    return true;
}

int main() {
    cout << boolalpha << isPalindrome("madam");
    return 0;
}"""
                },
                "expected_output": "True",
                "explanation": "The characters at matching positions from both ends are equal."
            },
            {
                "question": "Given a sorted array, remove duplicates in place and return the number of unique elements.",
                "difficulty": "Medium",
                "hint": "Use one pointer to track the last unique position and another to scan the array.",
                "solution": {
                    "python": """def remove_duplicates(nums):
    if not nums:
        return 0

    i = 0

    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]

    return i + 1

nums = [1, 1, 2, 2, 3]
k = remove_duplicates(nums)

print(k)
print(nums[:k])""",
                    "java": """import java.util.Arrays;

public class Main {
    static int removeDuplicates(int[] nums) {
        if (nums.length == 0) return 0;

        int i = 0;

        for (int j = 1; j < nums.length; j++) {
            if (nums[j] != nums[i]) {
                i++;
                nums[i] = nums[j];
            }
        }

        return i + 1;
    }

    public static void main(String[] args) {
        int[] nums = {1, 1, 2, 2, 3};
        int k = removeDuplicates(nums);

        System.out.println(k);
        System.out.println(Arrays.toString(Arrays.copyOf(nums, k)));
    }
}""",
                    "cpp": """#include <iostream>
#include <vector>
using namespace std;

int removeDuplicates(vector<int>& nums) {
    if (nums.empty()) return 0;

    int i = 0;

    for (int j = 1; j < nums.size(); j++) {
        if (nums[j] != nums[i]) {
            i++;
            nums[i] = nums[j];
        }
    }

    return i + 1;
}

int main() {
    vector<int> nums = {1, 1, 2, 2, 3};
    int k = removeDuplicates(nums);

    cout << k << endl;

    for (int i = 0; i < k; i++) {
        cout << nums[i] << " ";
    }

    return 0;
}"""
                },
                "expected_output": "3\n[1, 2, 3]",
                "explanation": "The first three positions contain the unique sorted values. The remaining array positions do not matter.",
                "complexity": "O(n) time and O(1) auxiliary space."
            }
        ],

        "interview_questions": [
            {
                "question": "What is the Two Pointers technique?",
                "answer": "It is an algorithmic technique that uses two indices to traverse a data structure efficiently."
            },
            {
                "question": "What are the main types of Two Pointers?",
                "answer": "Opposite-direction pointers, same-direction pointers, and fast-and-slow pointers."
            },
            {
                "question": "Why is Two Pointers useful?",
                "answer": "It can reduce nested-loop solutions from O(n squared) to O(n) when the problem has the required structure."
            },
            {
                "question": "Does the pair-sum Two Pointers approach require a sorted array?",
                "answer": "The simple left-right approach relies on sorted order to decide which pointer to move."
            },
            {
                "question": "How do you reverse an array using Two Pointers?",
                "answer": "Swap the elements at the left and right pointers and move both pointers toward the center."
            },
            {
                "question": "How can Two Pointers check a palindrome?",
                "answer": "Compare characters at both ends and move inward until they meet or a mismatch is found."
            },
            {
                "question": "What is the Fast and Slow Pointer technique?",
                "answer": "Two pointers traverse a structure at different speeds, often used for linked-list cycle detection."
            },
            {
                "question": "How can Two Pointers remove duplicates from a sorted array?",
                "answer": "Use one pointer to track the last unique value and another to scan the remaining elements."
            },
            {
                "question": "What is the time complexity of reversing an array using Two Pointers?",
                "answer": "O(n), because each element is processed at most once."
            },
            {
                "question": "What is the auxiliary space complexity of in-place reversal?",
                "answer": "O(1), because only a constant number of variables are used."
            },
            {
                "question": "Can Two Pointers be used on strings?",
                "answer": "Yes. Common examples include palindrome checking and reversing characters."
            },
            {
                "question": "What is the difference between Sliding Window and Two Pointers?",
                "answer": "Sliding Window maintains a contiguous range and updates its contents as boundaries move. Two Pointers is a broader technique using two indices."
            },
            {
                "question": "What happens if the input array is unsorted in the pair-sum problem?",
                "answer": "The sorted two-pointer logic cannot be directly applied. One option is to sort the values first, while preserving original indices if required."
            },
            {
                "question": "How does Two Pointers optimize a brute-force pair search?",
                "answer": "It avoids examining every pair by using the ordering or other problem properties to eliminate multiple possibilities."
            },
            {
                "question": "Name some common Two Pointers interview problems.",
                "answer": "Two Sum II, Valid Palindrome, Remove Duplicates from Sorted Array, Container With Most Water, and 3Sum."
            }
        ],

        "mcqs": [
            {
                "question": "What is the usual time complexity of pair sum in a sorted array using Two Pointers?",
                "options": ["O(1)", "O(log n)", "O(n)", "O(n squared)"],
                "answer": "O(n)",
                "explanation": "Each pointer moves through the array at most n times."
            },
            {
                "question": "Where do opposite-direction pointers usually start?",
                "options": ["Both at index 0", "Both at the last index", "One at each end", "At random positions"],
                "answer": "One at each end",
                "explanation": "They move toward each other."
            },
            {
                "question": "Which input property makes the standard pair-sum Two Pointers approach work?",
                "options": ["The array is sorted", "The array has only negative values", "The array has unique elements", "The array is circular"],
                "answer": "The array is sorted",
                "explanation": "Sorted order tells us which pointer should move."
            },
            {
                "question": "If the current sum is smaller than the target in a sorted array, which pointer moves?",
                "options": ["Right pointer moves left", "Left pointer moves right", "Both pointers move left", "Neither moves"],
                "answer": "Left pointer moves right",
                "explanation": "Moving left forward increases the sum or keeps it from decreasing."
            },
            {
                "question": "If the current sum is greater than the target, which pointer moves?",
                "options": ["Left pointer moves right", "Right pointer moves left", "Both move right", "Neither moves"],
                "answer": "Right pointer moves left",
                "explanation": "Moving right backward decreases the sum or keeps it from increasing."
            },
            {
                "question": "Which technique is commonly used to detect a cycle in a linked list?",
                "options": ["Binary Search", "Fast and Slow Pointers", "Prefix Sum", "Merge Sort"],
                "answer": "Fast and Slow Pointers",
                "explanation": "The fast pointer moves two steps while the slow pointer moves one."
            },
            {
                "question": "What is the auxiliary space complexity of in-place array reversal?",
                "options": ["O(n)", "O(log n)", "O(1)", "O(n squared)"],
                "answer": "O(1)",
                "explanation": "Only a constant number of variables are required."
            },
            {
                "question": "Which problem is a common Two Pointers application?",
                "options": ["Valid Palindrome", "Matrix Chain Multiplication", "Dijkstra's Algorithm", "Merge Sort"],
                "answer": "Valid Palindrome",
                "explanation": "Characters can be compared from opposite ends."
            },
            {
                "question": "What is the main difference between Sliding Window and general Two Pointers?",
                "options": ["They are identical in every situation", "Sliding Window maintains a contiguous range", "Two Pointers only works on trees", "Sliding Window always uses three pointers"],
                "answer": "Sliding Window maintains a contiguous range",
                "explanation": "A sliding window is a specialized use of pointer boundaries."
            },
            {
                "question": "What is the time complexity of removing duplicates from a sorted array using Two Pointers?",
                "options": ["O(n squared)", "O(log n)", "O(n)", "O(2 to the power n)"],
                "answer": "O(n)",
                "explanation": "The scanning pointer visits each element once."
            }
        ]
    }
})


DSA_TRACK.update({
    "dsa-strings-basics": {
        "title": "Strings and String Manipulation",
        "subtitle": "Master string operations, searching, frequency counting and common interview problems",

        "content": """
# 1. What is a String?

A string is a sequence of characters used to represent text.

Examples:
- "Hello"
- "CodeQuest"
- "Data Science"

Strings are supported by Python, Java and C++.

In Java, String is a class.
In Python, str is an immutable sequence type.
In C++, strings are commonly handled using std::string.

# 2. String Indexing

Characters can be accessed using their positions.

Example:
s = "CODE"

Index:
C -> 0
O -> 1
D -> 2
E -> 3

Python also supports negative indexing:
s[-1] gives E.

Java and C++ commonly use zero-based indexing.

# 3. String Traversal

A string can be traversed using a loop.

Python:
for ch in s:
    print(ch)

Java:
for (int i = 0; i < s.length(); i++) {
    System.out.println(s.charAt(i));
}

C++:
for (char ch : s) {
    cout << ch << endl;
}

# 4. String Immutability

In Python and Java, strings are immutable.

This means that an existing string cannot be modified character by character.

For example, in Python:
s = "hello"
s = s + " world"

A new string is created and assigned to s.

In Java, StringBuilder is useful when many modifications are needed.

In C++, std::string supports modification of its contents.

# 5. Important String Operations

Length:
- Python: len(s)
- Java: s.length()
- C++: s.length()

Access character:
- Python: s[0]
- Java: s.charAt(0)
- C++: s[0]

Substring:
- Python: s[start:end]
- Java: s.substring(start, end)
- C++: s.substr(start, length)

Convert to lowercase:
- Python: s.lower()
- Java: s.toLowerCase()
- C++: use transform with tolower.

Reverse:
- Python: s[::-1]
- Java: StringBuilder(s).reverse()
- C++: reverse(s.begin(), s.end()).

# 6. Common String Interview Patterns

## A. Palindrome

A palindrome reads the same forward and backward.

Examples:
- madam
- level
- racecar

A two-pointer approach compares characters from both ends.

## B. Anagram

Two strings are anagrams if they contain the same characters with the same frequencies.

Example:
listen and silent

One approach:
1. Check whether lengths are equal.
2. Count character frequencies.
3. Compare the frequencies.

## C. Character Frequency

Frequency counting calculates how many times each character appears.

Example:
"banana"

a = 3
b = 1
n = 2

A hash map or frequency array can be used.

## D. Reverse a String

Reverse the order of characters.

Example:
"hello" becomes "olleh".

## E. First Non-Repeating Character

Find the first character whose frequency is exactly one.

Example:
"swiss"

The first non-repeating character is w.

# 7. String Searching

Substring searching checks whether a smaller string appears inside a larger string.

For simple built-in operations:
- Python: pattern in text
- Java: text.contains(pattern)
- C++: text.find(pattern)

For more advanced problems, learn:
- Naive pattern matching
- KMP algorithm
- Rabin-Karp algorithm
- Z algorithm

# 8. StringBuilder in Java

StringBuilder is a mutable sequence of characters.

It avoids creating many intermediate String objects when repeatedly modifying text.

Example:

StringBuilder sb = new StringBuilder();
sb.append("Code");
sb.append("Quest");

System.out.println(sb.toString());

Output:
CodeQuest

Common operations:
- append()
- insert()
- delete()
- reverse()
- toString()

# 9. Complexity Analysis

For a string of length n:

- Access by index: O(1).
- Full traversal: O(n).
- Reverse: O(n).
- Frequency counting: O(n).
- Compare two strings: O(n) in the worst case.
- Naive substring search: O(n × m), where m is pattern length.
- Hash-based anagram checking: O(n) expected time for a fixed character set or suitable hash operations.

Remember that creating a new string can require O(n) additional space.

# 10. Important Interview Tips

- Understand whether the problem is case-sensitive.
- Check whether spaces and punctuation should be ignored.
- Consider empty strings.
- Handle uppercase and lowercase characters carefully.
- Understand Unicode when the problem is not restricted to English letters.
- Use StringBuilder for repeated modifications in Java.
- Use frequency counting for anagram and duplicate-character problems.
""",

        "key_concepts": [
            {
                "name": "String",
                "description": "A sequence of characters used to represent text."
            },
            {
                "name": "Indexing",
                "description": "Accessing a character using its zero-based position."
            },
            {
                "name": "Immutability",
                "description": "Python and Java strings cannot be modified in place."
            },
            {
                "name": "Substring",
                "description": "A continuous portion of an existing string."
            },
            {
                "name": "Palindrome",
                "description": "A string that reads the same forward and backward."
            },
            {
                "name": "Anagram",
                "description": "Two strings containing the same characters with the same frequencies."
            },
            {
                "name": "Frequency Counting",
                "description": "Counting how often each character appears."
            },
            {
                "name": "StringBuilder",
                "description": "A mutable string-building class in Java."
            },
            {
                "name": "Pattern Matching",
                "description": "Finding occurrences of a pattern inside a larger string."
            }
        ],

        "examples": {
            "python": {
                "title": "Basic String Operations in Python",
                "code": """s = "CodeQuest"

print("Length:", len(s))
print("First character:", s[0])
print("Last character:", s[-1])
print("Uppercase:", s.upper())
print("Lowercase:", s.lower())
print("Substring:", s[0:4])
print("Reversed:", s[::-1])

text = "banana"
frequency = {}

for ch in text:
    frequency[ch] = frequency.get(ch, 0) + 1

print("Frequency:", frequency)""",
                "output": """Length: 9
First character: C
Last character: t
Uppercase: CODEQUEST
Lowercase: codequest
Substring: Code
Reversed: tseuQedoC
Frequency: {'b': 1, 'a': 3, 'n': 2}"""
            },
            "java": {
                "title": "String Operations in Java",
                "code": """import java.util.HashMap;
import java.util.Map;

public class Main {
    public static void main(String[] args) {
        String s = "CodeQuest";

        System.out.println("Length: " + s.length());
        System.out.println("First character: " + s.charAt(0));
        System.out.println("Last character: " + s.charAt(s.length() - 1));
        System.out.println("Uppercase: " + s.toUpperCase());
        System.out.println("Lowercase: " + s.toLowerCase());
        System.out.println("Substring: " + s.substring(0, 4));

        StringBuilder sb = new StringBuilder(s);
        System.out.println("Reversed: " + sb.reverse());

        String text = "banana";
        Map<Character, Integer> frequency = new HashMap<>();

        for (char ch : text.toCharArray()) {
            frequency.put(ch, frequency.getOrDefault(ch, 0) + 1);
        }

        System.out.println("Frequency: " + frequency);
    }
}""",
                "output": """Length: 9
First character: C
Last character: t
Uppercase: CODEQUEST
Lowercase: codequest
Substring: Code
Reversed: tseuQedoC
Frequency: {a=3, b=1, n=2}"""
            },
            "cpp": {
                "title": "String Operations in C++",
                "code": """#include <iostream>
#include <string>
#include <algorithm>
#include <unordered_map>
using namespace std;

int main() {
    string s = "CodeQuest";

    cout << "Length: " << s.length() << endl;
    cout << "First character: " << s[0] << endl;
    cout << "Last character: " << s[s.length() - 1] << endl;
    cout << "Substring: " << s.substr(0, 4) << endl;

    string reversed = s;
    reverse(reversed.begin(), reversed.end());
    cout << "Reversed: " << reversed << endl;

    string text = "banana";
    unordered_map<char, int> frequency;

    for (char ch : text) {
        frequency[ch]++;
    }

    cout << "Frequency of a: " << frequency['a'] << endl;
    cout << "Frequency of b: " << frequency['b'] << endl;
    cout << "Frequency of n: " << frequency['n'] << endl;

    return 0;
}""",
                "output": """Length: 9
First character: C
Last character: t
Substring: Code
Reversed: tseuQedoC
Frequency of a: 3
Frequency of b: 1
Frequency of n: 2"""
            }
        },

        "dry_run": {
            "title": "Dry Run: Character Frequency",
            "code": "s = 'banana'",
            "steps": [
                {
                    "step": 1,
                    "value": "b",
                    "explanation": "The character b appears for the first time. Frequency becomes 1."
                },
                {
                    "step": 2,
                    "value": "a",
                    "explanation": "The character a appears for the first time. Frequency becomes 1."
                },
                {
                    "step": 3,
                    "value": "n",
                    "explanation": "The character n appears for the first time. Frequency becomes 1."
                },
                {
                    "step": 4,
                    "value": "a",
                    "explanation": "The existing frequency of a increases to 2."
                },
                {
                    "step": 5,
                    "value": "n",
                    "explanation": "The existing frequency of n increases to 2."
                },
                {
                    "step": 6,
                    "value": "a",
                    "explanation": "The frequency of a increases to 3."
                }
            ],
            "result": "b = 1, a = 3, n = 2"
        },

        "practice_questions": [
            {
                "question": "Reverse a given string.",
                "difficulty": "Easy",
                "hint": "Use slicing in Python, StringBuilder in Java, or reverse() in C++.",
                "solution": {
                    "python": """def reverse_string(s):
    return s[::-1]

print(reverse_string("hello"))""",
                    "java": """public class Main {
    public static void main(String[] args) {
        String s = "hello";
        StringBuilder sb = new StringBuilder(s);
        System.out.println(sb.reverse());
    }
}""",
                    "cpp": """#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main() {
    string s = "hello";
    reverse(s.begin(), s.end());
    cout << s;
    return 0;
}"""
                },
                "expected_output": "olleh",
                "explanation": "The characters are arranged in reverse order.",
                "complexity": "O(n) time and O(n) auxiliary space for the resulting string."
            },
            {
                "question": "Check whether two strings are anagrams of each other.",
                "difficulty": "Easy",
                "hint": "Compare character frequencies. Assume lowercase English letters.",
                "solution": {
                    "python": """def are_anagrams(a, b):
    if len(a) != len(b):
        return False

    frequency = [0] * 26

    for ch in a:
        frequency[ord(ch) - ord('a')] += 1

    for ch in b:
        frequency[ord(ch) - ord('a')] -= 1

    return all(count == 0 for count in frequency)

print(are_anagrams("listen", "silent"))""",
                    "java": """public class Main {
    static boolean areAnagrams(String a, String b) {
        if (a.length() != b.length()) return false;

        int[] frequency = new int[26];

        for (char ch : a.toCharArray()) {
            frequency[ch - 'a']++;
        }

        for (char ch : b.toCharArray()) {
            frequency[ch - 'a']--;
        }

        for (int count : frequency) {
            if (count != 0) return false;
        }

        return true;
    }

    public static void main(String[] args) {
        System.out.println(areAnagrams("listen", "silent"));
    }
}""",
                    "cpp": """#include <iostream>
#include <string>
#include <vector>
using namespace std;

bool areAnagrams(string a, string b) {
    if (a.size() != b.size()) return false;

    vector<int> frequency(26, 0);

    for (char ch : a) frequency[ch - 'a']++;
    for (char ch : b) frequency[ch - 'a']--;

    for (int count : frequency) {
        if (count != 0) return false;
    }

    return true;
}

int main() {
    cout << boolalpha << areAnagrams("listen", "silent");
    return 0;
}"""
                },
                "expected_output": "True",
                "explanation": "Both strings have exactly the same character frequencies. The solution assumes lowercase English letters.",
                "complexity": "O(n) time and O(1) auxiliary space for the fixed 26-letter alphabet."
            },
            {
                "question": "Find the first non-repeating character in a string. Return -1 if none exists.",
                "difficulty": "Medium",
                "hint": "First count character frequencies, then scan the string again.",
                "solution": {
                    "python": """def first_unique(s):
    frequency = {}

    for ch in s:
        frequency[ch] = frequency.get(ch, 0) + 1

    for ch in s:
        if frequency[ch] == 1:
            return ch

    return -1

print(first_unique("swiss"))""",
                    "java": """import java.util.HashMap;
import java.util.Map;

public class Main {
    static char firstUnique(String s) {
        Map<Character, Integer> frequency = new HashMap<>();

        for (char ch : s.toCharArray()) {
            frequency.put(ch, frequency.getOrDefault(ch, 0) + 1);
        }

        for (char ch : s.toCharArray()) {
            if (frequency.get(ch) == 1) {
                return ch;
            }
        }

        return '#';
    }

    public static void main(String[] args) {
        System.out.println(firstUnique("swiss"));
    }
}""",
                    "cpp": """#include <iostream>
#include <string>
#include <unordered_map>
using namespace std;

char firstUnique(string s) {
    unordered_map<char, int> frequency;

    for (char ch : s) frequency[ch]++;

    for (char ch : s) {
        if (frequency[ch] == 1) return ch;
    }

    return '#';
}

int main() {
    cout << firstUnique("swiss");
    return 0;
}"""
                },
                "expected_output": "w",
                "explanation": "The frequency of s is 3, w is 1, and i is 1. The first character with frequency one is w.",
                "complexity": "O(n) expected time and O(k) space, where k is the number of distinct characters."
            }
        ],

        "interview_questions": [
            {
                "question": "What is a string?",
                "answer": "A string is a sequence of characters used to represent text."
            },
            {
                "question": "Are strings mutable in Python?",
                "answer": "No. Python strings are immutable. Operations that appear to modify them create new strings."
            },
            {
                "question": "Are strings mutable in Java?",
                "answer": "No. Java String objects are immutable. StringBuilder provides a mutable alternative."
            },
            {
                "question": "What is the difference between String and StringBuilder in Java?",
                "answer": "String is immutable, whereas StringBuilder allows modifications without creating a new object for every operation."
            },
            {
                "question": "What is a palindrome?",
                "answer": "A palindrome is a sequence that reads the same forward and backward."
            },
            {
                "question": "What is an anagram?",
                "answer": "Two strings are anagrams when they contain the same characters with identical frequencies."
            },
            {
                "question": "How can you check whether two strings are anagrams?",
                "answer": "Compare their character frequencies or sort both strings and compare the results."
            },
            {
                "question": "How do you find the frequency of each character?",
                "answer": "Traverse the string and maintain a frequency array or hash map."
            },
            {
                "question": "What is a substring?",
                "answer": "A substring is a contiguous sequence of characters within a string."
            },
            {
                "question": "What is the time complexity of traversing a string?",
                "answer": "O(n), where n is the string length."
            },
            {
                "question": "How do you find the first non-repeating character?",
                "answer": "Count character frequencies in one pass and scan again to find the first character with frequency one."
            },
            {
                "question": "What is the KMP algorithm?",
                "answer": "Knuth-Morris-Pratt is a string matching algorithm that uses a prefix-function or LPS array to avoid unnecessary comparisons. It runs in O(n + m) time."
            },
            {
                "question": "What is the Rabin-Karp algorithm?",
                "answer": "It uses rolling hashes to search for a pattern within a larger string."
            },
            {
                "question": "What is the difference between a character and a string?",
                "answer": "A character represents a single character value, while a string is a sequence of characters."
            },
            {
                "question": "Why should edge cases be checked in string problems?",
                "answer": "Empty strings, repeated characters, case differences, spaces and punctuation can change the correct result."
            }
        ],

        "mcqs": [
            {
                "question": "What is the index of the first character in a typical Java string?",
                "options": ["-1", "0", "1", "Depends on the string"],
                "answer": "0",
                "explanation": "Java uses zero-based indexing."
            },
            {
                "question": "Which Java class is mutable and useful for repeated string modifications?",
                "options": ["String", "StringBuilder", "Integer", "Character"],
                "answer": "StringBuilder",
                "explanation": "StringBuilder supports mutable character sequences."
            },
            {
                "question": "Which of these is a palindrome?",
                "options": ["hello", "world", "madam", "code"],
                "answer": "madam",
                "explanation": "madam reads the same in both directions."
            },
            {
                "question": "What is the time complexity of traversing a string of length n?",
                "options": ["O(1)", "O(log n)", "O(n)", "O(n squared)"],
                "answer": "O(n)",
                "explanation": "Every character is visited once."
            },
            {
                "question": "Which technique is commonly used to check anagrams efficiently?",
                "options": ["Binary Search", "Character Frequency Counting", "DFS", "Merge Sort only"],
                "answer": "Character Frequency Counting",
                "explanation": "Anagrams have identical character frequencies."
            },
            {
                "question": "What does Python len(s) return?",
                "options": ["Last index", "Number of characters", "First character", "Memory address"],
                "answer": "Number of characters",
                "explanation": "len() returns the length of the string."
            },
            {
                "question": "Which Python operation reverses a string?",
                "options": ["s.reverse()", "s[::-1]", "reverse(s, 1)", "s[-1:0]"],
                "answer": "s[::-1]",
                "explanation": "A negative step traverses the string backward."
            },
            {
                "question": "Which algorithm uses an LPS array for pattern matching?",
                "options": ["KMP", "Dijkstra", "Prim", "Binary Search"],
                "answer": "KMP",
                "explanation": "KMP uses the longest proper prefix which is also a suffix."
            },
            {
                "question": "What is an anagram of 'listen'?",
                "options": ["silent", "listed", "little", "lines"],
                "answer": "silent",
                "explanation": "Both strings contain the same characters with the same frequencies."
            },
            {
                "question": "What is the auxiliary space complexity of frequency counting with a fixed 26-character array?",
                "options": ["O(n)", "O(1)", "O(n squared)", "O(log n)"],
                "answer": "O(1)",
                "explanation": "The array always has 26 entries, independent of input length."
            }
        ]
    }
})


DSA_TRACK.update({
    "dsa-hashmap": {
        "title": "Hashing, HashMap and HashSet",
        "subtitle": "Fast lookup, frequency counting and duplicate detection",

        "content": """
# 1. What is Hashing?

Hashing is a technique that converts a key into an index or hash value using a hash function.

It helps store and retrieve information efficiently.

For example, suppose we want to store student marks:

Aman -> 85
Riya -> 92
Karan -> 78

Instead of searching through every student record, a hash-based data structure can locate a record using its key.

# 2. What is a HashMap?

A HashMap stores data as key-value pairs.

Example:
{
    "Aman": 85,
    "Riya": 92,
    "Karan": 78
}

Each key is associated with a value.

Important properties:
- Keys are unique.
- Values can be duplicated.
- Lookup is O(1) on average.
- Inserting an entry is O(1) on average.
- Worst-case performance depends on collisions and implementation.

Language equivalents:
- Python: dict
- Java: HashMap
- C++: unordered_map

# 3. What is a HashSet?

A HashSet stores unique elements without storing a separate value for each key.

Example:
{10, 20, 30, 40}

Adding 20 again does not create a duplicate entry.

Language equivalents:
- Python: set
- Java: HashSet
- C++: unordered_set

Common applications:
- Removing duplicates.
- Checking whether an element exists.
- Finding common elements.
- Tracking visited nodes.

# 4. Hash Function

A hash function maps a key to a hash value.

Conceptually:

index = hash(key) % table_size

A good hash function should distribute keys uniformly to reduce collisions.

# 5. Hash Collision

A collision happens when two different keys map to the same hash table location.

Example:
hash(15) % 10 = 5
hash(25) % 10 = 5

Both keys map to index 5.

Common collision handling techniques:

## A. Separate Chaining

Each table position maintains a collection of entries.

When multiple keys map to the same position, they are stored in that collection.

## B. Open Addressing

If a position is occupied, another position is searched.

Common methods:
- Linear probing
- Quadratic probing
- Double hashing

# 6. Important HashMap Operations

Insert or update:
- Python: mp[key] = value
- Java: map.put(key, value)
- C++: mp[key] = value

Search:
- Python: key in mp
- Java: map.containsKey(key)
- C++: mp.find(key) != mp.end()

Retrieve:
- Python: mp.get(key)
- Java: map.get(key)
- C++: mp[key] for an existing key, or find() to avoid inserting a missing key.

Delete:
- Python: mp.pop(key, None)
- Java: map.remove(key)
- C++: mp.erase(key)

# 7. Common Interview Patterns

## A. Frequency Counting

Count how often each number or character occurs.

Example:
[1, 2, 2, 3, 1, 1]

Frequency:
1 -> 3
2 -> 2
3 -> 1

## B. Two Sum

Given an array and a target, find two indices whose values add up to the target.

A HashMap stores previously visited values and their indices.

For each value x:
1. Calculate complement = target - x.
2. Check whether complement exists.
3. If yes, return the two indices.
4. Otherwise store x and its index.

Expected time complexity: O(n).

## C. Duplicate Detection

Use a HashSet to check whether an element has already appeared.

## D. Intersection of Arrays

Store elements from one array in a set and check which elements also occur in the other array.

# 8. HashMap vs HashSet

HashMap:
- Stores key-value pairs.
- Useful for frequency counting and mapping.
- Keys are unique.

HashSet:
- Stores unique elements.
- Useful for membership checking.
- Does not associate separate values with elements.

# 9. Complexity Analysis

For a well-distributed hash table:

- Insert: O(1) average.
- Search: O(1) average.
- Delete: O(1) average.

Worst-case operations can take O(n).

Space complexity for storing n entries is O(n).

# 10. Interview Tips

- Use HashMap for frequency counting.
- Use HashSet for duplicate detection.
- Check whether duplicate keys overwrite previous values.
- Be aware that average O(1) is not a worst-case guarantee.
- Understand how collisions are handled.
- Consider space complexity as well as time complexity.
""",

        "key_concepts": [
            {
                "name": "Hashing",
                "description": "Maps keys to hash values for efficient storage and retrieval."
            },
            {
                "name": "Hash Function",
                "description": "Calculates a hash value from a key."
            },
            {
                "name": "HashMap",
                "description": "Stores unique keys associated with values."
            },
            {
                "name": "HashSet",
                "description": "Stores unique elements without separate mapped values."
            },
            {
                "name": "Collision",
                "description": "Occurs when different keys map to the same hash table location."
            },
            {
                "name": "Separate Chaining",
                "description": "Handles collisions by storing multiple entries in a collection at a table position."
            },
            {
                "name": "Open Addressing",
                "description": "Handles collisions by searching for another available table position."
            },
            {
                "name": "Frequency Counting",
                "description": "Uses a map to track how often each element occurs."
            }
        ],

        "examples": {
            "python": {
                "title": "HashMap and HashSet in Python",
                "code": """# HashMap using dictionary
marks = {
    "Aman": 85,
    "Riya": 92,
    "Karan": 78
}

marks["Aman"] = 90
marks["Neha"] = 88

print("Aman's marks:", marks["Aman"])
print("Riya exists:", "Riya" in marks)

# HashSet
numbers = {10, 20, 30, 20}
numbers.add(40)

print("Unique numbers:", sorted(numbers))

# Frequency counting
arr = [1, 2, 2, 3, 1, 1]
frequency = {}

for num in arr:
    frequency[num] = frequency.get(num, 0) + 1

print("Frequency:", frequency)""",
                "output": """Aman's marks: 90
Riya exists: True
Unique numbers: [10, 20, 30, 40]
Frequency: {1: 3, 2: 2, 3: 1}"""
            },

            "java": {
                "title": "HashMap and HashSet in Java",
                "code": """import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

public class Main {
    public static void main(String[] args) {
        Map<String, Integer> marks = new HashMap<>();

        marks.put("Aman", 85);
        marks.put("Riya", 92);
        marks.put("Karan", 78);

        marks.put("Aman", 90);

        System.out.println("Aman's marks: " + marks.get("Aman"));
        System.out.println("Riya exists: " + marks.containsKey("Riya"));

        Set<Integer> numbers = new HashSet<>();

        numbers.add(10);
        numbers.add(20);
        numbers.add(30);
        numbers.add(20);
        numbers.add(40);

        System.out.println("Unique numbers: " + numbers);

        int[] arr = {1, 2, 2, 3, 1, 1};
        Map<Integer, Integer> frequency = new HashMap<>();

        for (int num : arr) {
            frequency.put(num, frequency.getOrDefault(num, 0) + 1);
        }

        System.out.println("Frequency: " + frequency);
    }
}""",
                "output": """Aman's marks: 90
Riya exists: true
Unique numbers: [20, 40, 10, 30]
Frequency: {1=3, 2=2, 3=1}"""
            },

            "cpp": {
                "title": "unordered_map and unordered_set in C++",
                "code": """#include <iostream>
#include <unordered_map>
#include <unordered_set>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    unordered_map<string, int> marks;

    marks["Aman"] = 85;
    marks["Riya"] = 92;
    marks["Karan"] = 78;

    marks["Aman"] = 90;

    cout << "Aman's marks: " << marks["Aman"] << endl;
    cout << "Riya exists: " << (marks.find("Riya") != marks.end()) << endl;

    unordered_set<int> numbers = {10, 20, 30, 20};
    numbers.insert(40);

    vector<int> uniqueNumbers(numbers.begin(), numbers.end());
    sort(uniqueNumbers.begin(), uniqueNumbers.end());

    cout << "Unique numbers: ";
    for (int num : uniqueNumbers) cout << num << " ";
    cout << endl;

    vector<int> arr = {1, 2, 2, 3, 1, 1};
    unordered_map<int, int> frequency;

    for (int num : arr) {
        frequency[num]++;
    }

    cout << "Frequency of 1: " << frequency[1] << endl;
    cout << "Frequency of 2: " << frequency[2] << endl;
    cout << "Frequency of 3: " << frequency[3] << endl;

    return 0;
}""",
                "output": """Aman's marks: 90
Riya exists: 1
Unique numbers: 10 20 30 40
Frequency of 1: 3
Frequency of 2: 2
Frequency of 3: 1"""
            }
        },

        "dry_run": {
            "title": "Dry Run: Frequency Counting",
            "code": "arr = [1, 2, 2, 3, 1]",
            "steps": [
                {
                    "step": 1,
                    "value": "Read 1",
                    "explanation": "1 is new. Store frequency 1 -> 1."
                },
                {
                    "step": 2,
                    "value": "Read 2",
                    "explanation": "2 is new. Store frequency 2 -> 1."
                },
                {
                    "step": 3,
                    "value": "Read 2",
                    "explanation": "2 already exists. Increase its frequency to 2."
                },
                {
                    "step": 4,
                    "value": "Read 3",
                    "explanation": "3 is new. Store frequency 3 -> 1."
                },
                {
                    "step": 5,
                    "value": "Read 1",
                    "explanation": "1 already exists. Increase its frequency to 2."
                }
            ],
            "result": "1 -> 2, 2 -> 2, 3 -> 1"
        },

        "practice_questions": [
            {
                "question": "Find the indices of two elements whose sum equals the target. Assume exactly one valid answer exists.",
                "difficulty": "Easy",
                "hint": "Store previously visited values and their indices in a HashMap.",
                "solution": {
                    "python": """def two_sum(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[complement], i]

        seen[num] = i

    return []

print(two_sum([2, 7, 11, 15], 9))""",
                    "java": """import java.util.HashMap;
import java.util.Map;
import java.util.Arrays;

public class Main {
    static int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> seen = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];

            if (seen.containsKey(complement)) {
                return new int[]{seen.get(complement), i};
            }

            seen.put(nums[i], i);
        }

        return new int[]{};
    }

    public static void main(String[] args) {
        System.out.println(
            Arrays.toString(twoSum(new int[]{2, 7, 11, 15}, 9))
        );
    }
}""",
                    "cpp": """#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

vector<int> twoSum(vector<int>& nums, int target) {
    unordered_map<int, int> seen;

    for (int i = 0; i < nums.size(); i++) {
        int complement = target - nums[i];

        if (seen.find(complement) != seen.end()) {
            return {seen[complement], i};
        }

        seen[nums[i]] = i;
    }

    return {};
}

int main() {
    vector<int> nums = {2, 7, 11, 15};
    vector<int> result = twoSum(nums, 9);

    cout << result[0] << " " << result[1];
    return 0;
}"""
                },
                "expected_output": "[0, 1]",
                "explanation": "The complement of 7 is 2, which was previously stored at index 0.",
                "complexity": "O(n) expected time and O(n) space."
            },
            {
                "question": "Check whether an array contains any duplicate element.",
                "difficulty": "Easy",
                "hint": "Use a HashSet to track previously seen elements.",
                "solution": {
                    "python": """def contains_duplicate(nums):
    seen = set()

    for num in nums:
        if num in seen:
            return True

        seen.add(num)

    return False

print(contains_duplicate([1, 2, 3, 1]))""",
                    "java": """import java.util.HashSet;
import java.util.Set;

public class Main {
    static boolean containsDuplicate(int[] nums) {
        Set<Integer> seen = new HashSet<>();

        for (int num : nums) {
            if (!seen.add(num)) {
                return true;
            }
        }

        return false;
    }

    public static void main(String[] args) {
        System.out.println(
            containsDuplicate(new int[]{1, 2, 3, 1})
        );
    }
}""",
                    "cpp": """#include <iostream>
#include <unordered_set>
using namespace std;

bool containsDuplicate(int nums[], int n) {
    unordered_set<int> seen;

    for (int i = 0; i < n; i++) {
        if (seen.find(nums[i]) != seen.end()) {
            return true;
        }

        seen.insert(nums[i]);
    }

    return false;
}

int main() {
    int nums[] = {1, 2, 3, 1};
    cout << boolalpha << containsDuplicate(nums, 4);
    return 0;
}"""
                },
                "expected_output": "True",
                "explanation": "The second occurrence of 1 is already present in the set.",
                "complexity": "O(n) expected time and O(n) space."
            },
            {
                "question": "Find the intersection of two arrays and return each common element only once.",
                "difficulty": "Medium",
                "hint": "Store the first array in a set and remove matched elements to avoid duplicate results.",
                "solution": {
                    "python": """def intersection(a, b):
    values = set(a)
    answer = set()

    for num in b:
        if num in values:
            answer.add(num)

    return sorted(answer)

print(intersection([1, 2, 2, 3], [2, 2, 3, 4]))""",
                    "java": """import java.util.HashSet;
import java.util.Set;
import java.util.TreeSet;

public class Main {
    static Set<Integer> intersection(int[] a, int[] b) {
        Set<Integer> values = new HashSet<>();
        Set<Integer> answer = new TreeSet<>();

        for (int num : a) values.add(num);

        for (int num : b) {
            if (values.contains(num)) {
                answer.add(num);
            }
        }

        return answer;
    }

    public static void main(String[] args) {
        int[] a = {1, 2, 2, 3};
        int[] b = {2, 2, 3, 4};

        System.out.println(intersection(a, b));
    }
}""",
                    "cpp": """#include <iostream>
#include <unordered_set>
#include <set>
using namespace std;

set<int> intersection(int a[], int n, int b[], int m) {
    unordered_set<int> values;
    set<int> answer;

    for (int i = 0; i < n; i++) {
        values.insert(a[i]);
    }

    for (int i = 0; i < m; i++) {
        if (values.find(b[i]) != values.end()) {
            answer.insert(b[i]);
        }
    }

    return answer;
}

int main() {
    int a[] = {1, 2, 2, 3};
    int b[] = {2, 2, 3, 4};

    set<int> result = intersection(a, 4, b, 4);

    for (int num : result) cout << num << " ";

    return 0;
}"""
                },
                "expected_output": "[2, 3]",
                "explanation": "2 and 3 occur in both arrays. The result contains each common value once.",
                "complexity": "O(n + m) expected time and O(n + m) space."
            }
        ],

        "interview_questions": [
            {
                "question": "What is hashing?",
                "answer": "Hashing converts a key into a hash value using a hash function to support efficient storage and retrieval."
            },
            {
                "question": "What is a HashMap?",
                "answer": "A HashMap stores data in key-value pairs and provides average O(1) insertion, lookup and deletion."
            },
            {
                "question": "What is a HashSet?",
                "answer": "A HashSet stores unique elements and supports efficient average-time membership checks."
            },
            {
                "question": "What is a hash collision?",
                "answer": "A collision occurs when two different keys map to the same hash table location."
            },
            {
                "question": "How are hash collisions handled?",
                "answer": "Common approaches include separate chaining and open addressing."
            },
            {
                "question": "What is separate chaining?",
                "answer": "It stores multiple entries mapped to the same table position in a collection such as a linked list or bucket."
            },
            {
                "question": "What is open addressing?",
                "answer": "It searches for another available table position when a collision occurs."
            },
            {
                "question": "What is the average lookup complexity of a HashMap?",
                "answer": "O(1) average time, assuming a suitable hash distribution."
            },
            {
                "question": "What is the worst-case lookup complexity of a hash table?",
                "answer": "It can be O(n), depending on collision handling and implementation."
            },
            {
                "question": "Can a HashMap contain duplicate keys?",
                "answer": "No. Adding a value for an existing key updates or replaces its previous value."
            },
            {
                "question": "Can a HashMap contain duplicate values?",
                "answer": "Yes. Different keys can map to the same value."
            },
            {
                "question": "What is the difference between HashMap and HashSet?",
                "answer": "HashMap stores key-value pairs, while HashSet stores unique elements."
            },
            {
                "question": "How can a HashMap solve Two Sum?",
                "answer": "Store previously seen values and indices. For each value, search for its complement in the map."
            },
            {
                "question": "How can you count character frequencies efficiently?",
                "answer": "Traverse the string and increment the corresponding character count in a HashMap."
            },
            {
                "question": "What is load factor in a hash table?",
                "answer": "It is the ratio of stored entries to the number of table buckets. Implementations may resize the table when this factor crosses a threshold."
            }
        ],

        "mcqs": [
            {
                "question": "Which data structure stores key-value pairs?",
                "options": ["Stack", "Queue", "HashMap", "HashSet"],
                "answer": "HashMap",
                "explanation": "A HashMap associates unique keys with values."
            },
            {
                "question": "Which data structure stores only unique elements?",
                "options": ["ArrayList", "HashSet", "Stack", "Queue"],
                "answer": "HashSet",
                "explanation": "A HashSet does not store duplicate elements."
            },
            {
                "question": "What is the average lookup complexity of a well-distributed hash table?",
                "options": ["O(n squared)", "O(log n)", "O(1)", "O(n)"],
                "answer": "O(1)",
                "explanation": "A suitable hash function allows direct average-time lookup."
            },
            {
                "question": "What is a collision?",
                "options": ["Two keys map to the same hash location", "A key is deleted", "A map is sorted", "A value becomes null"],
                "answer": "Two keys map to the same hash location",
                "explanation": "Different keys may produce the same hash table index."
            },
            {
                "question": "Which is a collision-handling technique?",
                "options": ["Binary Search", "Separate Chaining", "Merge Sort", "DFS"],
                "answer": "Separate Chaining",
                "explanation": "Separate chaining stores colliding entries in the same bucket collection."
            },
            {
                "question": "What happens when an existing key is inserted into a Java HashMap with a new value?",
                "options": ["A duplicate key is created", "The old value is replaced", "The map is cleared", "An exception always occurs"],
                "answer": "The old value is replaced",
                "explanation": "Keys in a HashMap are unique."
            },
            {
                "question": "Which Python data structure corresponds most closely to a HashMap?",
                "options": ["list", "tuple", "dict", "str"],
                "answer": "dict",
                "explanation": "Python dictionaries store key-value pairs."
            },
            {
                "question": "Which C++ container is commonly used as a hash map?",
                "options": ["map", "unordered_map", "stack", "vector"],
                "answer": "unordered_map",
                "explanation": "unordered_map uses hashing to store key-value pairs."
            },
            {
                "question": "Which data structure is most suitable for duplicate detection?",
                "options": ["HashSet", "Queue", "Stack", "Linked List"],
                "answer": "HashSet",
                "explanation": "A set efficiently tracks whether an element has already appeared."
            },
            {
                "question": "What is the expected time complexity of the HashMap-based Two Sum solution?",
                "options": ["O(n squared)", "O(log n)", "O(n)", "O(1)"],
                "answer": "O(n)",
                "explanation": "Each array element is processed once with expected constant-time map operations."
            }
        ]
    }
})


DSA_TRACK.update({
    "dsa-binary-search": {
        "title": "Binary Search",
        "subtitle": "Efficient searching in sorted data",

        "content": """
# 1. What is Binary Search?

Binary Search is an efficient searching algorithm used to find an element in a sorted array.

Instead of checking every element one by one, it repeatedly divides the search space into two halves.

It compares the target with the middle element.

Three possibilities:
1. If the middle element equals the target, return its index.
2. If the target is smaller, search the left half.
3. If the target is larger, search the right half.

# 2. Why do we use Binary Search?

Consider a sorted array:

[10, 20, 30, 40, 50, 60, 70]

Suppose we want to find 60.

Linear Search may check multiple elements sequentially.

Binary Search:
- Middle element is 40.
- 60 is greater than 40, so discard the left half.
- Search [50, 60, 70].
- Middle element is 60.
- Target found.

Binary Search takes O(log n) time.

# 3. Important Conditions

- The data must be sorted for ordinary binary search.
- Maintain correct left and right boundaries.
- Update the search range in every iteration.
- Handle the case when the target does not exist.
- Avoid incorrect midpoint calculations in languages with integer overflow.

# 4. Binary Search Algorithm

Initialize:
left = 0
right = n - 1

While left <= right:

1. Calculate mid = left + (right - left) // 2.
2. If arr[mid] == target, return mid.
3. If arr[mid] < target, set left = mid + 1.
4. Otherwise, set right = mid - 1.

If the loop finishes, return -1.

# 5. Complexity Analysis

Best case: O(1), when the middle element is the target.

Average case: O(log n).

Worst case: O(log n).

Iterative space complexity: O(1).

Recursive space complexity: O(log n), due to the recursion call stack.

# 6. Lower Bound and Upper Bound

Lower Bound:
Returns the first position where an element is greater than or equal to the target.

Upper Bound:
Returns the first position where an element is strictly greater than the target.

Example:

Array: [1, 2, 2, 2, 4, 5]
Target: 2

Lower Bound = index 1
Upper Bound = index 4

These concepts are useful for:
- Finding the first occurrence.
- Finding the last occurrence.
- Counting occurrences.
- Searching insertion positions.

# 7. Binary Search on Answer

Binary Search can also solve problems where the answer is a number rather than an array index.

Examples:
- Minimum capacity required to ship packages.
- Minimum speed required to finish a task.
- Minimum maximum workload.
- Square root of a number.

The key condition is that the answer space must have a suitable monotonic property.

For example, if a capacity works, every larger capacity may also work. We can binary search for the smallest working capacity.

# 8. Common Binary Search Variations

- Search in a sorted array.
- First occurrence of an element.
- Last occurrence of an element.
- Search in a rotated sorted array.
- Find the insertion position.
- Find the peak element.
- Binary search on answer.

# 9. Common Mistakes

1. Applying ordinary binary search to unsorted data.
2. Using left < right when left <= right is required.
3. Forgetting to update left or right.
4. Returning mid incorrectly.
5. Not handling an absent target.
6. Using an incorrect midpoint calculation.
7. Confusing lower bound with upper bound.

# 10. Interview Tip

Always explain why the search space can be discarded.

Do not just memorize the code. Understand the condition that tells you which half cannot contain the answer.
""",

        "key_concepts": [
            {
                "name": "Sorted Array",
                "description": "Binary search requires sorted data for its standard implementation."
            },
            {
                "name": "Middle Element",
                "description": "The element at the midpoint of the current search range."
            },
            {
                "name": "Search Space",
                "description": "The portion of the array that may still contain the target."
            },
            {
                "name": "Lower Bound",
                "description": "The first position containing an element greater than or equal to the target."
            },
            {
                "name": "Upper Bound",
                "description": "The first position containing an element strictly greater than the target."
            },
            {
                "name": "Binary Search on Answer",
                "description": "Searches a monotonic range of possible answers instead of array indices."
            },
            {
                "name": "Monotonic Property",
                "description": "A condition that changes in one direction, allowing half of the search space to be eliminated."
            }
        ],

        "examples": {
            "python": {
                "title": "Iterative Binary Search in Python",
                "code": """def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return -1


arr = [10, 20, 30, 40, 50, 60, 70]
target = 60

print("Target index:", binary_search(arr, target))""",
                "output": "Target index: 5"
            },

            "java": {
                "title": "Iterative Binary Search in Java",
                "code": """public class Main {

    static int binarySearch(int[] arr, int target) {
        int left = 0;
        int right = arr.length - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2;

            if (arr[mid] == target) {
                return mid;
            } else if (arr[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        return -1;
    }

    public static void main(String[] args) {
        int[] arr = {10, 20, 30, 40, 50, 60, 70};

        System.out.println(
            "Target index: " + binarySearch(arr, 60)
        );
    }
}""",
                "output": "Target index: 5"
            },

            "cpp": {
                "title": "Iterative Binary Search in C++",
                "code": """#include <iostream>
#include <vector>
using namespace std;

int binarySearch(vector<int>& arr, int target) {
    int left = 0;
    int right = arr.size() - 1;

    while (left <= right) {
        int mid = left + (right - left) / 2;

        if (arr[mid] == target) {
            return mid;
        }
        else if (arr[mid] < target) {
            left = mid + 1;
        }
        else {
            right = mid - 1;
        }
    }

    return -1;
}

int main() {
    vector<int> arr = {10, 20, 30, 40, 50, 60, 70};

    cout << "Target index: " << binarySearch(arr, 60);

    return 0;
}""",
                "output": "Target index: 5"
            }
        },

        "dry_run": {
            "title": "Dry Run: Search for 60",
            "code": "arr = [10, 20, 30, 40, 50, 60, 70], target = 60",
            "steps": [
                {
                    "step": 1,
                    "value": "left = 0, right = 6, mid = 3",
                    "explanation": "arr[3] = 40. Since 60 > 40, search the right half. Set left = 4."
                },
                {
                    "step": 2,
                    "value": "left = 4, right = 6, mid = 5",
                    "explanation": "arr[5] = 60. The target has been found."
                }
            ],
            "result": "Target found at index 5."
        },

        "practice_questions": [
            {
                "question": "Given a sorted array of distinct integers, return the index of the target. Return -1 if it is absent.",
                "difficulty": "Easy",
                "hint": "Use left, right and mid pointers to repeatedly eliminate half of the search space.",
                "solution": {
                    "python": """def search(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

print(search([-1, 0, 3, 5, 9, 12], 9))""",
                    "java": """public class Main {
    static int search(int[] nums, int target) {
        int left = 0, right = nums.length - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2;

            if (nums[mid] == target) return mid;
            else if (nums[mid] < target) left = mid + 1;
            else right = mid - 1;
        }

        return -1;
    }

    public static void main(String[] args) {
        int[] nums = {-1, 0, 3, 5, 9, 12};
        System.out.println(search(nums, 9));
    }
}""",
                    "cpp": """#include <iostream>
#include <vector>
using namespace std;

int search(vector<int>& nums, int target) {
    int left = 0, right = nums.size() - 1;

    while (left <= right) {
        int mid = left + (right - left) / 2;

        if (nums[mid] == target) return mid;
        else if (nums[mid] < target) left = mid + 1;
        else right = mid - 1;
    }

    return -1;
}

int main() {
    vector<int> nums = {-1, 0, 3, 5, 9, 12};
    cout << search(nums, 9);
    return 0;
}"""
                },
                "expected_output": "4",
                "explanation": "The target 9 is present at index 4.",
                "complexity": "O(log n) time and O(1) auxiliary space."
            },
            {
                "question": "Find the first and last occurrence of a target in a sorted array that may contain duplicates.",
                "difficulty": "Medium",
                "hint": "Perform binary search twice. When the target is found, continue searching towards the appropriate boundary.",
                "solution": {
                    "python": """def search_range(nums, target):
    def boundary(find_first):
        left, right = 0, len(nums) - 1
        answer = -1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                answer = mid

                if find_first:
                    right = mid - 1
                else:
                    left = mid + 1

            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return answer

    return [boundary(True), boundary(False)]

print(search_range([5, 7, 7, 8, 8, 10], 8))""",
                    "java": """import java.util.Arrays;

public class Main {
    static int boundary(int[] nums, int target, boolean first) {
        int left = 0, right = nums.length - 1;
        int answer = -1;

        while (left <= right) {
            int mid = left + (right - left) / 2;

            if (nums[mid] == target) {
                answer = mid;

                if (first) right = mid - 1;
                else left = mid + 1;
            }
            else if (nums[mid] < target) {
                left = mid + 1;
            }
            else {
                right = mid - 1;
            }
        }

        return answer;
    }

    static int[] searchRange(int[] nums, int target) {
        return new int[]{
            boundary(nums, target, true),
            boundary(nums, target, false)
        };
    }

    public static void main(String[] args) {
        int[] nums = {5, 7, 7, 8, 8, 10};
        System.out.println(Arrays.toString(searchRange(nums, 8)));
    }
}""",
                    "cpp": """#include <iostream>
#include <vector>
using namespace std;

int boundary(vector<int>& nums, int target, bool first) {
    int left = 0, right = nums.size() - 1;
    int answer = -1;

    while (left <= right) {
        int mid = left + (right - left) / 2;

        if (nums[mid] == target) {
            answer = mid;

            if (first) right = mid - 1;
            else left = mid + 1;
        }
        else if (nums[mid] < target) {
            left = mid + 1;
        }
        else {
            right = mid - 1;
        }
    }

    return answer;
}

int main() {
    vector<int> nums = {5, 7, 7, 8, 8, 10};

    cout << boundary(nums, 8, true) << " "
         << boundary(nums, 8, false);

    return 0;
}"""
                },
                "expected_output": "[3, 4]",
                "explanation": "The first occurrence of 8 is at index 3 and the last occurrence is at index 4.",
                "complexity": "O(log n) time and O(1) auxiliary space."
            },
            {
                "question": "Search for a target in a rotated sorted array containing distinct elements. Return its index or -1.",
                "difficulty": "Medium",
                "hint": "At least one half of the current search range is always sorted. Identify that half and check whether the target lies inside it.",
                "solution": {
                    "python": """def search_rotated(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid

        # Left half is sorted
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        # Right half is sorted
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1

print(search_rotated([4, 5, 6, 7, 0, 1, 2], 0))""",
                    "java": """public class Main {
    static int search(int[] nums, int target) {
        int left = 0, right = nums.length - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2;

            if (nums[mid] == target) return mid;

            if (nums[left] <= nums[mid]) {
                if (nums[left] <= target && target < nums[mid]) {
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            } else {
                if (nums[mid] < target && target <= nums[right]) {
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            }
        }

        return -1;
    }

    public static void main(String[] args) {
        int[] nums = {4, 5, 6, 7, 0, 1, 2};
        System.out.println(search(nums, 0));
    }
}""",
                    "cpp": """#include <iostream>
#include <vector>
using namespace std;

int search(vector<int>& nums, int target) {
    int left = 0, right = nums.size() - 1;

    while (left <= right) {
        int mid = left + (right - left) / 2;

        if (nums[mid] == target) return mid;

        if (nums[left] <= nums[mid]) {
            if (nums[left] <= target && target < nums[mid]) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        } else {
            if (nums[mid] < target && target <= nums[right]) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
    }

    return -1;
}

int main() {
    vector<int> nums = {4, 5, 6, 7, 0, 1, 2};
    cout << search(nums, 0);
    return 0;
}"""
                },
                "expected_output": "4",
                "explanation": "The target 0 is present at index 4. The algorithm identifies the sorted half at each step.",
                "complexity": "O(log n) time and O(1) auxiliary space."
            }
        ],

        "interview_questions": [
            {
                "question": "What is Binary Search?",
                "answer": "Binary Search is a searching algorithm that repeatedly divides a sorted search space into halves."
            },
            {
                "question": "What is the time complexity of Binary Search?",
                "answer": "O(log n) in average and worst cases."
            },
            {
                "question": "What is the best-case complexity?",
                "answer": "O(1), when the target is found at the first middle position."
            },
            {
                "question": "Why does Binary Search require sorted data?",
                "answer": "Sorting allows us to determine which half cannot contain the target and safely discard it."
            },
            {
                "question": "What is the space complexity of iterative Binary Search?",
                "answer": "O(1), because it uses only a fixed number of variables."
            },
            {
                "question": "What is the space complexity of recursive Binary Search?",
                "answer": "O(log n), because recursive calls use the call stack."
            },
            {
                "question": "How is the middle index calculated safely?",
                "answer": "Use mid = left + (right - left) / 2 to reduce the risk of integer overflow."
            },
            {
                "question": "What is the difference between lower bound and upper bound?",
                "answer": "Lower bound finds the first element greater than or equal to the target. Upper bound finds the first element strictly greater than it."
            },
            {
                "question": "How do you find the first occurrence of a duplicate element?",
                "answer": "When the target is found, store its index and continue searching the left half."
            },
            {
                "question": "How do you find the last occurrence?",
                "answer": "When the target is found, store its index and continue searching the right half."
            },
            {
                "question": "Can Binary Search be applied to a rotated sorted array?",
                "answer": "Yes. Identify the sorted half and determine whether the target belongs to that half."
            },
            {
                "question": "What is Binary Search on Answer?",
                "answer": "It searches a range of possible numerical answers when a monotonic feasibility condition exists."
            },
            {
                "question": "What is a monotonic search condition?",
                "answer": "It is a condition whose result changes in only one direction across the candidate range, such as false to true."
            },
            {
                "question": "How can Binary Search find the square root of a number?",
                "answer": "Search the integer range from 0 to the number and compare mid * mid with the given number, using a wider numeric type where necessary."
            },
            {
                "question": "When is Linear Search preferable to Binary Search?",
                "answer": "For small datasets, unsorted data, or when sorting would cost more than the search itself."
            }
        ],

        "mcqs": [
            {
                "question": "Binary Search is primarily applied to which type of array?",
                "options": ["Unsorted array", "Sorted array", "Random array only", "Empty array only"],
                "answer": "Sorted array",
                "explanation": "The standard algorithm relies on sorted order."
            },
            {
                "question": "What is the worst-case time complexity of Binary Search?",
                "options": ["O(n)", "O(n squared)", "O(log n)", "O(1)"],
                "answer": "O(log n)",
                "explanation": "The search space is halved in every iteration."
            },
            {
                "question": "What is the best-case time complexity?",
                "options": ["O(n)", "O(log n)", "O(1)", "O(n log n)"],
                "answer": "O(1)",
                "explanation": "The target may be found at the first midpoint."
            },
            {
                "question": "What is the iterative space complexity?",
                "options": ["O(n)", "O(log n)", "O(1)", "O(n squared)"],
                "answer": "O(1)",
                "explanation": "Only a fixed number of variables are used."
            },
            {
                "question": "If an array has 64 elements, approximately how many halvings are needed to reduce the search space to one element?",
                "options": ["4", "6", "8", "64"],
                "answer": "6",
                "explanation": "64 -> 32 -> 16 -> 8 -> 4 -> 2 -> 1 requires six halvings."
            },
            {
                "question": "What should happen when arr[mid] is smaller than the target?",
                "options": ["right = mid - 1", "left = mid + 1", "Stop immediately", "Sort the array"],
                "answer": "left = mid + 1",
                "explanation": "The target, if present, must be in the right half."
            },
            {
                "question": "What does a lower bound return?",
                "options": ["Last element smaller than target", "First element greater than target", "First element greater than or equal to target", "Always the middle index"],
                "answer": "First element greater than or equal to target",
                "explanation": "Lower bound identifies the first position that is not smaller than the target."
            },
            {
                "question": "What does an upper bound return?",
                "options": ["First element strictly greater than target", "First equal element", "Last equal element", "First smaller element"],
                "answer": "First element strictly greater than target",
                "explanation": "Upper bound skips all occurrences equal to the target."
            },
            {
                "question": "Which condition is commonly used in iterative Binary Search?",
                "options": ["left <= right", "left == right only", "left > right", "mid == 0"],
                "answer": "left <= right",
                "explanation": "This allows the algorithm to inspect a search range containing one element."
            },
            {
                "question": "Which expression helps avoid midpoint addition overflow?",
                "options": ["(left + right) * 2", "left + (right - left) / 2", "right - left * 2", "left / right"],
                "answer": "left + (right - left) / 2",
                "explanation": "It avoids directly adding two potentially large indices."
            }
        ]
    }
})


DSA_TRACK.update({
    "dsa-sorting": {
        "title": "Sorting Algorithms",
        "subtitle": "Arrange data efficiently using different sorting techniques",

        "content": """
# 1. What is Sorting?

Sorting is the process of arranging elements in a particular order.

Ascending order:
[5, 2, 8, 1, 3] -> [1, 2, 3, 5, 8]

Descending order:
[5, 2, 8, 1, 3] -> [8, 5, 3, 2, 1]

Sorting makes searching, comparison and data processing easier.

# 2. Bubble Sort

Bubble Sort repeatedly compares adjacent elements and swaps them if they are in the wrong order.

Example:
[5, 3, 2, 4]

Pass 1:
[3, 5, 2, 4]
[3, 2, 5, 4]
[3, 2, 4, 5]

The largest element reaches the last position.

Complexity:
- Best: O(n), with an early-exit optimization.
- Average: O(n²).
- Worst: O(n²).
- Space: O(1).

Bubble Sort is stable and in-place.

# 3. Selection Sort

Selection Sort repeatedly finds the smallest element from the unsorted portion and places it at the beginning.

Example:
[5, 3, 2, 4]

Find minimum 2 and swap with 5:
[2, 3, 5, 4]

Find minimum in remaining portion:
[2, 3, 4, 5]

Complexity:
- Best: O(n²).
- Average: O(n²).
- Worst: O(n²).
- Space: O(1).

Standard selection sort is generally not stable.

# 4. Insertion Sort

Insertion Sort builds a sorted portion one element at a time.

It takes each new element and inserts it into its correct position.

Example:
[5, 3, 4, 1]

Insert 3:
[3, 5, 4, 1]

Insert 4:
[3, 4, 5, 1]

Insert 1:
[1, 3, 4, 5]

Complexity:
- Best: O(n), when already sorted.
- Average: O(n²).
- Worst: O(n²).
- Space: O(1).

Insertion Sort is stable and in-place.

It works well for small or nearly sorted arrays.

# 5. Merge Sort

Merge Sort uses the Divide and Conquer technique.

Steps:
1. Divide the array into two halves.
2. Recursively sort both halves.
3. Merge the sorted halves.

Example:
[8, 3, 5, 2]

Divide:
[8, 3] and [5, 2]

Divide again:
[8], [3], [5], [2]

Merge:
[3, 8] and [2, 5]

Final merge:
[2, 3, 5, 8]

Complexity:
- Best: O(n log n).
- Average: O(n log n).
- Worst: O(n log n).
- Auxiliary space: O(n) for arrays.

Merge Sort is stable when equal elements are merged carefully.

# 6. Quick Sort

Quick Sort also uses Divide and Conquer.

Steps:
1. Choose a pivot element.
2. Partition the array around the pivot.
3. Place smaller elements on one side and larger elements on the other.
4. Recursively sort both partitions.

Complexity:
- Best: O(n log n).
- Average: O(n log n).
- Worst: O(n²).
- Average auxiliary stack space: O(log n).
- Worst auxiliary stack space: O(n).

Quick Sort is generally not stable.

Its performance depends on pivot selection and partitioning.

# 7. Counting Sort

Counting Sort is a non-comparison-based sorting algorithm.

It counts how many times each value occurs.

Example:
[4, 2, 2, 1, 3]

Frequencies:
1 -> 1
2 -> 2
3 -> 1
4 -> 1

Reconstruct:
[1, 2, 2, 3, 4]

Complexity:
- Time: O(n + k).
- Space: O(k), for the basic frequency-array implementation.

Here k is the size of the value range.

It is useful when integer values have a reasonably small range.

# 8. Sorting Algorithm Comparison

Bubble Sort:
- Best O(n), average O(n²), worst O(n²).
- Stable.
- In-place.

Selection Sort:
- Best O(n²), average O(n²), worst O(n²).
- Usually unstable.
- In-place.

Insertion Sort:
- Best O(n), average O(n²), worst O(n²).
- Stable.
- In-place.

Merge Sort:
- Best O(n log n), average O(n log n), worst O(n log n).
- Stable.
- Usually requires O(n) auxiliary space for arrays.

Quick Sort:
- Best O(n log n), average O(n log n), worst O(n²).
- Usually unstable.
- Average auxiliary stack space O(log n).

Counting Sort:
- O(n + k) time.
- Can be stable in its cumulative-counting form.
- Requires extra space.

# 9. Important Sorting Terms

Stable sorting:
Equal elements retain their relative order.

In-place sorting:
Uses very little additional memory, usually O(1) auxiliary space.

Adaptive sorting:
Takes advantage of existing order in the input.

Comparison-based sorting:
Determines order through comparisons between elements.

Divide and Conquer:
Breaks a problem into smaller subproblems, solves them, and combines the results.

# 10. Which Sorting Algorithm Should You Use?

- Small or nearly sorted data: Insertion Sort.
- Guaranteed O(n log n) time: Merge Sort or Heap Sort.
- Practical general-purpose in-memory sorting: Quick Sort or optimized variants.
- Small range of non-negative integers: Counting Sort.
- Learning adjacent swaps: Bubble Sort.
- Learning minimum selection: Selection Sort.

# 11. Interview Tips

- Understand why Merge Sort has O(n log n) complexity.
- Explain why Quick Sort can degrade to O(n²).
- Know the difference between stable and unstable sorting.
- Compare auxiliary space requirements.
- Understand when non-comparison sorting is useful.
""",

        "key_concepts": [
            {
                "name": "Bubble Sort",
                "description": "Repeatedly swaps adjacent elements that are in the wrong order."
            },
            {
                "name": "Selection Sort",
                "description": "Selects the smallest remaining element and places it in its correct position."
            },
            {
                "name": "Insertion Sort",
                "description": "Builds a sorted portion by inserting each new element at its correct position."
            },
            {
                "name": "Merge Sort",
                "description": "Uses divide and conquer to recursively sort and merge smaller arrays."
            },
            {
                "name": "Quick Sort",
                "description": "Partitions data around a pivot and recursively sorts the partitions."
            },
            {
                "name": "Counting Sort",
                "description": "Sorts integer values using their frequencies instead of pairwise comparisons."
            },
            {
                "name": "Stable Sorting",
                "description": "Preserves the relative order of elements with equal sorting keys."
            },
            {
                "name": "In-place Sorting",
                "description": "Uses constant or very small auxiliary memory."
            }
        ],

        "examples": {
            "python": {
                "title": "Bubble, Insertion and Merge Sort in Python",
                "code": """def bubble_sort(arr):
    arr = arr.copy()
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break

    return arr


def insertion_sort(arr):
    arr = arr.copy()

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


numbers = [5, 3, 8, 1, 2]

print("Bubble:", bubble_sort(numbers))
print("Insertion:", insertion_sort(numbers))
print("Merge:", merge_sort(numbers))""",
                "output": """Bubble: [1, 2, 3, 5, 8]
Insertion: [1, 2, 3, 5, 8]
Merge: [1, 2, 3, 5, 8]"""
            },

            "java": {
                "title": "Bubble, Insertion and Merge Sort in Java",
                "code": """import java.util.Arrays;

public class Main {

    static void bubbleSort(int[] arr) {
        int n = arr.length;

        for (int i = 0; i < n; i++) {
            boolean swapped = false;

            for (int j = 0; j < n - i - 1; j++) {
                if (arr[j] > arr[j + 1]) {
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                    swapped = true;
                }
            }

            if (!swapped) break;
        }
    }

    static void insertionSort(int[] arr) {
        for (int i = 1; i < arr.length; i++) {
            int key = arr[i];
            int j = i - 1;

            while (j >= 0 && arr[j] > key) {
                arr[j + 1] = arr[j];
                j--;
            }

            arr[j + 1] = key;
        }
    }

    static void merge(int[] arr, int left, int mid, int right) {
        int[] temp = new int[right - left + 1];

        int i = left, j = mid + 1, k = 0;

        while (i <= mid && j <= right) {
            if (arr[i] <= arr[j]) {
                temp[k++] = arr[i++];
            } else {
                temp[k++] = arr[j++];
            }
        }

        while (i <= mid) temp[k++] = arr[i++];
        while (j <= right) temp[k++] = arr[j++];

        for (int p = 0; p < temp.length; p++) {
            arr[left + p] = temp[p];
        }
    }

    static void mergeSort(int[] arr, int left, int right) {
        if (left >= right) return;

        int mid = left + (right - left) / 2;

        mergeSort(arr, left, mid);
        mergeSort(arr, mid + 1, right);

        merge(arr, left, mid, right);
    }

    public static void main(String[] args) {
        int[] a = {5, 3, 8, 1, 2};
        int[] b = a.clone();
        int[] c = a.clone();

        bubbleSort(a);
        insertionSort(b);
        mergeSort(c, 0, c.length - 1);

        System.out.println("Bubble: " + Arrays.toString(a));
        System.out.println("Insertion: " + Arrays.toString(b));
        System.out.println("Merge: " + Arrays.toString(c));
    }
}""",
                "output": """Bubble: [1, 2, 3, 5, 8]
Insertion: [1, 2, 3, 5, 8]
Merge: [1, 2, 3, 5, 8]"""
            },

            "cpp": {
                "title": "Bubble, Insertion and Merge Sort in C++",
                "code": """#include <iostream>
#include <vector>
using namespace std;

void bubbleSort(vector<int>& a) {
    int n = a.size();

    for (int i = 0; i < n; i++) {
        bool swapped = false;

        for (int j = 0; j < n - i - 1; j++) {
            if (a[j] > a[j + 1]) {
                swap(a[j], a[j + 1]);
                swapped = true;
            }
        }

        if (!swapped) break;
    }
}

void insertionSort(vector<int>& a) {
    for (int i = 1; i < a.size(); i++) {
        int key = a[i];
        int j = i - 1;

        while (j >= 0 && a[j] > key) {
            a[j + 1] = a[j];
            j--;
        }

        a[j + 1] = key;
    }
}

void merge(vector<int>& a, int left, int mid, int right) {
    vector<int> temp;

    int i = left, j = mid + 1;

    while (i <= mid && j <= right) {
        if (a[i] <= a[j]) temp.push_back(a[i++]);
        else temp.push_back(a[j++]);
    }

    while (i <= mid) temp.push_back(a[i++]);
    while (j <= right) temp.push_back(a[j++]);

    for (int k = 0; k < temp.size(); k++) {
        a[left + k] = temp[k];
    }
}

void mergeSort(vector<int>& a, int left, int right) {
    if (left >= right) return;

    int mid = left + (right - left) / 2;

    mergeSort(a, left, mid);
    mergeSort(a, mid + 1, right);

    merge(a, left, mid, right);
}

void display(const vector<int>& a) {
    for (int x : a) cout << x << " ";
    cout << endl;
}

int main() {
    vector<int> a = {5, 3, 8, 1, 2};
    vector<int> b = a;
    vector<int> c = a;

    bubbleSort(a);
    insertionSort(b);
    mergeSort(c, 0, c.size() - 1);

    cout << "Bubble: ";
    display(a);

    cout << "Insertion: ";
    display(b);

    cout << "Merge: ";
    display(c);

    return 0;
}""",
                "output": """Bubble: 1 2 3 5 8
Insertion: 1 2 3 5 8
Merge: 1 2 3 5 8"""
            }
        },

        "dry_run": {
            "title": "Dry Run: Bubble Sort",
            "code": "arr = [5, 3, 2, 4]",
            "steps": [
                {
                    "step": 1,
                    "value": "[3, 5, 2, 4]",
                    "explanation": "Compare 5 and 3. Swap because 5 is greater."
                },
                {
                    "step": 2,
                    "value": "[3, 2, 5, 4]",
                    "explanation": "Compare 5 and 2. Swap."
                },
                {
                    "step": 3,
                    "value": "[3, 2, 4, 5]",
                    "explanation": "Compare 5 and 4. Swap. The largest element is now at the end."
                },
                {
                    "step": 4,
                    "value": "[2, 3, 4, 5]",
                    "explanation": "The next pass swaps 3 and 2. Remaining elements are in sorted order."
                }
            ],
            "result": "[2, 3, 4, 5]"
        },

        "practice_questions": [
            {
                "question": "Sort an integer array in ascending order using Insertion Sort.",
                "difficulty": "Easy",
                "hint": "Maintain a sorted left portion and insert each next element into its correct position.",
                "solution": {
                    "python": """def insertion_sort(nums):
    nums = nums.copy()

    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1

        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j -= 1

        nums[j + 1] = key

    return nums

print(insertion_sort([5, 2, 4, 1, 3]))""",
                    "java": """import java.util.Arrays;

public class Main {
    static void insertionSort(int[] nums) {
        for (int i = 1; i < nums.length; i++) {
            int key = nums[i];
            int j = i - 1;

            while (j >= 0 && nums[j] > key) {
                nums[j + 1] = nums[j];
                j--;
            }

            nums[j + 1] = key;
        }
    }

    public static void main(String[] args) {
        int[] nums = {5, 2, 4, 1, 3};
        insertionSort(nums);
        System.out.println(Arrays.toString(nums));
    }
}""",
                    "cpp": """#include <iostream>
#include <vector>
using namespace std;

void insertionSort(vector<int>& nums) {
    for (int i = 1; i < nums.size(); i++) {
        int key = nums[i];
        int j = i - 1;

        while (j >= 0 && nums[j] > key) {
            nums[j + 1] = nums[j];
            j--;
        }

        nums[j + 1] = key;
    }
}

int main() {
    vector<int> nums = {5, 2, 4, 1, 3};
    insertionSort(nums);

    for (int x : nums) cout << x << " ";
    return 0;
}"""
                },
                "expected_output": "[1, 2, 3, 4, 5]",
                "explanation": "Each element is inserted into its correct position in the already sorted portion.",
                "complexity": "O(n squared) average and worst-case time, O(n) best-case time, O(1) auxiliary space."
            },
            {
                "question": "Merge two sorted arrays into one sorted array.",
                "difficulty": "Easy",
                "hint": "Use two pointers, compare their current elements, and append the smaller one.",
                "solution": {
                    "python": """def merge_sorted(a, b):
    i = j = 0
    result = []

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1

    result.extend(a[i:])
    result.extend(b[j:])

    return result

print(merge_sorted([1, 3, 5], [2, 4, 6]))""",
                    "java": """import java.util.Arrays;

public class Main {
    static int[] mergeSorted(int[] a, int[] b) {
        int[] result = new int[a.length + b.length];

        int i = 0, j = 0, k = 0;

        while (i < a.length && j < b.length) {
            if (a[i] <= b[j]) result[k++] = a[i++];
            else result[k++] = b[j++];
        }

        while (i < a.length) result[k++] = a[i++];
        while (j < b.length) result[k++] = b[j++];

        return result;
    }

    public static void main(String[] args) {
        System.out.println(Arrays.toString(
            mergeSorted(new int[]{1, 3, 5}, new int[]{2, 4, 6})
        ));
    }
}""",
                    "cpp": """#include <iostream>
#include <vector>
using namespace std;

vector<int> mergeSorted(vector<int>& a, vector<int>& b) {
    vector<int> result;
    int i = 0, j = 0;

    while (i < a.size() && j < b.size()) {
        if (a[i] <= b[j]) result.push_back(a[i++]);
        else result.push_back(b[j++]);
    }

    while (i < a.size()) result.push_back(a[i++]);
    while (j < b.size()) result.push_back(b[j++]);

    return result;
}

int main() {
    vector<int> a = {1, 3, 5};
    vector<int> b = {2, 4, 6};

    vector<int> result = mergeSorted(a, b);

    for (int x : result) cout << x << " ";
    return 0;
}"""
                },
                "expected_output": "[1, 2, 3, 4, 5, 6]",
                "explanation": "The two pointers always select the smallest remaining element.",
                "complexity": "O(n + m) time and O(n + m) output space."
            },
            {
                "question": "Sort an array containing only 0, 1 and 2 without using a built-in sorting function.",
                "difficulty": "Medium",
                "hint": "Use the Dutch National Flag algorithm with low, mid and high pointers.",
                "solution": {
                    "python": """def sort_colors(nums):
    low, mid, high = 0, 0, len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1

        elif nums[mid] == 1:
            mid += 1

        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1

    return nums

print(sort_colors([2, 0, 2, 1, 1, 0]))""",
                    "java": """import java.util.Arrays;

public class Main {
    static void sortColors(int[] nums) {
        int low = 0, mid = 0, high = nums.length - 1;

        while (mid <= high) {
            if (nums[mid] == 0) {
                int temp = nums[low];
                nums[low] = nums[mid];
                nums[mid] = temp;

                low++;
                mid++;
            }
            else if (nums[mid] == 1) {
                mid++;
            }
            else {
                int temp = nums[mid];
                nums[mid] = nums[high];
                nums[high] = temp;

                high--;
            }
        }
    }

    public static void main(String[] args) {
        int[] nums = {2, 0, 2, 1, 1, 0};
        sortColors(nums);
        System.out.println(Arrays.toString(nums));
    }
}""",
                    "cpp": """#include <iostream>
#include <vector>
using namespace std;

void sortColors(vector<int>& nums) {
    int low = 0, mid = 0, high = nums.size() - 1;

    while (mid <= high) {
        if (nums[mid] == 0) {
            swap(nums[low], nums[mid]);
            low++;
            mid++;
        }
        else if (nums[mid] == 1) {
            mid++;
        }
        else {
            swap(nums[mid], nums[high]);
            high--;
        }
    }
}

int main() {
    vector<int> nums = {2, 0, 2, 1, 1, 0};
    sortColors(nums);

    for (int x : nums) cout << x << " ";
    return 0;
}"""
                },
                "expected_output": "[0, 0, 1, 1, 2, 2]",
                "explanation": "The low region contains 0s, the middle region contains 1s, and the high region contains 2s. The middle pointer processes the unknown region.",
                "complexity": "O(n) time and O(1) auxiliary space."
            }
        ],

        "interview_questions": [
            {
                "question": "What is sorting?",
                "answer": "Sorting arranges data in a specified order, such as ascending or descending."
            },
            {
                "question": "What is Bubble Sort?",
                "answer": "It repeatedly compares adjacent elements and swaps them when they are in the wrong order."
            },
            {
                "question": "What is the worst-case time complexity of Bubble Sort?",
                "answer": "O(n squared)."
            },
            {
                "question": "What is Selection Sort?",
                "answer": "It repeatedly selects the minimum element from the unsorted part and places it at the next sorted position."
            },
            {
                "question": "What is the time complexity of Selection Sort?",
                "answer": "O(n squared) in best, average and worst cases."
            },
            {
                "question": "What is Insertion Sort?",
                "answer": "It builds a sorted portion by inserting each new element at its correct position."
            },
            {
                "question": "When is Insertion Sort useful?",
                "answer": "It is useful for small or nearly sorted datasets."
            },
            {
                "question": "Explain Merge Sort.",
                "answer": "Merge Sort divides the array, recursively sorts both halves and merges the sorted results."
            },
            {
                "question": "What is Merge Sort's time complexity?",
                "answer": "O(n log n) in best, average and worst cases."
            },
            {
                "question": "What is Quick Sort?",
                "answer": "Quick Sort selects a pivot, partitions the array and recursively sorts the partitions."
            },
            {
                "question": "What is the worst-case complexity of Quick Sort?",
                "answer": "O(n squared), often caused by highly unbalanced partitions."
            },
            {
                "question": "What is a stable sorting algorithm?",
                "answer": "A stable algorithm preserves the relative order of records with equal sorting keys."
            },
            {
                "question": "Is Merge Sort stable?",
                "answer": "Yes, when equal elements are merged while preserving their original relative order."
            },
            {
                "question": "What is Counting Sort?",
                "answer": "It counts occurrences of values and reconstructs the sorted sequence without comparison-based sorting."
            },
            {
                "question": "What is the difference between Merge Sort and Quick Sort?",
                "answer": "Merge Sort guarantees O(n log n) time but generally needs O(n) extra array space. Quick Sort has O(n log n) average time, O(n squared) worst-case time and typically uses less auxiliary memory."
            }
        ],

        "mcqs": [
            {
                "question": "Which sorting algorithm repeatedly compares adjacent elements?",
                "options": ["Merge Sort", "Bubble Sort", "Quick Sort", "Counting Sort"],
                "answer": "Bubble Sort",
                "explanation": "Bubble Sort swaps adjacent elements when they are out of order."
            },
            {
                "question": "Which sorting algorithm repeatedly selects the minimum element?",
                "options": ["Selection Sort", "Insertion Sort", "Merge Sort", "Quick Sort"],
                "answer": "Selection Sort",
                "explanation": "It places the smallest remaining element at the next sorted position."
            },
            {
                "question": "Which sorting algorithm is efficient for nearly sorted data?",
                "options": ["Selection Sort", "Insertion Sort", "Counting Sort", "Quick Sort"],
                "answer": "Insertion Sort",
                "explanation": "Its best-case time complexity is O(n)."
            },
            {
                "question": "What is Merge Sort's worst-case time complexity?",
                "options": ["O(n)", "O(n squared)", "O(n log n)", "O(log n)"],
                "answer": "O(n log n)",
                "explanation": "It divides the array into logarithmic levels and performs linear merging at each level."
            },
            {
                "question": "What is Quick Sort's worst-case time complexity?",
                "options": ["O(n)", "O(log n)", "O(n log n)", "O(n squared)"],
                "answer": "O(n squared)",
                "explanation": "Highly unbalanced partitions can produce quadratic work."
            },
            {
                "question": "Which algorithm is generally stable?",
                "options": ["Merge Sort", "Standard Quick Sort", "Standard Selection Sort", "Heap Sort"],
                "answer": "Merge Sort",
                "explanation": "A careful merge operation preserves the order of equal elements."
            },
            {
                "question": "Which algorithm can sort small-range integers in O(n + k) time?",
                "options": ["Bubble Sort", "Counting Sort", "Quick Sort", "Selection Sort"],
                "answer": "Counting Sort",
                "explanation": "It counts the frequency of each value in a range of size k."
            },
            {
                "question": "Which algorithm uses the Divide and Conquer approach?",
                "options": ["Bubble Sort only", "Selection Sort only", "Merge Sort", "Insertion Sort only"],
                "answer": "Merge Sort",
                "explanation": "Merge Sort recursively divides and then merges subproblems."
            },
            {
                "question": "What is the best-case complexity of optimized Bubble Sort?",
                "options": ["O(n)", "O(n squared)", "O(log n)", "O(n log n)"],
                "answer": "O(n)",
                "explanation": "An early-exit flag stops after one pass if no swaps are required."
            },
            {
                "question": "Which algorithm uses the pivot concept?",
                "options": ["Insertion Sort", "Quick Sort", "Counting Sort", "Bubble Sort"],
                "answer": "Quick Sort",
                "explanation": "Quick Sort partitions elements around a selected pivot."
            }
        ]
    }
})


DSA_TRACK.update({
    "dsa-linked-list": {
        "title": "Linked Lists",
        "subtitle": "Dynamic data structures, pointers and node manipulation",

        "content": """
# 1. What is a Linked List?

A Linked List is a linear data structure consisting of nodes.

Each node contains:
- Data: the value stored in the node.
- Link: a reference or pointer to another node.

Example:

10 -> 20 -> 30 -> None

The first node is called the Head.
The last node points to None in a normal singly linked list.

Unlike arrays, linked list elements are not required to occupy contiguous memory locations.

# 2. Why use Linked Lists?

Advantages:
- Dynamic size.
- Efficient insertion and deletion when the node position is already known.
- Does not require a contiguous memory block.

Disadvantages:
- No direct indexing.
- Searching takes O(n).
- Extra memory is required for pointers or references.
- Poorer cache locality than arrays in many implementations.

# 3. Types of Linked Lists

## A. Singly Linked List

Each node points to the next node.

10 -> 20 -> 30 -> None

Traversal is possible only in the forward direction.

## B. Doubly Linked List

Each node contains:
- Previous pointer.
- Data.
- Next pointer.

None <- 10 <-> 20 <-> 30 -> None

Traversal is possible in both directions.

## C. Circular Linked List

The last node points back to the first node.

10 -> 20 -> 30
^           |
|___________|

There is no None at the end in a normal circular linked list.

# 4. Basic Operations

## Traversal

Visit every node starting from the head.

Time complexity: O(n).

## Insertion at the Beginning

1. Create a new node.
2. Set its next pointer to the current head.
3. Update head to the new node.

Time complexity: O(1).

## Insertion at the End

1. Create a new node.
2. Traverse to the last node.
3. Set the last node's next pointer to the new node.

Time complexity: O(n) without a tail pointer.

## Deletion

To delete a node:
1. Find the node to delete.
2. Update the previous node's next pointer.
3. Release or allow the removed node to be reclaimed.

Time complexity: O(n) when searching for the value.

# 5. Reversing a Linked List

Suppose:

10 -> 20 -> 30 -> None

After reversing:

30 -> 20 -> 10 -> None

Use three pointers:
- prev
- current
- next_node

For each node:
1. Save the next node.
2. Reverse the current node's link.
3. Move prev forward.
4. Move current forward.

Time complexity: O(n).
Auxiliary space: O(1).

# 6. Slow and Fast Pointer Technique

Use two pointers:
- Slow moves one node at a time.
- Fast moves two nodes at a time.

Applications:

Finding the middle:
When fast reaches the end, slow is at the middle.

Detecting a cycle:
If slow and fast meet, a cycle exists.

Finding the starting node of a cycle:
After detecting a meeting, move one pointer to head. Move both one step at a time. Their next meeting identifies the cycle's starting node.

# 7. Complexity Analysis

Operation                  Singly Linked List
Access by index             O(n)
Search                      O(n)
Insert at head              O(1)
Insert at tail              O(n), without tail pointer
Delete head                 O(1)
Delete by value             O(n)
Traversal                   O(n)
Reverse                     O(n)

A doubly linked list can delete a known node in O(1) when its previous and next links are available.

# 8. Linked List vs Array

Array:
- Usually contiguous memory.
- Direct indexing: O(1).
- Insertion in the middle: O(n) due to shifting.
- Less memory overhead per element.

Linked List:
- Nodes can occupy different memory locations.
- Access by index: O(n).
- Insertion after a known node: O(1).
- Additional pointer memory.

# 9. Common Interview Problems

- Reverse a linked list.
- Find the middle node.
- Detect a cycle.
- Merge two sorted linked lists.
- Remove the Nth node from the end.
- Find the intersection of two linked lists.
- Check whether a linked list is a palindrome.

# 10. Interview Tips

- Always handle an empty list.
- Check the single-node case.
- Be careful not to lose the next pointer while reversing.
- Understand the difference between changing a node's value and changing its link.
- Know when to use a dummy node.
- Explain both time and auxiliary space complexity.
""",

        "key_concepts": [
            {
                "name": "Node",
                "description": "A basic linked list element containing data and one or more references to other nodes."
            },
            {
                "name": "Head",
                "description": "The reference to the first node of a linked list."
            },
            {
                "name": "Singly Linked List",
                "description": "Each node points to the next node."
            },
            {
                "name": "Doubly Linked List",
                "description": "Each node contains references to both previous and next nodes."
            },
            {
                "name": "Circular Linked List",
                "description": "The final node links back to the first node."
            },
            {
                "name": "Traversal",
                "description": "Visiting nodes one by one, starting from the head."
            },
            {
                "name": "Reversal",
                "description": "Changing node links so the list is traversed in the opposite direction."
            },
            {
                "name": "Fast and Slow Pointers",
                "description": "Two pointers moving at different speeds to find the middle or detect a cycle."
            },
            {
                "name": "Cycle",
                "description": "A loop in which following next pointers eventually revisits a node."
            }
        ],

        "examples": {
            "python": {
                "title": "Singly Linked List in Python",
                "code": """class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = new_node

    def display(self):
        current = self.head

        while current:
            print(current.data, end=" -> ")
            current = current.next

        print("None")

    def reverse(self):
        prev = None
        current = self.head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev


ll = LinkedList()
ll.insert_end(10)
ll.insert_end(20)
ll.insert_end(30)

print("Original:")
ll.display()

ll.reverse()

print("Reversed:")
ll.display()""",
                "output": """Original:
10 -> 20 -> 30 -> None
Reversed:
30 -> 20 -> 10 -> None"""
            },

            "java": {
                "title": "Singly Linked List in Java",
                "code": """class Node {
    int data;
    Node next;

    Node(int data) {
        this.data = data;
        this.next = null;
    }
}

public class Main {
    Node head;

    void insertEnd(int data) {
        Node newNode = new Node(data);

        if (head == null) {
            head = newNode;
            return;
        }

        Node current = head;

        while (current.next != null) {
            current = current.next;
        }

        current.next = newNode;
    }

    void display() {
        Node current = head;

        while (current != null) {
            System.out.print(current.data + " -> ");
            current = current.next;
        }

        System.out.println("null");
    }

    void reverse() {
        Node prev = null;
        Node current = head;

        while (current != null) {
            Node nextNode = current.next;
            current.next = prev;
            prev = current;
            current = nextNode;
        }

        head = prev;
    }

    public static void main(String[] args) {
        Main list = new Main();

        list.insertEnd(10);
        list.insertEnd(20);
        list.insertEnd(30);

        System.out.println("Original:");
        list.display();

        list.reverse();

        System.out.println("Reversed:");
        list.display();
    }
}""",
                "output": """Original:
10 -> 20 -> 30 -> null
Reversed:
30 -> 20 -> 10 -> null"""
            },

            "cpp": {
                "title": "Singly Linked List in C++",
                "code": """#include <iostream>
using namespace std;

struct Node {
    int data;
    Node* next;

    Node(int value) {
        data = value;
        next = nullptr;
    }
};

class LinkedList {
public:
    Node* head = nullptr;

    void insertEnd(int data) {
        Node* newNode = new Node(data);

        if (head == nullptr) {
            head = newNode;
            return;
        }

        Node* current = head;

        while (current->next != nullptr) {
            current = current->next;
        }

        current->next = newNode;
    }

    void display() {
        Node* current = head;

        while (current != nullptr) {
            cout << current->data << " -> ";
            current = current->next;
        }

        cout << "nullptr" << endl;
    }

    void reverse() {
        Node* prev = nullptr;
        Node* current = head;

        while (current != nullptr) {
            Node* nextNode = current->next;
            current->next = prev;
            prev = current;
            current = nextNode;
        }

        head = prev;
    }
};

int main() {
    LinkedList list;

    list.insertEnd(10);
    list.insertEnd(20);
    list.insertEnd(30);

    cout << "Original:" << endl;
    list.display();

    list.reverse();

    cout << "Reversed:" << endl;
    list.display();

    return 0;
}""",
                "output": """Original:
10 -> 20 -> 30 -> nullptr
Reversed:
30 -> 20 -> 10 -> nullptr"""
            }
        },

        "dry_run": {
            "title": "Dry Run: Reverse a Linked List",
            "code": "10 -> 20 -> 30 -> None",
            "steps": [
                {
                    "step": 1,
                    "value": "prev = None, current = 10",
                    "explanation": "Save next_node = 20. Change 10.next to None. Move prev to 10 and current to 20."
                },
                {
                    "step": 2,
                    "value": "prev = 10, current = 20",
                    "explanation": "Save next_node = 30. Change 20.next to 10. Move prev to 20 and current to 30."
                },
                {
                    "step": 3,
                    "value": "prev = 20, current = 30",
                    "explanation": "Save next_node = None. Change 30.next to 20. Move prev to 30 and current to None."
                },
                {
                    "step": 4,
                    "value": "current = None",
                    "explanation": "The traversal is finished. Update head to prev, which points to 30."
                }
            ],
            "result": "30 -> 20 -> 10 -> None"
        },

        "practice_questions": [
            {
                "question": "Reverse a singly linked list and return the new head.",
                "difficulty": "Easy",
                "hint": "Use prev, current and next_node pointers.",
                "solution": {
                    "python": """class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def reverse_list(head):
    prev = None
    current = head

    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev

def build(values):
    dummy = Node(0)
    tail = dummy

    for value in values:
        tail.next = Node(value)
        tail = tail.next

    return dummy.next

def display(head):
    result = []

    while head:
        result.append(head.val)
        head = head.next

    print(result)

head = build([1, 2, 3, 4])
display(reverse_list(head))""",
                    "java": """class ListNode {
    int val;
    ListNode next;

    ListNode(int val) {
        this.val = val;
    }
}

public class Main {
    static ListNode reverseList(ListNode head) {
        ListNode prev = null;
        ListNode current = head;

        while (current != null) {
            ListNode nextNode = current.next;
            current.next = prev;
            prev = current;
            current = nextNode;
        }

        return prev;
    }

    public static void main(String[] args) {
        ListNode a = new ListNode(1);
        a.next = new ListNode(2);
        a.next.next = new ListNode(3);
        a.next.next.next = new ListNode(4);

        ListNode head = reverseList(a);

        while (head != null) {
            System.out.print(head.val + " ");
            head = head.next;
        }
    }
}""",
                    "cpp": """#include <iostream>
using namespace std;

struct Node {
    int val;
    Node* next;

    Node(int x) : val(x), next(nullptr) {}
};

Node* reverseList(Node* head) {
    Node* prev = nullptr;
    Node* current = head;

    while (current != nullptr) {
        Node* nextNode = current->next;
        current->next = prev;
        prev = current;
        current = nextNode;
    }

    return prev;
}

int main() {
    Node* head = new Node(1);
    head->next = new Node(2);
    head->next->next = new Node(3);
    head->next->next->next = new Node(4);

    head = reverseList(head);

    while (head != nullptr) {
        cout << head->val << " ";
        head = head->next;
    }

    return 0;
}"""
                },
                "expected_output": "[4, 3, 2, 1]",
                "explanation": "Each next pointer is reversed. The original last node becomes the new head.",
                "complexity": "O(n) time and O(1) auxiliary space."
            },
            {
                "question": "Find the middle node of a singly linked list. If there are two middle nodes, return the second one.",
                "difficulty": "Easy",
                "hint": "Move slow by one node and fast by two nodes.",
                "solution": {
                    "python": """class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def middle_node(head):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

print(middle_node(head).val)""",
                    "java": """class ListNode {
    int val;
    ListNode next;

    ListNode(int val) {
        this.val = val;
    }
}

public class Main {
    static ListNode middleNode(ListNode head) {
        ListNode slow = head;
        ListNode fast = head;

        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }

        return slow;
    }

    public static void main(String[] args) {
        ListNode head = new ListNode(1);
        head.next = new ListNode(2);
        head.next.next = new ListNode(3);
        head.next.next.next = new ListNode(4);
        head.next.next.next.next = new ListNode(5);

        System.out.println(middleNode(head).val);
    }
}""",
                    "cpp": """#include <iostream>
using namespace std;

struct Node {
    int val;
    Node* next;

    Node(int x) : val(x), next(nullptr) {}
};

Node* middleNode(Node* head) {
    Node* slow = head;
    Node* fast = head;

    while (fast != nullptr && fast->next != nullptr) {
        slow = slow->next;
        fast = fast->next->next;
    }

    return slow;
}

int main() {
    Node* head = new Node(1);
    head->next = new Node(2);
    head->next->next = new Node(3);
    head->next->next->next = new Node(4);
    head->next->next->next->next = new Node(5);

    cout << middleNode(head)->val;
    return 0;
}"""
                },
                "expected_output": "3",
                "explanation": "Fast moves twice as quickly as slow. When fast reaches the end, slow points to the middle.",
                "complexity": "O(n) time and O(1) auxiliary space."
            },
            {
                "question": "Detect whether a linked list contains a cycle.",
                "difficulty": "Medium",
                "hint": "Use Floyd's cycle detection algorithm with slow and fast pointers.",
                "solution": {
                    "python": """class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def has_cycle(head):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow is fast:
            return True

    return False

a = Node(1)
b = Node(2)
c = Node(3)

a.next = b
b.next = c
c.next = b

print(has_cycle(a))""",
                    "java": """class ListNode {
    int val;
    ListNode next;

    ListNode(int val) {
        this.val = val;
    }
}

public class Main {
    static boolean hasCycle(ListNode head) {
        ListNode slow = head;
        ListNode fast = head;

        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;

            if (slow == fast) return true;
        }

        return false;
    }

    public static void main(String[] args) {
        ListNode a = new ListNode(1);
        ListNode b = new ListNode(2);
        ListNode c = new ListNode(3);

        a.next = b;
        b.next = c;
        c.next = b;

        System.out.println(hasCycle(a));
    }
}""",
                    "cpp": """#include <iostream>
using namespace std;

struct Node {
    int val;
    Node* next;

    Node(int x) : val(x), next(nullptr) {}
};

bool hasCycle(Node* head) {
    Node* slow = head;
    Node* fast = head;

    while (fast != nullptr && fast->next != nullptr) {
        slow = slow->next;
        fast = fast->next->next;

        if (slow == fast) return true;
    }

    return false;
}

int main() {
    Node* a = new Node(1);
    Node* b = new Node(2);
    Node* c = new Node(3);

    a->next = b;
    b->next = c;
    c->next = b;

    cout << boolalpha << hasCycle(a);
    return 0;
}"""
                },
                "expected_output": "True",
                "explanation": "The fast and slow pointers eventually meet because the linked list contains a cycle.",
                "complexity": "O(n) time and O(1) auxiliary space."
            }
        ],

        "interview_questions": [
            {
                "question": "What is a linked list?",
                "answer": "A linked list is a linear data structure made of nodes connected using references or pointers."
            },
            {
                "question": "What is the head of a linked list?",
                "answer": "The head is the reference to the first node."
            },
            {
                "question": "What is the difference between an array and a linked list?",
                "answer": "Arrays usually use contiguous memory and support O(1) indexing. Linked lists use connected nodes and require O(n) access by position."
            },
            {
                "question": "What are the types of linked lists?",
                "answer": "Common types are singly linked, doubly linked and circular linked lists."
            },
            {
                "question": "What is a singly linked list?",
                "answer": "Each node stores data and a reference to the next node."
            },
            {
                "question": "What is a doubly linked list?",
                "answer": "Each node stores data and references to both the previous and next nodes."
            },
            {
                "question": "What is a circular linked list?",
                "answer": "A linked list in which the last node points back to the first node."
            },
            {
                "question": "What is the time complexity of searching a linked list?",
                "answer": "O(n), because nodes may need to be visited sequentially."
            },
            {
                "question": "What is the time complexity of inserting at the head?",
                "answer": "O(1), because only the new node's next reference and head need to be updated."
            },
            {
                "question": "How do you reverse a singly linked list?",
                "answer": "Use previous, current and next pointers to reverse each link while traversing the list."
            },
            {
                "question": "How can you find the middle node?",
                "answer": "Use slow and fast pointers. Slow moves one step while fast moves two steps."
            },
            {
                "question": "How can you detect a cycle?",
                "answer": "Use Floyd's cycle detection algorithm. If slow and fast pointers meet, a cycle exists."
            },
            {
                "question": "What is the advantage of a doubly linked list?",
                "answer": "It supports traversal in both directions and allows efficient deletion of a known node when its links are available."
            },
            {
                "question": "What is a dummy node?",
                "answer": "A temporary helper node placed before the head to simplify insertion and deletion logic, especially at the beginning."
            },
            {
                "question": "What is Floyd's cycle detection algorithm?",
                "answer": "It uses two pointers moving at different speeds to detect whether a linked list contains a cycle."
            }
        ],

        "mcqs": [
            {
                "question": "What does each node in a singly linked list contain?",
                "options": ["Only data", "Data and next pointer", "Only previous pointer", "Two arrays"],
                "answer": "Data and next pointer",
                "explanation": "A singly linked list node stores a value and a reference to the next node."
            },
            {
                "question": "What is the time complexity of accessing an arbitrary linked list element by index?",
                "options": ["O(1)", "O(log n)", "O(n)", "O(n squared)"],
                "answer": "O(n)",
                "explanation": "Nodes must be traversed from the head."
            },
            {
                "question": "What is the time complexity of inserting a node at the beginning?",
                "options": ["O(1)", "O(n)", "O(log n)", "O(n squared)"],
                "answer": "O(1)",
                "explanation": "Only the new node's next pointer and the head reference need updating."
            },
            {
                "question": "Which linked list supports forward and backward traversal?",
                "options": ["Singly", "Doubly", "Linear array", "Stack"],
                "answer": "Doubly",
                "explanation": "A doubly linked list has both previous and next references."
            },
            {
                "question": "In a normal circular linked list, what does the last node point to?",
                "options": ["None", "Itself always", "The first node", "A random node"],
                "answer": "The first node",
                "explanation": "The last node connects back to the head."
            },
            {
                "question": "Which pointers are commonly used to reverse a singly linked list iteratively?",
                "options": ["low and high", "prev, current and next", "left and right", "root and leaf"],
                "answer": "prev, current and next",
                "explanation": "These pointers allow links to be reversed without losing the remaining list."
            },
            {
                "question": "Which technique finds the middle node efficiently?",
                "options": ["Binary Search", "Slow and fast pointers", "Sorting", "Hash sorting"],
                "answer": "Slow and fast pointers",
                "explanation": "The fast pointer travels twice as quickly as the slow pointer."
            },
            {
                "question": "Which algorithm is used for linked list cycle detection?",
                "options": ["Dijkstra", "Floyd's cycle detection", "Merge Sort", "Kruskal"],
                "answer": "Floyd's cycle detection",
                "explanation": "It detects cycles using slow and fast pointers."
            },
            {
                "question": "What is the auxiliary space complexity of iterative linked list reversal?",
                "options": ["O(n)", "O(log n)", "O(1)", "O(n squared)"],
                "answer": "O(1)",
                "explanation": "Only a fixed number of pointers are used."
            },
            {
                "question": "What is a major disadvantage of linked lists compared with arrays?",
                "options": ["Dynamic size", "No direct O(1) indexing", "Easy insertion at head", "Sequential traversal"],
                "answer": "No direct O(1) indexing",
                "explanation": "An arbitrary position must be reached by traversing nodes."
            }
        ]
    }
})


DSA_TRACK.update({
    "dsa-stack-queue": {
        "title": "Stacks and Queues",
        "description": "Learn LIFO and FIFO data structures, their operations, implementations, and common interview problems.",
        "content": """
# 1. Stack

A Stack is a linear data structure that follows LIFO:
Last In, First Out.

The element inserted last is removed first.

Real-life example:
A stack of plates. You place a new plate on top and remove the top plate first.

### Stack operations

1. push(x): Insert an element.
2. pop(): Remove the top element.
3. peek(): View the top element.
4. isEmpty(): Check whether the stack is empty.

Most stack operations take O(1) time.

### Applications

- Undo and redo operations.
- Browser history.
- Function calls and recursion.
- Expression evaluation.
- Parentheses matching.
- Monotonic stack problems.

# 2. Queue

A Queue is a linear data structure that follows FIFO:
First In, First Out.

The element inserted first is removed first.

Real-life example:
People standing in a ticket counter queue.

### Queue operations

1. enqueue(x): Insert an element at the rear.
2. dequeue(): Remove the front element.
3. front(): View the first element.
4. isEmpty(): Check whether the queue is empty.

A properly implemented queue supports O(1) insertion and deletion.

### Applications

- CPU scheduling.
- Printer scheduling.
- Breadth First Search (BFS).
- Request processing.
- Message queues.

# 3. Types of Queues

### Simple Queue
Insertion happens at the rear and deletion at the front.

### Circular Queue
The last position connects logically to the first position.
It reuses empty spaces in a fixed-size array.

### Deque
Double-ended queue.
Insertion and deletion are possible at both ends.

### Priority Queue
Elements are removed according to priority rather than insertion order.

# 4. Stack vs Queue

| Feature | Stack | Queue |
|---|---|---|
| Principle | LIFO | FIFO |
| Insertion | Top | Rear |
| Deletion | Top | Front |
| Main operations | Push, Pop | Enqueue, Dequeue |
| Example | Plates | Ticket line |

# 5. Important Problem-Solving Patterns

### Balanced Parentheses
Use a stack to remember opening brackets.
For every closing bracket, check whether it matches the most recent opening bracket.

### Next Greater Element
Use a monotonic stack to find the next greater value for each array element.

### BFS
Use a queue to process graph or tree nodes level by level.

### Sliding Window Maximum
A deque can maintain useful indices in decreasing order and efficiently find maximum values.

# 6. Complexity

| Operation | Stack | Queue |
|---|---|---|
| Insert | O(1) | O(1) |
| Delete | O(1) | O(1) |
| Peek/front | O(1) | O(1) |
| Search | O(n) | O(n) |
""",
        "key_concepts": [
            "Stack follows LIFO: Last In, First Out.",
            "Queue follows FIFO: First In, First Out.",
            "push() inserts into a stack.",
            "pop() removes the top stack element.",
            "enqueue() inserts into a queue.",
            "dequeue() removes the front queue element.",
            "A deque supports operations at both ends.",
            "A priority queue processes elements by priority.",
            "Stacks are used in recursion and expression evaluation.",
            "Queues are used in BFS and scheduling.",
            "Balanced parentheses can be checked using a stack.",
            "A monotonic stack helps solve next greater element problems."
        ],
        "examples": {
            "python": {
                "title": "Stack and Queue in Python",
                "code": "from collections import deque\n\n# Stack\nstack = []\nstack.append(10)\nstack.append(20)\nstack.append(30)\nprint('Stack:', stack)\nprint('Popped:', stack.pop())\nprint('Top:', stack[-1])\n\n# Queue\nqueue = deque()\nqueue.append(10)\nqueue.append(20)\nqueue.append(30)\nprint('Queue:', list(queue))\nprint('Removed:', queue.popleft())\nprint('Front:', queue[0])",
                "output": "Stack: [10, 20, 30]\nPopped: 30\nTop: 20\nQueue: [10, 20, 30]\nRemoved: 10\nFront: 20"
            },
            "java": {
                "title": "Stack and Queue in Java",
                "code": "import java.util.*;\n\npublic class Main {\n    public static void main(String[] args) {\n        Stack<Integer> stack = new Stack<>();\n        stack.push(10);\n        stack.push(20);\n        stack.push(30);\n        System.out.println(\"Popped: \" + stack.pop());\n        System.out.println(\"Top: \" + stack.peek());\n\n        Queue<Integer> queue = new LinkedList<>();\n        queue.offer(10);\n        queue.offer(20);\n        queue.offer(30);\n        System.out.println(\"Removed: \" + queue.poll());\n        System.out.println(\"Front: \" + queue.peek());\n    }\n}",
                "output": "Popped: 30\nTop: 20\nRemoved: 10\nFront: 20"
            },
            "cpp": {
                "title": "Stack and Queue in C++",
                "code": "#include <iostream>\n#include <stack>\n#include <queue>\nusing namespace std;\n\nint main() {\n    stack<int> st;\n    st.push(10);\n    st.push(20);\n    st.push(30);\n    cout << \"Popped: \" << st.top() << endl;\n    st.pop();\n    cout << \"Top: \" << st.top() << endl;\n\n    queue<int> q;\n    q.push(10);\n    q.push(20);\n    q.push(30);\n    cout << \"Removed: \" << q.front() << endl;\n    q.pop();\n    cout << \"Front: \" << q.front() << endl;\n    return 0;\n}",
                "output": "Popped: 30\nTop: 20\nRemoved: 10\nFront: 20"
            }
        },
        "dry_run": [
            {
                "step": 1,
                "operation": "Push 10, 20, 30 into stack",
                "stack": "[10, 20, 30]",
                "explanation": "30 is at the top because it was inserted last."
            },
            {
                "step": 2,
                "operation": "Pop from stack",
                "stack": "[10, 20]",
                "explanation": "30 is removed first because stack follows LIFO."
            },
            {
                "step": 3,
                "operation": "Insert 10, 20, 30 into queue",
                "queue": "[10, 20, 30]",
                "explanation": "10 is at the front because it was inserted first."
            },
            {
                "step": 4,
                "operation": "Dequeue",
                "queue": "[20, 30]",
                "explanation": "10 is removed first because queue follows FIFO."
            }
        ],
        "practice_questions": [
            {
                "title": "Valid Parentheses",
                "difficulty": "Easy",
                "problem": "Given a string containing (), {}, and [], determine whether the brackets are balanced and correctly nested.",
                "approach": "Push opening brackets onto a stack. For every closing bracket, check and remove its matching opening bracket. The string is valid if no mismatch occurs and the stack is empty at the end.",
                "solution": {
                    "python": "def is_valid(s):\n    stack = []\n    pairs = {')': '(', '}': '{', ']': '['}\n    for ch in s:\n        if ch in pairs:\n            if not stack or stack.pop() != pairs[ch]:\n                return False\n        else:\n            stack.append(ch)\n    return len(stack) == 0\n\nprint(is_valid('{[()]}'))\nprint(is_valid('([)]'))",
                    "java": "import java.util.*;\nclass Main {\n    static boolean isValid(String s) {\n        Stack<Character> st = new Stack<>();\n        for (char ch : s.toCharArray()) {\n            if (ch == '(' || ch == '{' || ch == '[') st.push(ch);\n            else {\n                if (st.isEmpty()) return false;\n                char top = st.pop();\n                if ((ch == ')' && top != '(') ||\n                    (ch == '}' && top != '{') ||\n                    (ch == ']' && top != '[')) return false;\n            }\n        }\n        return st.isEmpty();\n    }\n    public static void main(String[] args) {\n        System.out.println(isValid(\"{[()]}\"));\n        System.out.println(isValid(\"([)]\"));\n    }\n}",
                    "cpp": "#include <iostream>\n#include <stack>\nusing namespace std;\n\nbool isValid(string s) {\n    stack<char> st;\n    for (char ch : s) {\n        if (ch == '(' || ch == '{' || ch == '[') st.push(ch);\n        else {\n            if (st.empty()) return false;\n            char top = st.top(); st.pop();\n            if ((ch == ')' && top != '(') ||\n                (ch == '}' && top != '{') ||\n                (ch == ']' && top != '[')) return false;\n        }\n    }\n    return st.empty();\n}\nint main() {\n    cout << boolalpha << isValid(\"{[()]}\") << endl;\n    cout << isValid(\"([)]\") << endl;\n}"
                },
                "expected_output": "True\nFalse"
            },
            {
                "title": "Implement Queue Using Two Stacks",
                "difficulty": "Medium",
                "problem": "Implement a queue with enqueue and dequeue operations using only two stacks.",
                "approach": "Push new elements into the input stack. When the output stack is empty, transfer all input elements into it. Pop from the output stack to dequeue.",
                "solution": {
                    "python": "class MyQueue:\n    def __init__(self):\n        self.in_stack = []\n        self.out_stack = []\n\n    def enqueue(self, x):\n        self.in_stack.append(x)\n\n    def dequeue(self):\n        if not self.out_stack:\n            while self.in_stack:\n                self.out_stack.append(self.in_stack.pop())\n        return self.out_stack.pop() if self.out_stack else None\n\nq = MyQueue()\nq.enqueue(10)\nq.enqueue(20)\nprint(q.dequeue())",
                    "java": "import java.util.*;\nclass MyQueue {\n    Stack<Integer> in = new Stack<>();\n    Stack<Integer> out = new Stack<>();\n    void enqueue(int x) { in.push(x); }\n    int dequeue() {\n        if (out.isEmpty()) while (!in.isEmpty()) out.push(in.pop());\n        return out.isEmpty() ? -1 : out.pop();\n    }\n    public static void main(String[] args) {\n        MyQueue q = new MyQueue();\n        q.enqueue(10); q.enqueue(20);\n        System.out.println(q.dequeue());\n    }\n}",
                    "cpp": "#include <iostream>\n#include <stack>\nusing namespace std;\nclass MyQueue {\n    stack<int> in, out;\npublic:\n    void enqueue(int x) { in.push(x); }\n    int dequeue() {\n        if (out.empty()) while (!in.empty()) {\n            out.push(in.top()); in.pop();\n        }\n        if (out.empty()) return -1;\n        int x = out.top(); out.pop(); return x;\n    }\n};\nint main() {\n    MyQueue q; q.enqueue(10); q.enqueue(20);\n    cout << q.dequeue() << endl;\n}"
                },
                "expected_output": "10"
            },
            {
                "title": "Next Greater Element",
                "difficulty": "Medium",
                "problem": "For every element in an array, find the first greater element to its right. Return -1 if no such element exists.",
                "approach": "Traverse from right to left. Remove all smaller or equal elements from a decreasing stack. The remaining top is the next greater element.",
                "solution": {
                    "python": "def next_greater(arr):\n    stack = []\n    ans = [-1] * len(arr)\n    for i in range(len(arr) - 1, -1, -1):\n        while stack and stack[-1] <= arr[i]:\n            stack.pop()\n        if stack:\n            ans[i] = stack[-1]\n        stack.append(arr[i])\n    return ans\n\nprint(next_greater([4, 5, 2, 10]))",
                    "java": "import java.util.*;\nclass Main {\n    static int[] nextGreater(int[] a) {\n        int n = a.length;\n        int[] ans = new int[n];\n        Arrays.fill(ans, -1);\n        Stack<Integer> st = new Stack<>();\n        for (int i = n - 1; i >= 0; i--) {\n            while (!st.isEmpty() && st.peek() <= a[i]) st.pop();\n            if (!st.isEmpty()) ans[i] = st.peek();\n            st.push(a[i]);\n        }\n        return ans;\n    }\n    public static void main(String[] args) {\n        System.out.println(Arrays.toString(nextGreater(new int[]{4,5,2,10})));\n    }\n}",
                    "cpp": "#include <iostream>\n#include <vector>\n#include <stack>\nusing namespace std;\nvector<int> nextGreater(vector<int>& a) {\n    int n = a.size();\n    vector<int> ans(n, -1);\n    stack<int> st;\n    for (int i = n - 1; i >= 0; i--) {\n        while (!st.empty() && st.top() <= a[i]) st.pop();\n        if (!st.empty()) ans[i] = st.top();\n        st.push(a[i]);\n    }\n    return ans;\n}\nint main() {\n    vector<int> a = {4,5,2,10};\n    for (int x : nextGreater(a)) cout << x << \" \";\n}"
                },
                "expected_output": "5 10 10 -1"
            }
        ],
        "interview_questions": [
            {"question": "What is a stack?", "answer": "A linear data structure that follows Last In, First Out (LIFO)."},
            {"question": "What is a queue?", "answer": "A linear data structure that follows First In, First Out (FIFO)."},
            {"question": "What is stack overflow?", "answer": "An error caused when a stack exceeds its available capacity, such as excessive recursion or pushing into a full fixed-size stack."},
            {"question": "What is stack underflow?", "answer": "Attempting to remove an element from an empty stack."},
            {"question": "What is queue overflow?", "answer": "Attempting to insert into a full fixed-capacity queue."},
            {"question": "What is a circular queue?", "answer": "A queue that logically connects its last position to the first to reuse available space."},
            {"question": "What is a deque?", "answer": "A double-ended queue that supports insertion and deletion at both ends."},
            {"question": "What is a priority queue?", "answer": "A queue-like structure where removal is based on priority, commonly implemented using a heap."},
            {"question": "How can a queue be implemented using stacks?", "answer": "Use an input stack for enqueue and an output stack for dequeue, transferring elements when the output stack is empty."},
            {"question": "How can a stack be implemented using queues?", "answer": "Use one or two queues and arrange elements so that the newest item is removed first."},
            {"question": "What is the time complexity of stack push and pop?", "answer": "O(1) for a standard stack implementation."},
            {"question": "What is the time complexity of queue enqueue and dequeue?", "answer": "O(1) with a linked list or circular buffer implementation."},
            {"question": "Why is a stack used in DFS?", "answer": "DFS explores a path deeply before returning, which naturally matches LIFO behavior."},
            {"question": "Why is a queue used in BFS?", "answer": "FIFO processing visits nodes in increasing distance or level order."},
            {"question": "What is a monotonic stack?", "answer": "A stack maintained in increasing or decreasing order to solve problems such as next greater or smaller element efficiently."}
        ],
        "mcqs": [
            {"question": "Which principle does a stack follow?", "options": ["FIFO", "LIFO", "Random", "Priority"], "answer": "LIFO", "explanation": "The last inserted element is removed first."},
            {"question": "Which principle does a queue follow?", "options": ["LIFO", "FIFO", "Sorted", "Random"], "answer": "FIFO", "explanation": "The first inserted element is removed first."},
            {"question": "Which operation inserts an item into a stack?", "options": ["pop", "push", "dequeue", "poll"], "answer": "push", "explanation": "push adds an element to the top."},
            {"question": "Which operation removes an item from a queue?", "options": ["push", "peek", "dequeue", "enqueue"], "answer": "dequeue", "explanation": "dequeue removes the front element."},
            {"question": "Which structure is commonly used in BFS?", "options": ["Stack", "Queue", "Heap", "Trie"], "answer": "Queue", "explanation": "A queue ensures level-order processing."},
            {"question": "Which structure is useful for balanced parentheses?", "options": ["Queue", "Stack", "Array only", "Heap"], "answer": "Stack", "explanation": "The latest opening bracket must be matched first."},
            {"question": "What does a deque allow?", "options": ["Only front insertion", "Only rear deletion", "Operations at both ends", "Sorted insertion only"], "answer": "Operations at both ends", "explanation": "Deque means double-ended queue."},
            {"question": "What is the typical time complexity of push?", "options": ["O(n)", "O(log n)", "O(1)", "O(n log n)"], "answer": "O(1)", "explanation": "A standard stack inserts at its top in constant time."},
            {"question": "Which data structure is commonly used to implement a priority queue?", "options": ["Heap", "Stack", "Trie", "Linked list only"], "answer": "Heap", "explanation": "A heap supports efficient priority-based access."},
            {"question": "A monotonic stack is useful for which problem?", "options": ["Next greater element", "Merge sort", "Binary search only", "Hashing"], "answer": "Next greater element", "explanation": "It maintains a monotonic order to find next greater values efficiently."}
        ]
    }
})


DSA_TRACK.update({
    "dsa-binary-tree": {
        "title": "Binary Trees and Binary Search Trees",
        "description": "Understand tree structures, traversals, recursion, Binary Search Trees, and common interview problems.",
        "content": """
# 1. What is a Tree?

A Tree is a non-linear hierarchical data structure made of nodes connected by edges.

Important terminology:
- Root: The first node of a tree.
- Parent: A node that has children.
- Child: A node connected below another node.
- Leaf: A node with no children.
- Subtree: A node and all its descendants.
- Height: The longest path from a node to a leaf, measured in edges.
- Depth: The number of edges from the root to a node.

# 2. What is a Binary Tree?

A Binary Tree is a tree in which each node can have at most two children:
- Left child
- Right child

Example:

        10
       /  \\
      5    20
     / \\     \\
    3   7     30

# 3. Types of Binary Trees

Full Binary Tree:
Every node has either zero or two children.

Complete Binary Tree:
All levels are completely filled except possibly the last, which is filled from left to right.

Perfect Binary Tree:
Every internal node has two children and all leaves are at the same level.

Balanced Binary Tree:
The heights of the left and right subtrees remain within a defined bound. For common height-balanced trees, the difference is at most one.

Skewed Binary Tree:
Each node has only one child, forming a chain.

# 4. Tree Traversals

Traversal means visiting every node in a particular order.

Consider:

        1
       / \\
      2   3
     / \\
    4   5

Inorder (Left, Root, Right):
4, 2, 5, 1, 3

Preorder (Root, Left, Right):
1, 2, 4, 5, 3

Postorder (Left, Right, Root):
4, 5, 2, 3, 1

Level Order:
1, 2, 3, 4, 5

DFS traversals include inorder, preorder, and postorder.
Level order traversal uses BFS with a queue.

# 5. Binary Search Tree (BST)

A BST is a binary tree with an ordering property:
- Values in the left subtree are smaller than the node.
- Values in the right subtree are greater than the node.

This property allows efficient searching when the tree is balanced.

Average search, insertion and deletion: O(log n).
Worst case for a skewed tree: O(n).

# 6. Important Tree Problems

- Find the maximum depth.
- Count nodes and leaf nodes.
- Search for a value.
- Invert a binary tree.
- Check whether two trees are identical.
- Find the lowest common ancestor.
- Validate a BST.
- Find the diameter of a tree.

# 7. Complexity

For a tree with n nodes:
- Traversal: O(n).
- Counting nodes: O(n).
- Searching in a general binary tree: O(n).
- Searching in a balanced BST: O(log n).
- Searching in a skewed BST: O(n).

A recursive traversal uses O(h) call-stack space, where h is the tree height.
""",
        "key_concepts": [
            "A tree is a hierarchical non-linear data structure.",
            "The root is the topmost node.",
            "A leaf node has no children.",
            "A binary tree has at most two children per node.",
            "A BST stores smaller values on the left and larger values on the right.",
            "Inorder traversal of a BST produces sorted order when keys are distinct.",
            "Preorder traversal visits root before its subtrees.",
            "Postorder traversal visits root after its subtrees.",
            "Level order traversal uses a queue.",
            "DFS traversals commonly use recursion or a stack.",
            "Balanced BST operations are generally O(log n).",
            "A skewed BST can have O(n) search time.",
            "Tree traversal takes O(n) time.",
            "Recursive traversal uses O(h) auxiliary call-stack space."
        ],
        "examples": {
            "python": {
                "title": "Binary Tree Traversals in Python",
                "code": "from collections import deque\n\nclass Node:\n    def __init__(self, val):\n        self.val = val\n        self.left = None\n        self.right = None\n\nroot = Node(1)\nroot.left = Node(2)\nroot.right = Node(3)\nroot.left.left = Node(4)\nroot.left.right = Node(5)\n\ndef inorder(node):\n    if node is None:\n        return\n    inorder(node.left)\n    print(node.val, end=' ')\n    inorder(node.right)\n\ndef preorder(node):\n    if node is None:\n        return\n    print(node.val, end=' ')\n    preorder(node.left)\n    preorder(node.right)\n\ndef postorder(node):\n    if node is None:\n        return\n    postorder(node.left)\n    postorder(node.right)\n    print(node.val, end=' ')\n\ndef level_order(root):\n    if root is None:\n        return\n    q = deque([root])\n    while q:\n        node = q.popleft()\n        print(node.val, end=' ')\n        if node.left:\n            q.append(node.left)\n        if node.right:\n            q.append(node.right)\n\nprint('Inorder:', end=' ')\ninorder(root)\nprint('\\nPreorder:', end=' ')\npreorder(root)\nprint('\\nPostorder:', end=' ')\npostorder(root)\nprint('\\nLevel order:', end=' ')\nlevel_order(root)",
                "output": "Inorder: 4 2 5 1 3\nPreorder: 1 2 4 5 3\nPostorder: 4 5 2 3 1\nLevel order: 1 2 3 4 5"
            },
            "java": {
                "title": "Binary Tree Traversals in Java",
                "code": "import java.util.*;\n\nclass Node {\n    int val;\n    Node left, right;\n    Node(int val) { this.val = val; }\n}\n\npublic class Main {\n    static void inorder(Node root) {\n        if (root == null) return;\n        inorder(root.left);\n        System.out.print(root.val + \" \");\n        inorder(root.right);\n    }\n    static void preorder(Node root) {\n        if (root == null) return;\n        System.out.print(root.val + \" \");\n        preorder(root.left);\n        preorder(root.right);\n    }\n    static void postorder(Node root) {\n        if (root == null) return;\n        postorder(root.left);\n        postorder(root.right);\n        System.out.print(root.val + \" \");\n    }\n    static void levelOrder(Node root) {\n        if (root == null) return;\n        Queue<Node> q = new LinkedList<>();\n        q.offer(root);\n        while (!q.isEmpty()) {\n            Node cur = q.poll();\n            System.out.print(cur.val + \" \");\n            if (cur.left != null) q.offer(cur.left);\n            if (cur.right != null) q.offer(cur.right);\n        }\n    }\n    public static void main(String[] args) {\n        Node root = new Node(1);\n        root.left = new Node(2);\n        root.right = new Node(3);\n        root.left.left = new Node(4);\n        root.left.right = new Node(5);\n        System.out.print(\"Inorder: \"); inorder(root);\n        System.out.print(\"\\nPreorder: \"); preorder(root);\n        System.out.print(\"\\nPostorder: \"); postorder(root);\n        System.out.print(\"\\nLevel order: \"); levelOrder(root);\n    }\n}",
                "output": "Inorder: 4 2 5 1 3\nPreorder: 1 2 4 5 3\nPostorder: 4 5 2 3 1\nLevel order: 1 2 3 4 5"
            },
            "cpp": {
                "title": "Binary Tree Traversals in C++",
                "code": "#include <iostream>\n#include <queue>\nusing namespace std;\n\nstruct Node {\n    int val;\n    Node *left, *right;\n    Node(int x) : val(x), left(nullptr), right(nullptr) {}\n};\n\nvoid inorder(Node* root) {\n    if (!root) return;\n    inorder(root->left);\n    cout << root->val << \" \";\n    inorder(root->right);\n}\nvoid preorder(Node* root) {\n    if (!root) return;\n    cout << root->val << \" \";\n    preorder(root->left);\n    preorder(root->right);\n}\nvoid postorder(Node* root) {\n    if (!root) return;\n    postorder(root->left);\n    postorder(root->right);\n    cout << root->val << \" \";\n}\nvoid levelOrder(Node* root) {\n    if (!root) return;\n    queue<Node*> q;\n    q.push(root);\n    while (!q.empty()) {\n        Node* cur = q.front(); q.pop();\n        cout << cur->val << \" \";\n        if (cur->left) q.push(cur->left);\n        if (cur->right) q.push(cur->right);\n    }\n}\nint main() {\n    Node* root = new Node(1);\n    root->left = new Node(2);\n    root->right = new Node(3);\n    root->left->left = new Node(4);\n    root->left->right = new Node(5);\n    cout << \"Inorder: \"; inorder(root);\n    cout << \"\\nPreorder: \"; preorder(root);\n    cout << \"\\nPostorder: \"; postorder(root);\n    cout << \"\\nLevel order: \"; levelOrder(root);\n    return 0;\n}",
                "output": "Inorder: 4 2 5 1 3\nPreorder: 1 2 4 5 3\nPostorder: 4 5 2 3 1\nLevel order: 1 2 3 4 5"
            }
        },
        "dry_run": [
            {
                "step": 1,
                "operation": "Start inorder traversal at node 1",
                "tree": "1 -> left subtree",
                "explanation": "Inorder visits the left subtree before the current node."
            },
            {
                "step": 2,
                "operation": "Visit node 4",
                "tree": "4",
                "explanation": "Node 4 is the leftmost node, so it is visited first."
            },
            {
                "step": 3,
                "operation": "Return and visit node 2",
                "tree": "4, 2",
                "explanation": "After finishing node 2's left subtree, visit node 2."
            },
            {
                "step": 4,
                "operation": "Visit node 5, then node 1, then node 3",
                "tree": "4, 2, 5, 1, 3",
                "explanation": "Continue with the right subtree of 2, then the root, then the right subtree."
            }
        ],
        "practice_questions": [
            {
                "title": "Maximum Depth of Binary Tree",
                "difficulty": "Easy",
                "problem": "Given the root of a binary tree, return its maximum depth, measured as the number of nodes on the longest root-to-leaf path.",
                "approach": "If the node is null, return 0. Otherwise, calculate the depths of the left and right subtrees and return 1 plus their maximum.",
                "solution": {
                    "python": "def max_depth(root):\n    if root is None:\n        return 0\n    return 1 + max(max_depth(root.left), max_depth(root.right))",
                    "java": "class Solution {\n    public int maxDepth(TreeNode root) {\n        if (root == null) return 0;\n        return 1 + Math.max(maxDepth(root.left), maxDepth(root.right));\n    }\n}",
                    "cpp": "class Solution {\npublic:\n    int maxDepth(TreeNode* root) {\n        if (root == nullptr) return 0;\n        return 1 + max(maxDepth(root->left), maxDepth(root->right));\n    }\n};"
                },
                "expected_output": "For tree [3,9,20,null,null,15,7], output is 3."
            },
            {
                "title": "Search in a Binary Search Tree",
                "difficulty": "Easy",
                "problem": "Given the root of a BST and a target value, return the node containing that value, or null if it does not exist.",
                "approach": "If the target equals the current node, return it. If the target is smaller, search left; otherwise, search right.",
                "solution": {
                    "python": "def search_bst(root, target):\n    if root is None or root.val == target:\n        return root\n    if target < root.val:\n        return search_bst(root.left, target)\n    return search_bst(root.right, target)",
                    "java": "class Solution {\n    public TreeNode searchBST(TreeNode root, int val) {\n        if (root == null || root.val == val) return root;\n        if (val < root.val) return searchBST(root.left, val);\n        return searchBST(root.right, val);\n    }\n}",
                    "cpp": "class Solution {\npublic:\n    TreeNode* searchBST(TreeNode* root, int val) {\n        if (!root || root->val == val) return root;\n        if (val < root->val) return searchBST(root->left, val);\n        return searchBST(root->right, val);\n    }\n};"
                },
                "expected_output": "For BST [4,2,7,1,3] and target 2, return the node with value 2."
            },
            {
                "title": "Invert Binary Tree",
                "difficulty": "Easy",
                "problem": "Given the root of a binary tree, swap the left and right children of every node.",
                "approach": "For every node, swap its left and right references, then recursively invert both resulting subtrees.",
                "solution": {
                    "python": "def invert_tree(root):\n    if root is None:\n        return None\n    root.left, root.right = root.right, root.left\n    invert_tree(root.left)\n    invert_tree(root.right)\n    return root",
                    "java": "class Solution {\n    public TreeNode invertTree(TreeNode root) {\n        if (root == null) return null;\n        TreeNode temp = root.left;\n        root.left = root.right;\n        root.right = temp;\n        invertTree(root.left);\n        invertTree(root.right);\n        return root;\n    }\n}",
                    "cpp": "class Solution {\npublic:\n    TreeNode* invertTree(TreeNode* root) {\n        if (!root) return nullptr;\n        swap(root->left, root->right);\n        invertTree(root->left);\n        invertTree(root->right);\n        return root;\n    }\n};"
                },
                "expected_output": "For tree [4,2,7,1,3,6,9], the inverted tree is [4,7,2,9,6,3,1]."
            }
        ],
        "interview_questions": [
            {"question": "What is a binary tree?", "answer": "A tree in which each node has at most two children."},
            {"question": "What is a Binary Search Tree?", "answer": "A binary tree where left-subtree keys are smaller and right-subtree keys are greater than the current key, under the usual distinct-key convention."},
            {"question": "What is inorder traversal?", "answer": "A traversal that visits left subtree, root, and right subtree."},
            {"question": "What is preorder traversal?", "answer": "A traversal that visits root, left subtree, and right subtree."},
            {"question": "What is postorder traversal?", "answer": "A traversal that visits left subtree, right subtree, and root."},
            {"question": "Which traversal uses a queue?", "answer": "Level order traversal, which is BFS."},
            {"question": "What is a leaf node?", "answer": "A node that has no children."},
            {"question": "What is a balanced binary tree?", "answer": "A tree whose height is kept within a bound relative to the number of nodes; height-balanced trees commonly restrict child-subtree height difference to at most one."},
            {"question": "What is a complete binary tree?", "answer": "A tree where all levels except possibly the last are full and the last level is filled from left to right."},
            {"question": "What is a full binary tree?", "answer": "A tree in which each node has either zero or two children."},
            {"question": "What is a perfect binary tree?", "answer": "A tree where all internal nodes have two children and all leaves are at the same depth."},
            {"question": "What is the average search complexity in a balanced BST?", "answer": "O(log n)."},
            {"question": "What is the worst-case search complexity in a skewed BST?", "answer": "O(n)."},
            {"question": "What is the time complexity of tree traversal?", "answer": "O(n), because each node is visited once."},
            {"question": "What is the auxiliary space complexity of recursive DFS traversal?", "answer": "O(h), where h is the height of the tree due to the recursion call stack."}
        ],
        "mcqs": [
            {"question": "How many children can a binary tree node have at most?", "options": ["1", "2", "3", "Unlimited"], "answer": "2", "explanation": "A binary tree allows at most a left and a right child."},
            {"question": "Which traversal visits root first?", "options": ["Inorder", "Preorder", "Postorder", "None"], "answer": "Preorder", "explanation": "Preorder follows Root, Left, Right."},
            {"question": "Which traversal visits root last?", "options": ["Preorder", "Inorder", "Postorder", "Level order"], "answer": "Postorder", "explanation": "Postorder follows Left, Right, Root."},
            {"question": "Which traversal of a BST gives sorted order for distinct keys?", "options": ["Preorder", "Inorder", "Postorder", "Level order"], "answer": "Inorder", "explanation": "Inorder visits all smaller keys before the root and larger keys after it."},
            {"question": "Which data structure is used for level order traversal?", "options": ["Stack", "Queue", "Heap", "HashMap"], "answer": "Queue", "explanation": "FIFO processing visits nodes level by level."},
            {"question": "What is the traversal time for n nodes?", "options": ["O(1)", "O(log n)", "O(n)", "O(n squared)"], "answer": "O(n)", "explanation": "Every node is visited once."},
            {"question": "A node with no children is called?", "options": ["Root", "Parent", "Leaf", "Sibling"], "answer": "Leaf", "explanation": "A leaf node has no children."},
            {"question": "What is average search time in a balanced BST?", "options": ["O(n)", "O(log n)", "O(n squared)", "O(1)"], "answer": "O(log n)", "explanation": "A balanced BST reduces the search space at each level."},
            {"question": "What is worst-case BST search time in a skewed tree?", "options": ["O(1)", "O(log n)", "O(n)", "O(n log n)"], "answer": "O(n)", "explanation": "A skewed BST behaves like a linked list."},
            {"question": "Which traversal is a depth-first traversal?", "options": ["Level order", "Inorder", "Only BFS", "None"], "answer": "Inorder", "explanation": "Inorder is one of the standard DFS traversals."}
        ]
    }
})


DSA_TRACK.update({
    "dsa-graphs": {
        "title": "Graphs and Graph Algorithms",
        "description": "Learn graph representation, BFS, DFS, shortest paths, cycle detection, and connected components.",
        "content": """
# 1. What is a Graph?

A Graph is a non-linear data structure consisting of:
- Vertices (V): Nodes in the graph.
- Edges (E): Connections between vertices.

Example:
A social network can be represented as a graph.
People are vertices, and friendships are edges.

# 2. Types of Graphs

Undirected Graph:
Edges have no direction. If A connects to B, B also connects to A.

Directed Graph:
Edges have a direction. A -> B does not necessarily mean B -> A.

Weighted Graph:
Every edge has a weight or cost.

Unweighted Graph:
Edges do not carry weights.

Connected Graph:
Every pair of vertices has a path between them (for an undirected graph).

Cyclic Graph:
Contains at least one cycle.

Acyclic Graph:
Contains no cycle.

DAG:
A Directed Acyclic Graph. It has directed edges and no directed cycles.

# 3. Graph Representation

### Adjacency Matrix

A V x V matrix.
matrix[u][v] indicates whether an edge exists from u to v.

Space: O(V^2).
Checking whether an edge exists: O(1).

### Adjacency List

Each vertex stores a list of its neighbors.

Space: O(V + E).
Useful for sparse graphs.

### Edge List

Stores all edges as pairs or triples (u, v, weight).

Useful in algorithms such as Kruskal's Minimum Spanning Tree.

# 4. Breadth First Search (BFS)

BFS explores a graph level by level.

It uses a Queue.

Steps:
1. Mark the starting vertex visited.
2. Add it to a queue.
3. Remove the front vertex.
4. Visit its unvisited neighbors and add them to the queue.
5. Continue until the queue becomes empty.

Time: O(V + E) using an adjacency list.

Applications:
- Shortest path in an unweighted graph.
- Level-order traversal.
- Finding connected components.

# 5. Depth First Search (DFS)

DFS explores as deeply as possible before backtracking.

It uses recursion or an explicit stack.

Steps:
1. Mark the starting vertex visited.
2. Process it.
3. Visit an unvisited neighbor recursively.
4. Backtrack when no unvisited neighbors remain.

Time: O(V + E) using an adjacency list.

Applications:
- Cycle detection.
- Connected components.
- Topological sorting.
- Path exploration.

# 6. Shortest Path Algorithms

### BFS
Finds shortest paths in unweighted graphs when all edges have equal cost.

### Dijkstra's Algorithm
Finds shortest paths from one source in a graph with non-negative edge weights.

It commonly uses a min-priority queue.
A standard implementation with a binary heap takes O((V + E) log V).

### Bellman-Ford
Supports negative edge weights and detects reachable negative-weight cycles.
Time: O(VE).

### Floyd-Warshall
Finds shortest paths between all pairs of vertices.
Time: O(V^3).
Space: O(V^2).

# 7. Minimum Spanning Tree (MST)

A Minimum Spanning Tree connects every vertex in a connected, undirected, weighted graph with minimum total edge weight and no cycles.

### Prim's Algorithm
Grows a tree by repeatedly selecting a minimum-weight edge connecting the current tree to an unvisited vertex.

### Kruskal's Algorithm
Sorts edges by weight and uses Disjoint Set Union (DSU) to avoid cycles.

# 8. Topological Sorting

A linear ordering of vertices in a DAG such that for every directed edge u -> v, u appears before v.

Methods:
- Kahn's Algorithm using indegrees and a queue.
- DFS-based topological sorting.

Applications:
- Course prerequisite scheduling.
- Build systems.
- Task dependency resolution.

# 9. Complexity Summary

| Algorithm | Time Complexity |
|---|---|
| BFS | O(V + E) |
| DFS | O(V + E) |
| Dijkstra with binary heap | O((V + E) log V) |
| Bellman-Ford | O(VE) |
| Floyd-Warshall | O(V^3) |
| Kruskal | O(E log E) |
| Topological sort | O(V + E) |

The graph representation affects the complexity of individual operations.
""",
        "key_concepts": [
            "A graph consists of vertices and edges.",
            "An undirected edge has no direction.",
            "A directed edge has a direction.",
            "A weighted graph stores a cost on each edge.",
            "An adjacency matrix uses O(V squared) space.",
            "An adjacency list uses O(V + E) space.",
            "BFS uses a queue.",
            "DFS uses recursion or a stack.",
            "BFS finds shortest paths in unweighted graphs.",
            "Dijkstra requires non-negative edge weights.",
            "Bellman-Ford supports negative edge weights.",
            "Floyd-Warshall computes all-pairs shortest paths.",
            "A DAG is a directed acyclic graph.",
            "Topological sorting is defined for DAGs.",
            "Kruskal uses Disjoint Set Union to avoid cycles.",
            "Prim and Kruskal find minimum spanning trees."
        ],
        "examples": {
            "python": {
                "title": "Graph BFS and DFS in Python",
                "code": "from collections import deque\n\ngraph = {\n    0: [1, 2],\n    1: [0, 3],\n    2: [0, 3],\n    3: [1, 2]\n}\n\ndef bfs(start):\n    visited = {start}\n    q = deque([start])\n    result = []\n    while q:\n        node = q.popleft()\n        result.append(node)\n        for neighbor in graph[node]:\n            if neighbor not in visited:\n                visited.add(neighbor)\n                q.append(neighbor)\n    return result\n\ndef dfs(start, visited=None):\n    if visited is None:\n        visited = set()\n    visited.add(start)\n    result = [start]\n    for neighbor in graph[start]:\n        if neighbor not in visited:\n            result.extend(dfs(neighbor, visited))\n    return result\n\nprint('BFS:', bfs(0))\nprint('DFS:', dfs(0))",
                "output": "BFS: [0, 1, 2, 3]\nDFS: [0, 1, 3, 2]"
            },
            "java": {
                "title": "Graph BFS and DFS in Java",
                "code": "import java.util.*;\n\npublic class Main {\n    static List<Integer>[] graph;\n    static boolean[] visited;\n\n    static List<Integer> bfs(int start) {\n        boolean[] seen = new boolean[graph.length];\n        Queue<Integer> q = new LinkedList<>();\n        List<Integer> result = new ArrayList<>();\n        seen[start] = true;\n        q.offer(start);\n        while (!q.isEmpty()) {\n            int node = q.poll();\n            result.add(node);\n            for (int next : graph[node]) {\n                if (!seen[next]) {\n                    seen[next] = true;\n                    q.offer(next);\n                }\n            }\n        }\n        return result;\n    }\n\n    static void dfs(int node, List<Integer> result) {\n        visited[node] = true;\n        result.add(node);\n        for (int next : graph[node]) {\n            if (!visited[next]) dfs(next, result);\n        }\n    }\n\n    public static void main(String[] args) {\n        graph = new ArrayList[4];\n        for (int i = 0; i < 4; i++) graph[i] = new ArrayList<>();\n        int[][] edges = {{0,1},{0,2},{1,3},{2,3}};\n        for (int[] e : edges) {\n            graph[e[0]].add(e[1]);\n            graph[e[1]].add(e[0]);\n        }\n        System.out.println(\"BFS: \" + bfs(0));\n        visited = new boolean[4];\n        List<Integer> result = new ArrayList<>();\n        dfs(0, result);\n        System.out.println(\"DFS: \" + result);\n    }\n}",
                "output": "BFS: [0, 1, 2, 3]\nDFS: [0, 1, 3, 2]"
            },
            "cpp": {
                "title": "Graph BFS and DFS in C++",
                "code": "#include <iostream>\n#include <vector>\n#include <queue>\nusing namespace std;\n\nvector<int> graph[4];\nbool visited[4];\n\nvector<int> bfs(int start) {\n    bool seen[4] = {false};\n    queue<int> q;\n    vector<int> result;\n    seen[start] = true;\n    q.push(start);\n    while (!q.empty()) {\n        int node = q.front(); q.pop();\n        result.push_back(node);\n        for (int next : graph[node]) {\n            if (!seen[next]) {\n                seen[next] = true;\n                q.push(next);\n            }\n        }\n    }\n    return result;\n}\n\nvoid dfs(int node, vector<int>& result) {\n    visited[node] = true;\n    result.push_back(node);\n    for (int next : graph[node]) {\n        if (!visited[next]) dfs(next, result);\n    }\n}\n\nint main() {\n    int edges[][2] = {{0,1},{0,2},{1,3},{2,3}};\n    for (auto &e : edges) {\n        graph[e[0]].push_back(e[1]);\n        graph[e[1]].push_back(e[0]);\n    }\n    cout << \"BFS: \";\n    for (int x : bfs(0)) cout << x << \" \";\n    cout << \"\\nDFS: \";\n    vector<int> result;\n    dfs(0, result);\n    for (int x : result) cout << x << \" \";\n    return 0;\n}",
                "output": "BFS: 0 1 2 3\nDFS: 0 1 3 2"
            }
        },
        "dry_run": [
            {
                "step": 1,
                "operation": "Start BFS at vertex 0",
                "queue": "[0]",
                "visited": "{0}",
                "explanation": "Mark the starting vertex visited and add it to the queue."
            },
            {
                "step": 2,
                "operation": "Remove 0 and add its neighbors 1 and 2",
                "queue": "[1, 2]",
                "visited": "{0, 1, 2}",
                "explanation": "BFS discovers all immediate neighbors before going deeper."
            },
            {
                "step": 3,
                "operation": "Remove 1 and discover 3",
                "queue": "[2, 3]",
                "visited": "{0, 1, 2, 3}",
                "explanation": "Vertex 3 is discovered through vertex 1."
            },
            {
                "step": 4,
                "operation": "Remove 2, then 3",
                "queue": "[]",
                "visited": "{0, 1, 2, 3}",
                "explanation": "All vertices have been processed. BFS order is 0, 1, 2, 3."
            }
        ],
        "practice_questions": [
            {
                "title": "Number of Connected Components",
                "difficulty": "Medium",
                "problem": "Given n vertices and an undirected edge list, count how many connected components are present.",
                "approach": "Build an adjacency list. Start DFS from each unvisited vertex and increment the component count whenever a new DFS starts.",
                "solution": {
                    "python": "def count_components(n, edges):\n    graph = [[] for _ in range(n)]\n    for u, v in edges:\n        graph[u].append(v)\n        graph[v].append(u)\n    visited = set()\n    def dfs(node):\n        visited.add(node)\n        for nei in graph[node]:\n            if nei not in visited:\n                dfs(nei)\n    count = 0\n    for node in range(n):\n        if node not in visited:\n            count += 1\n            dfs(node)\n    return count\n\nprint(count_components(5, [(0,1),(1,2),(3,4)]))",
                    "java": "import java.util.*;\nclass Solution {\n    public int countComponents(int n, int[][] edges) {\n        List<Integer>[] g = new ArrayList[n];\n        for (int i = 0; i < n; i++) g[i] = new ArrayList<>();\n        for (int[] e : edges) {\n            g[e[0]].add(e[1]); g[e[1]].add(e[0]);\n        }\n        boolean[] seen = new boolean[n];\n        int count = 0;\n        for (int i = 0; i < n; i++) {\n            if (!seen[i]) {\n                count++;\n                dfs(i, g, seen);\n            }\n        }\n        return count;\n    }\n    void dfs(int u, List<Integer>[] g, boolean[] seen) {\n        seen[u] = true;\n        for (int v : g[u]) if (!seen[v]) dfs(v, g, seen);\n    }\n}",
                    "cpp": "#include <vector>\nusing namespace std;\nclass Solution {\n    void dfs(int u, vector<vector<int>>& g, vector<bool>& seen) {\n        seen[u] = true;\n        for (int v : g[u]) if (!seen[v]) dfs(v, g, seen);\n    }\npublic:\n    int countComponents(int n, vector<vector<int>>& edges) {\n        vector<vector<int>> g(n);\n        for (auto &e : edges) {\n            g[e[0]].push_back(e[1]);\n            g[e[1]].push_back(e[0]);\n        }\n        vector<bool> seen(n, false);\n        int count = 0;\n        for (int i = 0; i < n; i++) {\n            if (!seen[i]) { count++; dfs(i, g, seen); }\n        }\n        return count;\n    }\n};"
                },
                "expected_output": "2"
            },
            {
                "title": "Shortest Path in an Unweighted Graph",
                "difficulty": "Medium",
                "problem": "Given an undirected unweighted graph and source vertex, find the minimum number of edges from the source to every vertex. Return -1 for unreachable vertices.",
                "approach": "Use BFS. The first time a vertex is discovered gives its shortest distance in an unweighted graph.",
                "solution": {
                    "python": "from collections import deque\n\ndef shortest_distances(n, edges, source):\n    graph = [[] for _ in range(n)]\n    for u, v in edges:\n        graph[u].append(v)\n        graph[v].append(u)\n    dist = [-1] * n\n    dist[source] = 0\n    q = deque([source])\n    while q:\n        u = q.popleft()\n        for v in graph[u]:\n            if dist[v] == -1:\n                dist[v] = dist[u] + 1\n                q.append(v)\n    return dist\n\nprint(shortest_distances(5, [(0,1),(0,2),(1,3)], 0))",
                    "java": "import java.util.*;\nclass Solution {\n    public int[] shortestDistances(int n, int[][] edges, int source) {\n        List<Integer>[] g = new ArrayList[n];\n        for (int i = 0; i < n; i++) g[i] = new ArrayList<>();\n        for (int[] e : edges) { g[e[0]].add(e[1]); g[e[1]].add(e[0]); }\n        int[] dist = new int[n]; Arrays.fill(dist, -1);\n        Queue<Integer> q = new LinkedList<>();\n        dist[source] = 0; q.offer(source);\n        while (!q.isEmpty()) {\n            int u = q.poll();\n            for (int v : g[u]) if (dist[v] == -1) {\n                dist[v] = dist[u] + 1; q.offer(v);\n            }\n        }\n        return dist;\n    }\n}",
                    "cpp": "#include <vector>\n#include <queue>\n#include <algorithm>\nusing namespace std;\nvector<int> shortestDistances(int n, vector<vector<int>>& edges, int source) {\n    vector<vector<int>> g(n);\n    for (auto &e : edges) { g[e[0]].push_back(e[1]); g[e[1]].push_back(e[0]); }\n    vector<int> dist(n, -1);\n    queue<int> q; q.push(source); dist[source] = 0;\n    while (!q.empty()) {\n        int u = q.front(); q.pop();\n        for (int v : g[u]) if (dist[v] == -1) {\n            dist[v] = dist[u] + 1; q.push(v);\n        }\n    }\n    return dist;\n}"
                },
                "expected_output": "[0, 1, 1, 2, -1]"
            },
            {
                "title": "Detect a Cycle in an Undirected Graph",
                "difficulty": "Medium",
                "problem": "Given an undirected graph, determine whether it contains a cycle.",
                "approach": "Use DFS and track the parent of each vertex. If a visited neighbor is not the current vertex's parent, a cycle exists.",
                "solution": {
                    "python": "def has_cycle(n, edges):\n    graph = [[] for _ in range(n)]\n    for u, v in edges:\n        graph[u].append(v)\n        graph[v].append(u)\n    visited = set()\n    def dfs(u, parent):\n        visited.add(u)\n        for v in graph[u]:\n            if v not in visited:\n                if dfs(v, u):\n                    return True\n            elif v != parent:\n                return True\n        return False\n    for u in range(n):\n        if u not in visited and dfs(u, -1):\n            return True\n    return False\n\nprint(has_cycle(3, [(0,1),(1,2),(2,0)]))",
                    "java": "import java.util.*;\nclass Solution {\n    boolean hasCycle(int n, int[][] edges) {\n        List<Integer>[] g = new ArrayList[n];\n        for (int i = 0; i < n; i++) g[i] = new ArrayList<>();\n        for (int[] e : edges) { g[e[0]].add(e[1]); g[e[1]].add(e[0]); }\n        boolean[] seen = new boolean[n];\n        for (int i = 0; i < n; i++)\n            if (!seen[i] && dfs(i, -1, g, seen)) return true;\n        return false;\n    }\n    boolean dfs(int u, int parent, List<Integer>[] g, boolean[] seen) {\n        seen[u] = true;\n        for (int v : g[u]) {\n            if (!seen[v]) { if (dfs(v, u, g, seen)) return true; }\n            else if (v != parent) return true;\n        }\n        return false;\n    }\n}",
                    "cpp": "#include <vector>\nusing namespace std;\nclass Solution {\n    bool dfs(int u, int parent, vector<vector<int>>& g, vector<bool>& seen) {\n        seen[u] = true;\n        for (int v : g[u]) {\n            if (!seen[v]) { if (dfs(v, u, g, seen)) return true; }\n            else if (v != parent) return true;\n        }\n        return false;\n    }\npublic:\n    bool hasCycle(int n, vector<vector<int>>& edges) {\n        vector<vector<int>> g(n);\n        for (auto &e : edges) { g[e[0]].push_back(e[1]); g[e[1]].push_back(e[0]); }\n        vector<bool> seen(n, false);\n        for (int i = 0; i < n; i++)\n            if (!seen[i] && dfs(i, -1, g, seen)) return true;\n        return false;\n    }\n};"
                },
                "expected_output": "True"
            }
        ],
        "interview_questions": [
            {"question": "What is a graph?", "answer": "A non-linear data structure made of vertices and edges."},
            {"question": "What is the difference between directed and undirected graphs?", "answer": "Directed edges have a direction, while undirected edges represent two-way connections."},
            {"question": "What is a weighted graph?", "answer": "A graph whose edges store values such as distance or cost."},
            {"question": "What is an adjacency matrix?", "answer": "A V by V matrix that records whether edges exist between pairs of vertices."},
            {"question": "What is an adjacency list?", "answer": "A representation where each vertex stores its neighboring vertices."},
            {"question": "What is BFS?", "answer": "Breadth First Search explores vertices level by level using a queue."},
            {"question": "What is DFS?", "answer": "Depth First Search explores as far as possible along a path before backtracking, using recursion or a stack."},
            {"question": "What is the complexity of BFS using an adjacency list?", "answer": "O(V + E)."},
            {"question": "What is the complexity of DFS using an adjacency list?", "answer": "O(V + E)."},
            {"question": "When is BFS useful for shortest paths?", "answer": "For unweighted graphs, or graphs where all edges have equal cost."},
            {"question": "What is Dijkstra's algorithm?", "answer": "A single-source shortest-path algorithm for graphs with non-negative edge weights."},
            {"question": "Can Dijkstra handle negative edge weights?", "answer": "No. Bellman-Ford is a common alternative when negative edge weights are present."},
            {"question": "What is a DAG?", "answer": "A Directed Acyclic Graph: a directed graph with no directed cycles."},
            {"question": "What is topological sorting?", "answer": "A linear ordering of DAG vertices in which every directed edge goes from an earlier vertex to a later one."},
            {"question": "What is a Minimum Spanning Tree?", "answer": "A minimum-total-weight set of edges connecting all vertices of a connected, undirected, weighted graph without cycles."}
        ],
        "mcqs": [
            {"question": "Which data structure does BFS use?", "options": ["Stack", "Queue", "Heap", "Trie"], "answer": "Queue", "explanation": "BFS uses FIFO processing to visit vertices level by level."},
            {"question": "Which data structure is naturally used by recursive DFS?", "options": ["Queue", "Call stack", "Heap", "Hash table"], "answer": "Call stack", "explanation": "Recursive calls are managed by the program's call stack."},
            {"question": "Which representation requires O(V squared) space?", "options": ["Adjacency list", "Edge list", "Adjacency matrix", "Queue"], "answer": "Adjacency matrix", "explanation": "It stores a cell for every pair of vertices."},
            {"question": "What is the BFS complexity with an adjacency list?", "options": ["O(V)", "O(E)", "O(V + E)", "O(V squared)"], "answer": "O(V + E)", "explanation": "Each vertex and edge is processed a constant number of times."},
            {"question": "Which algorithm finds shortest paths in an unweighted graph?", "options": ["DFS", "BFS", "Kruskal", "Prim"], "answer": "BFS", "explanation": "BFS explores vertices in increasing number of edges from the source."},
            {"question": "Dijkstra's algorithm assumes edge weights are:", "options": ["Negative", "Non-negative", "All zero", "Strings"], "answer": "Non-negative", "explanation": "Negative edges can invalidate Dijkstra's greedy finalization."},
            {"question": "Which algorithm supports negative edge weights?", "options": ["BFS", "Bellman-Ford", "Prim", "Kruskal"], "answer": "Bellman-Ford", "explanation": "Bellman-Ford supports negative weights and can detect reachable negative cycles."},
            {"question": "A DAG contains:", "options": ["Undirected cycles", "Directed cycles", "No directed cycles", "Only one vertex"], "answer": "No directed cycles", "explanation": "DAG stands for Directed Acyclic Graph."},
            {"question": "Topological sorting is applicable to:", "options": ["Every graph", "DAG", "Only complete graphs", "Only trees"], "answer": "DAG", "explanation": "A topological ordering exists only for directed acyclic graphs."},
            {"question": "Which algorithm uses DSU in a common MST implementation?", "options": ["BFS", "Dijkstra", "Kruskal", "Floyd-Warshall"], "answer": "Kruskal", "explanation": "DSU efficiently checks whether an edge would connect vertices already in the same component."}
        ]
    }
})
