from app import exactly_two_positive

def test_positive_numbers():
    assert exactly_two_positive(2, 4, -3) == True
    assert exactly_two_positive(-4, 6, 8) == True
    assert exactly_two_positive(4, -6, 9) == True

def test_mixed_numbers():
    assert exactly_two_positive(-4, 6, 0) == False
    assert exactly_two_positive(4, 6, 10) == False
    assert exactly_two_positive(-14, -3, -4) == False
