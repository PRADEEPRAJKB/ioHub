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

Running the Example
---
Plug in an eye tracker, make sure it is working with Quick Glance...
Close Quick Glance and run:

    python quicklink2.py

###Example Output

	QL2 API Version:  2.7.3.1
	num of devices found: 1
	Device id: 1
	Model:	EyeOn
	SN:	4806
	Sensor:	2592x1944
	starting device
	
	ImageData:	 PixelData:	<__main__.LP_c_ubyte object at 0x00000000069E9B48>
	 Size:	2592x1944
	 Timestamp:	1295773750.40
	 Gain:	37
	 FrameNumber:	416
	 ROI:	680,208 1296x576
	 Reserved:	<__main__.c_void_p_Array_14 object at 0x00000000069E9B48>
	LeftEye:	True 1724.15,475.75
	RightEye:	True 842.66,447.60
	GazePoint:	 Valid:	False
	 x:	0.0
	 y:	0.0
	Focus:	13.44
	Distance:	42.66
	Bandwidth:	63
	DeviceId:	1
	
	...
	
	done

Troubleshooting
----
    OSError: [WinError 126] The specified module could not be found

The dll's are not in the working directory folder.  Download the dll's and put them in.

    OSError: [WinError 193] %1 is not a valid Win32 application

The dll bitness does not match the bitness of your python distribution.  Download the right set of dlls to match what you are using with it.

