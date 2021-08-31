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
    print('os name is', os.name, 'use', separator, 'separator')

    print()
    print('--- folders that can be removed from PATH are marked *** ---')
    print()

    path = os.environ['PATH']
    folders = path.split(separator)
    folders.sort()
    for folder in folders:
        exist = os.path.exists(folder)

        if not exist:
            print('*** FOLDER NOT FOUND', '\t', folder)
        else:
            files = os.listdir(folder)
            if len(files)==0:
                print('*** FOLDER IS EMPTY', '\t', folder)
            else:
                print('%6d' % len(files), "files found", '\t', folder)

if __name__=='__main__':
    main()
