# simplemath

A tiny example Python package with simple arithmetic classes.

## Install (editable for development)
```bash
pip install -e .

## Usage

from simplemath import Calculator, Accumulator

c = Calculator()
print(c.add(2, 3))  # 5

a = Accumulator(10)
print(a.add(7))     # 17