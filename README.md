[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/IZKxKZ71)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=19272834&assignment_repo_type=AssignmentRepo)
# Task1-classes

Repository containing exercises focused on Python classes, specifically inheritance and properties.

## Project Structure

-   `tasks/`: Contains the exercise files.
    -   `shape.py`: Defines the abstract base class `Shape`.
    -   `task1.py`: Exercise 1 - Implementing `Rectangle` and `Square` using inheritance.
    -   `task2.py`: Exercise 2 - Implementing `Circle` using properties.

## Exercises

### Exercise 1: Inheritance (`tasks/task1.py`)

Implement the `Rectangle` class inheriting from `Shape`. It should have `width` and `height` attributes and implement `get_area`, `get_perimeter`, and `__str__`.
Implement the `Square` class inheriting from `Rectangle`. It should take a single `side` length during initialization.

### Exercise 2: Properties (`tasks/task2.py`)

Implement the `Circle` class inheriting from `Shape`. It should have a `radius` attribute. Implement `get_area`, `get_perimeter`, and `__str__`.
Implement a `diameter` property using `@property` for the getter and `@diameter.setter` for the setter. The setter should validate that the diameter is positive.

# Setup Instructions

## Environment setup using `uv`
```bash
uv venv
uv sync
.venv\Scripts\activate
```

## Running the Code

The `main.py` script serves as the entry point to run the examples for both tasks. Uncomment the relevant sections within `main.py` to test the implementations.

```bash
python main.py
```

## Running Tests

Tests are provided in the `tests/` directory. You can run them using `pytest`:

```bash
pytest
```
