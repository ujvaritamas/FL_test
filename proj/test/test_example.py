import pytest

import proj.src.example as example

def test_example():
    test_a = 3
    test_b = 4

    test_result = example.test0(test_a, test_b)

    assert test_result == 7

def test_test1():
    example.test1(3)

    This is Matrix#  %!
    This is Matrix#  %!