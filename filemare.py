# oh god oh fuck why

import sys
import os
import time
import string
import random

from pathlib import Path


timestamp = time.time()
args = sys.argv[1:]

if len(args) == 0:
    exit("Usage: python3 filemare.py <program_dir>")


program_dir = args[0]
program_dir_path = os.path.join(os.getcwd(), program_dir)
program_dir_list = os.listdir(program_dir_path)


outfile = f"output-{timestamp}.txt"
outfile_path = os.path.join(program_dir_path, outfile)


input_directory_path = os.path.join(program_dir_path, "input")
if not os.path.exists(input_directory_path):
    os.mkdir(input_directory_path)

data_directory = f"data-{timestamp}"
base_data_directory_path = os.path.join(program_dir_path, "data")
if not os.path.exists(base_data_directory_path):
    os.mkdir(base_data_directory_path)

data_directory_path = os.path.join(base_data_directory_path, data_directory)
os.mkdir(data_directory_path)
os.chdir(data_directory_path)


############
# Helper Functions
############


def exit(message):
    """
    Prints an error message and exits the program.
    """
    print(message)
    sys.exit(1)


def write_output(data):
    """
    Write data to the FileMare standard output (the output file lmao)
    """
    with open(outfile_path, "a+") as f:
        f.write(str(data))


def random_name(length = 10):
    """
    Returns a random filename for the data files
    """
    chars = string.ascii_uppercase + string.digits
    return "".join(random.choice(chars) for _ in range(length))


def create_files(count = 7):
    """
    Creates the specified amount of randomly named files
    at the current location.

    Default increment is 7 (this cannot be changed by the user)
    """
    for _ in range(count):
        current_val = get_value()
        if current_val >= 255:
            delete_files(current_val)
            continue

        with open(random_name(), "w") as f:
            pass


def delete_files(count = 3):
    """
    Deletes `count` random files from the current
    location.

    Default decrement is 3 (this cannot be changed by the user)
    """
    for _ in range(count):
        directory_list = os.listdir()

        if len(directory_list) == 0:
            create_files(255)
            continue

        filename = random.choice(directory_list)
        os.remove(filename)


def get_value():
    """
    Get the value of the current variable.

    If you're not in a variable data thing right now 
    this will return something very weird indeed.
    """
    return len(os.listdir())


def get_input():
    """
    Obtain input from the user
    """
    input_file = random_name() + ".txt"
    input_path = os.path.join(input_directory_path, input_file)
    with open(input_path, "w") as f:
        pass

    write_output(f"Please provide your input here: {input_path}")

    time.sleep(20)

    with open(input_path, "r") as f:
        data = f.read().strip()
        try:
            num = int(data)
            create_files(num)
        except:
            create_files(random.randint(0, 255))


def get_instructions(path, exclude = ["data", "input", outfile]):
    """
    Get the instructions in the given directory.
    Returns a dictionary { ins: type } where type can either be `file` or `dir`.
    """
    listing = []

    # Get all entries (files and directories) in the specified path
    with os.scandir(path) as entries:
        # Loop through the entries
        for entry in entries:
            # Remove the file extension from the name (for files)
            name = os.path.splitext(entry.name)[0] if entry.is_file() else entry.name

            # If the name is in the exclude list, skip it
            if any(exclusion in name for exclusion in exclude):
                continue

            # Get the creation time of the entry
            creation_time = os.path.getctime(entry.path)

            # Determine whether it's a file or a directory
            entry_type = 'file' if entry.is_file() else 'dir'

            # Add the entry to the listing as a dictionary
            listing.append({"instruction": name, "type": entry_type, "path": os.path.join(path, entry.name), "creation_time": creation_time})

    # Sort the listing by creation time
    sorted_listing = sorted(listing, key=lambda x: x['creation_time'])

    # Remove the 'creation_time' key from the final output
    return [{"instruction": item["instruction"], "type": item["type"], "path": item["path"]} for item in sorted_listing]


def get_file_data(path):
    """
    Returns the data inside the given file.
    """
    with open(path, "r") as f:
        return f.read().strip()


def eval_ins(instruction, data):
    match instruction:
        case "MKVAR":
            os.mkdir(data)
        
        case "CD":
            os.chdir(data)

        case "ADD":
            create_files()

        case "SUB":
            delete_files()

        case "WRITE":
            write_output(get_value())

        case "WRITE_CHAR":
            write_output(chr(get_value()))

        case "READ":
            get_input()


discovered_functions = {}


def eval_dir(path):
    instructions = get_instructions(path)
    for ins_entry in instructions:
        ins = ins_entry["instruction"]
        if ins_entry["type"] == "file":
            data = get_file_data(ins_entry["path"])

            if ins == "CALL":
                if data in discovered_functions.keys():
                    eval_dir(discovered_functions[data])
                else:
                    exit("You're calling a function that doesn't exist, wtf.")
            else:
                eval_ins(ins, data)
        elif ins_entry["type"] == "dir":
            if ins.startswith("LOOP_"):
                try:
                    itercount = int(ins.split("_")[1])
                    new_path = ins_entry["path"]
                    for _ in range(itercount):
                        eval_dir(new_path)
                except:
                    exit("You defined your loop to iterate a not-number amount of times...")
            elif ins.startswith("FUNCTION_"):
                name = ins.replace("FUNCTION_", "")
                discovered_functions[name] = ins_entry["path"]

eval_dir(program_dir_path)