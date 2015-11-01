import wpf

from System.Windows import Application, Window
from System.Windows.Controls import TabItem

class MyWindow(Window):
    def __init__(self):
        wpf.LoadComponent(self, 'CountMyMoney.xaml')    
        testTab = TabItem()
        testTab.Header = "СЧЁТ 1"
        self.tabControlMain.Items.Add(testTab)

if __name__ == '__main__':
    Application().Run(MyWindow())
