from pytube import YouTube

goodYsObject = False
yt = None
while not goodYsObject:
    
    link = input("Enter the youtube the link for the video: ")
    try:
        yt = YouTube(link)
        goodYsObject = True
        
        print("Title: " ,yt.title)
        print("Number of views: ",yt.views)
        print("Length of video: ",yt.length,"seconds")
        print("Description: ",yt.description)
        print("channel: ",yt.channel_url)
        print("thumb", yt.thumbnail_url)

        answer = input('Is this the desired video (yes:1 no:0): ')
        if answer == '1':
            goodYsObject = True
            
        else:
            goodYsObject = False
    except:
        print('Please enter a valid link')


def multStream(Streams):
    for stream in streams:
        print(stream)

    itag = int(input('Please enter the itag of the stream you wish to download'))
    video = yt.streams.get_by_itag(itag)
    return video

downloadAgain = True

while downloadAgain:
    print('')
    print("Which type of streams would you like: ")
    print("1: Highest Resolution")
    print("2: Audio Only")
    print("3: Mp4")
    print("4: All Streams")
    choice = input("Please enter a choice (1-4): ")

    if choice == "1":
        video = yt.streams.get_highest_resolution()
        
    elif choice =='2':
        streams = yt.streams.filter(only_audio=True)
        
        video = multStream(streams)
        
    elif choice == '3':
        streams = yt.streams.filter(file_extension='mp4')
        
        video = multStream(streams)
    else:
        streams = yt.streams

        video = multStream(streams)


    video.download()

    downagain = input("Would you like to download another video (yes/no)")
    if downagain.lower == "yes":
        downloadAgain = True
    else:
        downloadAgain = False
