f = open('D:/3d_printing/assess/ip.txt', 'r')
x = f.readlines();
a=int(x[0])-1;
b=int(x[1])-1;
c=int(x[2])-1;
d=int(x[3])-1;

F1 = open('D:/3d_printing/assess/ip.txt','w')
F1.write(str(a));F1.write("\n");
F1.write(str(b)); F1.write("\n");
F1.write(str(c)); F1.write("\n");
F1.write(str(d));

print (a );
print (b );
print (c);
print (d);