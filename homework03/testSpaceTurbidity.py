from spaceTurbidity import calculate_turbidity, calculate_time
import pytest

def test_calculate_turbidity():
    assert calculate_turbidity([ {'c' : 1, 'd' : 2} ],'c','d',0) == 2
    assert isinstance(calculate_turbidity([ {'c' : 1, 'd' : 2} ],'c','d',0), int) == False
    assert isinstance(calculate_turbidity([ {'c' : 1, 'd' : 2} ],'c','d',0), float) == True

def test_calc_time():
    assert calculate_time(3) >= 0
    assert isinstance(calculate_time(4), (int, float)) == True
    assert isinstance(calculate_time(5), str) == False

def test_calculate_turbidity_exceptions():
    with pytest.raises(IndexError):
        calculate_turbidity( [ {'cali' : 1, 'detect' : 2} ], 'cali',' detector', 1)
    with pytest.raises(NameError):
        calculate_turbidiy( [ {'cali' : 1, 'detect' : 2} ], 'cali', 'detect', 1)

def test_calculate_time_exceptions():
    with pytest.raises(TypeError):
        calculate_time([ { 'cali' : 1}, 1 ])
    with pytest.raises(NameError):
        calculate_tim([ {'cali' : 1, 'detect' : 2} ], 1)
