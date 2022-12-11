from http.server import BaseHTTPRequestHandler
from duckduckgo_images_api import search
import json
import urllib.parse

class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    # Query variables
    query_params = {}
    path = self.path
    if '?' in path:
      _, query_string = path.split('?', 1)
      query_params = urllib.parse.parse_qs(query_string)
    # Search duckduckgo for images
    print("query_params:", query_params, query_params["q"][0])
    image_search_results = search(query_params["q"][0])
    self.send_response(200)
    self.send_header('Content-type','text/json')
    self.end_headers()
    self.wfile.write(json.dumps(image_search_results).encode(encoding='utf_8'))
    return
