import json
import os
import sys
from collections import OrderedDict


def subtractRanges(As, Ae, Bs, Be):
    '''SUBTRACTS A FROM B'''
    # e.g, A =    ------
    #      B =  -----------
    # result =  --      ---
    # Returns list of new range(s)

    if As > Be or Bs > Ae or (Ae == Bs and Be > Ae):  # All of B visible
        return [[Bs, Be]]
    result = []
    if As > Bs:  # Beginning of B visible
        result.append([Bs, As])
    if (Be > Ae > Bs) or (As == Bs and Ae < Be):  # End of B visible
        result.append([Ae, Be])
    if As == Bs and Ae > Be:
        result.append([Be, Ae])
    return result


def schedule(input_file):
    # Opening JSON file
    f = open(input_file, 'r')

    # returns JSON object as
    # a dictionary
    data = json.load(f)
    file_name = os.path.splitext(input_file)[0]

    # sort by start time and priority
    data = sorted(data, key=lambda d: (d['start'], d['priority']))
    i = 0  # Start at lowest span
    while i < len(data):
        for superior in data[i + 1:]:  # Iterate through all spans above
            result = subtractRanges(superior['start'], superior['finish'], data[i]['start'], data[i]['finish'])
            if not result:  # If span is completely covered
                del data[i]  # Remove it from list
                i -= 1  # Compensate for list shifting
                break  # Skip to next span
            else:  # If there is at least one resulting span
                data[i]['start'] = result[0][0]
                data[i]['finish'] = result[0][1]
                if len(result) > 1:  # If there are two resulting spans
                    # Insert another span with the same name
                    data.insert(i + 1, {'band': data[i]['band'], 'start': result[1][0], 'finish': result[1][1]})
        i += 1

    for d in data:
        d.pop('priority', None)
    json_object = json.dumps(sorted(data, key=lambda d: d['start']), indent=4)

    # Writing to sample.json
    with open(file_name + '.optimal.json', "w") as outfile:
        outfile.write(json_object)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    schedule(sys.argv[1])

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
