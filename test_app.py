
import pytest
from app import calculate_total


def test_total_without_discount():
    assert calculate_total(200) == 210.00


def test_total_at_300():
    assert calculate_total(300) == 315.00


def test_total_with_discount():
    assert calculate_total(400) == 378.00


def test_decimal_amount():
    assert calculate_total(100.50) == 105.53


def test_demo_failure():
    assert calculate_total(100) == 999