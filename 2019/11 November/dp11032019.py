# This problem was recently asked by Facebook:

# Given a file path with folder names, '..' (Parent directory), and '.' (Current directory),
# return the shortest possible file path (Eliminate all the '..' and '.').


def shortest_path(file_path):
    # Fill this in.
    inPath = file_path.split("/")
    resStack = []
    for path in inPath:
        if path == ".":
            continue
        elif path == "..":
            del resStack[-1]
        else:
            resStack.append(path)
    resPath = ""
    del resStack[0]
    for path in resStack:
        resPath = f"{resPath}/{path}"

    return resPath


print(shortest_path("/Users/Joma/Documents/../Desktop/./../"))
# /Users/Joma/
