"""
Given the participants' score sheet, you are required to find the runner-up
score. You are given n scores. Store them in a list and find the score of the
runner-up.

"""
#for the interpreter
if __name__ == '__main__ ' :

    #get user input as an integer and assign to n
    n = int (input())

    #split a string into array of parts
    # return the new array called arr
    
    arr = map(int, input().split())

    #convert arr to list and get set 
    arr_y = set(list (arr))

    #convert set to list
    arr_z = list(arr_y)

    #get length of list arr_z
    len_arr = len(arr_z)

    #sort using sorted and get second last elem  [-2]
    #print(sorted(arr_z)[len_arr -2])
    arr_x = sorted(arr_z)
    
    print(arr_x[len_arr -2])
    


