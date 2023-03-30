# Dataset Creator for NanoGPT

This is a Python script that extracts text from one or more EPUB files and writes the text to a CSV file, which can be used to train a language model like NanoGPT.

## Requirements

* Python 3.6 or later
* ebooklib library (`pip install ebooklib`)
* CSV library (`pip install csv`)

## Usage

1. Clone this repository to your local machine.
2. Install the required libraries listed above.
3. Place your EPUB files in a directory on your local machine.
4. Modify the `books_dir` variable in `create_dataset.py` to point to the directory containing your EPUB files.
5. Run the `create_dataset.py` script using the command `python create_dataset.py`.
6. The script will create a new file called `books_text.csv` in the same directory as `create_dataset.py`. This file will contain the text extracted from the EPUB files.

## Contributing

If you find any issues with the script or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License

This script is released under the [MIT License](https://opensource.org/licenses/MIT).

