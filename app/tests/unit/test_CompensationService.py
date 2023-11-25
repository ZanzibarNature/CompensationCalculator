import pytest
import sys
import os
import re

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from service.CompensationService import CompensationService

def test_CalculateCompensation():
    service = CompensationService()

    # Test case 1: Convert to EUR
    result = service.CalculateCompensation(100, "EUR")
    assert result["co2FootprintInKG"] == 17.1
    assert result["totalCost"] == 0.47
    assert result["currency"] == "EUR"

def test_patternDistance():
    service = CompensationService()

    # Test case 1: Valid distance
    assert service.patternDistance(100) == True

    # Test case 2: Invalid distance
    with pytest.raises(Exception):
        service.patternDistance("abc")

def test_patternCurrency():
    service = CompensationService()

    # Test case 1: Valid currency
    assert service.patternCurrency("EUR") == True

    # Test case 2: Invalid currency
    with pytest.raises(Exception):
        service.patternCurrency("123")

if __name__ == "__main__":
    pytest.main()