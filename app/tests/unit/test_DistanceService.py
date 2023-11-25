import pytest

from service.DistanceService import DistanceService

def test_patternIata():
    service = DistanceService()

    # Test case 1: Valid input
    assert service.patternIata("JFK") == True

    # Test case 2: Invalid input
    with pytest.raises(Exception):
        service.patternIata("123")

    # Test case 3: Invalid input with special characters
    with pytest.raises(Exception):
        service.patternIata("LHR!")

if __name__ == "__main__":
    pytest.main()