# -*- coding: utf-8 -*-
"""
@author: richwang
"""
# 示範加上註解('''or""")，讓 help 可以引用。

# 函式內如果沒有加上註解('''or""")，這列會被 help 引用。
def newline(row=1):
    print()
    '''
    產生newline的效果！
    沒有給參數時會換一列，或是可以給定換行的列數。
    這部分的訊息可以經由 help(newline) 顯示。
    '''
    print('\n' * (row-1))

# 示範給參數名稱的用法:(印完後會換列) 
def markline(length=15, mark='-'):
    print(mark * length)
    #print("Show __name__ in markline:", __name__)
    
class Circle:
    PI = 3.141592653  # 類別成員(資料或函式)
    def __init__(self, r = 1):
        self.r = r  # 物件的資料成員
        
    def area(self): # 物件的成員函式
        return Circle.PI * self.r**2
    
    def perimeter(self):
        return 2* Circle.PI * self.r
    
    def about(self):
        pass
        
if __name__ == "__main__":  # 當測試完成後，可以當成 module 供外部使用！
    print("line 1")
    #newline()
    #newline(2)
    #markline(mark='*')  # 僅給定 mark
    #markline(length=5)  # 僅給定 length
    #markline(mark='#', length=30)  # 依相反的順序給定 mark, length
    markline(length=30, mark='#')  # 依序給定 length, mark 
    
    print(help(newline))  # 顯示緊接著定義在函式名稱下的註解: ''' or """。
    print(help(markline))
    
'''
呼叫 help(fun_name) 會顯示的內容:
1) 與 2) 不可兼得！
    
# 1) 如果沒有詳細說明就會顯示這部分！(必須緊接著函式定義)
def fun_name(...):
    """
    2) 函式的詳細說明！ 預設 help 會顯示這部分！
    """
'''    