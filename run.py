#! /usr/bin/python3
from app import app
import views


if __name__ == "__main__":
    # app.run()
    app.run(host='0.0.0.0', port=5555)
