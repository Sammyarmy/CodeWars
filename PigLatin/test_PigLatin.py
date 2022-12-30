from PigLatin import pig_it

def test_root_returns_correct_response():
    result = pig_it('Pig latin is cool')
    assert result == 'igPay atinlay siay oolcay'

def test_2():
    result = pig_it('This is my string')
    assert result == 'hisTay siay ymay tringsay'