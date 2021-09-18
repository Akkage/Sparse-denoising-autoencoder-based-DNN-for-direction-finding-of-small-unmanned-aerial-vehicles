from numpy import genfromtxt
import numpy as np
#import scipy.io
class HandleData(object):

    def __init__(self, total_data, data_per_angle, num_angles):
        self.total_data=total_data
        self.data_per_angle=data_per_angle
        self.num_angles = num_angles
        self.current_point = 0
        self.data_set = np.zeros((self.total_data, 4), dtype=np.float32)
        self.label_set = np.zeros((self.total_data, self.num_angles), dtype=np.float32)

    def onehot_encode(self,number):
        encoded_no = np.zeros(self.num_angles, dtype=np.float32)
        if number < self.num_angles:
            encoded_no[number] = 1
        return encoded_no

    def next_batch(self,batch_size):
        # print("start : " + str(self.current_point))
        if self.current_point == self.total_data:
            self.current_point = 0
        start = self.current_point
        end = start + batch_size
        return_data = self.data_set[start:end]
        return_label = self.label_set[start:end]
        self.current_point=end
        # print(return_data)
        # print("end : " + str(self.current_point))
        return return_data,return_label

    def get_synthatic_data(self,test_data):

        if test_data is False:            
            x_0 = genfromtxt('./Dround_Data_New/Nomalized/deg_0_normalize.csv', delimiter=',', dtype=np.float32)
            x_45 = genfromtxt('./Dround_Data_New/Nomalized/deg_45_normalize.csv',delimiter=',', dtype=np.float32)
            x_90 = genfromtxt('./Dround_Data_New/Nomalized/deg_90_normalize.csv', delimiter=',', dtype=np.float32)
            x_135 = genfromtxt('./Dround_Data_New/Nomalized/deg_135_normalize.csv',delimiter=',', dtype=np.float32)
            x_180 = genfromtxt('./Dround_Data_New/Nomalized/deg_180_normalize.csv', delimiter=',', dtype=np.float32)
            x_225 = genfromtxt('./Dround_Data_New/Nomalized/deg_225_normalize.csv',delimiter=',', dtype=np.float32)
            x_270 = genfromtxt('./Dround_Data_New/Nomalized/deg_270_normalize.csv', delimiter=',', dtype=np.float32)
            x_315 = genfromtxt('./Dround_Data_New/Nomalized/deg_315_normalize.csv',delimiter=',', dtype=np.float32)
        elif test_data is True:            
            x_0 = genfromtxt('./Dround_Data_New/Nomalized_test/deg_0_normalize.csv', delimiter=',', dtype=np.float32)
            x_45 = genfromtxt('./Dround_Data_New/Nomalized_test/deg_45_normalize.csv',delimiter=',', dtype=np.float32)
            x_90 = genfromtxt('./Dround_Data_New/Nomalized_test/deg_90_normalize.csv', delimiter=',', dtype=np.float32)
            x_135 = genfromtxt('./Dround_Data_New/Nomalized_test/deg_135_normalize.csv',delimiter=',', dtype=np.float32)
            x_180 = genfromtxt('./Dround_Data_New/Nomalized_test/deg_180_normalize.csv', delimiter=',', dtype=np.float32)
            x_225 = genfromtxt('./Dround_Data_New/Nomalized_test/deg_225_normalize.csv',delimiter=',', dtype=np.float32)
            x_270 = genfromtxt('./Dround_Data_New/Nomalized_test/deg_270_normalize.csv', delimiter=',', dtype=np.float32)
            x_315 = genfromtxt('./Dround_Data_New/Nomalized_test/deg_315_normalize.csv',delimiter=',', dtype=np.float32)
        else:
            x_45 = genfromtxt('./Dround_Data_New/Nomalized_test/test_45_normalize.csv',delimiter=',', dtype=np.float32)
            data_matrix = np.array([x_45], np.float32)
            for i in range(0, 1):
                for j in range(0, len(x_45)):
                    "add one hot"
                    "add data"
                    self.label_set[i * len(x_45) + j] = self.onehot_encode(1)
                    self.data_set[i * len(x_45) + j] = data_matrix[i][j]

            return self.data_set, self.label_set


        data_matrix = np.array([x_0,x_45, x_90,x_135, x_180,x_225, x_270,x_315], np.float32)
        

        for i in range(0, self.num_angles):
            for j in range(0, self.data_per_angle):
                "add one hot"
                "add data"
                self.label_set[i * self.data_per_angle + j] = self.onehot_encode(i)
                self.data_set[i * self.data_per_angle + j] = data_matrix[i][j]

        return self.data_set ,self.label_set


