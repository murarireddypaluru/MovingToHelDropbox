import dropbox
import os
from dropbox.files import WriteMode

class TransferData():
    def __init__(self, access_token):
        self.access_token = access_token
    def upload_files(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to, mode=WriteMode('overwrite'))
        for root, dirs, files in os.walk("/Users/madhupaluru/Documents/boring", topdown=False):
            for file in files:
                print(os.path.join(root, file))
                file = os.path.join(root, file)
                with open(file, "rb") as f:
                     dbx.files_upload(f.read(), file_to, mode=WriteMode('overwrite'))
        
def main():
    access_token = 'REUVB5_lGysAAAAAAAAAAU5MrpMf9G-DRn9wRwmo4KSNY7vR0_BLTgAu7iApSVBB'
    transferData = TransferData(access_token)
    file_from = '/Users/madhupaluru/Desktop/WhiteHatjr/text.txt'
    file_to = '/Applications/WhiteHatDropbox/test.txt'
    transferData.upload_files(file_from, file_to)
    print("File has been moved")    
main()

        


