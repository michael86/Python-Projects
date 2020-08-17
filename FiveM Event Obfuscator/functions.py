import random
import string
import codecs
import objects
import re
from os import path
from os import walk
from os.path import join, isfile
from pathlib import Path

root = 'resources'
obfuscated = 'obfuscated'


def get_items(files):
    for p, _, file_name in walk(root):
        for name in file_name:
            files.append(join(p, name))
    return files


def random_string(string_length=30):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(string_length))


def generate_path(directory):
    split_paths = (path.split(directory))  # 0 is path, 1 is file name
    resource_name = split_paths[0].partition('\\')  # split our path into a tuple.
    Path(obfuscated).mkdir(parents=True, exist_ok=True)  # Create obfuscated directory, in case deleted.
    resource_path = join(obfuscated, resource_name[2])
    Path(resource_path).mkdir(parents=True, exist_ok=True)  # Create new resource directory
    return join(resource_path, split_paths[1])


def get_events(files, event_names):
    for i in files:
        print(f'Reading {i}')
        if i.endswith('.lua'):
            with codecs.open(i, encoding='utf-8') as current:  # isfile(i) and i.endswith('.lua')
                lines = current.readlines()
                if lines:
                    for line in lines:
                        for event in objects.events:
                            contains = re.search(event, line)
                            if contains is not None:
                                if not event_names.__contains__(contains.group(1)):
                                    event_names[contains.group(1)] = random_string(30)
    return event_names


def write_file(files, event_names):

    for i in files:
        if isfile(i) and i.endswith('.lua'):
            f = open(generate_path(i), "a", encoding="utf-8")
            with codecs.open(i, encoding='utf-8') as current:
                lines = current.readlines()
                if lines:
                    lines = [s.replace('\r\n', '\r') for s in lines]  # Strip new line, due to having \r)
                    for line in lines:
                        fount = False
                        for event in objects.events:
                            contains = re.search(event, line)
                            if contains is not None:
                                if not contains.group(1) in objects.void_events:
                                    for old_event, new_event in event_names.items():
                                        if old_event in contains.group(1):
                                            print(f'Replacing {old_event} with {new_event}')
                                            fount = not fount
                                            line = line.replace(old_event, new_event).rstrip('\\n\\r')
                                            f.write(line)
                                            break
                        if not fount:
                            f.write(line)


def show_help():
    print('Valid options:\n'
          '-E: Obfuscate event names\n'
          #  '-F: obfuscate functions\n'
          #  '-V: obfuscate variables\n'
          '-B: Generate ban resource, needs to be used with -E\n'
          'Example: "python main.py -E -B" \n'
          'would obfuscate events, generate a new resource to ban when triggering old events\n')


def generate_ban(event_names):
    table = 'local events = {\n'
    with open(f'ban.lua', 'w+', encoding='utf-8') as f:
        for o, n in event_names.items():
            if o not in objects.void_events:
                table += f'\'{o}\',\n'
        table += '}\n\n' \
                 'for i=1, #events do\n' \
                 '  RegisterNetEvent(events[i])\n' \
                 '  AddEventHandler(events[i], function()\n' \
                 '  --TriggerBanEvent\n' \
                 '   end)\n' \
                 'end'
        f.write(table)
        f.close()
    print('Ban file generated')

