import argparse
import rosbag
import sensor_msgs.point_cloud2 as pc2
import sensor_msgs.msg as image_msg
import pcl
import numpy as np
from pathlib2 import Path
import glob

import sys
sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')
import cv2
sys.path.append('/opt/ros/kinetic/lib/python2.7/dist-packages')
from cv_bridge import CvBridge

if __name__=='__main__':
    parser = argparse.ArgumentParser(description='arg parser')
    parser.add_argument('--data_dir', type=str, default=None, help='directory path')
    parser.add_argument('--lidar_topic', type=str, default=None, help='lidar topic name')
    parser.add_argument('--sampling_rate', type=int,help='sampling rate')
    args = parser.parse_args()

    num = 0
    
    list_bag = sorted(glob.glob(args.data_dir+'/*.bag'))
    
    for bag_path in list_bag:
        
        bag = rosbag.Bag(bag_path)
        bridge = CvBridge()
        
        bag_filename = (bag_path.split('/')[-1]).split('.')[0]
        print(bag_filename)

        save_path = args.data_dir+'/'+bag_filename
        Path(save_path).mkdir(parents=True, exist_ok=True)

        for lidar_topic, lidar_msg, lidar_t in bag.read_messages(topics=[args.lidar_topic]):

            if(num % args.sampling_rate == 0):

                # lidar msg to numpy array(n,4)
                list_pc = []
                for data in pc2.read_points(lidar_msg, skip_nans=True):  
                    list_pc.append([data[0], data[1], data[2], data[3]])
                np_pc = np.array(list_pc, dtype=np.float32)

                # save numpy array to bin or pcd
                filename = str(lidar_t)
                print(filename)
                
                # np_pc_bin = np_pc.copy()
                # bin_path_ = save_path+'/bin'
                # Path(bin_path_).mkdir(parents=True, exist_ok=True)
                # bin_path = bin_path_ + "/" + filename + ".bin"
                # np_pc_bin.astype(np.float32).tofile(bin_path)
                
                np_pc_pcd = np_pc.copy()
                pcd_path_ = save_path+'/pcd'
                Path(pcd_path_).mkdir(parents=True, exist_ok=True)
                pcd_path = pcd_path_+"/"+filename+".pcd"
                pc_intensity = pcl.PointCloud_PointXYZI()
                pc_intensity.from_array(np_pc_pcd)
                pcl.save(pc_intensity, pcd_path)

            num += 1
