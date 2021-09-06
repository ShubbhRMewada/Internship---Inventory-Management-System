import json

f=open(r"C:\Users\NND\PycharmProjects\pythonProject\venv\DataSet.json","r")

str1=f.read()

pyt_data = json.loads(str1)

print(pyt_data)

f.close()

l=0

for i in pyt_data.keys():

    for j in pyt_data[i]:

        for k in pyt_data[i][j]:

            pyt_data[i][j][k][1]=100

json_obj=json.dumps(pyt_data,indent=2)

with open(r'C:\Users\NND\PycharmProjects\pythonProject\venv\DataSet.json','w') as file:

    file.write(json_obj)

    file.close()