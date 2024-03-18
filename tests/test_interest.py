from ..app.interest import simple_interest,compound_interest

def test_simple_interest():
    assert(simple_interest(100,1.05,3) == 3.15)
    assert(simple_interest(100,-1.05,3) == -3.15)

def test_compound_interest():
    assert(compound_interest(100,1.05,3) == 3.1831907624999767)