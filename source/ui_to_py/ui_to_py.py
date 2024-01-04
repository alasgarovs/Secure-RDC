import os
from PyQt5 import uic


def generate_python_files(ui_folder, py_folder, file_names):
    for file_name in file_names:
        py_path = os.path.join(py_folder, file_name + r'.py')
        ui_path = os.path.join(ui_folder, file_name + '.ui')

        with open(py_path, 'w', encoding="utf-8") as gui:
            uic.compileUi(ui_path, gui)


if __name__ == "__main__":
    base_folder = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    ui_folder = os.path.join(base_folder, 'ui_files')
    py_folder = os.path.join(base_folder, 'source')

    baza = ['connect', 'username']

    generate_python_files(ui_folder, py_folder, baza)

