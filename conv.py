'''
     - - - - - -- - - - - - - - - - - - - - - - - - - - - - -
    Name - - CNN - Convolution Neural Network For Photo Recognizing
    Goal - - Recognize Handing Writting Word Photo
    Detail：Total 5 layers neural network
            * Convolution layer
            * Pooling layer
            * Input layer layer of BP
            * Hiden layer of BP
            * Output layer of BP
    
    - - - - - -- - - - - - - - - - - - - - - - - - - - - - -
          '''


    
    from __future__ import print_function

    import numpy as np 
    import matplotlib.pyplot as plt 

    class CNN():

        def __init__(self,conv1_get,size_p1,bp_num1,bp_num2,bp_num3,rate_w=0.2,rate_t=0.2):
                '''
                :param conv1_get: [a,c,d], size, number, step of convolutional network
                :param size_p1: pooling size
                :param bp_num1: units number of flatten layer
                :param bp_num2: units number of hidden layer
                :param bp_num3: units number of output layer
                :param rate_w: rate of weight learning
                :param rate_t: rate of threshold learning
                '''    

                self.bp_num1 = bp_num1
                self.bp_num2 = bp_num2
                self.bp_num3 = bp_num3
                self.conv1 = conv1_get[:2]
                self.step_conv1 = conv1_get[2]
                self.size_pooling1 = size_p1
                self.rate_weight = rate_w
                self.rate_thre = rate_t
                self.w_conv1 = [np.mat(-1*np.random.rand(self.conv1[0], self.conv1[0])+0.5) for i in range(self.conv1[1])]
                self.wkj = np.mat(-1 * np.random.rand(self.num_b3, self.num_b2) + 0.5)
                self.vji = np.mat(-1 * np.random.rand(self.num_b2, self.num_b1) + 0.5)
                self.thre_conv1 = -2 * np.random.rand(self.conv1[1]) + 1
                self.thre_bp2 = -2*np.random.rand(self.num_b2) + 1
                self.thre_bp3 = -2*np.random.rand(self.num_b3) + 1


        def save_model(self, save_path):
                    #save model dict with pickle

                    import pickle
                    model_dic = {'num_bp1':self.num_bp1,
                                 'num_bp2':self.num_bp2,
                                 'num_bp3':self.num_bp3,
                                 'conv1':self.conv1,
                                 'step_conv1':self.step_conv1,
                                 'size_pooling1':self.size_pooling1,
                                 'rate_weight':self.rate_weight,
                                 'rate_thre':self.rate_thre,
                                 'w_conv1':self.w_conv1,
                                 'wkj':self.wkj,
                                 'vji':self.vji,
                                 'thre_conv1':self.thre_conv1,
                                 'thre_bp2':self.thre_bp2,
                                 'thre_bp3':self.thre_bp3}

                    with open(save_path, 'wb') as f:
                        pickle.dump(model_dic, f)

                    print('Model saved: %s'% save_path)
                    
                @classmethod
                def ReadModel(cls,model_path):
                    #read saved model
                    import pickle
                    with open(model_path, 'rb') as f:
                        model_dic = pickle.load(f)

                    conv_get = model_dic.get('conv1')
                    conv_get.append(model_dic.get('step_conv1'))
                    size_p1 = model_dic.get('size_pooling1')
                    bp1 = model_dic.get('num_bp1')
                    bp2 = model_dic.get('num_bp2')
                    bp3 = model_dic.get('num_bp3')      
                    r_w = model_dic.get('rate_weight')
                    r_t = model_dic.get('rate_thre')   
                    #create model instance
                    conv_ins = CNN(conv_get, size_p1,bp1,bp2,bp3,r_w,r_t)
                    #modify model parameter
                    conv_ins.w_conv1 = model_dic.get('w_conv1')
                    conv_ins.wkj = model_dic.get('wkj')
                    conv_ins.vji = model_dic.get('vji')
                    conv_ins.thre_conv1 = model_dic.get('thre_conv1')
                    conv_ins.thre_bp2 = model_dic.get('thre_bp2')
                    conv_ins.thre_bp3 = model_dic.get('thre_bp3')
                    return conv_ins

                
                def sig(self, x):
                        return 1 / (1 + np.exp(-1 * x))

                
                def do_round(self, x):
                                return round(x, 3)


                def convolute(self, data, convs, w_convs, thre_convs, conv_step):
                    #convolution process
                    size_conv                            

