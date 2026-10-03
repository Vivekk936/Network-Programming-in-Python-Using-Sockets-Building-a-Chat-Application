#  Network Programming in Python Using Sockets: Building a Chat Application

A simple **client-server chat application built with Python sockets and Tkinter**. This project demonstrates the fundamentals of network programming, TCP socket communication, and GUI-based messaging in Python.

---

##  Project Overview

This project implements a basic chat application using the **TCP/IP socket programming model**.

The application consists of:

* **Server** – waits for a client connection and communicates with it.
* **Client** – connects to the server and exchanges messages.
* **Layout** – provides the graphical user interface using Tkinter.
* **Main** – connects and runs the client/server components.

The project is designed to demonstrate how two Python programs can communicate with each other over a network using sockets.

---

##  Project Structure

```text
PythonChatApplication/
│
├── client.py
├── server.py
├── layout.py
├── main.py
├── .venv/
└── README.md
```

###  File Description

| File        | Description                                                      |
| ----------- | ---------------------------------------------------------------- |
| `client.py` | Creates the TCP client and handles communication with the server |
| `server.py` | Creates the TCP server and accepts client connections            |
| `layout.py` | Creates the Tkinter graphical user interface                     |
| `main.py`   | Main entry point that starts the server or client                |
| `README.md` | Project documentation                                            |

---

## 🔌 Technologies Used

* **Python**
* **Socket Programming**
* **TCP/IP**
* **Tkinter**
* **Object-Oriented Programming**
* **VS Code**

---

##  Concepts Demonstrated

This project demonstrates the following networking concepts:

### 1. Socket

A socket provides an endpoint for communication between two programs.

```python
socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```

### 2. TCP Communication

The application uses:

```text
AF_INET
```

for IPv4 communication and:

```text
SOCK_STREAM
```

for TCP communication.

### 3. Server

The server:

```text
Create Socket
     ↓
Bind IP + Port
     ↓
Listen
     ↓
Accept Client
     ↓
Send / Receive Data
```

### 4. Client

The client:

```text
Create Socket
     ↓
Connect to Server
     ↓
Send / Receive Data
```

### 5. GUI

Tkinter provides the chat interface with:

* Message display
* Text input
* Send button
* Receive button

---

##  How the Application Works

The basic communication model is:

```text
              TCP CONNECTION
       ┌─────────────────────────┐
       │                         │
       ▼                         ▼
┌─────────────┐             ┌─────────────┐
│   SERVER    │◄───────────►│   CLIENT    │
│             │             │             │
│ server.py   │             │ client.py   │
└──────┬──────┘             └──────┬──────┘
       │                           │
       └───────────┬───────────────┘
                   ▼
              layout.py
                   │
                   ▼
              Tkinter GUI
```

---
##  Installation

### 1. Clone the repository

```bash
git clone <YOUR-REPOSITORY-URL>
```

### 2. Open the project

```bash
cd PythonChatApplication
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

#### Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

#### Windows CMD

```cmd
.venv\Scripts\activate
```

---

##  Running the Application

The application uses a **server and client**.

### Step 1: Start the Server

Open the first VS Code terminal:

```bash
python main.py
```

Select:

```text
1
```

The server starts and waits for a client connection.

```text
Enter 1 for Server or 2 for Client: 1
Waiting for client...
```

---

### Step 2: Start the Client

Open a **second terminal** in VS Code:

```bash
python main.py
```

Select:

```text
2
```

The client connects to the server.

```text
Enter 1 for Server or 2 for Client: 2
```

---

##  Chat Interface

The application provides a simple Tkinter interface:

```text
┌──────────────────────────────────┐
│          Chat Application        │
│                                  │
│  You: Hello                      │
│  Receiver: Hi                    │
│                                  │
│                                  │
├──────────────────────────────────┤
│ Enter message...        [Send]   │
│                         [Receive]│
└──────────────────────────────────┘
```

---

##  Socket Communication

### Server

The server creates a socket and binds it to a port:

```python
server_socket.bind((HOST, PORT))
```

It then listens for incoming connections:

```python
server_socket.listen(1)
```

and accepts a client:

```python
client, address = server_socket.accept()
```

### Client

The client connects to the server:

```python
client_socket.connect((HOST, PORT))
```

---

 Sending Messages

Messages are converted into bytes before being sent through the socket:

socket.send(message.encode("utf-8"))

The receiver converts the bytes back into a string:

message.decode("utf-8")

The communication process is:

String
  ↓
encode()
  ↓
Bytes
  ↓
Socket
  ↓
Network
  ↓
Socket
  ↓
decode()
  ↓
String
 Project Features
 TCP socket communication
 Client-server architecture
 Python networking
 Tkinter GUI
 Send messages
 Receive messages
 Object-oriented structure
 Separate client and server modules
 Virtual environment support
 Learning Objectives

After completing this project, you can understand:

What computer sockets are
How TCP communication works
How a server accepts connections
How a client connects to a server
How data is sent through sockets
How data is encoded and decoded
How to create a GUI using Tkinter
How multiple Python modules work together
How to build a basic network application
 Future Improvements

The project can be extended with:

 Multiple clients
 Real-time messaging
 User authentication
 Encrypted communication
 Online/offline status
 File sharing
 Image sharing
 Message history
 Usernames
 Communication between different computers
 Improved chat interface
 Limitations

This is a basic educational project designed to demonstrate socket programming.

The current implementation is not intended to be a production-ready messaging application.

For a production chat application, additional features such as authentication, encryption, multiple-client handling, error handling, and secure communication would be required.

 What I Learned

Through this project, I learned how to:

Python
  │
  ├── Socket Programming
  │       │
  │       ├── Server
  │       └── Client
  │
  ├── TCP/IP Communication
  │
  ├── Data Encoding / Decoding
  │
  ├── Tkinter GUI
  │
  └── Modular Python Programming
 Author

Vivek

This project was created as part of learning Python Network Programming and Socket Programming.

 Support

If you find this project useful for learning Python networking, consider giving the repository a ⭐ on GitHub.

📄 License

This project is intended for educational and learning purposes.

