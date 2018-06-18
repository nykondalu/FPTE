import numpy
e=0.01
post_perovskite=[[2.4723811499996495,  0.0000000000000000,  0.0000000000000000],
                 [1.2361905749998248,  4.0498106311729405,  0.0000000000000000],
                 [0.0000000000000000,  0.0000000000000000,  6.1356913942619702]]

unity=numpy.array([[1, 0, 0],
      [0 , 1, 0],
      [0 , 0, 1]])

d1=[[1+e, 0, 0],
    [0  , 1, 0],
    [0  , 0, 1]]

d2=[[1  , 0, 0],
    [0  , 1+e, 0],
    [0  , 0, 1]]

d3=[[1  , 0, 0],
    [0  , 1, 0],
    [0  , 0, 1+e]]

d4=[[1/((1-e**2)**(1/3)), 0.00000000000000000, 0.00000000000000000],
    [0.00000000000000000, 1/((1-e**2)**(1/3)), e/((1-e**2)**(1/3))],
    [0.00000000000000000, e/((1-e**2)**(1/3)), 1/((1-e**2)**(1/3))]]


d5=[[1/((1-e**2)**(1/3)), 0.00000000000000000, e/((1-e**2)**(1/3))],
    [0.00000000000000000, 1/((1-e**2)**(1/3)), 0.00000000000000000],
    [e/((1-e**2)**(1/3)), 0.00000000000000000, 1/((1-e**2)**(1/3))]]

d6=[[1/((1-e**2)**(1/3)), e/((1-e**2)**(1/3)), 0.00000000000000000],
    [e/((1-e**2)**(1/3)), 1/((1-e**2)**(1/3)), 0.00000000000000000],
    [0.00000000000000000, 0.00000000000000000, 1/((1-e**2)**(1/3))]]

numd6=numpy.array([[1/((1-e**2)**(1/3)), e/((1-e**2)**(1/3)), 0.00000000000000000],
    [e/((1-e**2)**(1/3)), 1/((1-e**2)**(1/3)), 0.00000000000000000],
    [0.00000000000000000, 0.00000000000000000, 1/((1-e**2)**(1/3))]])

d7=[[(1+e)/((1-e**2)**(1/3)), 0.000000000000000000000, 0.00000000000000000],
    [0.000000000000000000000, (1-e)/((1-e**2)**(1/3)), 0.00000000000000000],
    [0.000000000000000000000, 0.000000000000000000000, 1/((1-e**2)**(1/3))]]

d8=[[(1+e)/((1-e**2)**(1/3)), 0.00000000000000000, 0.000000000000000000000],
    [0.000000000000000000000, 1/((1-e**2)**(1/3)), 0.000000000000000000000],
    [0.000000000000000000000, 0.00000000000000000, (1-e)/((1-e**2)**(1/3))]]


d9=[[1/((1-e**2)**(1/3)), 0.000000000000000000000, 0.000000000000000000000],
    [0.00000000000000000, (1+e)/((1+e**2)**(1/3)), 0.000000000000000000000],
    [0.00000000000000000, 0.000000000000000000000, (1-e)/((1-e**2)**(1/3))]]

print(numd6-unity)
print()

#
# numpy.matmul(d1, post_perovskite)
# a=0
# for i in [d1, d2, d3, d4, d5, d6, d7, d8, d9]:
#     a+=1
#     with open('POSCAR'+str(a),'a+') as f:
#
#         # f.write(' '.join(map(str,numpy.matmul(d1, post_perovskite))))
#         # (numpy.matmul(d1, post_perovskite)).strip('[,]'))
#         f.write(' Mg Si O                                                     '+'\n')
#         f.write('    1.00000000000000                                         '+'\n')
#         f.write('\n'.join(' '.join(str(cell) for cell in row) for row in numpy.matmul(i, post_perovskite))+'\n')
#         # f.write('\n')
#         f.write('    Mg   Si   O                                              '+'\n')
#         f.write('    2    2    6                                              '+'\n')
#         f.write('Direct                                                       '+'\n')
#         f.write('   0.7469239890883586  0.5061520218232616  0.2500000000000000'+'\n')
#         f.write('   0.2530760109116414  0.4938479781767384  0.7500000000000000'+'\n')
#         f.write('   0.0000000000000000  0.0000000000000000  0.0000000000000000'+'\n')
#         f.write('   0.0000000000000000  0.0000000000000000  0.5000000000000000'+'\n')
#         f.write('   0.0733163031647734  0.8533673936704460  0.2500000000000000'+'\n')
#         f.write('   0.9266836968352266  0.1466326063295540  0.7500000000000000'+'\n')
#         f.write('   0.3639887016191494  0.2720225967617154  0.4408192873872139'+'\n')
#         f.write('   0.6360112983808577  0.7279774032382846  0.5591806826127907'+'\n')
#         f.write('   0.6360112983808577  0.7279774032382846  0.9408193173872093'+'\n')
#         f.write('   0.3639887016191494  0.2720225967617154  0.0559210962607147'+'\n')