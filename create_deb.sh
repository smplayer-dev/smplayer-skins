#! /bin/sh
 
ln -s debian-rvm debian

#dpkg-buildpackage -rfakeroot

# This should be faster:
rm build-stamp
fakeroot debian/rules build
fakeroot debian/rules binary

