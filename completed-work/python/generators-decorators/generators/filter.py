import source

def predicate(item):
    if len(item)>70:
        return True
    else:
        return False
    


lines=source.read_large_file("Projects/file.txt")

def filter_lines(lines,predicate):
    for i in lines:
        if predicate(i):
            print("[filter]")
            yield i


filtered=filter_lines(lines,predicate)
print(next(filtered))
print(next(filtered))
print(next(filtered))
