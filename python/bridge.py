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

        combinations_arr = get_combinations(fromplace_arr, max_n_eles)
        for elements_ls in combinations_arr:
            # remember the last step
            fromplace_arr_laststep=fromplace_arr
            toplace_arr_laststep = toplace_arr
            direction_laststep = direction
            time_laststep = time
            cumusteps_last = cumusteps
            # print ('from ', fromplace_arr)
            # print ('move', direction, elements_ls )
            # print ('to', toplace_arr)

            move_results= move_once(elements_ls, fromplace_arr, toplace_arr)
            # # update the results
            fromplace_arr_aftermove = move_results[0]
            toplace_arr_aftermove = move_results[1]        
            time_thismove = move_results[2]          
            time = time + time_thismove
            # print('cumulative time used', time, 'minutes')
            thisstep={
                "from":fromplace_arr, 
                "direction":direction, 
                "move":elements_ls, 
                "to":toplace_arr, 
                'time':time
                }
            # print(thisstep)
            # swap to and from for the next move
            toplace_arr = fromplace_arr_aftermove
            fromplace_arr = toplace_arr_aftermove

            if (direction == 'forth'):                
                direction = 'back'
                max_n_eles=1
                left_aftermove = fromplace_arr_aftermove
            else:
                direction = 'forth'
                max_n_eles=2
                left_aftermove = toplace_arr_aftermove

            cumusteps = cumusteps + [thisstep]

            if (len(left_aftermove) >0):
                if (len(fromplace_arr)>0):                    
                    trys = move(direction, fromplace_arr, toplace_arr, max_n_eles, time, left_aftermove, trys, cumusteps)   
            else:
                print("done")
                trys=trys + [cumusteps]

            # use back the settings in the last step
            fromplace_arr=fromplace_arr_laststep
            toplace_arr= toplace_arr_laststep  
            direction = direction_laststep  
            time = time_laststep  
            cumusteps=cumusteps_last
        return trys

direction='forth'
fromplace_arr = left
toplace_arr = right
max_n_eles =2
time=0
left_aftermove=[]
trys =[]
cumusteps=[]
trys=move(direction, fromplace_arr, toplace_arr, max_n_eles, time, left_aftermove, trys, cumusteps) 

print (len(trys))
for tryx in trys:
    print(tryx)
# select those with time <=17
# besttrys

 
