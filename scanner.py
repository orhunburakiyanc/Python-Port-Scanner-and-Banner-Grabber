import socket
import threading
import sys
from datetime import datetime

# A lock is used to prevent multiple threads from printing at the same time,
# which would scramble the output in the terminal.
print_lock = threading.Lock()

def grab_banner(s):
    """
    Attempts to read the 'welcome message' (banner) sent by the service
    running on the open port.
    """
    try:
        # Wait a short duration for the service to send data (2 seconds)
        # Some services don't send data immediately, so a timeout is crucial.
        s.settimeout(2)
        
        # Receive up to 1024 bytes and decode bytes to string
        banner = s.recv(1024).decode().strip()
        return banner if banner else "Banner not available (Service active but silent)"
    except:
        return "No banner detected"

def scan_port(target, port):
    """
    Attempts to establish a TCP connection to the specified target and port.
    If the connection is successful (open port), it calls grab_banner.
    """
    try:
        # Create a socket object using IPv4 (AF_INET) and TCP (SOCK_STREAM)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Set a short timeout for the connection attempt to speed up scanning
        # 0.5 seconds is usually sufficient for local/fast networks.
        s.settimeout(0.5)
        
        # connect_ex returns 0 if the connection is successful
        result = s.connect_ex((target, port))
        
        if result == 0:
            # Connection successful! Now let's try to grab the banner.
            banner = grab_banner(s)
            
            # Use the lock to print cleanly
            with print_lock:
                print(f"[+] Port {port} is OPEN : {banner}")
            
            # Close the socket after we are done
            s.close()
            
    except socket.error:
        # If there is a socket error, just pass (port is likely closed or filtered)
        pass
    except Exception as e:
        pass

def main():
    # Check for correct command line arguments
    if len(sys.argv) != 4:
        print("Usage: python3 scanner.py <target_ip> <start_port> <end_port>")
        print("Example: python3 scanner.py 192.168.1.1 1 100")
        sys.exit()

    target = sys.argv[1]
    start_port = int(sys.argv[2])
    end_port = int(sys.argv[3])

    # Resolve the hostname to an IPv4 address
    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print("\n[!] Hostname could not be resolved.")
        sys.exit()
    #target_ip = target

    print("-" * 60)
    print(f"Scanning Target: {target_ip}")
    print(f"Time started: {datetime.now()}")
    print("-" * 60)

    t1 = datetime.now()
    
    threads = []

    try:
        # Loop through the port range and start a thread for each port
        for port in range(start_port, end_port + 1):
            t = threading.Thread(target=scan_port, args=(target_ip, port))
            threads.append(t)
            t.start()
            
        # Wait for all threads to complete before finishing the script
        for t in threads:
            t.join()

    except KeyboardInterrupt:
        print("\n[!] Scan interrupted by user. Exiting...")
        sys.exit()
    except socket.error:
        print("\n[!] Could not connect to server.")
        sys.exit()

    t2 = datetime.now()
    print("-" * 60)
    print(f"Scanning completed in: {t2 - t1}")
    print("-" * 60)

if __name__ == "__main__":
    main()