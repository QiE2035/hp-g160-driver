from PyQt5.QtWidgets import QWidget as __QWidget

from window import Ui_MainWindow


class MainWindow(__QWidget):

    from driver import Driver

    def __init__(self, driver: Driver):
        from window import Ui_MainWindow

        super().__init__()
        self.__ui = Ui_MainWindow()
        self.__driver = driver
        self.__ui.setupUi(self)
        self.__bind()

    def __bind(self):
        self.__ui.apply_buton.clicked.connect(
            self.__on_apply_button)

    def __on_apply_button(self):
        ui = self.__ui
        driver = self.__driver

        self.__set_keys(ui, driver)
        self.__set_dpi(ui, driver)
        self.__set_other(ui, driver)

    def __set_keys(self, ui: Ui_MainWindow,
                   driver: Driver):
        from driver import Key

        driver.set_key(Key.LEFT,
                       ui.left_spin.value())
        driver.set_key(Key.RIGHT,
                       ui.right_spin.value())
        driver.set_key(Key.MIDDLE,
                       ui.middle_spin.value())
        driver.set_key(Key.SIDE_UP,
                       ui.side_up_spin.value())
        driver.set_key(Key.SIDE_DOWN,
                       ui.side_down_spin.value())
        driver.set_key(Key.MID_UP,
                       ui.mid_up_spin.value())
        driver.set_key(Key.MID_DOWN,
                       ui.mid_down_spin.value())

    def __set_dpi(self, ui: Ui_MainWindow,
                  driver: Driver):
        def current_dpi():
            if(ui.dpi_1_radio.isChecked()):
                return 1
            elif(ui.dpi_2_radio.isChecked()):
                return 2
            elif(ui.dpi_3_radio.isChecked()):
                return 3
            elif(ui.dpi_4_radio.isChecked()):
                return 4

        current = current_dpi()
        driver.set_dpi(current, 1,
                       ui.dpi_1_spin.value())
        driver.set_dpi(current, 2,
                       ui.dpi_2_spin.value())
        driver.set_dpi(current, 3,
                       ui.dpi_3_spin.value())
        driver.set_dpi(current, 4,
                       ui.dpi_4_spin.value())

    def __set_other(self, ui: Ui_MainWindow,
                    driver: Driver):
        from driver import Breath

        driver.set_breath(
            Breath.from_index(
                ui.breath_combo.currentIndex()))
        driver.set_click_speed(
            ui.clisk_speed_spin.value())
        driver.set_scroll(
            ui.scroll_check.isChecked())
