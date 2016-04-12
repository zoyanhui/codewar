import sys,os
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  
sys.path.insert(0,parentdir) 
from testtool.testtool import test
from ipv4_parser import ipv4__parser

test.assert_equals(
    ipv4__parser('192.168.50.1', '255.255.255.0'), 
    ('192.168.50.0', '0.0.0.1')
)
test.assert_equals(
    ipv4__parser('192.168.50.129', '255.255.255.192'), 
    ('192.168.50.128', '0.0.0.1')
)
test.assert_equals(
    ipv4__parser('65.196.188.53', '255.255.240.0'), 
    ('65.196.176.0', '0.0.12.53')
)

test.run_test()
