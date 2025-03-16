import socket  # Import the socket module for network communication

def start_client():
    # Create a socket object using IPv4 (AF_INET) and TCP (SOCK_STREAM)
    # AF_INET = Address Family Internet (IPv4)
    # SOCK_STREAM = TCP protocol for reliable, connection-oriented communication
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Get the local machine's hostname automatically
    # This will be used as the server's address since we're connecting locally
    host = socket.gethostname()
    # Define the port number to connect to (must match server's port)
    port = 9999
    
    # Establish connection to the server using host and port
    # This initiates the TCP handshake with the server
    client_socket.connect((host, port))
    print(f"Connected to server at {host}:{port}")  # Confirm successful connection
    
    # Start an infinite loop for continuous communication
    while True:
        # Get user input for the message to send to server
        message = input("Your message: ")
        # Send the message to server after encoding it to bytes
        # encode() converts string to bytes using default UTF-8 encoding
        client_socket.send(message.encode())
        
        # Check if user wants to terminate the connection
        # Convert message to lowercase for case-insensitive comparison
        if message.lower() == "quit":
            print("Closing connection...")  # Inform user of connection closure
            break  # Exit the communication loop
            
        # Receive response from server (up to 1024 bytes)
        # decode() converts received bytes back to string
        response = client_socket.recv(1024).decode()
        print(f"Server: {response}")  # Display server's response
    
    # Close the socket connection
    # This terminates the connection cleanly after loop ends
    client_socket.close()
    print("Client closed")  # Confirm client has shut down

# Check if this script is being run directly (not imported)
# This is a common Python idiom for executable scripts
if __name__ == "__main__":
    start_client()  # Start the client program