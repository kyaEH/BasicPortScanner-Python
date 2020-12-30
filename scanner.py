import socket,errno
target = socket.gethostbyname(input("Target: "))  

vitesse = input("Set Timeout (Default: 0.5): ")
if vitesse=='':
    vitesse=0.5
    print("Timeout set to 0.5 (default) ")
vitesse=float(vitesse)

porta = input("Set last port (default 1): ")
if porta=='':
    porta=1
    print("First port set to 1 (default)")
porta=int(porta)

portb = input("Set last port (Default: 1000): ")
if portb=='':
    portb=1000
    print("Last port set to 1000")
portb=int(portb)
print("Scan initiated")
try: 
    for port in range(porta,portb): 
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        socket.setdefaulttimeout(vitesse) 
        
        # returns an error indicator 
        result = s.connect_ex((target,port))

        if result ==0: 
            s.send('WhoAreYou\r\n'.encode())
            banner=s.recv(4098)
            print("\n============\n\nOpen port: "+str(port)+"\nBanner:\n"+str(banner).replace("\\n","\n").replace("\\r","\r")+"\n============\n") 
        else: 
            print("Testing port: "+str(port)) 
    s.close() 
    print("End of the scan. https://github.com/kyaEH/")
          
except socket.error as error:
    if error.errno == errno.ECONNREFUSED:
        print("\n============\n\nOop! Something went wrong.\n")
        print(os.strerror(error.errno))
        print("============\n\n")
    else:
        print("\n============\n\nOop! Something went wrong.\nErreur:")
        raise
