import rospy
import numpy as np
import matplotlib.pyplot as plt
import rosbag
import sys
import time

latitude , longitude, timestamp_lat_lon = [], [], []
linear_x , linear_y, timestamp_vel = [], [], [] 
steer_whl_angle, steer_whl_torque, speed, timestamp_steer = [], [], [], [] 

topic_list = ['/vehicle/gps/fix','/vehicle/gps/vel','/vehicle/steering_report']

def smoothing(y_curve,points):
	y_smooth = np.convolve(y_curve,np.ones(points)/points, mode = 'same')
	return y_smooth

def exp_smoothing(y_curve, beta):
	y_smooth = [0.0]
	for v in y_curve:
		y_smooth.append(beta*y_smooth[-1] + (1-beta)*v)
	return np.array(y_smooth[1:])

def plot_compare_data(original_data,smooth_data, timestamp, ylabel, xlabel):
	fig = plt.figure()
	ax = fig.add_subplot(1,1,1)
	ax.plot(timestamp, original_data,'o', c = 'red', label = "Original data")
	ax.plot(timestamp, smooth_data,'-', c = 'steelblue', linewidth = 2, label = "Smoothened data")
	ax.set_xlabel(xlabel)
	ax.set_ylabel(ylabel)
	ax.legend(loc = 'best')
	plt.show()

def plot_data(data, timestamp, ylabel, xlabel):
	fig = plt.figure()
	ax = fig.add_subplot(1,1,1)
	ax.plot(timestamp, data,'o', c = 'steelblue')
	ax.set_xlabel(xlabel)
	ax.set_ylabel(ylabel)
	plt.show()


if __name__ == '__main__':
	bag = rosbag.Bag(sys.argv[1])
	for topic, msg, t in bag.read_messages(topics= ['/vehicle/gps/fix']):
		#print (t.to_sec(),msg.header.stamp.to_sec())
		longitude.append(msg.longitude)
		latitude.append(msg.latitude)
		longitude_smooth = exp_smoothing(longitude,0.0)
		latitude_smooth = exp_smoothing(latitude,0.0)
		timestamp_lat_lon.append(msg.header.stamp.to_sec())

	for topic, msg, t in bag.read_messages(topics= ['/vehicle/gps/vel']):
		#print (t.to_sec(),msg.header.stamp.to_sec())
		linear_x.append(float(msg.twist.linear.x))
		linear_y.append(msg.twist.linear.y)

		linear_x_smooth = exp_smoothing(linear_x,0.4)
		linear_y_smooth = exp_smoothing(linear_y,0.4)

		timestamp_vel.append(msg.header.stamp.to_sec())

	for topic, msg, t in bag.read_messages(topics= ['/vehicle/steering_report']):
		#print (t.to_sec(),msg.header.stamp.to_sec())
		steer_whl_angle.append(float(msg.steering_wheel_angle))
		steer_whl_torque.append(msg.steering_wheel_torque)
		speed.append(msg.speed)

		steer_whl_angle_smooth = exp_smoothing(steer_whl_angle,0.75)
		steer_whl_torque_smooth = exp_smoothing(steer_whl_torque, 0.8)
		speed_smooth = exp_smoothing(speed,0.6)

		timestamp_steer.append(msg.header.stamp.to_sec())

		
	bag.close()

	#print(timestamp_vel, len(timestamp_vel), len(timestamp_steer))

	'''
				plot_compare_data(longitude,longitude_smooth,timestamp_lat_lon, "longitude", "timestamp")
				plot_compare_data(latitude,latitude_smooth,timestamp_lat_lon, "latitude", "timestamp")
			
				plot_compare_data(linear_x,linear_x_smooth,timestamp_vel, "linear_x", "timestamp")
				plot_compare_data(linear_y,linear_y_smooth,timestamp_vel, "linear_y", "timestamp")
			
				plot_compare_data(steer_whl_angle,steer_whl_angle_smooth,timestamp_steer, "steering wheel angle", "timestamp")
				plot_compare_data(steer_whl_torque,steer_whl_torque_smooth,timestamp_steer, "steering wheel Torque", "timestamp")
				plot_compare_data(speed,speed_smooth,timestamp_steer, "speed", "timestamp")
			'''

	#print(timestamp_vel)
	'''
		plot_data(longitude,timestamp_lat_lon, "longitude", "timestamp")
		plot_data(latitude,timestamp_lat_lon, "latitude", "timestamp")
	
		plot_data(linear_x,timestamp_vel, "linear_x", "timestamp")
		plot_data(linear_y,timestamp_vel, "linear_y", "timestamp")
	
		plot_data(steer_whl_angle,timestamp_steer, "steering wheel angle", "timestamp")
		plot_data(steer_whl_torque,timestamp_steer, "Steering wheel Torque", "timestamp")
		plot_data(speed,timestamp_steer, "speed", "timestamp")
	
	'''	




	nearest_timestamp_list, nearest_timestamp_whl_angle_list, nearest_timestamp_whl_torque_list, nearest_timestamp_speed_list = [], [], [], []
	'''	
	start_time = time.time()

	for time_one in timestamp_lat_lon:
		temp_list = []
		for time_comp in timestamp_steer:
			temp_list.append(abs(time_one-time_comp))

		nearest_timestamp_list.append(timestamp_steer[temp_list.index(min(temp_list))])
		nearest_timestamp_whl_angle_list.append(steer_whl_angle[temp_list.index(min(temp_list))])
		nearest_timestamp_whl_torque_list.append(steer_whl_torque[temp_list.index(min(temp_list))])
		nearest_timestamp_speed_list.append(speed[temp_list.index(min(temp_list))])

	print("Time  Brute Force: {}".format(time.time() -  start_time))
	'''
	start_time = time.time()

	for time_one in timestamp_lat_lon:
		temp_list = abs(time_one - np.array(timestamp_steer))

		nearest_timestamp_list.append(timestamp_steer[np.argmin(temp_list)])
		nearest_timestamp_whl_angle_list.append(steer_whl_angle[np.argmin(temp_list)])
		nearest_timestamp_whl_torque_list.append(steer_whl_torque[np.argmin(temp_list)])
		nearest_timestamp_speed_list.append(speed[np.argmin(temp_list)])

	print("Time  Brute Force: {}".format(time.time() -  start_time))

	print(nearest_timestamp_list)

	'''
	start_time = time.time()

	temp_list = []
	for time_one in timestamp_lat_lon:
		previous_value = 0.0
		start_index = 0
		for i in range(len(timestamp_steer[start_index:])):
			if previous_value == 0:
				previous_value = (time_one - timestamp_steer[start_index:][i])
			elif previous_value*(time_one-timestamp_steer[start_index:][i]) < 0:
				temp_list.append(timestamp_steer[start_index:][i])
				start_index += i
				break

	print("Time Optimized: {} ".format(time.time() - start_time))

	print(temp_list)
	'''



	smooth_nearest_timestamp_whl_angle_list = exp_smoothing(nearest_timestamp_whl_angle_list,0.5)
	smooth_nearest_timestamp_whl_torque_list = exp_smoothing(nearest_timestamp_whl_torque_list,0.7)
	smooth_nearest_timestamp_speed_list = exp_smoothing(nearest_timestamp_speed_list,0.5)

	print(len(smooth_nearest_timestamp_whl_angle_list),len(smooth_nearest_timestamp_whl_torque_list),len(smooth_nearest_timestamp_speed_list))
	plot_compare_data(nearest_timestamp_whl_angle_list,smooth_nearest_timestamp_whl_angle_list,nearest_timestamp_list, "steering wheel angle", "timestamp")
	plot_compare_data(nearest_timestamp_whl_torque_list,smooth_nearest_timestamp_whl_torque_list,nearest_timestamp_list, "Steering wheel Torque", "timestamp")
	plot_compare_data(nearest_timestamp_speed_list,smooth_nearest_timestamp_speed_list,nearest_timestamp_list, "speed", "timestamp")
	