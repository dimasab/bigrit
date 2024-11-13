from flask import Flask, request, Response
import os
import json
import threading
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
refresh_lock = threading.Lock()

from ai_text import text
from ai_image import image
from ai_kalimat import kalimat
from ai_paragraf import paragraf
from ai_sections import sections
from modul_split_letter import split_letter
from modul_split_words import split_words

def process_ids(identifiers):
    result_data = {}
    
    def threaded_call(identifier):
        local_result = []

        if identifier == "text":
            local_result = text()
        
        if identifier == "image":
            local_result = [image_data for image_data in image()]
        
            for item in local_result:
                item['letters'] = split_letter(item['deskripsi'])
            
        if identifier == "kalimat":
            local_result = kalimat()
            
            for i, item in enumerate(local_result):
                if 'text_data' in item:
                    item['words'] = split_words(item['data_teks'])
                    
        if identifier == "paragraf":
            local_result = paragraf()
            nested_result = []
            
            for paragraph in local_result:
                if isinstance(paragraph, dict) and 'content' in paragraph:
                    nested_result.append(sections(paragraph['content']))
            local_result = nested_result
        
        if local_result:
            result_data[identifier] = local_result

    threads = []
    for identif in identifiers:
        thread = threading.Thread(target=threaded_call, args=(identif,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return result_data

@app.route('/main', methods=['GET'])
def main():
    with refresh_lock:
        username = request.headers.get('Username')
        password = request.headers.get('Password')

        if not username or username != os.environ.get('username'):
            return Response(status=401)
        if not password or password != os.environ.get('password'):
            return Response(status=401)
        
        identifiers = request.args.getlist('identif')
        
        if not identifiers:
            return Response("No identifiers provided", status=400)

        try:
            result_data = process_ids(identifiers)
            if not result_data:
                return Response("No data found", status=404)

            json_result = json.dumps(result_data, indent=4)
            return Response(json_result, content_type='application/json')

        except Exception as e:
            app.logger.error(f"An error occurred: {e}")
            return Response(status=500)

if __name__ == '__main__':
    app.run(debug=True)
