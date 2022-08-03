if __name__ == "__main__":
    import os
    import sys

    from PyQt5.QtWidgets import QApplication, QMessageBox

    from driver import Driver
    from gui import MainWindow

    app = QApplication(sys.argv)

    if os.geteuid() != 0:
        QMessageBox.critical(None, "错误", "需要root权限")
        exit(1)

    ui = MainWindow(Driver())
    ui.show()

    exit(app.exec_())
