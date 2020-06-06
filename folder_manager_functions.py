import os, shutil, re
from collections import Counter

# list of extensions (memory based)
image_files=['.jpg','.jpeg','.png','.gif', '.bmp', '.svg','.jfif', '.dwg']
text_and_document_files=['.pdf', '.txt', '.docx', '.doc', '.odt', '.ics']
compressed_files=['.zip', '.rar', '.7z', '.jar', '.gz', '.xz', '.deb', '.arc', '.arj']
video_files=['.mp4', '.m4p', '.m4v', '.mpv', '.mp2', '.webm','.mkv']
executable_files=['.exe', '.run', '.sh', '.desktop', '.out', '.bin','.msi']
presentation_files=['.ppt', '.pptx', '.odp']
spreadsheet_files=['.xls', 'xlsx','xlsb', '.xlsm', '.ods', '.sdc', 'sxc']
database_files=['.db', '.csv', '.dbf', '.json']
script_files=['.py','.c', '.js', '.cpp', '.css', '.html', '.jsp', '.xml',
              '.jspx', '.cs', '.dart', '.swift', '.kt', '.kts', '.ktm']
disk_file=['.iso']
audio_file=['.wav', '.mp3']

def ext_arrange(arr):
    dirr= arr[0]
    if os.path.isdir(dirr):

        #separating files

        img=list(filter(lambda x: os.path.splitext(x)[1] in image_files, os.listdir(dirr) ))
        documents_and_plaintext=list(filter(lambda x: os.path.splitext(x)[1] in text_and_document_files, os.listdir(dirr) ))
        archives=list(filter(lambda x: os.path.splitext(x)[1] in compressed_files, os.listdir(dirr) ))
        videos=list(filter(lambda x: os.path.splitext(x)[1] in video_files, os.listdir(dirr) ))
        executables=list(filter(lambda x: os.path.splitext(x)[1] in executable_files, os.listdir(dirr) ))
        presentations=list(filter(lambda x: os.path.splitext(x)[1] in presentation_files, os.listdir(dirr) ))
        spreadsheets=list(filter(lambda x: os.path.splitext(x)[1] in spreadsheet_files, os.listdir(dirr) ))
        databases=list(filter(lambda x: os.path.splitext(x)[1] in database_files, os.listdir(dirr) ))
        scripts=list(filter(lambda x: os.path.splitext(x)[1] in script_files, os.listdir(dirr) ))
        iso=list(filter(lambda x: os.path.splitext(x)[1] in disk_file, os.listdir(dirr) ))
        audio=list(filter(lambda x: os.path.splitext(x)[1] in audio_file, os.listdir(dirr) ))


        separation={'pictures': img,
                    'Docs':documents_and_plaintext,
                    'Compressed':archives,
                    'Videos':videos,
                    'executables': executables,
                    'presentations': presentations,
                    'Spreadsheets': spreadsheets,
                    'Database_Files': databases,
                    'Scripts': scripts,
                    'iso': iso,
                    'audios': audio
                    }

        for folder in separation:

            if not os.path.exists(os.path.join(dirr, folder)):
                os.makedirs(os.path.join(dirr,folder))
            
            new_folder=os.path.join(dirr, folder)
            try:

                for file in separation[folder]:

                    shutil.move(os.path.join(dirr, file),new_folder )
            except:
                print("Try running the same command again")

    else:
        print('your specified directory: {} is not a valid directory path on your machine'.format(dirr))



def name_arrange(arr):
    dirr= arr[0]
    if os.path.isdir(dirr):
        # list initials of all file names
        temp=list(map(lambda x: re.split(r'[\d\s_@#%&\'"*-]', x)[0], os.listdir(dirr)))

        all_files= [ os.path.splitext(x.lower())[0] for x in  temp]

        alpha=Counter(re.findall(r'\w+', ' '.join(all_files)))


        same= [ x for x in alpha if alpha[x]>1]


        for key in same:
            # print(key)
            if not os.path.exists(os.path.join(dirr, key)):

                os.makedirs(os.path.join(dirr, key))
            

            new_folder=os.path.join(dirr, key)

            for file in os.listdir(dirr):

                try:
                    if os.path.join(dirr,new_folder) in os.path.splitext(os.path.join(dirr,file.lower()))[0] :
                        shutil.move(os.path.join(dirr, file), new_folder)
                except:
                    pass


def deep_arrange(arr):
    mode, path=arr
    
    assert os.path.isdir(path)
    
    if mode=='1':
        # print('called deep arrange in mode {}'.format(mode))
        name_arrange(os.path.splitext(path))
        for sub_path in os.listdir(path):
           
            if os.path.isdir(os.path.join(path,sub_path)):
                ext_arrange(os.path.splitext(os.path.join(path,sub_path)))

    elif mode=='2':
        ext_arrange(os.path.splitext(path))
        for sub_path in os.listdir(path):
            if os.path.isdir(os.path.join(path,sub_path)):
                name_arrange(os.path.splitext(os.path.join(path,sub_path)))

    else:
        print('{} is not a valid mode. \n  python folder_manager.py -h'.format(mode))

def compress(arr):
    kind, target=arr

    assert os.path.isdir(target)
    
    # archives to have the same name as the original file or directory
    arc=os.path.splitext(target)[0]

    if kind=='xztar':
        print('this might take some time. xztar is the slowest archiving technique')
        shutil.make_archive(arc,'xztar',target)
        print('created an archive file. Now you can delete the original file')
    elif kind=='gztar':
        print('this might take some time')
        shutil.make_archive(arc,'gztar',target)
        print('created an archive file. Now you can delete the original file')
    elif kind=='zip':
        print('this might take some time. zip is the fastest archiving technique')        
        shutil.make_archive(arc,'zip',target)
        print('created an archive file. Now you can delete the original file')
    else:
        print('archive type {} is either not supported by by your Operating System or not available')



