import sys
from PyQt4 import QtGui, QtCore

class TestEclipseItem(QtGui.QGraphicsEllipseItem):
    def __init__(self, parent=None):
        QtGui.QGraphicsPixmapItem.__init__(self, parent)
        self.setPen(QtGui.QPen(QtCore.Qt.red,2))
        self.setFlag(QtGui.QGraphicsItem.ItemIsMovable, True)
        self.setFlag(QtGui.QGraphicsItem.ItemIsSelectable, True)
        
        text = TextItem(self)
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
    def __init__(self, parent=None):
        QtGui.QGraphicsPixmapItem.__init__(self, parent)
        self.setPen(QtGui.QPen(QtCore.Qt.blue,2))
        self.setFlag(QtGui.QGraphicsItem.ItemIsMovable, True)
        self.setFlag(QtGui.QGraphicsItem.ItemIsSelectable, True)
        

        # set move restriction rect for the item
        #self.move_restrict_rect = QtCore.QRectF(20, 20, 200, 200)
        # set item's rectangle
        self.setRect(QtCore.QRectF(0, 0, 50, 50))
        
class TextItem(QtGui.QGraphicsSimpleTextItem):
    def __init__(self, parent= None):
        super(TextItem, self).__init__(parent)
        self.setPen(QtGui.QPen(QtCore.Qt.red,2))
        self.setText("1")

class MainForm(QtGui.QWidget):
    def __init__(self, parent=None):
        super(MainForm, self).__init__(parent)
        self.resize(800, 800)
        gridlayout = QtGui.QGridLayout()
        scene = QtGui.QGraphicsScene(0, 0, 400, 400)

        ellipseItem = TestEclipseItem()
        scene.addItem(ellipseItem)

        
        ellipseItem_b = BlueEclipseItem()
        scene.addItem(ellipseItem_b)
        ellipseItem_b.moveBy(50,0)
        
        text = TextItem()
        #scene.addItem(text)
        print text.boundingRect().height()
        print text.boundingRect().width()
        

        view = QtGui.QGraphicsView()
        view.setScene(scene)
        view.setGeometry(QtCore.QRect(0, 0, 400, 400))
        gridlayout.addWidget(view, 0,0)
        
        
        button1 = QtGui.QPushButton( "button1" )
        button1.setFlat( True )
        gridlayout.addWidget( button1, 0, 1 )
        
        
        scene2 = QtGui.QGraphicsScene(0, 0, 400, 400)

        ellipseItem2 = TestEclipseItem()
        scene2.addItem(ellipseItem2)

        
        ellipseItem2_b = BlueEclipseItem()
        scene.addItem(ellipseItem2_b)
        ellipseItem2_b.moveBy(50,0)
        

        view2 = QtGui.QGraphicsView()
        view2.setScene(scene2)
        view2.setGeometry(QtCore.QRect(0, 0, 400, 400))
        gridlayout.addWidget(view2, 1,0)
        
        button2 = QtGui.QPushButton( "button2" )
        button2.setFlat( True )
        gridlayout.addWidget( button2, 1, 1 )
        #self.setCentralWidget(view)
        self.setLayout(gridlayout)
        

def main():
    app = QtGui.QApplication(sys.argv)
    form = MainForm()
    form.show()
     
    sys.exit(app.exec_()) 

if __name__ == '__main__':
    main()
