def test_a1():
    assert 4 > 3
    assert 4 < 2 
    assert 5 == 6
    assert 5 + 5 == 10

def test_a2():
    assert True
    assert 1
    assert 0
    assert 1 < 3 

def test_a4():
    assert( 3 - 1 * 4 / 2 ) == 4.0
    assert ((3-1) * ( 4 / 2 )) == 4.0

def test_a3():
    assert "abc" == "abcd"

def test_a5():
    assert divmod(9,5) == (1,4)
    assert divmod(9,5)
    assert "py" in "the test is pytest"
    assert "put" not in "the test is pytest"