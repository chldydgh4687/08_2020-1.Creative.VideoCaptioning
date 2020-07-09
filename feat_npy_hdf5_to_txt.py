import glob
import numpy as np
import h5py

# key 0 : vgg features npy files.
# key 1 : inceptionv4 features hdf5 file.

key = 1

if key == 0 :

    f1 = open('vgg_feat_train.txt','w')
    f2 = open('vgg_feat_val.txt','w')
    f3 = open('vgg_feat_test.txt','w')

    for i, feat_name in enumerate(sorted(glob.glob("./Features_VGG/*.npy"))):
        np_data = np.load(feat_name)
        print(feat_name)
        for j in range(len(np_data)):
            print("vid%d_frame_%d transform.." % (i+1, j+1))
            print(np_data[j,:].shape)
            d1 = "vid%d_frame_%d," % (i+1,j+1)
            d2 = ','.join(map(str,np_data[j,:]))
            data = d1 + d2 + '\n'
            if i < 1200:
                f1.write(data)
            elif i < 1300:
                f2.write(data)
            else:
                f3.write(data)

    f1.close()
    f2.close()
    f3.close()

elif key == 1:

    f1 = open('inceptionv4_feat_train.txt', 'w')
    f2 = open('inceptionv4_feat_val.txt', 'w')
    f3 = open('inceptionv4_feat_test.txt', 'w')

    with h5py.File('MSVD_InceptionV4old.hdf5','r') as ff:
        for vid, c in enumerate(sorted(ff.keys())):
            for frame, feat in enumerate(ff[c]):
                print("vid%d_frame_%d transform.." % (vid+1, frame+1))
                print(feat.shape)
                d1 = "vid%d_frame_%d," % (vid + 1, frame + 1)
                d2 = ','.join(map(str, feat))
                data = d1 + d2 + '\n'
                if vid < 1200:
                    f1.write(data)
                elif vid < 1300:
                    f2.write(data)
                else:
                    f3.write(data)

        f1.close()
        f2.close()
        f3.close()