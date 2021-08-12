import os


from pprint import pprint



def main():

        print '--- folders that can be removed from PATH ---'

        path = os.environ['PATH']
        folders = path.split(';')
        for folder in folders:
            exist = os.path.exists(folder)
            
            if not exist:
                print folder
            
            


if __name__=='__main__':
    main()