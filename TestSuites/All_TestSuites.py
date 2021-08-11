import unittest
from Package1.TC_Login_Personal import LoginTest_p
from Package1.TC_Signup_Personal import SignupTest_P
from Package1.TC_RecordingTest_Personal import RecordingTest_p

from Package2.TC_Login_Team import LoginTest_T
from Package2.TC_Signup_Team import SignupTest_T
from Package2.TC_RecordingTest_Team import RecordingTest_T

#get all tests from Logintest, signuptest , recordingtest

tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTest_p)
tc2 = unittest.TestLoader().loadTestsFromTestCase(SignupTest_P)
tc3 = unittest.TestLoader().loadTestsFromTestCase(RecordingTest_p)
tc4 = unittest.TestLoader().loadTestsFromTestCase(LoginTest_T)
tc5 = unittest.TestLoader().loadTestsFromTestCase(SignupTest_T)
tc6 = unittest.TestLoader().loadTestsFromTestCase(RecordingTest_T)

#creating test suites

sanityTestSuite = unittest.TestSuite([tc1,tc2,tc4,tc5]) #sanity test suite
functionalTestSuite = unittest.TestSuite([tc3]) #functional test suite
masterTestSuites = unittest.TestSuite([tc1,tc2,tc3,tc4,tc5]) #master test suites

# unittest.TextTestRunner().run(sanityTestSuite) # only sigup and login
unittest.TextTestRunner().run(functionalTestSuite) # only recording
# unittest.TextTestRunner().run(masterTestSuites) # all

