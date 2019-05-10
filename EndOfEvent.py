# it does need some 'ifs' for situations like adding 2 days to the 30th of May but I just wanted to show you the concept


def endOfEvent(start, duration):
    'calculates the end of event based on its start and duration'
    end = str(int(start[0:4]) + int(duration[0:4])) + "-" + str(
        int(start[5:7]) + int(duration[5:7])) + "-" + str(
        int(start[8:10]) + int(duration[8:10])) + "T" + str(
        int(start[11:13]) + int(duration[11:13])) + ":" + str(
        int(start[14:16]) + int(duration[14:16])) + ":" + str(
        int(start[17:19]) + int(duration[17:19]))
    return end
