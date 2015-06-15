"""
Quicklink.py
.. file: ioHub/devices/eyeTrackerInterface/HW/devices/pyEyeTrackerInterface/eyeTeck/QuickLink/quicklink.py

Copyright (C) 2012 EyeTech Inc.
Distributed under the terms of the GNU General Public License (GPL version 3 or any later version).

.. fileauthor:: Eye Tech Inc. & Sol Simpson & Peter Hyatt
"""
from ctypes import *
from ql2types import  * 

import inspect

if __name__ == "__main__":
    # If this file is ran expicitly, do a test of the functions here.
    ql2 = CDLL("QuickLink2.dll");
    # load the dll!
    print(ql2)
    # 
    print(ql2.QLAPI_GetVersion)
    
    buff_size = 128
    str = create_string_buffer(buff_size)    
    retVal = ql2.QLAPI_GetVersion(c_int(buff_size), str)
    if(retVal != QL_ERROR_OK):
        print("not okay!")
    else:
        print("QL2 API Version: ", str.value)
    
    print(ql2.QLAPI_ExportSettings)
    print(ql2.QLAPI_ImportSettings)
    print(ql2.QLDevice_Enumerate)
    
    num_devices = POINTER(c_int)
    num_devices.value = 10
    elems = (QLDeviceId * num_devices.value)()
    device_buffer = cast(elems, POINTER(QLDeviceId))
    retVal = ql2.QLDevice_Enumerate(num_devices, device_buffer)
    print(num_devices.value)
    
    device_id = device_buffer[0]
        
    
    print(ql2.QLDevice_GetInfo)
    print(ql2.QLDevice_ExportSettings)
    print(ql2.QLDevice_ImportSettings)
    print(ql2.QLDevice_IsSettingSupported)
    print(ql2.QLDevice_SetPassword)
    print(ql2.QLDevice_Start)

    ql2.QLDevice_Start(device_id)
    
    print(ql2.QLDevice_Stop)
    print(ql2.QLDevice_Stop_All)
    print(ql2.QLDevice_SetIndicator)
    print(ql2.QLDevice_GetIndicator)
    print(ql2.QLDevice_GetFrame)
    print(ql2.QLDevice_ApplyCalibration)
    print(ql2.QLDevice_CalibrateEyeRadius)
    print(ql2.QLDeviceGroup_Create)
    print(ql2.QLDeviceGroup_AddDevice)
    print(ql2.QLDeviceGroup_RemoveDevice)
    print(ql2.QLDeviceGroup_Enumerate)
    print(ql2.QLDeviceGroup_GetFrame)
    print(ql2.QLSettings_Load)
    print(ql2.QLSettings_Save)
    print(ql2.QLSettings_Create)
    print(ql2.QLSettings_AddSetting)
    print(ql2.QLSettings_RemoveSetting)
    print(ql2.QLSettings_SetValue)
    print(ql2.QLSettings_SetValueInt)
    print(ql2.QLSettings_SetValueDouble)
    print(ql2.QLSettings_SetValueString)
    print(ql2.QLSettings_GetValue)
    print(ql2.QLSettings_GetValueInt)
    print(ql2.QLSettings_GetValueDouble)
    print(ql2.QLSettings_GetValueString)
    print(ql2.QLCalibration_Load)
    print(ql2.QLCalibration_Save)
    print(ql2.QLCalibration_Create)
    print(ql2.QLCalibration_Initialize)
    print(ql2.QLCalibration_GetTargets)
    print(ql2.QLCalibration_Calibrate)
    print(ql2.QLCalibration_GetScoring)
    print(ql2.QLCalibration_GetStatus)
    print(ql2.QLCalibration_Finalize)
    print(ql2.QLCalibration_Cancel)
    print(ql2.QLCalibration_AddBias)
    
    
    
    print("done")
        
