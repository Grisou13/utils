def find_files_recursive(directory):
    for root, dirs, files in os.walk(directory):
        for basename in files:
            filename = os.path.join(root, basename)
            yield filename
        for d in dirs:
            for f in find_files(os.path.join(root, d)):
                yield f
                