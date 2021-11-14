# lidar_data_processing

**라이다 센서 데이터 정제 실습을 위한 코드입니다.**

    https://aidata.linkedu.co.kr/

**1) 아래의 Link에서 "kitti_2011_09_26_drive_0002_synced.bag" 파일을 다운로드합니다.**

    https://drive.google.com/file/d/1aFxXDqxc-AJjXUjremx3yjQA7m9CubRB

**2) 다운로드 받은 "kitti_2011_09_26_drive_0002_synced.bag" 파일을 다운받은 git 파일의 LiDAR_data_processing 폴더로 이동시킵니다.**

**3) 아래 명령어를 통해 bag 파일을 10Hz로 샘플링합니다. (rosbag_sampling.py)**

    python3 rosbag_sampling.py --data_dir ./ --lidar_topic /kitti/velo/pointcloud  --sampling_rate 10
    
**4) 아래 명령어를 통해 passthrough filter를 테스트합니다. (passthrough_filter.py)**

    python3 passthrough_filter.py
    
**5) 아래 명령어를 통해 noise filter를 테스트합니다. (noise_filter.py)**

    python3 noise_filter.py
    
**6) 아래 명령어를 통해 전체 통합된 코드를 테스트합니다. (rosbag_cleaning.py)**

    python3 rosbag_cleaning.py --data_dir ./ --lidar_topic /kitti/velo/pointcloud  --sampling_rate 10   
