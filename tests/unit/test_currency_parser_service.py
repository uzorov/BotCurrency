import pytest
from datetime import datetime
from app.service.currency_parser_service import getCurrency, get_exchange_list_xrates, get_exchange_list_metal

@pytest.mark.parametrize("currency1, expected_result", [
    ("EUR", None)
])
def test_getCurrency(currency1, expected_result):
    assert getCurrency(currency1) == expected_result

def test_get_exchange_list_xrates_returns_correct_types():
    currency = "USD"
    amount = 1
    price_datetime, exchange_rates = get_exchange_list_xrates(currency, amount)
    assert isinstance(price_datetime, datetime)
    assert isinstance(exchange_rates, dict)

def test_get_exchange_list_xrates_returns_exchange_rate_for_Russian_Ruble():
    currency = "USD"
    amount = 1
    _, exchange_rates = get_exchange_list_xrates(currency, amount)
    assert "Russian Ruble" in exchange_rates
    assert isinstance(exchange_rates["Russian Ruble"], float)

def test_get_exchange_list_metal_CGN_returns_valid_exchange_rate():
    metal = "CGN"
    assert get_exchange_list_metal(metal) != "0"

def test_get_exchange_list_metal_STL_returns_valid_exchange_rate():
    metal = "STL"
    assert get_exchange_list_metal(metal) != "0"

def test_getCurrency_returns_None_for_unsupported_currency():
    unsupported_currency = "EUR"
    assert getCurrency(unsupported_currency) is None

def test_get_exchange_list_metal_raises_exception_for_invalid_metal():
        invalid_metal = "INVALID"
        get_exchange_list_metal(invalid_metal)

def test_get_exchange_list_xrates_raises_exception_for_invalid_currency():
    with pytest.raises(Exception):
        invalid_currency = "INVALID"
        get_exchange_list_xrates(invalid_currency)




