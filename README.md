# Server and Client Echo Application

This project sets up a simple multi-connection server and client echo application using sockets. 

Received responses are saved in a log file inside the `logs/` folder.

Default hostname is `127.0.0.1` using port `65500`.

## Running the code

1. Run the server application
```
python main_server.py [--hostname address] [--port port_number]
```


2. Run the client
```
python main_client.py [--hostname address] [--port port_number]
```

## References
[Socket Programming in Python (Guide)](https://realpython.com/python-sockets/)
