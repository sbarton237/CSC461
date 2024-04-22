"""
The World Geodetic System is a set of international standards for describing the shape of the Earth.  In the latest WGS-84 revision, 
the Earth's geoid is approximated to a reference ellipsoid that takes the form of an oblate spheroid with semi-major and semi-minor axes 
a=6378137.0m and c=6356752.314245m respectively. Use the formula for the surface area of an oblate spheroid, to calculate the surface 
area of this reference ellipsoid and compare it with the surface area of the Earth assumed to be a sphere with radius 6371km.
"""

import math

a = 6378137
c = 6356752.314245
r = 6371000
e = math.sqrt(1 - c * c / a / a)
sa_oblate = 2 * math.pi * a * a * (1 + (c * c / a / a / e * math.atanh(e)))
sa_sphere = 4 * math.pi * r * r

if sa_oblate > sa_sphere:
    print("The surface area of Earth is greater than the assumed surface area of Earth as a sphere. It is " + str(round(sa_oblate - sa_sphere)) + " meters squared larger.")
elif sa_oblate < sa_sphere:
    print("The surface area of Earth is less than the assumed surface area of Earth as a sphere. It is " + str(round(sa_sphere - sa_oblate)) + " meters squared smaller.")
else:
    print("The surface area of Earth is the assumed surface area of Earth as a sphere.")