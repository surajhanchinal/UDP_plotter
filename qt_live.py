from PyQt4 import QtGui,QtCore
import sys
import ui_main
import numpy as np
import pylab
import time
import pyqtgraph
import udp_class
udp = udp_class.UDP_data()
class ExampleApp(QtGui.QMainWindow, ui_main.Ui_MainWindow):
    X = np.array([])
    Y_x = np.array([])
    count = 0
    def __init__(self, parent=None):
        pyqtgraph.setConfigOption('background', 'w') #before loading widget
        super(ExampleApp, self).__init__(parent)
        self.setupUi(self)
        self.btnAdd.clicked.connect(self.update)
        self.grPlot.plotItem.showGrid(True, True, 0.7)
        self.grPlot.setYRange(-20,20)
        udp.start("127.0.0.1",5005,'receive')


    def update(self):
        if(len(ExampleApp.X) > 500):
            ExampleApp.X = ExampleApp.X[len(ExampleApp.X)-499:]
            ExampleApp.Y_x = ExampleApp.Y_x[len(ExampleApp.Y_x)-499:]
        ExampleApp.count = ExampleApp.count + 1
        t1=time.clock()
        data = udp.update()
        print(data)
        ExampleApp.X = np.append(ExampleApp.X,ExampleApp.count)
        ExampleApp.Y_x = np.append(ExampleApp.Y_x,float(data))
        C=pyqtgraph.hsvColor(0,alpha=1)
        pen=pyqtgraph.mkPen(color=C,width=2)
        self.grPlot.plot(ExampleApp.X,ExampleApp.Y_x,pen=pen,clear=True)
        print("update took %.02f ms"%((time.clock()-t1)*1000))
        if self.chkMore.isChecked():
            QtCore.QTimer.singleShot(1, self.update) # QUICKLY repeat

if __name__=="__main__":
    app = QtGui.QApplication(sys.argv)
    form = ExampleApp()
    form.show()
    form.update() #start with something
    app.exec_()
    print("DONE")
