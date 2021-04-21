from app.tests.portal.ReciboTest import ReciboTest
from app.tests.portal.ReciboTest import LoginTest

import unittest

if __name__ == '__main__':
    #unittest.main()
    unittest.main(LoginTest(), exit = False)
    unittest.main(ReciboTest())
    unittest.main()
