# from aimavericks import app
# from aimavericks.config.projectpath import FLASK_PORT, FLASK_DEBUG, HOST


# if __name__ == '__main__':
#     app.run(debug=FLASK_DEBUG)

from app import app
from aimavericks.config.projectpath import FLASK_PORT, FLASK_DEBUG, HOST




if __name__ == '__main__':
    app.run(host=HOST, port= FLASK_PORT, debug=FLASK_DEBUG)


