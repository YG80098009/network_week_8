def validate_ip_format(address_str):
    octets = address_str.split('.')
    if len(octets) != 4:
        return False
    flag = True
    for octet in octets:
        num = int(octet)
        if num > 255 or num < 0:
            flag = False
    return flag



def validate_subnet_mask(mask_str):
    is_valid = validate_ip_format(mask_str)
    if not is_valid:
        return False

    mask_octets = [int(o) for o in mask_str.split('.')]
    binary_mask = ''.join(f"{o:08b}" for o in mask_octets)
    print(binary_mask)
    if '01' in binary_mask:
        return False
    return True



def network_address(ip_str, mask_str):
    ip_octets = [int(o) for o in ip_str.split('.')]

    mask_octets = [int(o) for o in mask_str.split('.')]
    
    network_octets = [(ip_octets[i] & mask_octets[i]) for i in range(4)]
    
    return ".".join(map(str, network_octets))


def broadcast_address(ip_str, mask_str):
    ip_octets = [int(o) for o in ip_str.split('.')]

    mask_octets = [int(o) for o in mask_str.split('.')]
    
    octets = [(255 - mask_octets[i]) for i in range(4)]
    
    network_octets = [(ip_octets[i] & mask_octets[i]) for i in range(4)]

    broadcast_octets = [(network_octets[i] | octets[i]) for i in range(4)]

    return ".".join(map(str, broadcast_octets))


def number_of_hosts(cidr):
    bits_of_host = 32 - cidr
    
    if bits_of_host >= 2:
        return (2 ** bits_of_host) - 2
    elif bits_of_host == 1:
        return 0
    else:  
        return 0

def ip_class(ip_str):
    octet_one = int(ip_str.split('.')[0])
    
    if 1 <= octet_one <= 126:
        return 'Class A', 8
    elif 128 <= octet_one <= 191:
        return 'Class B', 16
    elif 192 <= octet_one <= 223:
        return 'Class C', 24
    else:
        return 'Classless'