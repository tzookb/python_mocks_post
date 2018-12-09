from src.some_module import some_method
import othersrc.other_module as om

def main1():
    return some_method()

def main2():
    return om.other_method()

def code_with_exception_check():
    try:
        some_method()
    except Exception as ex:
        return "error"

def main3():
    return om.method_with_param("a_param", "b_param")

def main4():
    res = {
        "a": some_method(),
        "b": om.other_method()
    }
    return res

class HasDependency:
    def __init__(self, dependency):
        self.dependency = dependency
    def run(self):
        return self.dependency.run()
