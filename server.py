import http.server
import socketserver
import webbrowser
import threading
import time
import os

PORT = 8000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

def open_browser():
    # Wait a moment for the server to start
    time.sleep(1)
    print(f"Opening browser at http://localhost:{PORT}")
    webbrowser.open(f"http://localhost:{PORT}")

if __name__ == "__main__":
    # Ensure we are serving from the correct directory
    os.chdir(DIRECTORY)

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Serving at http://localhost:{PORT}")
        print("Press Ctrl+C to stop the server.")

        # Open the browser in a separate thread
        threading.Thread(target=open_browser, daemon=True).start()

        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")
            httpd.server_close()
