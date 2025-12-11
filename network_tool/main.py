import core.output_string as Out
from core.utils import *


def output_file():
    INPUT_IP = input("Enter IP")
    SUBNET_MASK= "255.255.255.192"
    ID = input("Enter your ID")
    filename = f"subnet_info_{INPUT_IP}_{ID}.txt"
    
    with open(filename, 'w') as f:
        
        f.write(Out.format_input_ip(INPUT_IP))
        f.write(Out.format_subnet_mask(SUBNET_MASK))
        f.write(Out.format_classful_status(ip_class(INPUT_IP)))
        f.write(Out.format_network_address(network_address(INPUT_IP,SUBNET_MASK)))
        f.write(Out.format_broadcast_address(broadcast_address(INPUT_IP,SUBNET_MASK)))
        f.write(Out.format_num_hosts(number_of_hosts(28)))
        f.write(Out.format_cidr_mask(number_of_hosts(28)))

output_file()
        

