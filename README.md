# FileMergeSort

This is a simple Python program that reads integers from two different text files sorted from smallest to largest and merges the content of both files into a third file where all numbers are sorted in ascending order.

## Prerequisites
- Python 3.x installed.

## Files
- `numbers1.txt` - First input file containing sorted integers (one integer per line).
- `numbers2.txt` - Second input file containing sorted integers (one integer per line).

**Please make sure both input files are available in the same directory as the script.**

## Usage
- Run the Python file in the terminal using the command `python combined.py`

## What the program does

1. The program opens and reads from two existing files (`numbers1.txt` and `numbers2.txt`).
2. It creates a temporary list to produce a sorted list of numbers from both files.
3. It reads from the existing files and adds the numbers in no particular order to the temporary list.
4. It then sorts the numbers in the temporary list from smallest to largest.
5. It creates a third file `all_numbers.txt`.
6. It adds the sorted list of numbers to the new file.
7. Finally, it closes all the files.

## Output
The output is a text file `all_numbers.txt` that contains all the integers from both `numbers1.txt` and `numbers2.txt` sorted in ascending order. Each number is written on a new line.

**Note:** The existing `all_numbers.txt` file in the directory will be overwritten each time the program runs.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
