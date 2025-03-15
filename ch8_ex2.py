def my_head(filename, num_lines, output_file=None):
    """Replicates the Linux head command in python"""

    reader = open(filename) # opens the file and reads it

    writer = None
    if output_file: #opens output file for writing
        writer = open(output_file, 'w')

    for i in range(num_lines):
        line = reader.readline()
        if not line: #stops at end of file
            break

        if writer:     # gives us options, to either write it or print it
            writer.write(line)
        else:
            print(line.strip())

    reader.close()
    if writer:
        writer.close()


