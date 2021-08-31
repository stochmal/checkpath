'''main module'''
import os


COPYRIGHT = 'Copyright (C) 2021 Tomasz Stochmal <stochmal@gmail.com>'
LICENSE = 'https://github.com/stochmal/checkpath/blob/main/LICENSE'

def main():
    '''main functiom'''
    print(COPYRIGHT)
    print(LICENSE)
    print()

    if os.name == 'nt':
        separator = ';'
    else:
        separator = ':'
    print("os name:", os.name, "use", separator)

    print()
    print('--- folders that can be removed from PATH ---')

    path = os.environ['PATH']
    folders = path.split(separator)
    for folder in folders:
        exist = os.path.exists(folder)

        if not exist:
            print(folder, '\t*** FOLDER NOT FOUND ***')
        else:
            files = os.listdir(folder)
            if len(files)==0:
                print(folder, '\t*** FOLDER IS EMPTY ***')

if __name__=='__main__':
    main()
