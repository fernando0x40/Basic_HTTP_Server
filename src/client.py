import http.client
import sys

ip_address = sys.argv[1]
port = sys.argv[2]
object_address = sys.argv[3]

connection = http.client.HTTPConnection(ip_address, port, timeout=10)
print(connection)

print("Requesting http://" + ip_address + ":" + port + object_address)

connection.request("GET", object_address)
response = connection.getresponse()
print("Status: {} and reason: {}".format(response.status, response.reason))