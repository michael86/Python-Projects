import sys
import functions as func

files = []
event_names = {}
new_events = []
options = ('-E', '-V', '-F', '-B')

if (len(sys.argv) - 1) == 0:
    func.show_help()
else:
    valid_arguments = True

    for i in range(len(sys.argv)):
        if not sys.argv[i] in options and i != 0:  # check i != 0 to ensure we don't try check the main.py arg
            func.show_help()
            valid_arguments = False

    if valid_arguments:  # Only entered if all args are valid.
        for i in range(len(sys.argv)):  # iterate for length of args
            if sys.argv[i] == '-E':
                files = func.get_items(files)
                event_names = func.get_events(files, event_names)
                func.write_file(files, event_names)
                if '-B' in sys.argv:
                    print('generating ban file')
                    func.generate_ban(event_names)
            elif sys.argv[i] == '-V':
                print('V')
            elif sys.argv[i] == '-F':
                print('F')
