from flask import Flask, request, Response
import os
import json
from dotenv import load_dotenv
import threading
load_dotenv()
app = Flask(__name__)
refresh_lock = threading.Lock()

from ai_text import text
from ai_image import image

@app.route('/main', methods=['GET'])
def main():
    if refresh_lock.locked():
        print("Lock currently held, ruanglaptop concurrent execution attempted")
    with refresh_lock:
        if not request.headers.get(os.environ['username']):
            return Response(status=401)
        elif request.headers[os.environ['vler']] != os.environ['password']:
            return Response(status=401)
        
        if id.args.get('identif'):
            id = request.args.get('identif')
        else:
            id = None
        
        # Call the first app to get array from seller products
        try:
            if id == "text":
                array = text()
            elif id == "image":
                array = image()
        except Exception as e:
            app.logger.error(f"An error occurred while calling ruanglaptop app: {e}")

        for items in array:

        array_gb = {
            'array_text': array_text,
            'array_image': array_image
        }
        
        json_array_gb = json.dumps(array_gb)

        return Response(json_array_gb, content_type='application/json')
