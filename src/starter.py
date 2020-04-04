from src.SubsTimer import SubsTimer, TimeUnit
import traceback


time_diff = TimeUnit(hours=1, minutes=17, seconds=57, milliseconds=341)
operation = "-"
input_file = "/home/nandha/Videos/12_Angry_men.srt"
output_file = "/home/nandha/Videos/myOutFile.srt"

TIMELINE_SEPARATOR = " --> "


def get_converted_time_line(_line):
    if TIMELINE_SEPARATOR not in line_str:
        return _line, False

    try:
        timeline_arr = str(_line).split(TIMELINE_SEPARATOR)
        start_time = timeline_arr[0]
        start = SubsTimer(start_time)
        start.update_time(time_diff, operation)
        end_time = timeline_arr[1]
        end = SubsTimer(end_time)
        end.update_time(time_diff, operation)
        updated_line = "{}{}{}".format(start, TIMELINE_SEPARATOR, end)
        return updated_line, True
    except Exception as exp:
        print(exp)
        print(traceback.format_exc())
        return _line, False


outF = open(output_file, "w")
with open(input_file) as fp:
    line = fp.readline()

    while line:
        line_str = str(line)
        content, need_new_line = get_converted_time_line(line_str)
        outF.write(content)
        if need_new_line:
            outF.write("\n")

        line = fp.readline()

outF.close()

print("Update completed")
