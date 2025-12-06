import backend.flask_server as server
import requests
import sys
import threading
import time
import webview

def wait_for_server(url, timeout=5):
    start = time.time()
    while True:
        try:
            response = requests.get(url)
            if response.status_code < 400:
                return True
        except:
            if time.time() - start > timeout:
                return False
            time.sleep(0.1)

if __name__ == "__main__":

    server_thread = threading.Thread(target=server.start, daemon=True)
    server_thread.start()

    is_server_active = wait_for_server("http://127.0.0.1:59776/_health")
    if not is_server_active:
        sys.exit(1)

    webview.create_window('Hello world', 'http://127.0.0.1:59776')
    webview.start()

    requests.get("http://127.0.0.1:59776/_kill")