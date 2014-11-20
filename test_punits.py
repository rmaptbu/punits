from punits import punit
import nose.tools as ns

def test_unit_conversion():
	length1=punit(1,'millimeter')
	length2=punit(1E-6, 'kilometer')
	ns.assert_equal(length1, length2)
	time1=punit(2,'minutes')
	time2=punit(120, 'seconds')
	ns.assert_equal(time1,time2)
	
def test_raises():
	ns.assert_raises(ValueError, punit, 1, "abc")
	ns.assert_raises(ValueError, lambda a,b: a==b, punit(1,'meter'), 1)