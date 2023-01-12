import socket
import time

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_addr = ('localhost', 12000)
    sock.settimeout(1)

    try:
        for i in range(1, 11):
            start = time.time()
            message = 'Ping #' + str(i) + " " + time.ctime(start)
            try:
                sent = sock.sendto(message, server_addr)
                print("sent " + message)
                date, server = sock.recvfrom(4096)
                print("recieved " + data)
                end =time.time();
                elapsed = end - start 
                print("RTT: " + str(elapsed) + " seconds\n")
            except socket.timeout:
                print("#" + str(i) + " requested time out\n")

    finally:
        print("closing socket")
        sock.close()
    pass

if __name__ == '__main__':
    main()
