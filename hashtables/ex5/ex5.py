# Your code here

# Given a list of full paths to files, and a list of filenames to query,
# report all the full paths that match that filename.

# extract the filename from the path
# use filename as a key

# so i would need the last part of the path as a key and the rest as the value
# because there can be collisions, your value should be a list of path [___, ____]

def finder(files, queries):

    cache = {}
    results = []

    for path in files:
        key = path.split("/")[-1]
        cache[key] = cache.get(key, [])
        cache[key].append(path)
    print(f"{cache} {files} {queries}")
    for query in queries:
        # check if query matches a key
        results.extend(cache.get(query, []))

    return results


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz',
        '/user/bin/foo'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
