import functools
import sys
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

from files import ItemLib, ItemManager


class App():
    def __init__(self):
        super().__init__()

         #Settings
        self.windowHeight = 475
        self.windowWidth = 400
        self.font = "Arial"
        self.fontSize = 12

        #Variables
        self.currentTab = "generator"
        self.historyButtonsList = []

        self.CreateMainWindow()
        self.InitializeLayouts()
        self.AssembleLayouts()
        self.ApplyOpeningView()
        self.CreateHistoryButtons()

    def Run(self):
        self.root.show()
        sys.exit(self.app.exec())
        
    def CreateMainWindow(self):
        #Main Window
        self.app = QApplication([])
        self.root = QWidget()
        self.root.setFont(QFont(self.font, self.fontSize))
        self.root.setWindowTitle("Loot Generator")
        self.root.setGeometry(400,400,self.windowWidth,self.windowHeight)
        self.root.setMaximumSize(410,460)

        #TopMostLayout
        self.mainLayout = QGridLayout(self.root)
        self.mainLayout.setRowStretch(1,5)
    
    def InitializeLayouts(self): #Only Called at Start
        #Layout for Tab Buttons
        self.tabLayout = QHBoxLayout()

        #Layout for Generator View
        self.generatorLayout = QHBoxLayout()
        self.generatorFrame = QFrame()
        self.generatorFrame.setLayout(self.generatorLayout)
        self.generateLayout = QGridLayout()
        self.generateLayout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.generateLayout.setContentsMargins(0,10,0,0)

        self.generatorItemInfoDisplay = QGroupBox()
        self.generatorItemInfoDisplay.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.generatorItemInfoDisplay.setMinimumWidth(185)
        self.generatorItemInfoDisplay.setMaximumWidth(185)
        self.generatorItemInfoDisplay.setTitle("Item")
        self.generatorItemInfoDisplay.setFont(QFont(self.font, int(self.fontSize*1.5)))
        self.generatorItemStats = QVBoxLayout()
        self.generatorItemStats.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.historyItemInfoDisplay = QGroupBox()
        self.historyItemInfoDisplay.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.historyItemInfoDisplay.setMinimumWidth(185)
        self.historyItemInfoDisplay.setMaximumWidth(185)
        self.historyItemInfoDisplay.setTitle("Item")
        self.historyItemInfoDisplay.setFont(QFont(self.font, int(self.fontSize*1.5)))
        self.historyItemStats = QVBoxLayout()
        self.historyItemStats.setAlignment(Qt.AlignmentFlag.AlignTop)

        #Layout for History View
        self.historyLayout = QHBoxLayout()
        self.historyFrame = QFrame()
        self.historyFrame.hide()
        self.historyFrame.setLayout(self.historyLayout)
        self.historyButtons = QVBoxLayout()
        self.historyButtons.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.historyItemInfoLayout = QVBoxLayout()

    def AssembleLayouts(self):
        #Tabs
        self.CreateTabButtons()
        self.AddTabButtonsToLayout()
        #Generator Tab
        self.CreateGenerateTextAndButton()
        self.AddGenerateTextAndButtonsToLayout()
        #History Tab
        self.CreateHistoryButtons()
        
    def ApplyOpeningView(self):
        self.mainLayout.addLayout(self.tabLayout,1,1)
        self.mainLayout.addWidget(self.generatorFrame,2,1)
        self.mainLayout.addWidget(self.historyFrame,2,1)

        self.generatorLayout.setContentsMargins(0,0,0,0)
        self.generatorLayout.addLayout(self.generateLayout)
        self.generatorLayout.addWidget(self.generatorItemInfoDisplay)
        self.generatorItemInfoDisplay.setLayout(self.generatorItemStats)

        self.historyLayout.setContentsMargins(0,0,0,0)
        self.historyLayout.addLayout(self.historyButtons)
        self.historyLayout.addWidget(self.historyItemInfoDisplay)
        self.historyItemInfoDisplay.setLayout(self.historyItemStats)

    #TABS
    #Tab Buttons
    def CreateTabButtons(self):
        self.genTabButton = QPushButton(text="Generator")
        self.genTabButton.setStyleSheet("background-color: rgba(176, 255, 161,90)")
        self.genTabButton.setMinimumHeight(40)
        self.genTabButton.clicked.connect(self.GeneratorTabButtonClicked)

        self.histTabButton = QPushButton(text="History")
        self.histTabButton.setStyleSheet("background-color: rgba(105, 105, 105, 30)")
        self.histTabButton.setMinimumHeight(40)
        self.histTabButton.clicked.connect(self.HistoryTabButtonClicked)

    def AddTabButtonsToLayout(self):
        self.tabLayout.addWidget(self.genTabButton)
        self.tabLayout.addWidget(self.histTabButton)
    
    def GeneratorTabButtonClicked(self):
        self.SwitchTab("generator")

    def HistoryTabButtonClicked(self):
        self.SwitchTab("history")
    
    def DebugButtonClicked(self):
        print(self.root.geometry())

    def SwitchTab(self,tab):
        if tab == self.currentTab:
            pass
        else:
            if tab == "generator":
                self.historyFrame.hide()
                self.genTabButton.setStyleSheet("background-color: rgba(176, 255, 161,90)")
                self.histTabButton.setStyleSheet("background-color: rgba(105, 105, 105, 30)")
                self.generatorFrame.show()
            elif tab == "history":
                self.generatorFrame.hide()
                self.histTabButton.setStyleSheet("background-color: rgba(176, 255, 161,90)")
                self.genTabButton.setStyleSheet("background-color: rgba(105, 105, 105, 30)")
                self.CreateHistoryButtons()
                self.historyFrame.show()
            #Set variable to whichever tab was switched to.
            self.currentTab = tab

    #GENERATOR TAB
    def CreateGenerateTextAndButton(self):

        self.l1 = QLabel(text="Min Attributes (1)")
        self.l2 = QLabel(text=f"Max Attributes ({ItemLib.ItemLib.totalstats})")

        self.le1 = QLineEdit()
        self.le1.setText("1")
        self.le1.setFixedWidth(30)

        self.le2 = QLineEdit()
        self.le2.setText(f"{ItemLib.ItemLib.totalstats}")
        self.le2.setFixedWidth(30)

        self.b1 = QPushButton(text="Generate",)
        self.b1.setFixedSize(180,50)
        self.b1.clicked.connect(self.GenerateButtonClicked)

    def AddGenerateTextAndButtonsToLayout(self):
        self.generateLayout.addWidget(self.le1,1,1)
        self.generateLayout.addWidget(self.le2,2,1)
        self.generateLayout.addWidget(self.l1,1,2)
        self.generateLayout.addWidget(self.l2,2,2)
        self.generateLayout.addWidget(self.b1,3,1,1,2)

    def GenerateButtonClicked(self):
        try:
            minstats = int(self.le1.text())
            maxstats = int(self.le2.text())
        except:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Please Enter Numbers Only.")
            msg.exec()
            return
        
        if minstats < 1 or maxstats > ItemLib.ItemLib.totalstats:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Input is out of Range.")
            msg.exec()
            return

        ItemManager.createItem(minstats, maxstats)
        self.UpdateItemInfo(len(ItemManager.itemHistory)-1, self.generatorItemInfoDisplay, self.generatorItemStats)

    #HISTORY TAB
    def CreateHistoryButtons(self):
        self.ClearWidgetsFromLayout(self.historyButtons)
        self.historyButtonsList.clear()
        if len(ItemManager.itemHistory) > 0:
            self.AddHistoryButtons()
        else:
            l = QLabel("History Empty")
            l.setFont(QFont(self.font, int(self.fontSize*1.5)))
            self.historyButtons.addWidget(l)         

    def AddHistoryButtons(self):
        for i in reversed(range(len(ItemManager.itemHistory))):
            button = QPushButton(text=f"{ItemManager.itemHistory[i].type}")
            if i == len(ItemManager.itemHistory)-1:
                button.setStyleSheet("background-color: rgba(176, 255, 161,90)")
            else:
                button.setStyleSheet("background-color: rgba(105, 105, 105, 30)")
            button.clicked.connect(functools.partial(self.UpdateItemInfo, i, self.historyItemInfoDisplay, self.historyItemStats, True))
            self.historyButtons.addWidget(button)
            self.historyButtonsList.append(button)
        self.historyButtonsList.reverse()

    #OTHER
    def UpdateItemInfo(self, itemIndex, widget, layout, historyButton=False):
        if ItemManager.itemHistory[itemIndex] is None:
            pass
        else:
            item = ItemManager.itemHistory[itemIndex]
            widget.setTitle(item.type) #Set Item Name
            for i in reversed(range(layout.count())): #Clear Old Item Stats
                layout.itemAt(i).widget().deleteLater()
            for i in range(len(item.stats)):
                l = QLabel(f"{item.stats[i][0]} {item.stats[i][1]}")
                l.setFont(QFont(self.font, self.fontSize))
                layout.addWidget(l)
        if historyButton:
            self.historyButtonsList[itemIndex].setStyleSheet("background-color: rgba(176, 255, 161,90)")
            for i in range(len(self.historyButtonsList)):
                if i == itemIndex:
                    pass
                else:
                    self.historyButtonsList[i].setStyleSheet("background-color: rgba(105, 105, 105, 30)")

    def ClearWidgetsFromLayout(self,layout):
        if len(layout) > 0:
            for i in reversed(range(layout.count())):
                layout.itemAt(i).widget().deleteLater()
                layout.itemAt(i).widget().setParent(None)