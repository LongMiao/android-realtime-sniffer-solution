import sys
import socket
from time import sleep
import win32pipe, win32file

HOST = '127.0.0.1'
PORT = 6666

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.settimeout(2)

pipe = win32pipe.CreateNamedPipe(
	r'\\.\pipe\wireshark',
    win32pipe.PIPE_ACCESS_OUTBOUND,
    win32pipe.PIPE_TYPE_MESSAGE | win32pipe.PIPE_WAIT,
    1, 65536, 65536,
    300,
    None)
print 'wait connect pip'
win32pipe.ConnectNamedPipe(pipe, None)

while True:
    try:
        msg = s.recv(4096)
    except socket.timeout, e:
        err = e.args[0]
        # this next if/else is a bit redundant, but illustrates how the
        # timeout exception is setup
        if err == 'timed out':
            sleep(1)
            print 'recv timed out, retry later'
            continue
        else:
            print e
            sys.exit(1)
    except socket.error, e:
        # Something else happened, handle error, exit, etc.
        print e
        sys.exit(1)
    else:
        if len(msg) == 0:
            print 'orderly shutdown on server end'
            sys.exit(0)
        else:
            win32file.WriteFile(pipe, msg)



