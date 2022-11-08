#!/usr/bin/env python
# coding: utf-8

# -*- coding: utf-8 -*-
"""
CS 351 - Artificial Intelligence 
Assignment 3

Student 1(Name and ID): Shahzaib Amir - sa05578
Student 2(Name and ID): Muhammad Saad - ms05496

"""

import random
import math
import numpy as np
import matplotlib.pyplot as pl



def initializePoints(count):
    points = []
    for i in range(int(count/3)):
        points.append([random.gauss(0,10),random.gauss(100,10)])
    for i in range(int(count/3)):
        points.append([random.gauss(-30,20),random.gauss(10,10)])
    for i in range(int(count/3)):
        points.append([random.gauss(30,20),random.gauss(10,10)])

    return points



def cluster(points,K,visuals = True):
    
    centroids = random.sample(points, K)
    centroid0 = centroids[0]
    centroid1 = centroids[1]
    centroid2 = centroids[2]
    delta_centroid0 = 1000 ## 1000 2D points for 3 sets of points (as K = 3)
    delta_centroid1 = 1000
    delta_centroid2 = 1000
    while ((delta_centroid0) >= 0.1 or (delta_centroid1 >= 0.1) or (delta_centroid2 >= 0.1)):
        clusters, cluster0, cluster1, cluster2 = ([] for i in range(4))
        for value in points:
            distance_cluster0 = math.sqrt(((value[0] - centroid0[0])**2) + ((value[1] - centroid0[1])**2))
            distance_cluster1 = math.sqrt(((value[0] - centroid1[0])**2) + ((value[1] - centroid1[1])**2))
            distance_cluster2 = math.sqrt(((value[0] - centroid2[0])**2) + ((value[1] - centroid2[1])**2))
            closest_distance = min(distance_cluster0, distance_cluster1, distance_cluster2)
            
            if (closest_distance == distance_cluster0):
                cluster0.append(value)
            elif (closest_distance == distance_cluster1):
                cluster1.append(value)
            elif (closest_distance == distance_cluster2):
                cluster2.append(value)

        clusters.append(cluster0)
        clusters.append(cluster1)
        clusters.append(cluster2)
        
        if (visuals == True):
            pl.scatter(*zip(*cluster0), color = 'blue')
            pl.scatter(*zip(*cluster1), color = 'green')
            pl.scatter(*zip(*cluster2), color = 'red')
            pl.scatter(*zip(*centroids), color = 'black')
            pl.show()

        
        temp_centroid0 = centroid0
        temp_centroid1 = centroid1
        temp_centroid2 = centroid2
        
        temp = 0
        sum_x = 0
        sum_y = 0
        while (temp < len(cluster0)):
            sum_x += cluster0[temp][0]
            sum_y += cluster0[temp][1]
            temp += 1

        average_cluster0_x = sum_x / len(cluster0)
        average_cluster0_y = sum_y / len(cluster0)

        temp = 0
        sum_x = 0
        sum_y = 0
        while (temp < len(cluster1)):
            sum_x += cluster1[temp][0]
            sum_y += cluster1[temp][1]
            temp += 1
        
        average_cluster1_x = sum_x / len(cluster1)
        average_cluster1_y = sum_y / len(cluster1)

        temp = 0
        sum_x = 0
        sum_y = 0
        while (temp < len(cluster2)):
            sum_x += cluster2[temp][0]
            sum_y += cluster2[temp][1]
            temp += 1
        
        average_cluster2_x = sum_x / len(cluster2)
        average_cluster2_y = sum_y / len(cluster2)

        centroid0 = [average_cluster0_x, average_cluster0_y]
        centroid1 = [average_cluster1_x, average_cluster1_y]
        centroid2 = [average_cluster2_x, average_cluster2_y]
        delta_centroid0 = abs(centroid0[0] - temp_centroid0[0]) + abs(centroid0[1] - temp_centroid0[1])
        delta_centroid1 = abs(centroid1[0] - temp_centroid1[0]) + abs(centroid1[1] - temp_centroid1[1])
        delta_centroid2 = abs(centroid2[0] - temp_centroid2[0]) + abs(centroid2[1] - temp_centroid2[1])

        centroids = []
        centroids.append(centroid0)
        centroids.append(centroid1)
        centroids.append(centroid2)
        
    clusters.append(centroids)
    
    return clusters



def clusterQuality(clusters):
    score = -1
    final_scores = []
    for i in range(10): ##running K-means 10 times as asked in part c
        cluster = clusters[i]
        cluster0 = cluster[0]
        cluster1 = cluster[1]
        cluster2 = cluster[2]
        centroids = cluster[3]
        centroid0 = centroids[0]
        centroid1 = centroids[1]
        centroid2 = centroids[2]

        sum_cluster0, sum_cluster1, sum_cluster2, temp = [0 for i in range(4)]

        ##Accessing 3 lists of clustered points to calculate the total score and find the best K-means iteration
        while (temp < len(cluster0)):
            sum_cluster0 += ((cluster0[temp][0] - centroid0[0])**2) + ((cluster0[temp][1] - centroid0[1])**2)
            temp += 1

        temp = 0
        
        while (temp < len(cluster1)):
            sum_cluster1 += ((cluster1[temp][0] - centroid1[0])**2) + ((cluster1[temp][1] - centroid1[1])**2)
            temp += 1

        temp = 0
        while (temp < len(cluster2)):
            sum_cluster2 += ((cluster2[temp][0] - centroid2[0])**2) + ((cluster2[temp][1] - centroid2[1])**2)
            temp += 1

        total = sum_cluster0 + sum_cluster1 + sum_cluster2
        final_scores.append(total)
    counter = np.argmin(final_scores) ## To find the best K-means cluster
    score = min(final_scores)
    print("The best K-means cluster:", counter + 1)
    return score
    

def keepClustering(points,K,N,visuals):
    clusters = []
    for i in range(10): #10 iterations of K-means (N = 10)
        print("No of Iterations: ", i + 1)
        repeated_clusters = cluster(points, K, False)
        clusters.append(repeated_clusters)

        if (visuals == True):
            pl.scatter(*zip(*repeated_clusters[0]), color = 'blue')
            pl.scatter(*zip(*repeated_clusters[1]), color = 'green')
            pl.scatter(*zip(*repeated_clusters[2]), color = 'red')
            pl.scatter(*zip(*repeated_clusters[3]), color = 'black')
            pl.show() 

    return clusters
    

K = 3
N = 10
points = initializePoints(1000)
clusters = keepClustering(points,K,N,True)
print ("The score of best Kmeans clustering is:", clusterQuality(clusters))

