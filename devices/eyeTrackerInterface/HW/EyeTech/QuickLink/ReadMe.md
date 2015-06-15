QuickLink2 Python Wrapper
----------------

To avoid Win32 errors, make sure the version of QL2 matches the bit-ness of the python package you are using.

Copy and download the appropriate QL2 library into this folder.

64 bit https://office.eyetechds.com/downloads/gitlab_releases/matlab_wrapper_x64/QL2MatlabWrapper_15.03.31_x64.zip

32 bit http://www.eyetechds.com/uploads/4/7/3/0/47308795/eyetechquicklink2installer15.06.03.43.exe

This library was built around Python 3.4.

If you use the ctypesgen library, you will need Python 2.7 (last checked June 2015).

Anaconda and Spyder are good tools for writing and working with Python:

http://continuum.io/downloads#py34

To install python 2.7 with chocolatey, enter this:

    choco install python -version 2.7.6

Then after it has downloaded, go to: `C:\Python27` and rename `python.exe` to `python27.exe`.

