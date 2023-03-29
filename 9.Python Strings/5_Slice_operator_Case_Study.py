s = 'abcdefghij'

s[1:6:2] # begin to end - 1 , 1 to 5 , every 2nd char => bdf
s[::1] # start to end => abcdefghij
s[::-1] # end to start => jihgfedcba
s[3:7:-1] # backward direction , begin to end + 1 , 3 to 8 => empty string
s[7:4:-1] # backward direction , begin to end + 1 , 7 to 5 => hgf
s[0:10000:1] # forward direction , 0 to 9999 , Index not avalible , but no index error in slice operator => abcdefghij
s[-4:1:-1] # backward direction , begin to end + 1 , -4 to 2 => gfedc
s[-4:1:-2] # backward direction , begin to end + 1 , -4 to 2 with step as -2 => g gec
s[5:0:1] # forward direction with end value 0 => empty string
s[9:0:0] # we can't identify the direction as step value is zero => value error.
s[0:-10:-1] # backward direction , begin to end + 1 , 0 to -9 , start value is zero => empty string.
s[0:-11:-1] # backward direction , begin to end + 1 , 0 to -10 =>  a 
s[0:0:1] # empty
s[0:-9:-2] # backward direction , begin to end + 1 , 0 to -8 => empty string.
s[-5:-9:-2] # backward direction , begin to end + 1 , -5 to -8 , step 2 => fd
s[10:-1:-1] # backward direction , begin to end + 1 , -1 to 11 , end atribute is -1 => empty
s[10000:2:-1] # backward direction , begin to end + 1 , 10000 to 3 , step -1 => jihgfed