import sys
import os
class subsystem_messages:
    """docstring for subsystem_message."""
    def __init__ (self, name):
        self.name = name

    def ERROR(self, Code, Reason):
        self.Code = Code
        self.Reason = Reason
        print("ERROR", self.Code, ":", self.name , self.Reason)
class Load:
    """docstring for Load."""

    def __init__(self, name):
        self.name = name

    def Load_data(self):
        print(os.st(self))

try:
    assert sys.version_info <= (3, 7)
    print(sys.version)
    print(sys.version_info)

except AssertionError as version:
    version = subsystem_messages(version)
    version.ERROR(101, "'Incorrect or invaild please use python 3.6'")
    sys.exit(1)

except RuntimeError as Err0r:
    RuntimeError = subsystem_messages(RuntimeError)
    RuntimeError.ERROR(100, "has accured, please try again.")



try:
    from tqdm import tqdm
    print(tqdm)

except ImportWarning as module:
    module = subsystem_message(module)
    module.ERROR(102, "'module WARNING")


except ImportError as module:
    module = subsystem_messages(module)
    module.ERROR(103, "'module not found'")

except RuntimeError as Err0r:
    RuntimeError = subsystem_messages(RuntimeError)
    RuntimeError.ERROR(104, "has accured, please try again.")

try:
    import math
    print(math)

except ImportWarning as module:
    module = subsystem_message(module)
    module.ERROR(102, "'module WARNING")

except ImportError as module:
    module = subsystem_message(module)
    module.ERROR(103, "'module not found'")

except RuntimeError as Err0r:
    RuntimeError = subsystem_messages(RuntimeError)
    RuntimeError.ERROR(104, "has accured, please try again.")

try:
    import numpy
    print(numpy)

except ImportWarning as module:
    module = subsystem_message(module)
    module.ERROR(102, "'module WARNING")

except ImportError as module:
    module = subsystem_message(module)
    module.ERROR(103, "'module not found'")

except RuntimeError as Err0r:
    RuntimeError = subsystem_messages(RuntimeError)
    RuntimeError.ERROR(104, "has accured, please try again.")
