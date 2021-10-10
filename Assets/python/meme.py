import urllib.request
import praw
import os
import time
from Auth.auth import reduser, repass, redsecret, redid


#myPath = 'PATH\\TO\\WHERE\\YOU\\WANT\\YOUR\\MEMES\\SAVED'

#default path
myPath = 'meme-folder'

#make a reddit account and look up how to find this stuff. its called PRAW
reddit = praw.Reddit(client_id=redid, 
	client_secret=redsecret, 
	username=reduser,
	password=repass,
	user_agent='chrome')


#number of pics you want your bot to send
numPics = 1

#waiting time to get data, don't change it
waitTime = 2

def get_meme(string):
	'''dowload memes from a given subreddit and outputs location of the files'''
	
	subreddit = reddit.subreddit(string)
	new_memes = subreddit.rising(limit=numPics) #.hot/.rising/.new   reddit sorting algorithm
	print('\n\n---checking posts on reddit---\n')
	paths = []
	while True:
		for subbmission in new_memes:
			if subbmission.is_self == True: #checking if post is only text.
				print("Post was text, skipping to next post.")
				continue
			else:
				pass
			url = subbmission.url
			print('checking if the post is new...')
			print('>>>' +url +'<<<')
			filename = 'memes.txt'
			#check if meme is old
			with open('memes.txt', 'r') as rf:
				with open(filename, 'a') as af:
					read = rf.read()
					if url not in read:
						print('All right post is ok!')
						af.write("\n" + url)
					else:
						print('This photo was already posted')
						continue						
			time.sleep(waitTime)
			filename = str(subbmission)
			time.sleep(waitTime)
			fullfilename = os.path.join(myPath, filename)
			fullfilename += '.jpg'
			print('full file name: ',fullfilename)
			urllib.request.urlretrieve(url, fullfilename)
			print('The photo has just been downloaded')
			paths.append(fullfilename)
		break
	print('finished task')
	return paths