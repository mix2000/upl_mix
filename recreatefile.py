def recreatefile(blockFile, dateFileUpdate):
    f = open(blockFile, 'w')
    f.write(dateFileUpdate)
    f.close()
