from flask import Flask, request, render_template
import requests

app = Flask(__name__)

# Global variable to store the proxy content
proxy_content = None

@app.route('/')
def index():
    global proxy_content  # Access the global variable
    return render_template('index.html', content=proxy_content)

@app.route('/proxy', methods=['GET'])
def proxy():
    global proxy_content  # Access the global variable
    url = request.args.get('url', '')
    if not url.startswith('http'):
        url = 'http://' + url

    try:
        response = requests.get(url)
        proxy_content = response.content.decode('utf-8')  # Store content in global variable
        return render_template('index.html', content=proxy_content)
    except requests.exceptions.RequestException as e:
        return f"Error fetching URL: {e}"

if __name__ == '__main__':
    app.run(debug=True)
