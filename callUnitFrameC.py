from UnitFrameC import UnitFrame
import unittest

if __name__ == "__main__":
	#unittest.main(warnings='ignore')
	loader = unittest.TestLoader()
	sitaRunner = unittest.TextTestRunner(verbosity=2)
	sitaSuite = loader.loadTestsFromTestCase(UnitFrame)
	sitaRunner.run(sitaSuite)
