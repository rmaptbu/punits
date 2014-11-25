from punits import punit
import nose.tools as ns

def test_unit_conversion():
	length1=punit(2,'millimeter')
	length2=punit(2E-6, 'kilometer')
	time1=punit(2,'minutes')
	time2=punit(120, 'seconds')
	ns.assert_equal(length1, length2)
	ns.assert_equal(time1,time2)
	ns.assert_equal(1,punit(1))
	ns.assert_equal(0,punit(0))
	ns.assert_not_equal(length1,time1)
	
def test_raises():
	ns.assert_raises(ValueError, punit, 1, "abc")
	ns.assert_raises(ValueError, lambda a,b: a+b, punit(1,'meter'), punit(1))
	
def test_mul():
	energy=punit(5,'millijoule')
	power=punit(1,'kilowatts')
	weight1=punit(0.2,'kilogramme')
	weight2=punit(2.5,'milligram')
	time=punit(1,'second')
	ns.assert_equal(energy*weight1*2.5, power*time*weight2)
	ns.assert_not_equal(energy*weight1, power*time*weight2)
	ns.assert_not_equal(energy*weight1, power*weight2)
	
def test_add():
	time1=punit(60,'seconds')
	time2=punit(2,'minutes')
	ns.assert_equal(punit(3,'minutes'),time1+time2)
	ns.assert_equal(punit(1),punit(0)+1)
	ns.assert_not_equal(punit(1),punit(1)+1)
	
	