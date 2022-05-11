
# Q8.Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters. Go to the editor
# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Uppercase characters : 3
# No. of Lower case Characters : 12




def fun():
    string="The quick Brow Fox"
    count=0
    count1=-3
    i=0
    while i<len(string):
        if string[i]==" ":
            count+=1
        else:
            count1+=1
        i+=1
    print(count)
    print(count1)
fun()
        