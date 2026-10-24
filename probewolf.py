import socket 
import argparse
#flags and their settings
parser = argparse.ArgumentParser(prog="ProbeWolf", description="ProbeWolf is port scanner with few flags", epilog="Filip Novák 2026")
parser.add_argument("target", nargs="?", help="Targets IP adress")
parser.add_argument("-p", "--port", type=int, help="Scanner will scan only one port")
parser.add_argument("-s", "--start", type=int,default=1, help="Targets first port to scan [default is 1]")
parser.add_argument("-e", "--end", type=int, default=1024, help="Targets last port to scan [default is 1024]")
parser.add_argument("-t", "--timeout", type=float, default=0.5, help="Time for response in seconds [default is 0.5s]")
parser.add_argument("-6", "--ipv6", action="store_true", help="Switch scanner to IPv6")

args = parser.parse_args()
#if statement which checks if is something in target(first place after probewolf.py "target"), if not than it ask for the minimum informations
if args.target is None:
 ip = input("IPv4 or IPv4? [IPv4/IPv6] ")
 if ip == "IPv4" or ip == "ipv4": 
  args.ipv6 == False
 else:
  args.ipv6 == True
 args.target = input("Targets adress: ")
 port = input("Specific port? [y/N]")
 if port == "y" or port == "Y":
  args.port = int(input("Port: "))
 else:
  args.port = None
 
 
 

#checks if ipv6 flag is being used
if args.ipv6 is True:
 protocol = socket.AF_INET6
else:
 protocol = socket.AF_INET

#checks if specific port is specified
if args.port is None:
 for i in range(args.start, args.end+1):
  s = socket.socket(protocol, socket.SOCK_STREAM)
  s.settimeout(args.timeout)
  if s.connect_ex((args.target, i)) == 0:
    try:
      service = socket.getservbyport(i)
    except OSError:
     service = "unknown"
    print(f"Port: {i}/tcp {service} OPENED")
  s.close()
else:
 s = socket.socket(protocol, socket.SOCK_STREAM)
 s.settimeout(args.timeout)
 response = s.connect_ex((args.target, args.port))
 if response == 0:
   try:
    service = socket.getservbyport(args.port)
   except OSError:
    service = "unknown"
   print(f"Port: {args.port}/tcp {service} OPENED")
 else:
  print(f"Port: {args.port}/tcp CLOSED")

s.close()