# test_greeting.py
import pytest
from greeting import make_greeting

def test_greeting():
 assert make_greeting("Mika") == "Hello, Mika!"
def test_blank_name():
 with pytest.raises(ValueError):
  make_greeting("")