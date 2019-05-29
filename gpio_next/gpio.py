#!/usr/bin/env python
# -*- coding:utf-8 -*-

from ctypes import cdll, c_int, c_uint, c_long, c_char_p, c_void_p, Structure, POINTER, pointer


# struct timespec {
#    time_t   tv_sec;
#    long     tv_nsec;
# }
class timespec(Structure):
    _fields_ = [("tv_sec", c_long), ("tv_nsec", c_long)]


# struct gpiod_line_event {
# 	struct timespec ts;
# 	/**< Best estimate of time of event occurrence. */
# 	int event_type;
# 	/**< Type of the event that occurred. */
# };
class gpiod_line_event(Structure):
    _fields_ = [("ts", timespec), ("event_type", c_int)]



lib = None


def get_lib():
    global lib

    if lib:
        return lib

    try:
        lib = cdll.LoadLibrary('libgpiod.so.1')
    except OSError:
        raise OSError('libgpiod.so.1 is not found, try `apt install libgpiod1`')

    # /**
    #  * @brief Open a gpiochip by number.
    #  * @param num Number of the gpiochip.
    #  * @return GPIO chip handle or NULL if an error occurred.
    #  *
    #  * This routine appends num to '/dev/gpiochip' to create the path.
    #  */
    # struct gpiod_chip *gpiod_chip_open_by_number(unsigned int num) GPIOD_API;
    lib.gpiod_chip_open_by_number.argtypes = [c_uint]
    lib.gpiod_chip_open_by_number.restype = c_void_p

    # /**
    #  * @brief Close a GPIO chip handle and release all allocated resources.
    #  * @param chip The GPIO chip object.
    #  */
    # void gpiod_chip_close(struct gpiod_chip *chip) GPIOD_API;
    lib.gpiod_chip_close.argtypes = [c_void_p]
    lib.gpiod_chip_close.restype = None


    # /**
    #  * @brief Get the handle to the GPIO line at given offset.
    #  * @param chip The GPIO chip object.
    #  * @param offset The offset of the GPIO line.
    #  * @return Pointer to the GPIO line handle or NULL if an error occured.
    #  */
    # struct gpiod_line *
    # gpiod_chip_get_line(struct gpiod_chip *chip, unsigned int offset) GPIOD_API;
    lib.gpiod_chip_get_line.argtypes = [c_void_p, c_uint]
    lib.gpiod_chip_get_line.restype = c_void_p

    # /**
    #  * @brief Retrieve a set of lines and store them in a line bulk object.
    #  * @param chip The GPIO chip object.
    #  * @param offsets Array of offsets of lines to retrieve.
    #  * @param num_offsets Number of lines to retrieve.
    #  * @param bulk Line bulk object in which to store the line handles.
    #  * @return 0 on success, -1 on error.
    #  */
    # int gpiod_chip_get_lines(struct gpiod_chip *chip,
    # 			 unsigned int *offsets, unsigned int num_offsets,
    # 			 struct gpiod_line_bulk *bulk) GPIOD_API;
    # lib.gpiod_chip_get_lines.argtypes = [c_void_p, c_void_p, c_uint, c_void_p]
    # lib.gpiod_chip_get_lines.restype = c_int


    # /**
    #  * @brief Reserve a single line, set the direction to input.
    #  * @param line GPIO line object.
    #  * @param consumer Name of the consumer.
    #  * @return 0 if the line was properly reserved, -1 on failure.
    #  */
    # int gpiod_line_request_input(struct gpiod_line *line,
    # 			     const char *consumer) GPIOD_API;
    lib.gpiod_line_request_input.argtypes = [c_void_p, c_char_p]
    lib.gpiod_line_request_input.restype = c_int

    # /**
    #  * @brief Reserve a single line, set the direction to output.
    #  * @param line GPIO line object.
    #  * @param consumer Name of the consumer.
    #  * @param default_val Initial line value.
    #  * @return 0 if the line was properly reserved, -1 on failure.
    #  */
    # int gpiod_line_request_output(struct gpiod_line *line,
    # 			      const char *consumer, int default_val) GPIOD_API;
    lib.gpiod_line_request_output.argtypes = [c_void_p, c_char_p, c_int]
    lib.gpiod_line_request_output.restype = c_int

    # /**
    #  * @brief Read current value of a single GPIO line.
    #  * @param line GPIO line object.
    #  * @return 0 or 1 if the operation succeeds. On error this routine returns -1
    #  *         and sets the last error number.
    #  */
    # int gpiod_line_get_value(struct gpiod_line *line) GPIOD_API;
    lib.gpiod_line_get_value.argtypes = [c_void_p]
    lib.gpiod_line_get_value.restype = c_int


    # /**
    #  * @brief Read current values of a set of GPIO lines.
    #  * @param bulk Set of GPIO lines to reserve.
    #  * @param values An array big enough to hold line_bulk->num_lines values.
    #  * @return 0 is the operation succeeds. In case of an error this routine
    #  *         returns -1 and sets the last error number.
    #  *
    #  * If succeeds, this routine fills the values array with a set of values in
    #  * the same order, the lines are added to line_bulk. If the lines were not
    #  * previously requested together, the behavior is undefined.
    #  */
    # int gpiod_line_get_value_bulk(struct gpiod_line_bulk *bulk,
    # 			      int *values) GPIOD_API;


    # /**
    #  * @brief Set the value of a single GPIO line.
    #  * @param line GPIO line object.
    #  * @param value New value.
    #  * @return 0 is the operation succeeds. In case of an error this routine
    #  *         returns -1 and sets the last error number.
    #  */
    # int gpiod_line_set_value(struct gpiod_line *line, int value) GPIOD_API;
    lib.gpiod_line_set_value.argtypes = [c_void_p, c_int]
    lib.gpiod_line_set_value.restype = c_int


    # /**
    #  * @brief Set the values of a set of GPIO lines.
    #  * @param bulk Set of GPIO lines to reserve.
    #  * @param values An array holding line_bulk->num_lines new values for lines.
    #  * @return 0 is the operation succeeds. In case of an error this routine
    #  *         returns -1 and sets the last error number.
    #  *
    #  * If the lines were not previously requested together, the behavior is
    #  * undefined.
    #  */
    # int gpiod_line_set_value_bulk(struct gpiod_line_bulk *bulk,
    # 			      const int *values) GPIOD_API;
    # lib.gpiod_line_set_value_bulk.argtypes = [c_void_p, c_void_p]
    # lib.gpiod_line_set_value_bulk.restype = c_int


    # /**
    #  * @brief Request rising edge event notifications on a single line.
    #  * @param line GPIO line object.
    #  * @param consumer Name of the consumer.
    #  * @return 0 if the operation succeeds, -1 on failure.
    #  */
    # int gpiod_line_request_rising_edge_events(struct gpiod_line *line,
    # 					  const char *consumer) GPIOD_API;
    lib.gpiod_line_request_rising_edge_events.argtypes = [c_void_p, c_char_p]
    lib.gpiod_line_request_rising_edge_events.restype = c_int


    # /**
    #  * @brief Request falling edge event notifications on a single line.
    #  * @param line GPIO line object.
    #  * @param consumer Name of the consumer.
    #  * @return 0 if the operation succeeds, -1 on failure.
    #  */
    # int gpiod_line_request_falling_edge_events(struct gpiod_line *line,
    # 					   const char *consumer) GPIOD_API;
    lib.gpiod_line_request_falling_edge_events.argtypes = [c_void_p, c_char_p]
    lib.gpiod_line_request_falling_edge_events.restype = c_int


    # /**
    #  * @brief Request all event type notifications on a single line.
    #  * @param line GPIO line object.
    #  * @param consumer Name of the consumer.
    #  * @return 0 if the operation succeeds, -1 on failure.
    #  */
    # int gpiod_line_request_both_edges_events(struct gpiod_line *line,
    # 					 const char *consumer) GPIOD_API;
    lib.gpiod_line_request_both_edges_events.argtypes = [c_void_p, c_char_p]
    lib.gpiod_line_request_both_edges_events.restype = c_int

    # /**
    #  * @brief Wait for an event on a single line.
    #  * @param line GPIO line object.
    #  * @param timeout Wait time limit.
    #  * @return 0 if wait timed out, -1 if an error occurred, 1 if an event
    #  *         occurred.
    #  */
    # int gpiod_line_event_wait(struct gpiod_line *line,
    # 			  const struct timespec *timeout) GPIOD_API;
    lib.gpiod_line_event_wait.argtypes = [c_void_p, POINTER(timespec)]
    lib.gpiod_line_event_wait.restype = c_int


    # /**
    #  * @brief Wait for events on a set of lines.
    #  * @param bulk Set of GPIO lines to monitor.
    #  * @param timeout Wait time limit.
    #  * @param event_bulk Bulk object in which to store the line handles on which
    #  *                   events occurred. Can be NULL.
    #  * @return 0 if wait timed out, -1 if an error occurred, 1 if at least one
    #  *         event occurred.
    #  */
    # int gpiod_line_event_wait_bulk(struct gpiod_line_bulk *bulk,
    # 			       const struct timespec *timeout,
    # 			       struct gpiod_line_bulk *event_bulk) GPIOD_API;
    # lib.gpiod_line_event_wait_bulk.argtypes = [c_void_p, POINTER(timespec), c_void_p]
    # lib.gpiod_line_event_wait_bulk.restype = c_int

    # /**
    #  * @brief Read the last event from the GPIO line.
    #  * @param line GPIO line object.
    #  * @param event Buffer to which the event data will be copied.
    #  * @return 0 if the event was read correctly, -1 on error.
    #  * @note This function will block if no event was queued for this line.
    #  */
    # int gpiod_line_event_read(struct gpiod_line *line,
    # 			  struct gpiod_line_event *event) GPIOD_API;
    lib.gpiod_line_event_read.argtypes = [c_void_p, POINTER(gpiod_line_event)]
    lib.gpiod_line_event_read.restype = c_int

    
    # /**
    #  * @brief Get the event file descriptor.
    #  * @param line GPIO line object.
    #  * @return Number of the event file descriptor or -1 if the user tries to
    #  *         retrieve the descriptor from a line that wasn't configured for
    #  *         event monitoring.
    #  *
    #  * Users may want to poll the event file descriptor on their own. This routine
    #  * allows to access it.
    #  */
    # int gpiod_line_event_get_fd(struct gpiod_line *line) GPIOD_API;
    lib.gpiod_line_event_get_fd.argtypes = [c_void_p]
    lib.gpiod_line_event_get_fd.restype = c_int

    # /**
    #  * @brief Read the last GPIO event directly from a file descriptor.
    #  * @param fd File descriptor.
    #  * @param event Buffer in which the event data will be stored.
    #  * @return 0 if the event was read correctly, -1 on error.
    #  *
    #  * Users who directly poll the file descriptor for incoming events can also
    #  * directly read the event data from it using this routine. This function
    #  * translates the kernel representation of the event to the libgpiod format.
    #  */
    # int gpiod_line_event_read_fd(int fd, struct gpiod_line_event *event) GPIOD_API;
    lib.gpiod_line_event_read_fd.argtypes = [c_int, POINTER(gpiod_line_event)]
    lib.gpiod_line_event_read_fd.restype = c_int

    return lib


# class Input(object):
#     def __init__(self, pin, chip=0):
#         self.lib = get_lib()
#         self.chip = self.lib.gpiod_chip_open_by_number(chip)
#         self.line = self.lib.gpiod_chip_get_line(self.chip, pin)
#         self.name = 'in{}'.format(pin).encode()
#         self.lib.gpiod_line_request_input(self.line, self.name)

#     def __call__(self):
#         return self.lib.gpiod_line_get_value(self.line)

#     def read(self):
#         return self.lib.gpiod_line_get_value(self.line)


class Output(object):
    def __init__(self, pin, chip=0, default_value=0):
        self.lib = get_lib()
        self.chip = self.lib.gpiod_chip_open_by_number(chip)
        self.line = self.lib.gpiod_chip_get_line(self.chip, pin)
        self.name = 'out{}'.format(pin).encode()
        self.lib.gpiod_line_request_output(self.line, self.name, default_value)

    def __call__(self):
        return self.lib.gpiod_line_get_value(self.line)

    def read(self):
        return self.lib.gpiod_line_get_value(self.line)

    def write(self, value):
        self.lib.gpiod_line_set_value(self.line, value)



class Input(object):
    def __init__(self, pin, chip=0):
        self.lib = get_lib()
        self.chip = self.lib.gpiod_chip_open_by_number(chip)
        self.line = self.lib.gpiod_chip_get_line(self.chip, pin)
        self.name = 'in {}'.format(pin).encode()
        self.lib.gpiod_line_request_both_edges_events(self.line, self.name)
        self.event = gpiod_line_event()

    def __call__(self):
        return self.lib.gpiod_line_get_value(self.line)

    def read(self):
        return self.lib.gpiod_line_get_value(self.line)

    def wait(self, timeout=-1):
        if timeout >= 0:
            t = timespec(tv_sec=timeout, tv_nsec=0)
            result = self.lib.gpiod_line_event_wait(self.line, pointer(t))
            if result <= 0:
                return None

        self.lib.gpiod_line_event_read(self.line, pointer(self.event))

        return self.event.event_type, self.event.ts.tv_sec


