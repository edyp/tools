with open("what.html") as f, open("output.html", "w") as out:
    for line in f:
        out.write(line[10:])
    f.close()
    out.close()
