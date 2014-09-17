import logging
from flask import Flask, render_template, abort

from db import ImageStorage, HnStorage, SnStorage

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s - [%(asctime)s] %(message)s')
logger = logging.getLogger(__name__)

app = Flask(__name__)

imstore = ImageStorage()
hnstore = HnStorage()
snstore = SnStorage()

@app.route("/hackernews")
@app.route('/')
def hackernews():
    return render_template('index.html', title='Hacker News',
            news_list=hnstore.get_all())

@app.route("/startupnews")
def startupnews():
    return render_template('index.html', title='Startup News',
            news_list=snstore.get_all())

@app.route('/img/<img_id>')
def image(img_id):
    img = imstore.get(id=img_id)
    if not img:
       abort(404)
    return str(img['raw_data']), 200, {'Content-Type': img['content_type']}

if __name__ == "__main__":
    import os
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))

