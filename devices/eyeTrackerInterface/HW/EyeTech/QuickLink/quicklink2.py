"""
Quicklink.py
.. file: ioHub/devices/eyeTrackerInterface/HW/devices/pyEyeTrackerInterface/eyeTeck/QuickLink/quicklink.py

Copyright (C) 2012 EyeTech Inc.
Distributed under the terms of the GNU General Public License (GPL version 3 or any later version).

.. fileauthor:: Eye Tech Inc. & Sol Simpson & Peter Hyatt
"""
from ctypes import *
from ql2types import  * 
import time

#import inspect

def main():
    # If this file is ran explicitly, do a test of the functions here.
    # load the dll!
    ql2 = CDLL("QuickLink2.dll")
    if(ql2 == 0):
        raise ValueError('DLL not found')

    # QLAPI_GetVersion
    buff_size = 128
    version_str = create_string_buffer(buff_size)    
    ret_val = ql2.QLAPI_GetVersion(c_int(buff_size), version_str)
    if(ret_val != QL_ERROR_OK):
        raise ValueError(errorToString(ret_val))
    else:
        print("QL2 API Version: ", version_str.value.decode("utf-8"))
    
    if(False):
        print(ql2.QLAPI_ExportSettings)
        print(ql2.QLAPI_ImportSettings)
        print(ql2.QLDevice_Enumerate)
    
    device_id = 0
    
    # pass in a buffer of 100 DeviceId's
    num_devices = c_int(100)
    num_devices_ptr = pointer(num_devices)
    # device_buffer = (QLDeviceId * num_devices_ptr.contents.value)()
    device_buffer = (num_devices.value * QLDeviceId)()
    device_buffer_ptr = pointer(device_buffer)
    ret_val = ql2.QLDevice_Enumerate(num_devices_ptr, device_buffer_ptr)
    if(ret_val != QL_ERROR_OK):
        raise ValueError(errorToString(ret_val))
    else:
        print("num of devices found:", num_devices.value)
        for num in range(0, num_devices.value):
            print("Device id:",device_buffer[num])
        device_id = device_buffer[0]
        
    # we have a handle to a device!
    if(device_id == 0):
        raise ValueError('No devices found')
    
    # QLDevice_GetInfo
    device_info = (QLDeviceInfo)()
    device_info_ptr = pointer(device_info)
    ret_val = ql2.QLDevice_GetInfo(device_id, device_info_ptr)
    if(ret_val != QL_ERROR_OK):
        raise ValueError(errorToString(ret_val))
    else:
        print(infoToString(device_info))
    
    
    if(False):
        print(ql2.QLDevice_ExportSettings)
        print(ql2.QLDevice_ImportSettings)
        print(ql2.QLDevice_IsSettingSupported)
        print(ql2.QLDevice_SetPassword)
    
    #QLDevice_Start
    print("starting device")
    ret_val = ql2.QLDevice_Start(device_id)
    if(ret_val != QL_ERROR_OK):
        raise ValueError(errorToString(ret_val))
    
    if(False):
        print(ql2.QLDevice_Stop)
        print(ql2.QLDevice_Stop_All)
        print(ql2.QLDevice_SetIndicator)
        print(ql2.QLDevice_GetIndicator)
    
    
    frame = (QLFrameData)()
    frame_ptr = pointer(frame)
    wait_time = 500
    
    # run the eye tracker for 30 seconds
    duration_seconds = 30
    stop = time.time() + duration_seconds
    while time.time() < stop:
        ret_val = ql2.QLDevice_GetFrame(device_id, wait_time, frame_ptr)
        if(ret_val != QL_ERROR_OK):
            raise ValueError(errorToString(ret_val))
        else:
            if(False):
                print(frame)
            else:
                print(frameDataToString(frame))
    
    ret_val = ql2.QLDevice_Stop(device_id)
    if(ret_val != QL_ERROR_OK):
        raise ValueError(errorToString(ret_val))
    
    if(False):
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

if __name__ == "__main__":
    main()