import socket
import sys
import logging

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    try: 
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        print ("Socket successfully created")
    except socket.error as err: 
        print ("socket creation failed with error %s" %(err))
    
    try: 
        hostname = socket.gethostname()
        host_ip = socket.gethostbyname(hostname) 
        host_ip1  = socket.gethostbyname('www.google.com') 
    except socket.gaierror: 
    
        # this means could not resolve the host 
        return "there was an error resolving the host"
    
    # connecting to the server 
    s.connect((host_ip1, port)) 
    
    return '''the socket has successfully connected to google <br/>Hostname : {} <br/>IP :{}'''.format(hostname,host_ip)

@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

