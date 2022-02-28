import json
from ml_data_analysis import *
import pytest

data = {}
data['mass'] = []
data['class'] = []
data['mass'].append( {'mass': 1} )
data['mass'].append( {'mass': 2} )
data['class'].append( {"recclass": "hi" } )

def test_compute_average_mass():
    assert isinstance(compute_average_mass(data['mass'], 'mass'), float) == True
    assert compute_average_mass(data['mass'], 'mass') != 0
    assert isinstance(compute_average_mass(data['mass'],'mass'), str) == False
def test_compute_average_mass_exceptions():
    with pytest.raises(KeyError):
        compute_average_mass([{'mass':1}],'mss')
    with pytest.raises(NameError):
        compute_average_mas([{'mass':1}],'mass')

def test_check_hemisphere():
    assert check_hemisphere(1,1)== 'Northern & Eastern'
    assert isinstance(check_hemisphere(0.5,2), int) == False
    assert isinstance(check_hemisphere(0.5,2), str) == True
def test_check_hemisphere_exceptions():
    with pytest.raises(TypeError):
        check_hemisphere([{'one', 'two' }])
    with pytest.raises(NameError):
        check_hemispher([{2, 0.5}])

def test_count_classes():
    assert count_classes(data['class'], 'recclass') >= 0
    assert isinstance(count_classes(data['class'], 'recclass'), int) == False
    assert isinstance(count_classes(data['class'], 'recclass'), float) ==False
def test_count_classes_exceptions():
    with pytest.raises(KeyError):
        count_classes([{'recclass':1}],'mass')
    with pytest.raises(NameError):
        count_clases([{'recclass':1}],'recclass')
