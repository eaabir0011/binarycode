mark=input('Give me your marks I will provide the result:')
marks=int(mark)
if 0<=marks<=32:
    print('F Grade')
elif 33<= marks <=40:
    print('D Grade')
elif 41<=marks<=50:
    print('C grade')
elif 51<= marks <=60:
    print('B grade')
elif 61<=marks<=70:
    print('A- Grade')
elif 71<= marks <80:
    print('A Grade')
elif 80<= marks<=100:
    print('A+ Grade')
else:
    print('Not Under grading System')