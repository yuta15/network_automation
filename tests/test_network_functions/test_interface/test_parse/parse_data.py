test_parse_ethernet_data = {
    "mac-address": None,
    "auto-negotiate": None,
    "port-speed": None,
    "enable-flow-control": False,
    "hw-mac-address": "52:54:00:10:73:00",
    "negotiated-duplex-mode": None,
    "negotiated-port-speed": 'openconfig-if-ethernet:SPEED_1GB',
    "counters": {
        "in-mac-control-frames": "0",
        "in-mac-pause-frames": "0",
        "in-oversize-frames": "0",
        "in-jabber-frames": "0",
        "in-fragment-frames": "0",
        "in-8021q-frames": "0",
        "in-crc-errors": "0",
        "out-mac-control-frames": "0",
        "out-mac-pause-frames": "0",
        "out-8021q-frames": "0"
        }
    }
    

test_parse_state_data =  {
    "name": "GigabitEthernet1",
    "type": "iana-if-type:ethernetCsmacd",
    "enabled": None,
    "ifindex": 1,
    "admin-status": None,
    "oper-status": None,
    "last-change": None,
    "counters": {
        "in-octets": "0",
        "in-unicast-pkts": "0",
        "in-broadcast-pkts": "0",
        "in-multicast-pkts": "0",
        "in-discards": "0",
        "in-errors": "0",
        "in-unknown-protos": "0",
        "in-fcs-errors": "0",
        "out-octets": "0",
        "out-unicast-pkts": "0",
        "out-broadcast-pkts": "0",
        "out-multicast-pkts": "0",
        "out-discards": "0",
        "out-errors": "0",
        "last-clear": "1715487161000000000"
    }
}


test_parse_subint_ipv4_addr = {
    "address": [
        {
        "ip": "10.10.1.1",
        "config": {
            "ip": "10.10.1.1",
            "prefix-length": 30
            },
        "state": {
            "ip": "10.10.1.1",
            "prefix-length": 30
            }
        }
    ]
}