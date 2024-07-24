import numpy as np
import PlotSummaryDataRobinson as psdr
import OutputRobinsonDataExcel as orde
import RobinsonCode as rc

# ExampleUsingRobinsonCodeNew

# this sets the name of the outp[ut file. It stores the data for each of
# your tests so you'll need to call it something that indicates what
# experiment it is
# output_file='RobinsonTestExperimentTest1.mat'
output_file_xls = 'RobinsonTestExperimentTest1.xlsx'

# these parameters are for the first experiment
#
# probabilities of visiting each site from each other
# Default  probs = np.array([[0.91, 0.15, 0.03], [0.06, 0.8, 0.06], [0.03, 0.05, 0.91]])
probs = np.array([[0.76, 0.08, 0.08, 0.08],
                  [0.10, 0.82, 0.05, 0.05],
                  [0.09, 0.05, 0.82, 0.05],
                  [0.05, 0.05, 0.05, 0.82]])
#  original mean time to get between each nest
#time_means = np.array([[1, 46, 46, 56],
 #                      [46, 1, 80, 90],
  #                     [40, 80, 1, 90],
   #                    [56, 90, 90, 1]])
#modified mean time to get between each nest.
time_means = np.array([[1, 46, 46, 150],   # Increased the time taken to reach final site from site 1
                       [46, 1, 80, 150],   # Increased the time taken to reach final site from site 2
                       [40, 80, 1, 150],   # Increased the time taken to reach final site from site 3
                       [150, 150, 150, 1]]) # Increased the time taken to reach all other sites from the final site

# standard deviation of time to get between each nest
time_stddevs = time_means / 5

# mean quality of each nest. Note home is -infinity so it never gets picked
quals = np.array([-np.inf, 4, 6, 8])

# standard deviation of quality: essentially this controls
# how variable the ants assessment of each nest is. This is currently set
# as in the 1st experiment where the variability is the same for each nest
qual_stddev = np.array([1, 1, 1, 1])
# However, if you want to change is so nests perceived w different accuracy
# you could do eg qual_stddev = [1, 1, 4]

# set the number of ants
n = 1000 #increased the number of ants from 27 to 1000

# these govern the ant's threshold
threshold_mean = 7
threshold_stddev = 1

current_time, discovers, visits, accepts, Ants, rnd_seed, preqtimes, preqdiscovers, preqvisits, preqaccepts = \
    rc.RobinsonCode(n, quals, probs, threshold_mean, threshold_stddev, qual_stddev, time_means, time_stddevs, [], [])

# note: I have changed the order of saving data and plotting, as the matplotlib figure was blocking execution as long
# as it was open

# save the data as matlab variables - NOT IMPLEMENTED IN PYTHON
# save(output_file)

# save some of the data as excel
orde.OutputRobinsonDataExcel(output_file_xls, Ants, current_time, accepts, discovers, visits)

# Plot Summary data
psdr.PlotSummaryDataRobinson(current_time, accepts, discovers, visits, Ants)
