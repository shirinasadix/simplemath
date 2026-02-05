from __future__ import annotations

class Calculator:
    """A tiny calculator with basic arithmetic operations."""

    def add(self, a: float, b: float) -> float:
        return a + b

    def subtract(self, a: float, b: float) -> float:
        return a - b

    def multiply(self, a: float, b: float) -> float:
        return a * b

    def divide(self, a: float, b: float) -> float:
        if b == 0:
            raise ZeroDivisionError("b must not be zero")
        return a / b


class Accumulator:
    """Keeps a running total and supports simple operations."""

    def __init__(self, start: float = 0.0) -> None:
        self.total = float(start)

    def add(self, x: float) -> float:
        self.total += x
        return self.total

    def reset(self) -> None:
        self.total = 0.0
