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





class bridge_riddle:

    def __init__ (self, left, right, time,max_n_eles, unit_time):
        self.left = left
        self.right= right
        self.time = time
        self.max_n_eles = max_n_eles
        self.unit_time = unit_time
        self.direction='forth'
        self.solution=[]
        self.lasteles=[]
        self.lasttime=0
        self.lastleft=left
        self.lastright=right
        self.trys = 1

   # have a collection of complete combiantions (up to 2 elements)
    def get_combinations(self, thearr, max_n_eles):
        import itertools
        n_elements_arr=list(range(1,max_n_eles+1))
        results_arr=[]
        for x in n_elements_arr:
            combinations_arr = list(itertools.combinations(thearr, x))
            # print(combinations_arr)
            results_arr= results_arr +  combinations_arr
        return results_arr 

    def move_once(self, elements_ls, fromplace_arr, toplace_arr ):
        time_thismove = 0
        for ele in elements_ls:
            time_thismove= max(time_thismove , self.unit_time[ele])
            #remove the current ele from the left place
            if (ele in fromplace_arr):
                fromplace_arr = list(filter(lambda x:x != ele, fromplace_arr))
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
        return [fromplace_arr, toplace_arr, time_thismove]

    def move(self):
        if self.trys < 10:
            if (self.direction == 'forth'):
                fromplace_arr = self.left
                toplace_arr = self.right
            else:
                fromplace_arr = self.right
                toplace_arr = self.left  
            # get all combinations from the left place
            # print ("direction =============", self.direction)
            combinations_arr = self.get_combinations(fromplace_arr, self.max_n_eles)
            # print ('there are ', len(combinations_arr), ' combinations from the fromplace')
            # special rule, for the first type, the length of elements_ls has to be 2
            if (len(combinations_arr)>0):
                for elements_ls in combinations_arr:
                    # print ('self trys', self.trys)
                    # print ('len elements_ls', len(elements_ls))
                    goahead=0
                    if (self.trys > 1):
                        goahead =1
                    elif (len(elements_ls)>1):
                        goahead= 1
                    else:
                        print('')
                        # print ('@@@none!')
                    if ( goahead == 1):
                        print ('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
                        self.trys=self.trys+1
                        # print ("the elements_ls: ", elements_ls)
                        # print ("length of the elements_ls: ", len(elements_ls))
            
                        if elements_ls != self.lasteles:
                            self.lasteles=elements_ls
                            print ('left ', self.left)
                            print ('move', self.direction, elements_ls )
                            print ('right', self.right)
                            move_results= self.move_once(elements_ls, fromplace_arr, toplace_arr)
                            # update the results
                            fromplace_arr_aftermove = move_results[0]
                            toplace_arr_aftermove = move_results[1]
                        
                            time_thismove = move_results[2]
                            
                            
                            self.lastdirection = self.direction 
                            self.lastleft = self.left
                            self.lastright = self.right
                            self.lasttime = self.time

                            self.time = self.time + time_thismove

                            if (self.direction == 'forth'):
                                self.left = fromplace_arr_aftermove
                                self.right = toplace_arr_aftermove
                                self.direction = 'back'
                            else:
                                self.right = fromplace_arr_aftermove
                                self.left = toplace_arr_aftermove 
                                self.direction = 'forth'
                            print ('after moving ')
                            print ('left ', self.left)
                            print ('right',self.right )
                            print('time used', self.time, 'minutes')
                            print ('==========')
                            if self.time <= 17:
                                tmp = [elements_ls, self.lastdirection, self.time]
                                # print('==============')
                                # print(tmp)
                                self.solution = self.solution + tmp
                                # keep going
                                if (len(toplace_arr_aftermove)>0):
                                    self.move()
                                else:
                                    print ("DONE!!!")
                            else:
                                print ('!!! time used > 17, rewind')
                                self.solution=[]
                                self.direction = self.lastdirection
                                self.left = self.lastleft
                                self.right = self.lastright
                                self.time = self.lasttime
                                self.move()            

xx = bridge_riddle(left, right, time, max_n_eles, unit_time)
# print (xx.left)
# print (xx.move(('p', 'j'), left, right))
xx.move()




 