from glob import glob
"""
swithing ids in test/train/validation
"""
class_id_map ={
    0: "0",
    1: "1",
    2: "3",
    3: "4",
    4: "5",
    5: "2",
}
for txt_path in glob("AI/dataset/test/*.txt"):
    with open (txt_path,'r') as f:
        lines = f.readlines()
    res = ''
    for line in lines:
        line = line.strip()
        class_id, x_min, y_min, x_max, y_max =  line.split()
        class_id = class_id_map[int(class_id)]
        res += class_id + ' ' + x_min +' ' +  y_min + ' ' +  x_max + ' ' + y_max + '\n'
    with open (txt_path,'w') as f:
        f.write(res)
    