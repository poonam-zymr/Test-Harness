# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_new.ui'
#
# Created: Tue Oct 01 17:48:24 2013
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import atexit
import subprocess
import os
import time
import shutil
import sys

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(452, 501)
        self.gridLayout_5 = QtGui.QGridLayout(Dialog)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.groupBox_3 = QtGui.QGroupBox(Dialog)
        self.groupBox_3.setTitle(_fromUtf8(""))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_3 = QtGui.QLabel(self.groupBox_3)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)
        self.TestCase_treeView = QtGui.QTreeView(self.groupBox_3)
        self.TestCase_treeView.setObjectName(_fromUtf8("TestCase_treeView"))
        self.gridLayout_3.addWidget(self.TestCase_treeView, 1, 0, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_3, 2, 0, 1, 2)
        self.Results_groupBox_4 = QtGui.QGroupBox(Dialog)
        self.Results_groupBox_4.setObjectName(_fromUtf8("Results_groupBox_4"))
        self.gridLayout_4 = QtGui.QGridLayout(self.Results_groupBox_4)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.Result_textEdit = QtGui.QTextEdit(self.Results_groupBox_4)
        self.Result_textEdit.setObjectName(_fromUtf8("Result_textEdit"))
        self.gridLayout_4.addWidget(self.Result_textEdit, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.Results_groupBox_4, 3, 0, 1, 2)
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.TestCaseLocation_lineEdit = QtGui.QLineEdit(self.groupBox)
        self.TestCaseLocation_lineEdit.setObjectName(_fromUtf8("TestCaseLocation_lineEdit"))
        self.gridLayout.addWidget(self.TestCaseLocation_lineEdit, 1, 0, 1, 1)
        self.Browse_pushButton = QtGui.QPushButton(self.groupBox)
        self.Browse_pushButton.setObjectName(_fromUtf8("Browse_pushButton"))
        self.gridLayout.addWidget(self.Browse_pushButton, 1, 1, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox, 0, 0, 1, 2)
        self.groupBox_2 = QtGui.QGroupBox(Dialog)
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.ResultLocation_lineEdit = QtGui.QLineEdit(self.groupBox_2)
        self.ResultLocation_lineEdit.setObjectName(_fromUtf8("ResultLocation_lineEdit"))
        self.gridLayout_2.addWidget(self.ResultLocation_lineEdit, 1, 0, 1, 1)
        self.Browse_pushButton_2 = QtGui.QPushButton(self.groupBox_2)
        self.Browse_pushButton_2.setObjectName(_fromUtf8("Browse_pushButton_2"))
        self.gridLayout_2.addWidget(self.Browse_pushButton_2, 1, 1, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_2, 1, 0, 1, 2)
        self.frame = QtGui.QFrame(Dialog)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.OK_pushButton = QtGui.QPushButton(self.frame)
        self.OK_pushButton.setObjectName(_fromUtf8("OK_pushButton"))
        self.horizontalLayout.addWidget(self.OK_pushButton)
        self.Cancel_pushButton = QtGui.QPushButton(self.frame)
        self.Cancel_pushButton.setObjectName(_fromUtf8("Cancel_pushButton"))
        self.horizontalLayout.addWidget(self.Cancel_pushButton)
        self.gridLayout_5.addWidget(self.frame, 4, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label_3.setText(_translate("Dialog", "Choose test cases to run", None))
        self.Results_groupBox_4.setTitle(_translate("Dialog", "Results", None))
        self.label.setText(_translate("Dialog", "Please select test case location", None))
        self.Browse_pushButton.setText(_translate("Dialog", "Browse", None))
        self.label_2.setText(_translate("Dialog", "Please select location to store results", None))
        self.Browse_pushButton_2.setText(_translate("Dialog", "Browse", None))
        self.OK_pushButton.setText(_translate("Dialog", "OK", None))
        self.Cancel_pushButton.setText(_translate("Dialog", "Close", None))

class Convert_UI(QtGui.QWidget):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        global testcaselocatin,resultlocation,model
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.Result_textEdit.setReadOnly(True)
        model = QtGui.QStandardItemModel()
        self.setWindowTitle("Test Framework")
        QtCore.QObject.connect(self.ui.Browse_pushButton, QtCore.SIGNAL("clicked()"), self.browse_testcase_dir)
        QtCore.QObject.connect(self.ui.Browse_pushButton_2, QtCore.SIGNAL("clicked()"), self.browse_result_dir)
        QtCore.QObject.connect(self.ui.OK_pushButton, QtCore.SIGNAL("clicked()"), self.OK_clicked)
        QtCore.QObject.connect(self.ui.Cancel_pushButton, QtCore.SIGNAL("clicked()"), self.quitapp)
        QtCore.QObject.connect(self.ui.TestCase_treeView, QtCore.SIGNAL("clicked(QModelIndex)"), self.current_selection)
        QtCore.QObject.connect(self.ui.TestCaseLocation_lineEdit, QtCore.SIGNAL("returnPressed()"), self.lineEditPressed)

    def lineEditPressed(self):
        #print "Enter key is pressed"
        testcaselocation = str(self.ui.TestCaseLocation_lineEdit.displayText())
        if os.path.exists(testcaselocation):
             self.fetch_testsuites()
        elif os.path.exists(testcaselocation) == False:
            self.ui.Result_textEdit.clear()
            self.ui.Result_textEdit.setTextColor(Qt.red)
            mesg = ("Test case directory does not exist. Please verify.")
            self.ui.Result_textEdit.append(mesg)
            model.clear()
            
    def fetch_testsuites(self):
        self.ui.Result_textEdit.clear()
        self.ui.TestCase_treeView.setHeaderHidden(True)
        self.ui.TestCase_treeView.setModel(model)
        testcaselocation = self.ui.TestCaseLocation_lineEdit.displayText()
        boolval = False
        #print directory
        print testcaselocation
        testcaselocation = str(testcaselocation)
        global suites
        suites = []
        suitenames = []
        if os.path.exists(testcaselocation):
            for dirn,dir,files in os.walk(testcaselocation):
                #print 'yes'
                for file in files:
                    file = file.lower()
                    if 'config.ini' in file:
                        #print 'yes'
                        boolval = True
                if 'suite_' in dirn:
                    suitedir = os.path.basename(dirn)
                    if 'suite_' in suitedir:
                    #print suitedir
                        suitenames.append(suitedir)
                        suites.append(dirn)
        #print boolval
        #print dirn
        print suites
        for num,text in enumerate(suites):
            #print num
            #print text
            suitename = str(os.path.basename(text))
            #print suitename
            item = QtGui.QStandardItem('%s' % suitename)
            item.setCheckState(Qt.Unchecked)
            item.setCheckable(True)
            item.setEditable(False)
            item.setText('%s' % suitename)
            model.appendRow(item)
            #self.ui.TestCase_listView.appendRow(item)
            contents = os.listdir(text)
            for each in contents:
                each = each.lower()
                if 'config.ini' in each:
                    filepath = os.path.join(text,each)
                    fh = open(filepath, 'rb')
                    testcases = []
                    for line in fh:
                        #print line
                        if 'tests=' in line:
                            line = line.replace("\r\n", "")
                            line = line.split("=")
                            #print line
                            tests = line[1].split(",")
                            #print tests
                            for i in tests:
                                testcases.append(i)
                   # print testcases
                    for row,test in enumerate(testcases):
                    #    print test
                        item1 = QtGui.QStandardItem('%s' % test)
                        item1.setCheckState(Qt.Unchecked)
                        item1.setCheckable(True)
                        item1.setEditable(False)
                        item1.setText('%s' % test)
                        item.appendRow(item1)
           # model.appendRow(item)     
            
        if boolval == False:
            self.ui.Result_textEdit.setTextColor(Qt.red)
            self.ui.Result_textEdit.setText('Test cases are not found.\nPlease select appropriate directory.')
            model.clear()
            #model1 = QtGui.QStandardItemModel()
            #self.ui.TestCase_treeView.setModel(model1)
        self.ui.Result_textEdit.setTextColor(Qt.black)
        
    def browse_testcase_dir(self):
        global dialog
        dialog = QtGui.QFileDialog()
        directory = dialog.getExistingDirectory(self, 'Select test case directory', options=QFileDialog.ShowDirsOnly)
        dialog.setDirectory(directory)
        self.ui.TestCaseLocation_lineEdit.setText(directory)
        testcaselocation = str(self.ui.TestCaseLocation_lineEdit.displayText())
        print testcaselocation
        if testcaselocation != "" and testcaselocation != " ":
            #print 'yes'
            self.fetch_testsuites()

    def browse_result_dir(self):
        global dialog
        dialog1 = QtGui.QFileDialog()
        directory = dialog1.getExistingDirectory(self, 'Select directory to store results',options=QFileDialog.ShowDirsOnly)
        dialog1.setDirectory(directory)
        self.ui.ResultLocation_lineEdit.setText(directory)
        resultlocation = self.ui.ResultLocation_lineEdit.displayText()
        #print directory
        #print resultlocation

    def OK_clicked(self):
        print 'OK button is clicked'
        testcaselocation = str(self.ui.TestCaseLocation_lineEdit.displayText())
        resultlocation = str(self.ui.ResultLocation_lineEdit.displayText())
        if os.path.exists(testcaselocation) and os.path.exists(resultlocation):
            parentdir = os.path.split(testcaselocation)
            self.ui.Result_textEdit.clear()
            if "suite_" in parentdir[1]:
                parentdir1 = os.path.split(parentdir[0])
                resultdir = os.path.join(str(resultlocation), parentdir1[1])
            else:
                for dirn,dir,files in os.walk(testcaselocation):
                    #print dirn
                    listdir=os.listdir(dirn)
                    #print listdir
                    for each in listdir:
                        if 'suite_' in each:
                            #print dirn
                            parentdirectory = os.path.split(dirn)
                            resultdir = os.path.join(str(resultlocation), parentdirectory[1])
            #print parentdir
            #print resultdir
            if os.path.exists(resultdir):
                shutil.rmtree(resultdir, ignore_errors='true')
            else:
                os.mkdir(resultdir)
            if self.ui.ResultLocation_lineEdit.displayText() != " " and self.ui.TestCaseLocation_lineEdit.displayText() != " ":
                if len(suites) != 0:
                    for i in range(0,model.rowCount()):
                        modelitem = model.item(i)
                        if modelitem.checkState() == 2:
                            #print modelitem.text()
                            children = []
                            for j in range(0,modelitem.rowCount()):
                                childitem = modelitem.child(j)
                                if childitem.checkState() == 2:
                                    #print childitem.text()
                                    children.append(str(childitem.text()))
                            #print children
                            if len(children) != 0:
                                #print suites[i]
                                sourcedir = suites[i]
                                suitename = os.path.split(sourcedir)
                                self.setWindowTitle("Executing tests....")
                                #print sourcedir
                                config_temp_path = os.path.join(suites[i],"config_temp.ini")
                                config_path = os.path.join(suites[i],"config.ini")
                                fh = open(config_temp_path, "w+")
                                fh1 = open(config_path, "rb")
                                for line in fh1:
                                    if 'tests=' in line:
                                        newline = ("tests=%s" % children)
                                        newline = newline.replace("[","")
                                        newline = newline.replace("]","")
                                        newline = newline.replace(" ","")
                                        newline = newline.replace("'","")
                                        #print newline
                                        fh.write(newline)
                                    else:
                                        fh.write(line)
                                time.sleep(10)
                                try:
                                    destidir = os.path.join(resultdir, suitename[1])
                                    results = os.path.join(sourcedir, "Results")
                                    if os.path.exists(results):
                                        shutil.rmtree(results, ignore_errors='true')
                                    if os.path.exists(config_temp_path):
                                        os.chdir(suites[i])
                                        subprocess.Popen(["nosetests", "-c", "config_temp.ini"])
                                        #print i
                                        fh.close()
                                        fh1.close()
                                        #print sourcedir
                                        #print destidir
                                    #os.remove(config_temp_path)
                                #os.system(command)    
                                        sys.path.append("..")
                                        import main_index
                                        time.sleep(5)
                                        shutil.copytree(sourcedir, destidir, symlinks=False, ignore=shutil.ignore_patterns('*.py', '*.ini', '*.pyc', '*.coverage'))
                                        self.ui.Result_textEdit.setTextColor(Qt.green)
                                        mesg = ("Suite: %s executed successfully" % suitename[1])
                                        self.ui.Result_textEdit.append(mesg)
                                        self.setWindowTitle("Test Framework")        
                                except:
                                    self.ui.Result_textEdit.setTextColor(Qt.red)
                                    mesg = ("Suite: %s not executed successfully" % suitename[1])
                                    self.ui.Result_textEdit.append(mesg)
            #os.chdir(resultdir)
            self.ui.Result_textEdit.setTextColor(Qt.black)
            if os.path.exists(resultdir):
                main_index.write_main_index(str(resultdir))
        elif os.path.exists(testcaselocation) or os.path.exists(resultlocation):
            self.ui.Result_textEdit.clear()
            if os.path.exists(testcaselocation) == False:
                self.ui.Result_textEdit.setTextColor(Qt.red)
                mesg = ("Test case directory does not exist. Please verify.")
                self.ui.Result_textEdit.append(mesg)
            elif os.path.exists(resultlocation) == False:
                self.ui.Result_textEdit.setTextColor(Qt.red)
                mesg = ("Result location does not exist. Please verify.")
                self.ui.Result_textEdit.append(mesg)
        else:
            self.ui.Result_textEdit.clear()
            self.ui.Result_textEdit.setTextColor(Qt.red)
            mesg = ("Test case directory and result location are not valid. Please verify.")
            self.ui.Result_textEdit.append(mesg)
            
            
                        #print os.getcwd()
        #for i in model.selectedItems():
        #    print i
    def closeEvent(self, event):
        reply = QtGui.QMessageBox.question(self, 'Exit',"Do you want to exit?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            self.close()
        elif reply == QtGui.QMessageBox.No:
            event.ignore()
    def quitapp(self):
        self.close()

    def current_selection(self, index):
        #print index
        itemtext = index.model().itemFromIndex(index).text()
        selecteditem = index.model().itemFromIndex(index)
        itemindex = selecteditem.index()
        #print itemindex
        if selecteditem.checkState() == 2:
            if selecteditem.hasChildren() == False:
                parentitem = selecteditem.parent()
                print parentitem
                parentitem.setCheckState(Qt.Checked)
##            if selecteditem.hasChildren() == True:
##                row = selecteditem.rowCount()
##                #print row
##                for i in range(0, selecteditem.rowCount()):
##                    childitem = selecteditem.child(i)
##                    childitem.setCheckState(Qt.Checked)
        elif selecteditem.checkState() == 0:
            if selecteditem.hasChildren() == True:
                row = selecteditem.rowCount()
                #print row
                for i in range(0, selecteditem.rowCount()):
                    childitem = selecteditem.child(i)
                    childitem.setCheckState(Qt.Unchecked)
                    #print index.model().itemFromIndex(childitem).text()
                    #print newItem
    #            print selecteditem.takeChild(row)
            

def main():
    app = QtGui.QApplication(sys.argv)
    ex = Convert_UI()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

