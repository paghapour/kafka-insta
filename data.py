from insta import instagram

insta = instagram()

def get_information_user():
    return{
        "profile" : insta.profilepic(),
        "videos" : insta.video(),
        "hashtag" : insta.hashtag
    }
    
    
if __name__ == '__main__':
    print(get_information_user)