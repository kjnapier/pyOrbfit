from .Orbit import Orbit
import os
pymodulepath = os.path.dirname(__file__)
os.environ['ORBIT_EPHEMERIS'] = pymodulepath + '/data/binEphem.423'
os.environ['ORBIT_OBSERVATORIES'] = pymodulepath + '/data/observatories.dat'