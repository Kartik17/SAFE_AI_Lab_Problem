# SAFE AI Lab Problem 6

## Objective

1. Download and process the rosbag from https://drive.google.com/open?id=17YP45-GKin5YU2TP7tALvb0_E7EDnh6t
2. Process this rosbag and extract the messages from the following rostopics or attributes: The longitude of the vehicle The latitude of the vehicle /vehicle/gps/vel /vehicle/steering_report. Please specify the rostopics that contained the information of the longitude and latitude of the vehicle.
3. Plot the data of the mentioned attributes or rostopics and Extract information from rostopics Please smooth the mentioned data, specific the method you used for smoothing. 
4. Then synchronize the mentioned information or rostopics by aligning them with the same timestamps. (hint: For each time step, you may discard some data and only keep the data collected with a time interval.) Report the method you used for synchronizing.


## Plots of Raw Data

#### Longitude vs timestamp
![Longitude vs timestamp](https://github.com/Kartik17/SAFE_AI_Lab_Problem/blob/master/Images/longitude_timesatmp.png)

#### Latitude vs timestamp
![Latitude vs timestamp](https://github.com/Kartik17/SAFE_AI_Lab_Problem/blob/master/Images/latitude_timestamp.png)

#### Linear x vs timestamp
![Linear x vs timestamp](https://github.com/Kartik17/SAFE_AI_Lab_Problem/blob/master/Images/linearx_timestamp.png)

#### Linear y vs timestamp
![Linear y vs timestamp](https://github.com/Kartik17/SAFE_AI_Lab_Problem/blob/master/Images/lineary_timestamp.png)

#### Steering wheel Angle vs timestamp
![Steering wheel Angle vs timestamp](https://github.com/Kartik17/SAFE_AI_Lab_Problem/blob/master/Images/steering_whl_angle_timestamp.png)

#### Steering wheel torque vs timestamp
![Steering wheel torque vs timestamp](https://github.com/Kartik17/SAFE_AI_Lab_Problem/blob/master/Images/steering_whl_torque_timestamp.png)

#### Speed vs timestamp
![Speed vs timestamp](https://github.com/Kartik17/SAFE_AI_Lab_Problem/blob/master/Images/speed_timestamp.png)


## Plots of Smoothened Data


#### Longitude vs timestamp
![Longitude vs timestamp](https://github.com/Kartik17/SAFE_AI_Lab_Problem/blob/master/Images/longitude_smooth_timestamp.png)

#### Latitude vs timestamp
![Latitude vs timestamp](https://github.com/Kartik17/SAFE_AI_Lab_Problem/blob/master/Images/latitude_smooth_timestamp.png)

#### Linear x vs timestamp
![Linear x vs timestamp](https://github.com/Kartik17/SAFE_AI_Lab_Problem/blob/master/Images/linearx_smooth_timestamp.png)

#### Linear y vs timestamp
![Linear y vs timestamp](https://github.com/Kartik17/SAFE_AI_Lab_Problem/blob/master/Images/lineary_smooth_timestamp.png)

#### Steering wheel Angle vs timestamp
![Steering wheel Angle vs timestamp](https://github.com/Kartik17/SAFE_AI_Lab_Problem/blob/master/Images/steering_whl_angle_smooth_timestamp.png)

#### Steering wheel torque vs timestamp
![Steering wheel torque vs timestamp](https://github.com/Kartik17/SAFE_AI_Lab_Problem/blob/master/Images/steering_whl_torque_smooth_timestamp.png)

#### Speed vs timestamp
![Speed vs timestamp](https://github.com/Kartik17/SAFE_AI_Lab_Problem/blob/master/Images/speed_smooth_timestamp.png)


## Time Synchronization
Timestamps of topics '/vehicle/gps/fix' and '/vehicle/gps/vel' were already sychronized, though '/vehicle/steering_report' had more timestamps than both.
Method : 
- Take timestamp in the topic '/vehicle/gps/fix'
- Subtract that timestamp value from the timestamps of '/vehicle/steering_report',  and store the minimum value of the difference.

Timestamps - [1508620413.394021, 1508620414.415758, 1508620415.417381, 1508620416.439116, 1508620417.440769, 1508620418.462491, 1508620419.4641593, 1508620420.4858956, 1508620421.4875915, 1508620422.5092423, 1508620423.510952, 1508620424.5126266, 1508620425.5343273, 1508620426.5360014, 1508620427.5577233, 1508620428.5794737, 1508620429.5811334, 1508620430.5827901, 1508620431.6044807, 1508620432.6061764, 1508620433.6079364, 1508620434.6295877, 1508620435.651317, 1508620436.652955, 1508620437.654632, 1508620438.6763487]


## Plot of Time Sychronized Data

#### Steering wheel Angle vs timestamp
![Steering wheel Angle vs timestamp](https://github.com/Kartik17/SAFE_AI_Lab_Problem/blob/master/Images/steering_whl_angle_nearest_ts.png)

#### Steering wheel torque vs timestamp
![Steering wheel torque vs timestamp](https://github.com/Kartik17/SAFE_AI_Lab_Problem/blob/master/Images/steering_whl_torque_nearest.png)

#### Speed vs timestamp
![Speed vs timestamp](https://github.com/Kartik17/SAFE_AI_Lab_Problem/blob/master/Images/speed_nearest_timestamp.png)


## How to run the code

python2.7 SAFE_AI_Challenge.py right_pass2_sedan.bag

python Tracking_SAFE_AI.py 

