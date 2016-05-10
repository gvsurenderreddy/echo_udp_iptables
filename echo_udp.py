#!/usr/bin/env python
""" Sends and waits for an UDP message N times.
    Sample usage:
        ./echo_udp.py 55654 55655 "Foo" 3
"""
import sys
import socket
from time import sleep


if len(sys.argv) != 5:
    print "Usage: {} <UPD_port_listen> <UPD_port_send> <Message> <Number_times>".format(sys.argv[0])
    sys.exit(0)

UDP_IP = "127.0.0.1"
UDP_LISTEN_PORT = int(sys.argv[1])
UDP_SEND_PORT = int(sys.argv[2])
MESSAGE = sys.argv[3]
NUMBER_TIMES = int(sys.argv[4])

recv_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Internet UDP socket
recv_sock.settimeout(5)
recv_sock.bind((UDP_IP, UDP_LISTEN_PORT))

send_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Internet UDP socket
for _ in xrange(NUMBER_TIMES):
    print '-> send {} to {}:{}'.format(MESSAGE, UDP_IP, UDP_SEND_PORT)
    send_sock.sendto(MESSAGE, (UDP_IP, UDP_SEND_PORT))
    sleep(1)
    try:
        data, addr = recv_sock.recvfrom(1024)  # buffer size is 1024 bytes
        print "<- received: {} from: {}".format(data, addr)
    except socket.timeout as timeout:
        print "++ no data received, timeout."
