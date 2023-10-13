from src.crm_core.app_gen import app
from src.crm_core.views import *
if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000", debug=True)