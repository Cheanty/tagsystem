import sys
import os
import logging
os.environ['FLASK_APP'] = 'app.py'
logging.basicConfig(stream=sys.stderr)
sys.path.append("/home/work/flask/lib/python3.10/site-packages")
sys.path.insert(0, "/home/work/tagsystem")
from app import app as application