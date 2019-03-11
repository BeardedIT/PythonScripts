import urllib, json,os
# Determines which comic is the most recent
def get_latest():
    late_url="https://xkcd.com/info.0.json"
    response = urllib.urlopen(late_url)
    # Reads site as json
    xkcd = json.loads(response.read())
    # Pulls the latest comic number from json
    comic_number=str(xkcd['num'])
    return(comic_number)
def retrieve_info(url):
    response = urllib.urlopen(url)
    response_code = response.getcode()
    # # Checks to see if url is valid
    xkcd = json.loads(response.read())
    comic_number=str(xkcd['num'])
    image=(xkcd['img'])
    comic_title=xkcd['safe_title']
    # Replace spaces and slashes for the sake of error avoidance
    comic_title=comic_title.replace(' ','_')
    comic_title=comic_title.replace('/','-')
    # Concatenate strings into one
    filename=comic_number+'-'+comic_title
    return (filename,image)
    # Checks to see if file exists
# Downloads the image as name implies
def downloader(url, filename):
    if os.path.exists(filename):
        print filename+' exists - Skipping'
    elif not os.path.exists(filename):
        print'Downloading',filename
        # Download image to filename
        urllib.urlretrieve(url, filename)
def __main__():
    comic_number=int(get_latest())
    
    while comic_number > 1:
        info=retrieve_info('https://xkcd.com/'+str(comic_number)+'/info.0.json')
        downloader(info[1], info[0])
        comic_number=comic_number-1
        # Lazy way to avoid 404 Error
        # There is no comic 404
        if comic_number==404:
            comic_number=403
    else:
        print('Download completed')
        exit()
__main__()
