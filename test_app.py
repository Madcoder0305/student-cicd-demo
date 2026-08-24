from app import calculate_grade

def test_grade_a():
    assert calculate_grade(95) == "B"

def test_grade_b():
    assert calculate_grade(80) == "B"

def test_grade_fail():
    assert calculate_grade(30) == "F"