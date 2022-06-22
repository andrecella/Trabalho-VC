import os
from natsort import natsorted

path=(r'C:\Andre\7ºSemestre\3-VISÃO COMPUTACIONAL\14º Aula 14-06-2022\Trabalho_garrafas\data\B_200cl')
os.chdir(path)
    
def rename_files(path, new_name, extension):
    os.chdir(path)
    for (i, filename) in enumerate(natsorted(os.listdir(path))):
      print (filename)
      os.rename(src=filename, dst='{}{}{}'.format(new_name,i,extension))
rename_files(r'C:\Andre\7ºSemestre\3-VISÃO COMPUTACIONAL\14º Aula 14-06-2022\Trabalho_garrafas\data\B_200cl','B_200cl','.JPG')


