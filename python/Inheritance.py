#Single inheritance
class A():
    def __init__(self):
        print("con1")
class B(A):
        super().__init__()
        print("con2")
obj=B(A)        

'''
#Multilevel inheritance
class A():
    def __init__(self):
        point("con1")
class B(A):
    def __init__(self):
        super().__init__()
        print("con2")
class C(B):
    def __init__(self):
        super().__init__()
        print("con3")
obj=C()


#Multiple inheritance
class A():
    def __init__(self):
        print("con1")
class B():
    def __init__(self):
        super().__init__()
        print("con2")
class C(A,B):
    def __init__(self):
        super().__init__()
        print("con3")
obj=B()

#Hirarchial Inheritance
class A():
    def __init__(self):
        print("con1")
class B(A):
    def __init__(self):
        super().__init__()
        print("con2")
class C(A):
    def __init__(self):
        super().__init__()
        print("con3")
obj=B()

#Hybrid Inheritance



#Single inheritance program example
class s_marks():
    def __init__(self):
        print("Marks of s")
class m_marks(s_marks):
    def __init__(self):
        super().__init__()
        print("Marks of m")       
obj= m_marks(s_marks)        
 ''' 
