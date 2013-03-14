w_13 = -3
w_14 = 2
w_15 = 4
w_23 = 2
w_24 = -3
w_25 = 0.5
w_36 = 0.2
w_46 = 0.7
w_56 = 1.5

err_1 = 0
err_2 = 0
err_3 = 0
err_4 = 0
err_5 = 0
err_6 = 0

o_1 = 1
o_2 = 2
o_3 = 0.7311
o_4 = 0.0179
o_5 = 0.9933
o_6 = 0.8387

t_6 = 0
l = 10



### Calculate outpute layer error
err_6 = o_6*(1-o_6)*(t_6-o_6)



### Calculate Hidden layer errors
err_5 = o_5*(1-o_5)*(err_6*w_56)
err_4 = o_4*(1-o_4)*(err_6*w_46)
err_3 = o_3*(1-o_3)*(err_6*w_36)



### Update weights

w_13 = w_13 + l*err_3*o_1
w_14 = w_14 + l*err_4*o_1
w_15 = w_15 + l*err_5*o_1
w_23 = w_23 + l*err_3*o_2
w_24 = w_24 + l*err_4*o_2
w_25 = w_25 + l*err_5*o_2
w_36 = w_36 + l*err_6*o_3
w_46 = w_46 + l*err_6*o_4
w_56 = w_56 + l*err_6*o_5


print "w_13=", w_13
print "w_14=", w_14
print "w_15=", w_15
print "w_23=", w_23
print "w_24=", w_24
print "w_25=", w_25
print "w_36=", w_36
print "w_46=", w_46
print "w_56=", w_56

print "err_1=", err_1
print "err_2=", err_2
print "err_3=", err_3
print "err_4=", err_4
print "err_5=", err_5
print "err_6=", err_6



