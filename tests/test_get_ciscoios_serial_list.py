from plugins.filter.filter import FilterModule

ANSIBLE_FACTS_SINGLE = {
    "net_all_ipv4_addresses": [
        "192.168.0.164",
        "172.31.1.1",
        "172.31.0.1",
        "10.50.50.1",
    ],
    "net_all_ipv6_addresses": [],
    "net_api": "cliconf",
    "net_filesystems": ["flash0:"],
    "net_filesystems_info": {
        "flash0:": {"spacefree_kb": 1948176.0, "spacetotal_kb": 2092496.0}
    },
    "net_gather_network_resources": [],
    "net_gather_subset": ["hardware", "default", "interfaces"],
    "net_hostname": "BORDER",
    "net_image": "flash0:/vios-adventerprisek9-m",
    "net_interfaces": {
        "GigabitEthernet0/0": {
            "bandwidth": 1000000,
            "description": None,
            "duplex": "Auto",
            "ipv4": [{"address": "192.168.0.164", "subnet": "24"}],
            "lineprotocol": "up",
            "macaddress": "0c98.53d9.d800",
            "mediatype": "RJ45",
            "mtu": 1500,
            "operstatus": "up",
            "type": "iGbE",
        },
        "GigabitEthernet0/1": {
            "bandwidth": 1000000,
            "description": None,
            "duplex": "Auto",
            "ipv4": [{"address": "172.31.1.1", "subnet": "24"}],
            "lineprotocol": "up",
            "macaddress": "0c98.53d9.d801",
            "mediatype": "RJ45",
            "mtu": 1500,
            "operstatus": "up",
            "type": "iGbE",
        },
        "GigabitEthernet0/2": {
            "bandwidth": 1000000,
            "description": "Configured by Ansible",
            "duplex": "Auto",
            "ipv4": [{"address": "172.31.0.1", "subnet": "24"}],
            "lineprotocol": "up",
            "macaddress": "0c98.53d9.d802",
            "mediatype": "RJ45",
            "mtu": 1500,
            "operstatus": "up",
            "type": "iGbE",
        },
        "GigabitEthernet0/3": {
            "bandwidth": 1000000,
            "description": "Configured by Ansible",
            "duplex": "Auto",
            "ipv4": [],
            "lineprotocol": "down",
            "macaddress": "0c98.53d9.d803",
            "mediatype": "RJ45",
            "mtu": 1500,
            "operstatus": "down",
            "type": "iGbE",
        },
        "Loopback0": {
            "bandwidth": 8000000,
            "description": None,
            "duplex": None,
            "ipv4": [{"address": "10.50.50.1", "subnet": "32"}],
            "lineprotocol": "up",
            "macaddress": None,
            "mediatype": None,
            "mtu": 1514,
            "operstatus": "up",
            "type": None,
        },
    },
    "net_iostype": "IOS",
    "net_memfree_mb": 253431.28125,
    "net_memtotal_mb": 315455.65625,
    "net_model": "IOSv",
    "net_neighbors": {
        "GigabitEthernet0/2": [{"host": "wanrtr01.josh-v.com", "port": "Gi1"}]
    },
    "net_python_version": "3.8.1",
    "net_serialnum": "98TM4IDVPLTBHYGPX4Q21",
    "net_system": "ios",
    "net_version": "15.6(1)T",
    "network_resources": {},
}

ANSIBLE_FACTS_THREE = {
    "net_all_ipv4_addresses": [
        "192.168.0.164",
        "172.31.1.1",
        "172.31.0.1",
        "10.50.50.1",
    ],
    "net_all_ipv6_addresses": [],
    "net_api": "cliconf",
    "net_filesystems": ["flash0:"],
    "net_filesystems_info": {
        "flash0:": {"spacefree_kb": 1948176.0, "spacetotal_kb": 2092496.0}
    },
    "net_gather_network_resources": [],
    "net_gather_subset": ["hardware", "default", "interfaces"],
    "net_hostname": "BORDER",
    "net_image": "flash0:/vios-adventerprisek9-m",
    "net_interfaces": {
        "GigabitEthernet0/0": {
            "bandwidth": 1000000,
            "description": None,
            "duplex": "Auto",
            "ipv4": [{"address": "192.168.0.164", "subnet": "24"}],
            "lineprotocol": "up",
            "macaddress": "0c98.53d9.d800",
            "mediatype": "RJ45",
            "mtu": 1500,
            "operstatus": "up",
            "type": "iGbE",
        },
        "GigabitEthernet0/1": {
            "bandwidth": 1000000,
            "description": None,
            "duplex": "Auto",
            "ipv4": [{"address": "172.31.1.1", "subnet": "24"}],
            "lineprotocol": "up",
            "macaddress": "0c98.53d9.d801",
            "mediatype": "RJ45",
            "mtu": 1500,
            "operstatus": "up",
            "type": "iGbE",
        },
        "GigabitEthernet0/2": {
            "bandwidth": 1000000,
            "description": "Configured by Ansible",
            "duplex": "Auto",
            "ipv4": [{"address": "172.31.0.1", "subnet": "24"}],
            "lineprotocol": "up",
            "macaddress": "0c98.53d9.d802",
            "mediatype": "RJ45",
            "mtu": 1500,
            "operstatus": "up",
            "type": "iGbE",
        },
        "GigabitEthernet0/3": {
            "bandwidth": 1000000,
            "description": "Configured by Ansible",
            "duplex": "Auto",
            "ipv4": [],
            "lineprotocol": "down",
            "macaddress": "0c98.53d9.d803",
            "mediatype": "RJ45",
            "mtu": 1500,
            "operstatus": "down",
            "type": "iGbE",
        },
        "Loopback0": {
            "bandwidth": 8000000,
            "description": None,
            "duplex": None,
            "ipv4": [{"address": "10.50.50.1", "subnet": "32"}],
            "lineprotocol": "up",
            "macaddress": None,
            "mediatype": None,
            "mtu": 1514,
            "operstatus": "up",
            "type": None,
        },
    },
    "net_iostype": "IOS",
    "net_memfree_mb": 253431.28125,
    "net_memtotal_mb": 315455.65625,
    "net_model": "IOSv",
    "net_neighbors": {
        "GigabitEthernet0/2": [{"host": "wanrtr01.josh-v.com", "port": "Gi1"}]
    },
    "net_python_version": "3.8.1",
    "net_stacked_serialnums": ["98TM4IDVPLTBHYGPX4Q21", "NTCMSP1", "NTCDFW2"],
    "net_system": "ios",
    "net_version": "15.6(1)T",
    "network_resources": {},
}


def test_get_ciscoios_serial_list_single_device():
    """
    Functional test of get_ciscoios_serial_list
    """
    assert FilterModule.get_ciscoios_serial_list(ANSIBLE_FACTS_SINGLE) == [
        "98TM4IDVPLTBHYGPX4Q21"
    ]


def test_get_ciscoios_serial_list_three_devices():
    """
    Functional test for multiple devices in get_ciscoios_serial_list
    """
    assert FilterModule.get_ciscoios_serial_list(ANSIBLE_FACTS_THREE) == [
        "98TM4IDVPLTBHYGPX4Q21",
        "NTCMSP1",
        "NTCDFW2",
    ]
