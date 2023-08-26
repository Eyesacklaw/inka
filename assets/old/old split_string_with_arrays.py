def split_string_with_arrays(text):
    result = []
    string = ""
    inside_array = ""
    in_array = False
    for i in range(len(text)):
        if type(text[i]) != str:
            result.append(text[i])
        else: # If it is string
            line = text[i]
            for n in range(len(line)):
                if not in_array:
                    if line[n] == "[":
                        in_array = True
                        result.append(string)
                        string = ""
                    else:
                        string += line[n]
                else:
                    if line[n] == "]":
                        in_array = False
                        result.append(inside_array.split(",")) #
                        inside_array = ""
                    else:
                        inside_array += line[n]
    if string != "":
        result.append(string)
    if inside_array != "":
        result.append(inside_array)
    return result