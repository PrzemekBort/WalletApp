import sys
from src.MainApp import MainApp

if __name__ == "__main__":
    app = MainApp(sys.argv)
    sys.exit(app.exec())
