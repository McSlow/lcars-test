import psutil
from functools import reduce
from requests import get, post
import config

def get_ip_address_string():
    """
    Consolidates a list of IP addresses into a string, stripping out any blank
    entries as well as the local `127.0.0.1` entry.
    """

    try:
        return ' '.join(get_ip_addresses())
    except:
        return ''

def get_ip_addresses():
    """
    Returns all the IP addresses of the machine we're running on.
    Shamelessly derived from:
        https://stackoverflow.com/questions/270745/how-do-i-determine-all-of-my-ip-addresses-when-i-have-multiple-nics
    """

    ip_list = filter(
        lambda ip: ip is not None and ip != '127.0.0.1',
        [interface_to_ip(v) for v in psutil.net_if_addrs().values()])

    return ip_list


def interface_to_ip(interface):
    """
    Gets the IPv4 address from a `net_if_addrs` interface record.
    The record is passed as a `snic` `namedtuple`.
    This function locates the IPv4 one and returns it.
    """
    for record in interface:
        if record.family == 2:  # AF_INET
            return record.address

    return None

def get_stuff():
    url = 'http://192.168.1.101:8123/api/states/light.flurschrank'
    headers = {
                'Authorization': 'Bearer jdc4ttMJKSc9gw2kCVq9g4pBMbzJf-h19M8OOvNlnU',
                    'content-type': 'application/json',
                    }

    response = get(url, headers=headers)
    return response.text

def set_ikea():
    url = 'http://192.168.1.101:8123/api/services/light/toggle'
    headers = {
                'Authorization': 'Bearer MJKSc9gw2kCVq9g4pBMbzJf-h19M8OOvNlnU',
                    'content-type': 'application/json',
                    }
    data = '{"entity_id": "light.flurschrank"}'
    response = post(url, headers=headers, data=data)

