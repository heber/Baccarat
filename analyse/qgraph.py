import sys
from PyQt4 import QtGui, QtCore

class TestEclipseItem(QtGui.QGraphicsEllipseItem):
    def __init__(self,num, parent=None):
        QtGui.QGraphicsPixmapItem.__init__(self, parent)
        self.setPen(QtGui.QPen(QtCore.Qt.red,1))
        self.setFlag(QtGui.QGraphicsItem.ItemIsMovable, True)
        self.setFlag(QtGui.QGraphicsItem.ItemIsSelectable, True)
        self.setBrush(QtGui.QBrush(QtCore.Qt.yellow))
        
        text = TextItem(self)
        text.mysetText(num)
        text.moveBy(25- text.boundingRect().width() /2,25 - text.boundingRect().height()/2)
        
        
        

        # set move restriction rect for the item
        #self.move_restrict_rect = QtCore.QRectF(20, 20, 200, 200)
        # set item's rectangle
        self.setRect(QtCore.QRectF(0, 0, 50, 50))

    #def mouseMoveEvent(self, event):
    #    # check of mouse moved within the restricted area for the item 
    #    if self.move_restrict_rect.contains(event.scenePos()):
    #        QtGui.QGraphicsEllipseItem.mouseMoveEvent(self, event)

class BlueEclipseItem(QtGui.QGraphicsEllipseItem):
    def __init__(self, num, parent=None):
        QtGui.QGraphicsPixmapItem.__init__(self, parent)
        self.setPen(QtGui.QPen(QtCore.Qt.blue,1))
        self.setFlag(QtGui.QGraphicsItem.ItemIsMovable, True)
        self.setFlag(QtGui.QGraphicsItem.ItemIsSelectable, True)
        #self.brush()
        
        text = TextItem(self)
        text.mysetText(num)
        text.moveBy(25- text.boundingRect().width() /2,25 - text.boundingRect().height()/2)

        # set move restriction rect for the item
        #self.move_restrict_rect = QtCore.QRectF(20, 20, 200, 200)
        # set item's rectangle
        self.setRect(QtCore.QRectF(0, 0, 50, 50))
        
class TextItem(QtGui.QGraphicsSimpleTextItem):
    def __init__(self,parent= None):
        super(TextItem,  self).__init__(parent)
        #QtGui.QGraphicsSimpleTextItem.__init__(self, parent)
        self.setPen(QtGui.QPen(QtCore.Qt.red,1))
        
    def mysetText(self, num):
        self.setText(str(num))

def addscene(gridlayout, row, col):
    pailie = (1,0,0,1,0,1)
    
    scene = QtGui.QGraphicsScene(0, 0, 3500, 300)
    
    for col in range(70):
        for row in range(6):
            index = (- (col % 6) + row + 6) %6
            if pailie[index] == 1:
                ellipseItem = TestEclipseItem(col)
                scene.addItem(ellipseItem)
                ellipseItem.moveBy(50 * col, 50 * row)
            elif pailie[index] == 0:
                ellipseItem_b = BlueEclipseItem(col)
                scene.addItem(ellipseItem_b)
                ellipseItem_b.moveBy(50 * col, 50 * row)

    view = QtGui.QGraphicsView()
    view.setScene(scene)
    view.setGeometry(QtCore.QRect(0, 0, 300, 300))
    gridlayout.addWidget(view, row,col)

class MainForm(QtGui.QWidget):
    def __init__(self, parent=None):
        super(MainForm, self).__init__(parent)
        #self.resize(800, 800)
        gridlayout = QtGui.QGridLayout()

        for col in range(1):
            for row in range(2):
                print  row, col
        pailie = (1,0,0,1,0,1)
        
        scene = QtGui.QGraphicsScene(0, 0, 3500, 300)
        
        for col in range(70):
            for row in range(6):
                index = (- (col % 6) + row + 6) %6
                if pailie[index] == 1:
                    ellipseItem = TestEclipseItem(col)
                    scene.addItem(ellipseItem)
                    ellipseItem.moveBy(50 * col, 50 * row)
                elif pailie[index] == 0:
                    ellipseItem_b = BlueEclipseItem(col)
                    scene.addItem(ellipseItem_b)
                    ellipseItem_b.moveBy(50 * col, 50 * row)

        view = QtGui.QGraphicsView()
        view.setScene(scene)
        view.setGeometry(QtCore.QRect(0, 0, 300, 300))
        gridlayout.addWidget(view, 0,0)
         
        scene2 = QtGui.QGraphicsScene(0, 0, 3500, 300)
        
        for col in range(70):
            for row in range(6):
                index = (- (col % 6) + row + 6) %6
                if pailie[index] == 1:
                    ellipseItem = TestEclipseItem(col)
                    scene2.addItem(ellipseItem)
                    ellipseItem.moveBy(50 * col, 50 * row)
                elif pailie[index] == 0:
                    ellipseItem_b = BlueEclipseItem(col)
                    scene2.addItem(ellipseItem_b)
                    ellipseItem_b.moveBy(50 * col, 50 * row)

        view2 = QtGui.QGraphicsView()
        view2.setScene(scene2)
        view2.setGeometry(QtCore.QRect(0, 0, 300, 300))
        gridlayout.addWidget(view2, 0,1)
        #addscene(gridlayout, 0, 0)
        #addscene(gridlayout, 0, 1)
        
        #button1 = QtGui.QLabel( "button1" )
        #gridlayout.addWidget( button1, 0, 1 )
        
        
        #scene2 = QtGui.QGraphicsScene(0, 0, 400, 400)

        
        #ellipseItem2_b = BlueEclipseItem()
        #scene.addItem(ellipseItem2_b)
        #ellipseItem2_b.moveBy(50,0)
        

        #view2 = QtGui.QGraphicsView()
        #view2.setScene(scene2)
        #view2.setGeometry(QtCore.QRect(0, 0, 400, 400))
        #gridlayout.addWidget(view2, 1,0)
        
        #button2 = QtGui.QPushButton( "button2" )
        #button2.setFlat( True )
        #gridlayout.addWidget( button2, 1, 1 )
        #self.setCentralWidget(view)
        self.setLayout(gridlayout)
        

def main():
    app = QtGui.QApplication(sys.argv)
    form = MainForm()
    form.show()
     
    sys.exit(app.exec_()) 

if __name__ == '__main__':
    main()
