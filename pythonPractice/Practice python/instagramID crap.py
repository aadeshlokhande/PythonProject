#pip install instapy
from instagramy import InstagramUser
# Author = TECH_IN_SECONDS

id = input("Enter a Instagram Username = ")
user = InstagramUser(id.lower())
print('\nFullname\t=',user.fullname)
print('username\t=',user.username)
print('Followers\t=',user.number_of_followers)
print('Following\t=',user.number_of_followings)
print('Posts\t\t=',user.number_of_posts)
print('Private\t\t=',user.is_private)
print('Verified\t=',user.is_verified)
print('\nBio: \n',user.biography)


