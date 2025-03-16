import socket  # Import socket module for network communication

def start_server():
    # Create a socket object using IPv4 and TCP
    # AF_INET = Address Family Internet (IPv4)
    # SOCK_STREAM = TCP protocol for reliable communication
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Get local machine hostname for binding
    # This will be the server's address
    host = socket.gethostname()
    # Define port number server will listen on
    port = 9999
    
    # Bind socket to host and port
    # This associates the socket with a specific network interface and port
    server_socket.bind((host, port))
    
    # Start listening for incoming connections
    # 5 is the maximum backlog of pending connections
    server_socket.listen(5)
    
    print(f"Server started on {host}:{port}")  # Confirm server startup
    print("Waiting for client connection...")  # Indicate server is ready
    
    # Accept incoming client connection
    # Returns a new socket (client_socket) and client address (addr)
    client_socket, addr = server_socket.accept()
    print(f"Connected to client at {addr}")  # Confirm client connection
    
    # Start infinite loop for communication
    while True:
        # Receive data from client (up to 1024 bytes)
        # decode() converts bytes to string
        data = client_socket.recv(1024).decode()
        # If no data received, client has closed connection
        if not data:
            break
            
        print(f"Client: {data}")  # Display client's message
        
        # Get server's response from user input
        response = input("Server response: ")
        
        # Send response back to client after encoding to bytes
        # encode() converts string to bytes using UTF-8
        client_socket.send(response.encode())
        
        # Check if client sent quit message
        # Server will exit after sending response
        if data.lower() == "quit":
            print("Client has ended the session")  # Notify of session end
            break
    
    # Clean up by closing both sockets
    # First close client socket, then server socket
    client_socket.close()
    server_socket.close()
    print("Server closed")  # Confirm server shutdown

# Standard Python idiom to run code only if script is main module
if __name__ == "__main__":
    start_server()  # Start the server program