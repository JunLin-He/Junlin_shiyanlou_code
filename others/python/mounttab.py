import os

def parse_mounts():
    '''
    Analyse /proc/mounts and return the list of tuple
    '''
    result = []

    if os.path.exists('/proc/mounts'):
        fd = open('/proc/mounts')
        for line in fd:
            line = line.strip() # clear empty
            words = line.split()
            if len(words) > 5:
                res = (words[0], words[1], words[2], '({})'.format(' '.join(words[3:-2])))
            else:
                res = (words[0], words[1], words[2])
        fd.close()
    return result

def mount_details():
    '''
    Print detail message of mount
    '''
    result = parse_mounts()
    for line in result:
        if len(line) == 4:
            print('{} on {} type {} {}'.format(*line))
        else:
            print('{} on {} type {}'.format(*line))


if __name__ == '__main__':
    mount_details()



