class TimeUnit:

    def __init__(self, hours, minutes, seconds, milliseconds) -> None:
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.milliseconds = milliseconds
        self.converted_time = None
        super().__init__()

    def convert_to_milliseconds(self):
        if self.converted_time is not None:
            return self.converted_time

        total_minutes = (self.hours * 60) + self.minutes
        total_secs = (total_minutes * 60) + self.seconds
        self.converted_time = total_secs * 1000 + self.milliseconds
        return self.converted_time


class SubsTimer:

    def __init__(self, timer: str) -> None:
        self.timer = timer
        time_arr_c = str(self.timer).split(",")
        self.milliseconds = 0
        if len(time_arr_c) == 2:
            self.milliseconds = int(time_arr_c[1].strip())

        time_arr_col = str(time_arr_c[0]).split(":")
        self.hours = int(time_arr_col[0].strip())
        self.minutes = int(time_arr_col[1].strip())
        self.seconds = int(time_arr_col[2].strip())
        super().__init__()

    def convert_to_milliseconds(self, value, unit):
        if unit == "S":
            return value * 1000
        elif unit == "M":
            return value * 60 * 1000
        elif unit == "H":
            return value * 60 * 60 * 1000
        return value

    def convert_current_time_to_milliseconds(self):
        total_minutes = (self.hours * 60) + self.minutes
        total_secs = (total_minutes * 60) + self.seconds
        total_ms = total_secs * 1000 + self.milliseconds
        return total_ms

    def convert_milliseconds_to_time(self, total_ms):
        self.milliseconds = total_ms % 1000
        total_seconds = int(total_ms / 1000)
        self.seconds = total_seconds % 60
        total_minutes = int(total_seconds / 60)
        self.minutes = total_minutes % 60
        self.hours = int(total_minutes / 60)

    def update_time(self, value, operation="+"):
        u_milli_seconds = value.convert_to_milliseconds(value, unit)
        curr_time_in_ms = self.convert_current_time_to_milliseconds()

        if operation == "+":
            updated_time = curr_time_in_ms + u_milli_seconds
        else:
            updated_time = curr_time_in_ms - u_milli_seconds
            if updated_time < 0:
                print("Current time in milliseconds: {} Difference to be updated in milliseconds: {}".format(
                    curr_time_in_ms, u_milli_seconds))
                raise Exception("Please give the correct time difference. "
                                "Difference cannot be greater than actual value")
        self.convert_milliseconds_to_time(updated_time)

    def __str__(self) -> str:
        return "{:02d}:{:02d}:{:02d},{:03d}".format(self.hours,
                                                    self.minutes, self.seconds, self.milliseconds)
