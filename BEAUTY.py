#!/usr/bin/mason test
import sys
import time
import socket
import struct
import threading
from random import randint
from optparse import OptionParser
from pinject import IP, UDP

USAGE = '''
%prog target.com [options]        # DDoS
%prog benchmark [options]         # Calculate AMPLIFICATION factor
'''

LOGO = r'''
	   _____           __    __              
	  / ___/____ _____/ /___/ /___ _____ ___ 
	  \__ \/ __ `/ __  / __  / __ `/ __ `__ \
	 ___/ / /_/ / /_/ / /_/ / /_/ / / / / / /
	/____/\__,_/\__,_/\__,_/\__,_/_/ /_/ /_/ 
	https://github.com/OffensivePython/Saddam
	   https://twitter.com/OffensivePython
'''
