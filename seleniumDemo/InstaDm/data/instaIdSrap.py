# # pip install instaloader
# from instaloader import Instaloader

# loader = Instaloader()
# username = "aadesh_lokhande"
# loader.download_profile(username, profile_pic_only= True)

 # Get instance
import instaloader
insta = instaloader.Instaloader()

# Login or load session
insta.login("janvi_noodles", "Aadesh@007")        # (login)
#L.load_session_from_file(myaccount)


# Obtain profile metadata
profile = instaloader.Profile.from_username(insta.context, "hasin_khan38")

# Print list of followers


file = open(f"phillips.txt","a+")
for follower in profile.get_followers():
    user = follower.username
    file.write(f"{user}\n")
    print(user)
file.close()










