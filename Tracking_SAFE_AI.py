import numpy as np
import matplotlib.pyplot as plt


dt = 1
observation_list = [np.matrix([2,0.5,0.5,0.0]),np.matrix([4,0.5,0.5,0.0])]

F = np.matrix([[1,0,0,0,dt,0,0,0],
			   [0,1,0,0,0,dt,0,0],
			   [0,0,1,0,0,0,dt,0],
			   [0,0,0,1,0,0,0,dt],
			   [0,0,0,0,1,0,0,0],
			   [0,0,0,0,0,1,0,0],
			   [0,0,0,0,0,0,1,0],
			   [0,0,0,0,0,0,0,1]])

P = np.matrix([[5,0,0,0,0,0,0,0],
			   [0,5,0,0,0,0,0,0],
			   [0,0,5,0,0,0,0,0],
			   [0,0,0,5,0,0,0,0],
			   [0,0,0,0,5,0,0,0],
			   [0,0,0,0,0,5,0,0],
			   [0,0,0,0,0,0,5,0],
			   [0,0,0,0,0,0,0,5]])

Q_P = np.matrix([[0.05,0,0,0,0,0,0,0],
			     [0,0.05,0,0,0,0,0,0],
			     [0,0,0.05,0,0,0,0,0],
			     [0,0,0,0.05,0,0,0,0],
			     [0,0,0,0,0.05,0,0,0],
			     [0,0,0,0,0,0.05,0,0],
			     [0,0,0,0,0,0,0.05,0],
			     [0,0,0,0,0,0,0,0.05]])

H = np.matrix([[1,0,0,0,0,0,0,0],
			   [0,1,0,0,0,0,0,0],
			   [0,0,1,0,0,0,0,0],
			   [0,0,0,1,0,0,0,0]
				]) 

Q_S = np.matrix([[0.2,0,0,0],
			     [0,0.2,0,0],
			     [0,0,0.2,0],
			     [0,0,0,0.4],
			    ])


def predict(F,P,Q, X_old):
	# Predict t+1
	X_new = F*X_old 

	# Covariance
	P_new = F*P*np.transpose(F) + Q

	return X_new, P_new

def update(z,H,X_new,P_new,Q):
	#residual
	y = z - H*X_new
	# Update Covariance
	S = H*P_new*np.transpose(H) + Q
	# Kalman Gain
	K = P_new*np.transpose(H)*np.linalg.inv(S)
	# Optimal Prediction
	X_optimal = X_new + K*y
	# Update COvariance
	P_optimal = (np.eye(8) - K*H)*P_new

	return X_optimal, P_optimal



if __name__ == '__main__':
	state_vector = np.matrix([1,0.5,0.5,0.0,0.0,0.0,0.0,0.0])
	states = [state_vector.T]

	for i in range(10):
		if i <= (len(observation_list)-1):
			X_new, P_new = predict(F,P,Q_P,states[i])
			state_vector, P = update(observation_list[i].T,H,X_new,P_new,Q_S)
			states.append(state_vector)
			print(state_vector[0][0])

		elif i >(len(observation_list)-1):
			X_predict, P_new = predict(F,P,Q_P,states[i])
			states.append(X_predict)
			print(X_predict[0][0])


'''

Tracking for 3D cuboids

Kalman Filter 

Given:
First and Second frame annotation, which are coordinates of the cuboids

1. Prediction Step

State Vector(9x9) x = [px,py,pz,vx,vy,vz,ax,ay,az]

State Update Matrix (F) - 9x9 - (Constant Acceleration)

State Vector Covariance (P) 9x9 -  diagonal represent the variance of the state vector

Update = FPF_t + Q(noise)

2. Update Step

First, is to calculate the residual then the Kalman Gain

Measurement Vector : [px,py,pz]

(residual) y = z - Hx_new

Update the Covariance State matrix:
S = H(P_new)H_t + R

R is the noise Measurement matrix - 

Kalman Gain calculate:

K = P_new*H_t*inv(S)

Now calculate the posterior state vector and Covariance matrix

x_posterior = x_new + K*residual

P_posterior = (I - K*H)*P_new 



### Particle Filter ###

Define a state vector of each Particle

State Vector(9x9) x = [px,py,pz,vx,vy,vz,ax,ay,az]
weights of particle = w_i
Initial Belief - based on the first annotation and uncertainity


Update Step
Apply the motion update to the particles
and generate the new particles.

Apply weight to the particle , by comparing the predicted vs actual Measurements



'''