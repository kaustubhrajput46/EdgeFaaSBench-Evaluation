#!/usr/bin/env python3

import argparse
from conc_func.concurrency_rpi import *
from conc_func.get_ab_readings import *
from graphs_rpi.create_graphs import *
from conc_func.get_cpu_mem_readings import *

def main():



    app_name_list = [
#    "image-classification-alexnet-cpu",
    "image-classification-with-cpu",
    "sentiment-analysis",
    "matrix-multiplication-high",
#    "iperf3",
#    "image-classification-with-cuda",
#    "object-classification-yolo-no-gpu",
#    "image-processing-pillow",
#    "floating-point-operation-cosine",
    "fast-fourier-transform",
#    "matrix-multiplication-medium",
#    "dd-cmd",
#    "object-classification-yolo-gpu",
#    "floating-point-operation-sine",
#    "speech-to-text",
#    "sorter",
#    "image-classification-alexne-gpu",
#    "matrix-multiplication-low",
#    "floating-point-operation-sqrt",
    ]

#    device = "NANO";
    device = "RPI";
    print("Heyy you")

    for appname in app_name_list:
        #path_where_the_ab_output_files_present = "../cold_warm_start_AB/{0}/NANO".format(appanme)
#        path_where_the_ab_output_files_present = "../cold_warm_start_AB/{0}/RPI".format(appanme)

        # sample invoke
#        get_average_cold_warm_values_in_csv(path_where_the_ab_output_files_present, appanme)

    	# This function will be used to capture the required concurrecny related data we got from the apache benchmark output which will be stored in csv file.
    	get_required_values_from_all_ab_output("./{1}/{0}/ab_output/".format(appname, device), appname)
    
    	print("got all the ab outputs")
    	# This function will be used to capture the required concurrecny related data we got from the cpu_mem output csv files which will be stored in single csv file.
    	get_required_values_from_all_cpu_mem_output("./{1}/{0}/cpu_mem_output/".format(appname, device), appname)
    
    	print("got all mem cpu outputs")
    	# This function will create ab readings graphs in ./concurrency/appname/ folder with appname_ab_op_rpi.pdf name
    	create_ab_graph_from_csv("./{1}/{0}/ab_output/{0}_ab_readings.csv".format(appname, device), appname)

    	print("created ab graphs from csv")
    	# This function will create cpu_mem graphs in ./concurrency/appname/ folder with appname_cpu_mem_op.pdf name
    	create_cpu_mem_graphs_from_csv("./{1}/{0}/cpu_mem_output/{0}_cpu_mem_readings.csv".format(appname, device), appname)

    	print("created mem cpu graphs from csv") #remove
    
    print("Done") #remove
    

# calling the main function
if __name__=='__main__':
    main()