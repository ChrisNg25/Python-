'''
Đưa ra một RuntimeError exception. Gợi ý:
 
 Sử dụng raise() để đưa ra exception.
'''
#option 1: 
#raise RuntimeError('something wrong')
class RuntimeError(Exception):
    def __init__(self, mismatch):
        Exception.__init__(self, mismatch) 
try:
    print ("And now, the Vocational Guidance Counsellor Sketch.") 
    raise RuntimeError("Does not have proper hat")
    print ("This print statement will not be reached.") 
except RuntimeError as problem:
    print ("Vocation problem: {0}".format(problem))