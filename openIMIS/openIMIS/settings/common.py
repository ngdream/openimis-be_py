import os


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODE = os.environ.get("MODE", 'prod').lower()
# Fetch protocols and hosts from environment variables
protos = os.environ.get('PROTOS', default='https').split(',')
hosts = os.environ.get('HOSTS', default='localhost').split(',')
if MODE == "dev":
    DEBUG = True
else:
    DEBUG = os.environ.get("DEBUG", "false").lower() == "true"
