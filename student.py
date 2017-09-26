var1 = "student"

def test_scope1():
    print(var1)
    var2 = "classmate"
    return var1,var2

def test_scope2():
   # var2 = "another person"
    var1 = "changed var1"
    return var2,var1

print("global var1", var1)
print("test_scope1", test_scope1())
print("test_scope2", test_scope2())
