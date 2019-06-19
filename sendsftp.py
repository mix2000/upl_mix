import pysftp


def sendsftp(pathFile):
    global host, username, password, port
    cnopts = pysftp.CnOpts()
    cnopts.hostkeys = None
    with pysftp.Connection(host=host, username=username, password=password, cnopts=cnopts,
                           port=port) as sftp:
        sftp.put(pathFile, '/home/test.xlsx')
    sftp.close()
