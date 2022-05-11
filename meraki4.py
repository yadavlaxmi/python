# Question 4

# Write a program remove the first key value pair from a nested dictionary.
# Example :-
# Input :-

#     Dic= {
#   1: 'NAVGURUKUL',
#   2: 'IN',  
#     3:{ 
#     'A' : 'WELCOME',
#     'B' : 'To',
#     'C' : 'DHARAMSALA'
#    }
#   }

# Visualize
# Output :-

# Dic= {
# 1: 'NAVGURUKUL',
# 2: 'IN',
# 3:
# { 'B' : 'To',
# 'C' : 'DHARAMSALA'
# }
# }


dic= {
    1: 'NAVGURUKUL',
    2: 'IN',  
    3:
        {'A' : 'WELCOME',
         'B' : 'To',
         'C' : 'DHARAMSALA'}
}
del dic[3]['A']
print(dic)
    