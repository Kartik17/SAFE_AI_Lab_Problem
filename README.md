# SAFE AI Lab Problem

## Objective

1. Download and process the rosbag from https://drive.google.com/open?id=17YP45-GKin5YU2TP7tALvb0_E7EDnh6t
2. Process this rosbag and extract the messages from the following rostopics or attributes: The longitude of the vehicle The latitude of the vehicle /vehicle/gps/vel /vehicle/steering_report. Please specify the rostopics that contained the information of the longitude and latitude of the vehicle.
3. Plot the data of the mentioned attributes or rostopics and Extract information from rostopics Please smooth the mentioned data, specific the method you used for smoothing. 
4. Then synchronize the mentioned information or rostopics by aligning them with the same timestamps. (hint: For each time step, you may discard some data and only keep the data collected with a time interval.) Report the method you used for synchronizing.
