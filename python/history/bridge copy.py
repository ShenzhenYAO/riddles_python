# https://www.ted.com/talks/alex_gendler_can_you_solve_the_bridge_riddle/transcript?language=en

# four persons
unit_time = {
    "y": 1,
    "a":2,
    "j":5,
    "p":10
}

left = ["y", "a", "j", "p"]
right =[]
time=0


# the job is to move elements from the left collection to the right collection.
# the rules:
# each time up to two elements can be moving
# the unit_time move each element is accumulated into the variable 'time'
# all elements in the left collection must be moved to the right within 17 minutes

# analysis of the riddle.
#############################################################################################
#part A: always start with the dumbest way. 
# 1. have a collection of complete combinations (up to 2 elements for each combination)
#        of the elements in the left place collection
#       (e.g, ya, y, yj, etc. Note that ya is the same as ay)
# 2. loop for combinations in the collection from step 1.
#   2a. select a combitnation
#   2b. move the selected combination into the right place collection
#   2c. remove it from the left place
#   2d. acculumate time corresponding to the unit time of the element(s) in the selected combination
#       e.g., if ya is the selected combination, then time = unit_time["y"] + unit_time["a"]
#   2e, if time > 17, skip the current combination selected by 2a, and goto the next combination in the loop 
#   2f. have a collection of complet combinations (up to 2 elements for each combination)
#        of the elements in the right collection (similar to the approach as in step 1)
#   2g. loop for combinations in the collection by 2d
#       2ga, select a combination (by order of the combinations in the collection by 2d)
#       2gb, skip the combination of 2fa, if it is the same as 2a. (i.e., do not repeatedly move the same elements from one place to another)      
#       2gc, accumulate time correspoonding to the unit time of the elements in
#           the selected combination by 2fa
#       2gd, if time > 17, skip the current combination selected by 2fa, and goto the next combination in the loop 
########and that's it!

# need to develop a function to have a collection of complete combiantions (up to 2 elements)
def get_combinations(thelist, n_elements_arr):
    import itertools
    results_arr=[]
    for x in n_elements_arr:
        combinations_arr = list(itertools.combinations(thelist, x))
        # print(combinations_arr)
        results_arr=results_arr +  combinations_arr
    return results_arr

#n_elements=[1,2]
#get_combinations(left, n_elements)

# 1. have a combination of all elements in the left place
def eachmove(left, right, time):
    n_elements=[1,2]
    keepgoing = 0
    comb_left_arr=[]
    if (len(left)>0):
        comb_left_arr = get_combinations(left, n_elements)
        # print(comb_left_arr)
    # 2. loop for each combination in comb_left_arr
    for thiscomb_ls in comb_left_arr:
        print("moving", thiscomb_ls)
    #   2a. select a combitnation (which is a list like ('yr',) or ('y', 'a'))
        # accumulate the time
        for ele in thiscomb_ls:
            time = max(time , unit_time[ele])
        print ("time spent: ", time)
    #   2b. move the selected combination into the right place collection
        if time <=17:
            keepgoing = 1
            for ele in thiscomb_ls:
                # print(ele)
                # print(right)
                if not (ele in right):
                    right = right + [ele]
                    # print("right", right)
                    #2c. remove the current ele from the left place
                    left.remove(ele)
                    # print("left", left)
            if (len(left)>0):
                results_newmove=eachmove(right, left, time)
                keepgoing = results_newmove[3]
                if (keepgoing ==1):
                    left = results_newmove[0]
                    right = results_newmove[1]
                    time = results_newmove[2]
            else:
                keepgoing=0
                print ("done")            
        else:
            # print ('Opps, time is up! Need retry')
            keepgoing = 0
        if (keepgoing==1):
            print ("left", left)
            print ("right", right)
        return [left, right, time, keepgoing]
eachmove(left, right, 0)

#   2d. acculumate time corresponding to the unit time of the element(s) in the selected combination
#       e.g., if ya is the selected combination, then time = unit_time["y"] + unit_time["a"]
#   2e, if time > 17, skip the current combination selected by 2a, and goto the next combination in the loop 
#   2f. have a collection of complet combinations (up to 2 elements for each combination)
#        of the elements in the right collection (similar to the approach as in step 1)
#   2g. loop for combinations in the collection by 2d
#       2ga, select a combination (by order of the combinations in the collection by 2d)
#       2gb, skip the combination of 2fa, if it is the same as 2a. (i.e., do not repeatedly move the same elements from one place to another)      
#       2gc, accumulate time correspoonding to the unit time of the elements in
#           the selected combination by 2fa
#       2gd, if time > 17, skip the current combination selected by