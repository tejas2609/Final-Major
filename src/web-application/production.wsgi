# production.wsgi
import sys
 
sys.path.insert(0,"/var/www/html/final-major/")
 
from app import app as application
