from functools import partial
from importlib import import_module

from dcspy.dcsbios import ProtocolParser
from dcspy.starter import _prepare_socket


bios_data = {
    #'UHF_CHAN_DISP': {'class': 'StringBuffer', 'args': {'address': 0x45b0, 'max_length': 0x2}, 'value': ''},
    'MASTER_ARM_SW': {'class': 'IntegerBuffer', 'args': {'address': 0x4426, 'mask': 0xc000, 'shift_by': 0xe}, 'value': int()},
}


def callback(field_name, value):
    bios_data[field_name]['value'] = value
    print(f'{field_name}: {value}')


def _handle_connection(parser, sock):
    while True:
        try:
            dcs_bios_resp = sock.recv(2048)
            for int_byte in dcs_bios_resp:
                parser.process_byte(int_byte)
        except OSError as exp:
            print(f'Main loop error: {exp}')


def _subscribe(parser):
    for field_name, proto_data in bios_data.items():
        buffer = getattr(import_module('dcspy.dcsbios'), proto_data['class'])
        buffer(parser=parser, callback=partial(callback, field_name), **proto_data['args'])


def run():
    dcs_sock = _prepare_socket()
    parser = ProtocolParser()
    _subscribe(parser)
    try:
        _handle_connection(parser, dcs_sock)
    except KeyboardInterrupt:
        print('bye!')
    finally:
        dcs_sock.close()


if __name__ == '__main__':
    print('To exit press Ctrl-C')
    run()
