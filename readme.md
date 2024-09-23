## FileMare
> The most fun fun programming language ever! Definitely not a night**mare** to work with... (hah)

**FileMare** is a filesystem based programming language. You must create a new directory for your program, and use files inside that directory for instructions!

To create instructions, you must create files with the names of the instructions you want to use! To pass data to them, simply write the desired data inside the file.

Instructions are executed based on the timestamps of file creation, so chronologically.

---

### Working with Data
Working with data is of course very simple with FileMare! Data is stored in a filesystem format. You need to move around this filesystem to manipulate the data you want to change. Here's an example of some data that was stored:

```
- program/
  - var_num3/
    - 328947324.txt
    - 123890748.txt
    - 387924347.txt
  - var_num1/
    - 509392228.txt
```

This example data shows two variables, containing the numbers **3** and **1** respectively. Since FileMare is an ultra-modern language, numbers are all 8-bit.

See the instruction table below on how to traverse your data and how to manipulate it.

### Loops
Loops are super simple in FileMare. All you need to do is make a directory to contain your instructions, simple as that! See the table below for how to do this.

### Functions
FileMare is a high-level and high-iq language so of course it has support for defining your own functions. Just create a directory for your function and it's instructions, and you're good to go. Call the function as shown below.

### I/O
Input and output handling is quite the quirky feature in FileMare. Ouput is always written to a file, `output-{timestamp}.txt`. 

As for input, upon requesting input, the user has 20 seconds to write the desired data into a file. After this time has elapsed, the file will be read and the input will be used. If no data is present, a random 8-bit integer will be selected instead!

---

## Instructions

### Files

These are the file-based instructions available to you:

| Instruction | Operand(s) | Description |
| --- | --- | --- |
| MKVAR | \<name> | Creates a directory to house your variable |
| CD | \<path> | Traverse your data filesystem |
| ADD | --- | Adds 7 to the current data you are writing (by creating 7 randomly named files in the current data directory, make sure you know where you are!) |
| SUB | --- | Subtracts 3 from the current data you are writing |
| WRITE | --- | Writes the current variable to the program output |
| WRITE_CHAR | --- | Writes the current variable as a character to the program output |
| READ | --- | Prompts the user for input, overrides the data directory you are currently writing with this value. |
| CALL | \<name> | Call a function |

### Directories

And these are the directory-based instructions available to you:

| Instruction | Description |
| --- | --- |
| LOOP_\<itercount> | Runs the instructions inside that directory `itercount` times. |
| FUNCTION_\<name> | Creates a function with the specified name. Function arguments are not a thing, so you'll need to know what pieces of data your function requires and make sure to write them *before* calling the function! |

## Running FileMare

In order to run **FileMare** (why do you want to do that??), simply download the python code from here and run it with `python3 filemare.py <program_dir>`.

### Disclaimers
Some disclaimers: as you are literally working with code that deletes and creates files on your system, be careful with this power, as you can (probably?) mess and up ruin things you don't want to ruin. The python program running your code is changing directories as you say to create and read data. Good luck and have fun using **FileMare**!

### Reserved Words
Do not use these words in your file / directory names:
- `output-{timestamp}` (timestamp being the timestamp execution starts, it will be overwritten)
- `data`
- `input`