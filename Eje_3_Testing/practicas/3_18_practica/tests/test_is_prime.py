from practica_is_prime.is_prime import is_prime

def test_non_number_inputs():
    assert is_prime('seven') is False
    assert is_prime(None) is False
    assert is_prime([2]) is False

def test_non_integer_numbers():
    assert is_prime(2.5) is False
    assert is_prime(3.1) is False

def test_numbers_leq_one():
    assert is_prime(0) is False
    assert is_prime(1) is False
    assert is_prime(-5) is False

def test_non_prime_numbers():
    assert is_prime(4) is False
    assert is_prime(6) is False
    assert is_prime(9) is False

def test_prime_numbers():
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(5) is True
    assert is_prime(7) is True
