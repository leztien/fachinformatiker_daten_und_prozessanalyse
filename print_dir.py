def print_dir(directory, **kwargs):
    indent = kwargs.get('indent', 0)
    maxlen = kwargs.get('maxlen', 50)
    
    for e in listdir(directory):
        path = join(directory, e)
        if isfile(path):
            s = 'F'
        elif isdir(path):
            s = 'D'
        else:
            s = '?'
        print(' ' * indent + 
              "({}) {}"
              .format(s, e[:maxlen] + ('...' if len(e) > maxlen else '')))
        
        if isdir(path):
            print_dir(path, indent=indent + 3, maxlen=maxlen)
    print()



DIR = "/home/linux-ubuntu/Working/Folder"
print_dir(DIR)
