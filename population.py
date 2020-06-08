def get_list(list_data) :
    import csv
    file = open('population_2020.csv','r',encoding='utf-8')
    lines = csv.reader(file)

    header = next(lines)
    
    list_temp = []
    for line in lines :
        list_temp.append(line[:])
        
    for j in range(7):
        temp = []
        for i in range(len(list_temp)):
            temp.append(list_temp[i][j])
        list_data.append(temp)
          
def get_dict(list_data,keys,dict_data):
    area =get_area(list_data[0])
    dict_data.update({keys[0]:area})
    
    for i in range(1,7):
        if i == 3 or i == 6 :
            data = del_comma(list_data[i],'float')
        else:
            data = del_comma(list_data[i],'integer')
            
def get_area(data):
    temp = []
    for x in data:
        arr = x.split()
        temp.append(arr[0])
        
    return temp

def del_comma(data,t):
    temp = []
    for x in data :
        string = ''
        arr = x.split(',')
        for i in range(len(arr)) :
            string += arr[i]
        if t == 'integer' :
            temp.append(int(string))
        else :
            temp.append(float(string))
    return temp