from PyQt5 import QtWidgets

from point_spectra_gui.ui.WriteToCSV import Ui_Form
from point_spectra_gui.util.BasicFunctionality import Basics


class Ui_Form(Ui_Form, Basics):
    def setupUi(self, Form):
        super().setupUi(Form)
        self.connectWidgets()

    def get_widget(self):
        return self.groupBox

    def connectWidgets(self):
        self.setComboBox(self.chooseDataSetComboBox, self.datakeys)

    def function(self):
        params = self.getGuiParams()
        datakey = params['chooseDataSetComboBox']
        filename = params['specifyAFilenameLineEdit']
        selected_cols = self.variablesToWriteListWidget.selectedItems()
        cols = []
        for selection in selected_cols:
            cols.append(selection.text())

        try:
            datatemp = self.data[datakey].df[cols]
        except:
            datatemp = self.data[datakey][cols]

        try:
            datatemp.to_csv(self.outpath + '/' + filename)
        except:
            datatemp.to_csv(filename)

    def isEnabled(self):
        return self.get_widget().isEnabled()

    def setDisabled(self, bool):
        self.get_widget().setDisabled(bool)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
