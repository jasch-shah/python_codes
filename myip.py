import socket

try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
    
def public_ip():
	read_res = urlopen('http://ipecho.net/plain').read()
	return read_res.decode('utf-8')



def local_ip():
	return socket.gethostbyname(socket.gethostname())

	if __name__ == '__main__':
		print("Getting public and local IP.....")
		print("Public Ip: {}\nLocal IP: {}".format(public_ip(), local_ip()))

