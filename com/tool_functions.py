import os, sys, time

def display_clear():
    # This is the URL that this code was found on:
    # http://www.delftstack.com/howto/python/python-clear-console/
    """
    clears console
    """
    command = 'clear'
    if os.name in (
        'nt', 'dos'):
            command = 'cls'
    os.system(command)

def type_slowly(text): #https://stackoverflow.com/a/10390877
            for i in text:
                sys.stdout.write(i)
                sys.stdout.flush()
                time.sleep(0.02)