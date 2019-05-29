# Imports necessarios para execucao
import cv2
import csv
import glob
import numpy as np
from skimage import feature
import mahotas.features
import os
from scipy.stats import kurtosis, skew


def lbp(images, lbp_sampling_points, lbp_sampling_radius, method):
    eps = 1e-7

    csv.register_dialect('dial', delimiter=';')
    myFile = open('CSVs\\LBP_High.csv', 'w', newline="")  # High file
    writer = csv.writer(myFile, dialect='dial')
    myFile1 = open('CSVs\\LBP_Low.csv', 'w', newline="")  # Low file
    writer1 = csv.writer(myFile1, dialect='dial')

    row = []
    i = 0
    for img in images:
        lbp = feature.local_binary_pattern(img, lbp_sampling_points, lbp_sampling_radius, method=method)
        (hist, _) = np.histogram(lbp.ravel(), bins=np.arange(0, lbp_sampling_points + 3), range=(0, lbp_sampling_points + 2))
        hist = hist.astype("float")
        hist /= (hist.sum() + eps)
        row = list(hist)
        # high
        if i == 0:
            writer.writerow(row)
        # low
        if i == 1:
            writer1.writerow(row)
        row[:] = []
        i = i + 1
        print(row)

    myFile.close()
    myFile1.close()
