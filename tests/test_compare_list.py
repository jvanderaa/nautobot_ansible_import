"""
Test of Ansible Filters
"""
from plugins.filter.filter import FilterModule


def test_filtermodule_verify_compare_lists():
    """
    Functional test of Verify Serial Number
    """
    device_serial1 = ["99JCD34YT4C"]
    nautobot_serial1 = ["99JCD34YT4C"]
    nautobot_false_serial1 = ["NTCFTW"]
    assert FilterModule.compare_lists(device_serial1, nautobot_serial1)
    assert not FilterModule.compare_lists(device_serial1, nautobot_false_serial1)


def test_filtermodule_verify_multiple_compare_lists():
    """
    Functional test to verify multiple serial numbers are asserted properly
    """
    device_serial_list1 = ["99JCD34YT4C", "548SDFHA5D"]
    nautobot_serial1 = ["99JCD34YT4C", "548SDFHA5D"]
    nautobot_serial2 = ["99JCD34YT4C", "548SDFHA5D", "NTCISAWESOME", "REDHATFTW"]
    assert FilterModule.compare_lists(device_serial_list1, nautobot_serial1)
    assert not FilterModule.compare_lists(device_serial_list1, nautobot_serial2)
