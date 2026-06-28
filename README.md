# Student Status Dictionary

A beginner-friendly Python project that demonstrates how to use dictionaries in Python by storing a student's information, calculating their academic status, and displaying the stored data.

## Features

- Stores student information using a dictionary
- Records the student's name
- Records the student's average grade
- Determines whether the student passed or failed
- Displays all stored information using dictionary iteration

## Technologies Used

- Python 3

## How to Run

1. Clone this repository:

```bash
git clone https://github.com/your-username/student-status-dictionary.git
```

2. Navigate to the project folder:

```bash
cd student-status-dictionary
```

3. Run the script:

```bash
python main.py
```

## Example

### Input

```text
Name: Alice
Average for Alice: 8.5
```

### Output

```text
name --> Alice
average --> 8.5
status --> Passed
```

## Learning Objectives

This project demonstrates:

- Dictionaries (`dict`)
- Key-value pairs
- User input handling
- Conditional statements (`if` / `else`)
- Dictionary iteration with `items()`
- Formatted output

## Key Concepts

### Creating a Dictionary

```python
student = {}
```

Creates an empty dictionary.

### Adding Data

```python
student['name'] = 'Alice'
student['average'] = 8.5
```

Stores values using descriptive keys.

### Determining Student Status

```python
if student['average'] >= 7:
    student['status'] = 'Passed'
else:
    student['status'] = 'Failed'
```

Assigns the student's academic status based on the average grade.

### Iterating Through the Dictionary

```python
for key, value in student.items():
```

Loops through every key-value pair stored in the dictionary.
