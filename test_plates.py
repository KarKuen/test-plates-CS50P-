from plates import is_valid

def test_max():
    assert is_valid('CS12345') == False

def test_min():
    assert is_valid('C') == False

def test_zero():
    assert is_valid('CS05') == False

def test_letters():
    assert is_valid('C12345') == False

def test_punctuation():
    assert is_valid('CS50!') == False

def test_number():
    assert is_valid('CS50P') == False