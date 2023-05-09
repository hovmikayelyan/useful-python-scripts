# Import instabot library
from instabot import Bot

# Username
username = ""
password = ""

# Create a variable bot.
bot = Bot()

# Login
bot.login(username=username,
          password=password)


# To follow single person.
bot.follow("geeks_for_geeks")

# To follow more person.
list_of_user = ["user_id1", "user_id2", "user_id3", "...."]
bot.follow_users(list_of_user)

# To unfollow a single person.
bot.unfollow("geeks_for_geeks")

# To unfollow more person.
unfollow_list = ["user_id1", "user_id2", "user_id3", "..."]
bot.unfollow_users(unfollow_list)

# To unfollow everyone use:
# Please use this part very carefully.
bot.unfollow_everyone()

# Count number of followers
followers = bot.get_user_followers("geeks_for_geeks")
print("Total number of followers:")
print(len(followers))

# Message
# To send message to a single person.
message = "I like GFG"
bot.send_message(message, "geeks_for_geeks")

# Message
# To send same message to many follower.
message = "I like GFG"
list_of_userid = ["user_id1", "user_id2", "user_id3", "..."]
bot.send_messages(message, list_of_userid)

# Post photos
# Photos need be resized and, if not in ratio given below.
# jpg format works more better than others formats.
# Acceptable Ratio of image:-  90:47, 4:5, 1:1(square image).
# Keep image and program in same folder.
# -----------------------------------------------------------
bot.upload_photo("filename.jpg", caption="Write caption here.")
