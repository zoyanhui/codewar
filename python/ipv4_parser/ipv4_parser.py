# Write a function that takes two string parameters, an IP (v4) address and
# a subnet mask, and returns two strings: the network block,
# and the host identifier.

# For example:
# >>> print ipv4__parser('192.168.50.1', '255.255.255.0')
# ('192.168.50.0', '0.0.0.1')

def ipv4__parser(ip_addr, mask):
    ip_vals = [int(each) for each in ip_addr.split('.')]
    mask_vals = [int(each) for each in mask.split('.')]
    net_addrs = map(lambda ip,m: ip & m, ip_vals, mask_vals)
    host_addrs = map(lambda ip,m: ip & (~m), ip_vals, mask_vals)
    net_addr = '.'.join(str(each) for each in net_addrs)
    host_addr = '.'.join(str(each) for each in host_addrs)
    return net_addr, host_addr
