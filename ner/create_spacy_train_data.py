# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-

input_file = '/home/823892/Desktop/invoice.txt'
output_file = '/home/823892/Desktop/invoice_train.txt'

with open(input_file) as f:
    content = f.readlines()

content = [x.strip() for x in content] 



inv = ['KUL0001563701' , '142622' , '9401000814' , '020151' , 'AE20170207-01' , 'KUL0001563700' , '8013599' , '1428141' , 'KUL0001533622' , '5912623' , '21210' , '30023743' , '30021994' , 'KUL0001538047' , '5912624' , '05024P' , 'KUL0001538041' , '30023576' , 'BT5840005811' , 'A04948' , '5910255' , '80640' , '5910256' , '8012742' , 'KUL0001529089' , 'CORPCARDFEB22' , '142814' , '5910257' , 'IV-24721' , 'IV-24522' , 'JFC18544' , 'AE20170208-01']
#inv = ['142622' , '020151' , '8013599' , '1428141' , '5912623' , '21210' , '30023743' , '30021994' , '5912624' , '050241' , '30023576' ,'5910255' , '80640' , '5910256' , '8012742' , '142814' , '5910257']

new_content = []

#    
for i in inv :
    for x in content:
        new_x = x.replace('1234', i) 
        start = new_x.index (i)
        end = start + len (i) + 1
        new_line = "(\"" + new_x + "\", {'entities': [(" + str (start ) + " , " + str (end) + ", 'INVOICE')] }),"
        new_content.append (new_line)

f= open(output_file,"w+")
f.write (str(new_content))
f.close()

