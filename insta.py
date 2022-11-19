import instaloader

class instagram:
    L = instaloader.Instaloader()
    username = input("instagram user : ")
    password = input("password id : ")
    L.login(username,password)
    profilepic=L.download_profile(username,profile_pic_only=True)
    hashtag=L.download_highlights(username)
    video=L.download_videos(username)
    
    