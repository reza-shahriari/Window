from os.path import join,basename
from os import remove
from glob import glob
from  shutil import copy


main_src_path = '/home/reza/Vision/SoftWareDesign/CarDD_release/CarDD_release/CarDD_COCO/yolo_train'
if not main_src_path:
    main_src_path = input('Enter path to main folder...')
    
main_dst_path = '/home/reza/Vision/SoftWareDesign/CarDD_release/CarDD_release/CarDD_COCO/train2017'
if not main_dst_path:
    main_dst_path = input('Enter path to destionation folder...')

texts = glob(main_src_path+'/*.txt')

for txt in texts:
    name = basename(txt)
    copy(txt,join(main_dst_path,name))
    remove(txt)
