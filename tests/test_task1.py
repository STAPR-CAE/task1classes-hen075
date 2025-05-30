from typing import Type

import pytest

from tasks.shape import Shape


@pytest.fixture
def rectangle_class() -> Type[Shape]:
    try:
        from tasks.task1 import Rectangle

        return Rectangle
    except ImportError:
        pytest.fail("Rectangle class not found in task1.py")


@pytest.fixture
def square_class() -> Type[Shape]:
    try:
        from tasks.task1 import Square

        return Square
    except ImportError:
        pytest.fail("Square class not found in task1.py")


def test_rectangle(rectangle_class: Type[Shape]):
    rect = rectangle_class(5, 10)
    assert rect.width == 5
    assert rect.height == 10
    assert rect.get_area() == 50
    assert rect.get_perimeter() == 30


def test_square(square_class: Type[Shape]):
    square = square_class(5)
    assert square.width == 5
    assert square.height == 5
    assert square.get_area() == 25
    assert square.get_perimeter() == 20
