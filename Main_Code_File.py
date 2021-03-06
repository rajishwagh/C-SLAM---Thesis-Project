from Three_robot_functions import cp_field_value, first_map_update, matching, get_level, all_good_values
from Three_robot_functions import motion_deciding_function, var_update, adj_field_value
from all_long_codes import robot1, robot2, robot3, robot4, robot5
import pygame, sys, copy
from pygame import *
from random import randint
import time

global real_map

map_choice = [0,0,0,0,0,0]

map_choice[2] = [[1,1,1,1,0,0,0,0,1,0,0,0,0,0,0,0],
                 [0,0,0,1,0,0,0,0,1,0,0,0,0,1,1,1],
                 [0,1,1,1,1,1,1,1,1,0,0,0,0,1,0,1],
                 [0,0,1,0,0,0,0,0,1,1,1,1,1,1,1,1],
                 [0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0],
                 [0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0],
                 [0,0,1,0,0,0,1,1,1,1,1,1,1,1,1,1],
                 [0,0,1,1,1,1,1,0,0,1,0,0,0,1,0,0],
                 [1,1,1,0,0,0,1,0,0,1,0,0,0,1,0,0],
                 [1,0,0,0,1,1,1,0,0,1,0,0,0,1,1,1],
                 [1,0,0,0,0,1,0,0,0,1,0,0,0,1,0,1],
                 [1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1],
                 [1,0,1,0,0,1,0,0,0,0,0,1,0,0,0,0],
                 [1,1,1,0,0,1,0,0,0,0,0,1,0,0,0,0],
                 [0,1,0,0,0,1,0,0,0,0,0,1,0,0,0,0],
                 [0,1,1,1,1,1,0,0,0,0,0,1,0,0,0,0]]

map_choice[0] = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                 [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                 [1,0,1,1,1,1,1,1,1,1,1,1,1,1,0,1],
                 [1,0,1,0,0,0,0,0,0,0,0,0,0,1,0,1],
                 [1,0,1,0,1,1,1,1,1,1,1,1,0,1,0,1],
                 [1,0,1,0,1,0,0,0,0,0,0,1,0,1,0,1],
                 [1,0,1,0,1,0,1,1,1,1,0,1,0,1,0,1],
                 [1,0,1,0,1,0,1,0,0,1,0,1,0,1,0,1],
                 [1,0,1,0,1,0,1,0,1,1,0,1,0,1,0,1],
                 [1,0,1,0,1,0,1,0,0,0,0,1,0,1,0,1],
                 [1,0,1,0,1,0,1,1,1,1,1,1,0,1,0,1],
                 [1,0,1,0,1,0,0,0,0,0,0,0,0,1,0,1],
                 [1,0,1,0,1,1,1,1,1,1,1,1,1,1,0,1],
                 [1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1],
                 [1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                 [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],]

map_choice[1] = [[1,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0],
                 [0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0],
                 [0,1,0,0,0,0,1,1,1,1,1,1,0,0,0,1],
                 [0,1,1,1,0,0,0,0,0,1,0,0,0,0,1,1],
                 [0,0,0,1,0,0,0,0,1,1,0,0,0,1,1,0],
                 [0,0,0,1,1,1,0,0,1,0,0,0,0,1,0,0],
                 [1,1,0,0,0,1,1,1,1,1,1,0,0,1,0,0],
                 [0,1,1,1,0,0,0,0,1,0,1,1,1,1,0,0],
                 [0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0],
                 [0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0],
                 [0,0,0,1,0,0,0,0,1,0,0,1,1,1,0,0],
                 [0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0],
                 [0,0,1,1,0,0,0,1,1,0,0,0,0,1,0,0],
                 [0,1,1,0,0,0,1,1,0,0,0,1,1,1,1,0],
                 [0,1,0,0,0,0,1,0,0,0,1,1,0,0,1,1],
                 [1,1,0,0,0,0,1,0,0,0,1,0,0,0,0,1]]

map_choice[3] = [[1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,1],
                 [0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1],
                 [0,0,0,0,0,1,0,0,0,0,1,1,1,1,1,1],
                 [0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1],
                 [1,1,1,1,1,1,0,0,0,0,1,0,0,0,0,1],
                 [1,0,0,0,0,1,1,1,1,1,1,0,0,0,0,1],
                 [1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1],
                 [1,0,0,0,0,1,0,0,0,0,1,1,1,1,1,1],
                 [1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1],
                 [1,0,0,0,0,1,1,1,1,1,1,0,0,0,0,1],
                 [1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0],
                 [1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0],
                 [1,1,1,1,1,1,0,0,0,0,1,0,0,0,1,0],
                 [1,0,0,0,0,1,0,0,0,0,1,0,0,0,1,0],
                 [1,0,0,0,0,1,0,0,0,0,1,0,0,0,1,0],
                 [1,0,0,0,0,1,1,1,1,1,1,1,1,1,1,0]]

map_choice[4] = [[0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1],
                 [0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1],
                 [0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1],
                 [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                 [0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1],
                 [0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1],
                 [0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1],
                 [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                 [0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1],
                 [0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1],
                 [0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1],
                 [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                 [0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1],
                 [0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1],
                 [0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1],
                 [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

map_choice[5] = [[1,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1],
                 [0,1,1,0,0,0,0,0,1,0,0,0,0,0,1,1],
                 [0,0,1,0,0,0,0,1,1,0,0,0,0,1,1,0],
                 [0,0,1,1,1,0,0,1,0,0,0,0,1,1,0,0],
                 [0,0,0,0,1,0,0,1,0,0,0,1,1,0,0,0],
                 [0,1,1,1,1,1,0,1,0,0,1,1,0,0,0,0],
                 [1,1,0,0,0,1,0,1,0,1,1,0,0,0,0,0],
                 [0,0,0,0,1,1,1,1,1,1,0,0,0,1,1,1],
                 [0,1,1,1,1,0,0,1,0,1,1,1,1,1,0,0],
                 [1,1,0,0,0,0,0,1,1,1,0,0,0,0,0,0],
                 [0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0],
                 [0,0,0,0,1,1,0,1,1,1,1,1,0,0,0,0],
                 [0,0,0,1,1,0,0,1,0,0,0,1,1,1,0,0],
                 [0,0,0,1,0,0,0,1,0,0,0,0,0,1,1,0],
                 [0,1,1,1,0,0,0,1,0,0,0,0,0,0,1,1],
                 [1,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1]]


def main():
    mapno = 0
    
    while True:
        try:
            choice = int(input("Please enter the map_choice: 0 through 5:"))
            real_map = map_choice[choice]
            mapno = choice
            break
        except NameError:
            print "Oops! That's a non-numerical character. Try again..."
        except :
            print "Oops! That's not between 0 and 5. Try again..."
    
#     while True:
#         try:
#             comp_var = int(input("Please enter the comp_var: 3 through 8:"))
#             break
#         except NameError:
#             print "Oops! That's a non-numerical character. Try again..."
#      
#     while True:
#         try:
#             percy = float(input("Please enter the percy: 60 to 95:"))
#             break
#         except NameError:
#             print "Oops! That's a non-numerical character. Try again..."
    while True:
        try:
            cyc = int(input("Please enter the number of cycles needed: 20 through 50:"))
            break
        except NameError:
            print "Oops! That's a non-numerical character. Try again..."
    start_time = time.time()
    list = [0]
    agv = all_good_values(real_map) # List of all Good Values
    list = agv[1]
#     pep1 = copy.deepcopy(agv[0])
#     pep2 = copy.deepcopy(agv[0])
#     pep4 = copy.deepcopy(agv[0])
#     pep3 = copy.deepcopy(agv[0])
    pep5 = copy.deepcopy(agv[0])
    #robot1(pep1, real_map, mapno)
    i = 5
    
    for j in range (4,10):
        robot5(pep5, list, real_map, i, (10*j), cyc, mapno)
        temptime = time.time() - start_time
        print "For AP = ", 10*j, "Time = ", temptime
        start_time = time.time()
     
#     comp_var = 5
#     percy = 60
#     robot2(pep2, list, real_map, comp_var, percy, cyc, mapno)
#     robot3(pep3, list, real_map, comp_var, percy, cyc, mapno)
#     robot4(pep4, list, real_map, comp_var, percy, cyc, mapno)
#     robot5(pep5, list, real_map, comp_var, percy, cyc, mapno)
    print "It ran all the iterations perfectly..."
    elapsed_time = time.time() - start_time
    print "In ", elapsed_time, " seconds."
    
if __name__ == "__main__":
    main()
