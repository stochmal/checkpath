import os


from pprint import pprint

COPYRIGHT = 'Copyright (C) 2021 Tomasz Stochmal<stochmal@gmail.com>\nhttps://github.com/stochmal/checkpath/blob/main/LICENSE\n'

def main():

        print(COPYRIGHT)

        print('--- folders that can be removed from PATH ---')

        path = os.environ['PATH']
        folders = path.split(';')
        for folder in folders:
            exist = os.path.exists(folder)
            
            if not exist:
                print(folder)
            
            


if __name__=='__main__':
    main()