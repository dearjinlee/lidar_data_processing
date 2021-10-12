import pcl
import numpy as np
import os

def do_passthrough(pcl_data,filter_axis,axis_min,axis_max):

    passthrough = pcl_data.make_passthrough_filter()
    passthrough.set_filter_field_name(filter_axis)
    passthrough.set_filter_limits(axis_min, axis_max)
    return passthrough.filter()

cloud = pcl.load("./kitti_2011_09_26_drive_0002_synced/pcd/1317009764317411899.pcd")

filter_axis = 'x'
axis_min = -40.0
axis_max = 40.0
cloud = do_passthrough(cloud, filter_axis, axis_min, axis_max)

filter_axis = 'y'
axis_min = -40.0
axis_max = 40.0
cloud = do_passthrough(cloud, filter_axis, axis_min, axis_max)

pcl.save(cloud, './kitti_2011_09_26_drive_0002_synced/pcd/1317009764317411899_result.pcd') 