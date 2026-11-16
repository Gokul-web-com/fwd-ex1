from http.server import HTTPServer, BaseHTTPRequestHandler
content = """

<!DOCTYPE html>
<html>
<head>
    <title>TCP/IP Protocol List</title>
</head>

<body>

    <center>
        <h1>LIST OF TCP/IP PROTOCOLS</h1>
        <hr width="70%">

        <h2>Network Communication Protocols</h2>

        <table border="1" cellpadding="12" cellspacing="0">
            <tr>
                <th>S.No</th>
                <th>Protocol</th>
                <th>Full Form</th>
                <th>Purpose</th>
            </tr>

            <tr>
                <td>1</td>
                <td>TCP</td>
                <td>Transmission Control Protocol</td>
                <td>Reliable data transfer</td>
            </tr>

            <tr>
                <td>2</td>
                <td>IP</td>
                <td>Internet Protocol</td>
                <td>Addressing and routing</td>
            </tr>

            <tr>
                <td>3</td>
                <td>HTTP</td>
                <td>Hypertext Transfer Protocol</td>
                <td>Web communication</td>
            </tr>

            <tr>
                <td>4</td>
                <td>FTP</td>
                <td>File Transfer Protocol</td>
                <td>File transfer</td>
            </tr>

            <tr>
                <td>5</td>
                <td>DNS</td>
                <td>Domain Name System</td>
                <td>Domain name resolution</td>
            </tr>

            <tr>
                <td>6</td>
                <td>UDP</td>
                <td>User Datagram Protocol</td>
                <td>Fast data transmission</td>
            </tr>

            <tr>
                <td>7</td>
                <td>SMTP</td>
                <td>Simple Mail Transfer Protocol</td>
                <td>Sending emails</td>
            </tr>

            <tr>
                <td>8</td>
                <td>SSH</td>
                <td>Secure Shell</td>
                <td>Secure remote access</td>
            </tr>
        </table>

        <br>
        <hr width="70%">
        <p>End of TCP/IP Protocol List</p>

    </center>

</body>
</html>


"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',880)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()