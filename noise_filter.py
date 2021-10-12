import pcl
import numpy as np
import os

def do_statistical_outlier_filtering(pcl_data, mean_k, tr):

    outlier_filter = pcl_data.make_statistical_outlier_filter()
    outlier_filter.set_mean_k(mean_k)
    outlier_filter.set_std_dev_mul_thresh(tr)
    return outlier_filter.filter()


cloud = pcl.load("./kitti_2011_09_26_drive_0002_synced/pcd/1317009764317411899.pcd")

cloud = do_statistical_outlier_filtering(cloud, 3, 2.0)

pcl.save(cloud, './kitti_2011_09_26_drive_0002_synced/pcd/1317009764317411899_result.pcd') 