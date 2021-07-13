# https://www.ted.com/talks/alex_gendler_can_you_solve_the_bridge_riddle/transcript?language=en

# four persons
unit_time = {
    "y": 1,
    "a":2,
    "j":5,
    "p":10,
    "q":15
}

left = unit_time.keys()
# print(left)
right =[]
time=0
max_n_eles=2

def get_combinations(thearr, max_n_eles):
        import itertools
        # n_elements_arr=list(range(1, max_n_eles+1))
        results_arr=[]
        # for x in n_elements_arr:
        combinations_arr = list(itertools.combinations(thearr, max_n_eles))
        # print(combinations_arr)
        results_arr= results_arr +  combinations_arr
        return results_arr 

def move_once(elements_ls, fromplace_arr, toplace_arr ):
    time_thismove = 0
    # print("the elements are", elements_ls)
    for ele in elements_ls:
        # print('ele =', ele, 'unit time of the ele = ', unit_time[ele] )
        time_thismove= max(time_thismove , unit_time[ele])
        # print ('time_thismove so far: ', time_thismove)
        #remove the current ele from the left place
        if (ele in fromplace_arr):
            fromplace_arr = list(filter(lambda x:x != ele, fromplace_arr))
            # print('after moving, from:', fromplace_arr)
# # note: do not use .remove() 
# It could be very wrong as it changes the original value, for example
# c = ['a', 'b', 'c']
# d= c
# d.remove('b')
# # not only d's value is changed, but also c's value, although you might not want to change c's value
# e = list(filter(lambda x: x != 'b', d))
# print (e)                
            if not (ele in toplace_arr):
                toplace_arr = toplace_arr + [ele]
        # print('after moving, to:', toplace_arr)                
    return [fromplace_arr, toplace_arr, time_thismove]

def move(direction, fromplace_arr, toplace_arr, max_n_eles, time, left_aftermove, trys, cumusteps):
    # make an array with all move options (like, if left =['y','a','j','p'], the first move can be)
    # ['y','a'], or ['y', 'j'], or ['a', 'j'], etc 
    combinations_arr = get_combinations(fromplace_arr, max_n_eles)
    for elements_ls in combinations_arr:
        # remember the last step. We'll need to remeber that as everything running a different move option
        # we'll need to go back to where we started 
        fromplace_arr_laststep=fromplace_arr
        toplace_arr_laststep = toplace_arr
        direction_laststep = direction
        time_laststep = time
        cumusteps_last = cumusteps # this is for the historical moves from the first move up to this point
        left_beforemove = left_aftermove
        # print ('from ', fromplace_arr)
        # print ('move', direction, elements_ls )
        # print ('to', toplace_arr)

        # move one step, and get the changes 
        # like after moving ['y', 'a'] from ['y','a','j','p'] to [], we'll have
        # ['j', 'p'] on the from side, and  ['y', 'a'] on the to side, and it took 2 minutes to move ['y', 'a']
        # 2 minutes is the max time needed between the time need for 'y', and for 'a'
        move_results= move_once(elements_ls, fromplace_arr, toplace_arr)
        # # update the results
        fromplace_arr_aftermove = move_results[0]
        toplace_arr_aftermove = move_results[1]        
        time_thismove = move_results[2]          
        time = time + time_thismove
        # print('cumulative time used', time, 'minutes')

        # rememmber this step, and the cumulatative time used so far
        thisstep={
            "from":fromplace_arr, 
            "direction":direction, 
            "move":elements_ls, 
            "to":toplace_arr, 
            'time':time
            }
        # print(thisstep)

        # swap to and from for the next move
        # now we'll move someone to the opposite direction, so the previous from-place now becomes to-place,
        # while the previous to-place now the from-place.
        toplace_arr = fromplace_arr_aftermove
        fromplace_arr = toplace_arr_aftermove

        # redefine the move direction, and the number of persons to move
        # also, keep tracking the persons on the left side of the bridge
        if (direction == 'forth'):                
            direction = 'back'
            max_n_eles = 1
            left_aftermove = fromplace_arr_aftermove
        else:
            direction = 'forth'
            max_n_eles=2
            left_aftermove = toplace_arr_aftermove
                        
        # add the current step into the cumusteps
        cumusteps = cumusteps + [thisstep]

        # as long as there is still at least one person on the left side, recursively run the move module
        if (len(left_aftermove) >0):
            if (len(fromplace_arr)>0):                    
                trys = move(direction, fromplace_arr, toplace_arr, max_n_eles, time, left_aftermove, trys, cumusteps)   
        else: # otherwise (if the left side is empty, a complete pattern or a try has been done)
            # print("done")
            # now that the cumusteps contains all moves of the current try from the very first step to the last (last being that all person on the left are moved across the bridge to the right now)
            # push the cumusteps of this try to an array for recording all different tries. 
            trys=trys + [cumusteps]

        # before switching to a new choice other than in line 58, i.e., instead of moving
        # ['y','a'] from ['y','a','j','p'], chose to move ['a', 'j'] from ['y','a','j','p'] instead
        # to make this different try, we'll need to roll back to have persons on the left before moving
        fromplace_arr=fromplace_arr_laststep
        toplace_arr= toplace_arr_laststep  
        direction = direction_laststep  
        time = time_laststep  
        cumusteps=cumusteps_last
        left_aftermove = left_beforemove
    return trys

direction='forth'
fromplace_arr = left
toplace_arr = right
left_aftermove=left
trys =[]
cumusteps=[]
trys=move(direction, fromplace_arr, toplace_arr, max_n_eles, time, left_aftermove, trys, cumusteps) 
print ('Number of trys:', len(trys))

# find the shortest time
min_cumutime=9999
cumutime_trys = []
for tryx in trys:
    # for each tryx, find the cumulative time (the time recorded in the last element)
    lastpath = tryx[len(tryx)-1]
    # print(lastpath)
    cumutime = lastpath['time']
    cumutime_trys = cumutime_trys + [cumutime]
    min_cumutime = min(min_cumutime,cumutime )
print('the minumum time to spend is', min_cumutime, 'minutes')

# select records that are of the shortest time
i=0
besttrys=[]
for cumutime_eachtry in cumutime_trys:
    if (cumutime_eachtry == min_cumutime):
        besttrys = besttrys + [trys[i]]
    i=i+1
# print (besttrys)
# print(len(besttrys))

# now, list the best trys step by step
i=0
for eachtry in besttrys:
    i=i+1
    print("========best try", i)
    j=0
    for eachstep in eachtry:
        j=j+1
        print (j, "from", eachstep['from'], 'move', eachstep['direction'], eachstep['move'], 'to', eachstep['to'], "time used", eachstep['time'], "minutes.")

