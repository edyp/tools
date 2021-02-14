import re, sys
from datetime import timedelta

total_execution_time_sec = 0

def count_execution_time(seconds):
    global total_execution_time_sec
    total_execution_time_sec += seconds

def warning_value(number):
    if number > 10:
        return '\033[31;1m'
    else:
        return '\033[7m'

def substract_timestaps_from_log(log_name):
    global total_execution_time_sec
    with open(log_name, 'r') as log:
        lines = log.readlines()
        timestamps = [re.match(r'^[0-9]{10}', s) for s in lines]
        grouped_lines = [re.split(r'^[0-9]{10} : ', x) for x in lines]

        for i in reversed(range(len(timestamps))):
            if not timestamps[i]:
                del timestamps[i]
                del grouped_lines[i]

        new_log_name = log_name[:-4] + '_substracted_timestamps.txt'
        with open(new_log_name, 'w') as writer:
            for i in range(len(timestamps)):
                if i == 0:
                    writer.write(lines[i])
                else:
                    substracted_timestaps = int(timestamps[i].group(0)) - int(timestamps[i - 1].group(0))
                    count_execution_time(substracted_timestaps)
                    writer.write("{2}{0:+}\033[0m\t{1}".format(
                        substracted_timestaps,
                        grouped_lines[i][1],
                        warning_value(substracted_timestaps)))
            writer.write("{0} - total execution time from timestamps.".format(str(timedelta(seconds=total_execution_time_sec))))

    return new_log_name

def main():
    files_list = sys.argv[1:]

    for filename in files_list:
        try:
            file_with_substracted_timestamps = substract_timestaps_from_log(filename)
            print("File with substracted timestamps:", file_with_substracted_timestamps)

        except:
            print("I can't process file", filename)

if __name__ == '__main__':
    main()
