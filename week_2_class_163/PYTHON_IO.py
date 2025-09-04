# how to open nowadays
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
with open(f'{dir_path}/secrets.txt','a', encoding = 'utf-8') as f:
    f.write('\nBla for real')
    print('Content was added')



dir_path = os.path.dirname(os.path.realpath(__file__))
with open(f'{dir_path}/Star_Wars.txt','r', encoding = 'utf-8') as f:
    file_content = f.read()
    print(file_content)