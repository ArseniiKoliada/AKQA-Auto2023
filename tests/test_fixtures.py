import pytest

# test the fixtures
@pytest.mark.check
def test_change_name(user):
       assert user.name == 'Arsenii'

    
@pytest.mark.check
def test_change_second_name(user):
        assert user.second_name == 'Koliada'
