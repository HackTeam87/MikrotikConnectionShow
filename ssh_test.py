from netmiko import ConnectHandler

class Mikrotik:

    def send_show_command(self, host, username, password, port, device_type,read_timeout, command):
        conn = ConnectHandler(host=host, username=username, password=password, port=port, device_type=device_type)
        output = conn.send_command(command, read_timeout=read_timeout)
        conn.disconnect()
        return output
        # print(output)
        

    # print('Closing Connection')
    # 'mikrotik_routeros'
    # >>> from ssh_test import Mikrotik
    # >>> test = Mikrotik().send_show_command('1.1.1.1', 'login', 'pass', 22, 'mikrotik_routeros', 'system healt print')
    #  ip firewall connection print without-paging  where src-address~"178.211.135.168"

