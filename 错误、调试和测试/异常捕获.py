# try...except...finally
import logging
logging.basicConfig(level=logging.INFO)

class TestException(object):

    def bar(self):
        x = -1
        try:
            x = self.foo(0)
        except BaseException as e:
            logging.exception(e)
        finally:
            logging.info("finally...")
        return x

    def foo(self,x):
        return 100/int(x)

if __name__ =="__main__":
    test = TestException()
    test.bar()