from punits import punits
import nose.tools as ns

def test_unit_conversion():
	length1=punit(1,'millimeter')
	length2=punit(1E-6, 'kilometer')
	ns.assert_equal(length1, length2)