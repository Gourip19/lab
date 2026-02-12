import csv
file='training.csv'
with open(file,'r') as f:
 data=list(csv.reader(f))
 headers=data[0]
 concepts=[row[:-1] for row in data[1:]]
 target=[row[-1] for row in data[1:]]
hypothesis=['?' for _ in range(len(concepts[0]))]
for i, val in enumerate(concepts):
 if target[i]=='Yes':
 if hypothesis[0]=='?':
 hypothesis=val.copy()
 else:
 for j in range(len(hypothesis)):
 if hypothesis[j]!=val[j]:
 hypothesis[j]='?'
print('Final Hypothesis:',hypothesis)
Output :
Final Hypothesis: ['Sunny', 'Warm', 'High', 'Strong', 'Cold', 'Change']