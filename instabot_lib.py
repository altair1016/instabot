from instabot import Bot
import time
import random


def follow_users(hashtag, user_id, my_followed_id, bot):
	new_users_list = bot.get_hashtag_users(hashtag)
	username2follow = [elt for elt in new_users_list if elt != user_id and elt not in my_followed_id][0:5000]
	return username2follow

def random_follow(followed_list, bot):
	#followed_list = bot.get_user_following(my_username)
	rand_value = random.randrange(0,20,1)
	rand_sleep = 0
	if len(followed_list) > 0:
		for elt in followed_list:
			#rand_result = random.randrange(0,rand_value,1)
			#if rand_result > 5:
			user_info = bot.get_user_info(elt)
			if rand_value % 2 == 0:
				value_user = bot.get_username_from_user_id(elt)
				bot.follow(value_user)
			rand_sleep = random.randrange(0,10,1)
			rand_value = random.randrange(0,20,1)
			time.sleep(rand_sleep)

def random_likes(hashtag, bot):
	media_list = bot.get_hashtag_medias(hashtag)
	for media in media_list:
		rand_decision = random.randrange(0,10,1)
		if rand_decision % 2 == 0:
			bot.like(media)
		rand_sleep = random.randrange(0,20,1)
		time.sleep(rand_sleep)

def random_unlikes(bot):
	media_list = bot.like_timeline()
	print media_list
	rand_decision = random.randrange(0,len(media_list),1)[0:10]
	for media in media_list:
		rand_decision = random.randrange(0,10,1)
		if rand_decision % 2 == 0:
			bot.unlike(media)
		rand_sleep = random.randrange(0,20,1)
		time.sleep(rand_sleep)

def random_unfollow(bot, my_username):
	followed_list = bot.get_user_following(my_username)
	follower_list = bot.get_user_followers(my_username)

	unfollow_number = random.randrange(30, 50)
	user_set = {}
	for i in range(0,unfollow_number):
		unfollow_flag = 0
		user_rand = random.randrange(0,len(followed_list))
		user_id = followed_list[user_rand]
		#user_set.add()
		if followed_list[user_rand] not in follower_list:
			unfollow_flag = unfollow_flag + 1
		trg_username = bot.get_username_from_user_id(user_id)
		user_medias = len(bot.get_total_user_medias(trg_username))
		user_followed_count = len(bot.get_user_following(trg_username))
		user_follower_count = len(bot.get_user_following(trg_username))

		if user_followed_count/user_follower_count < 0.2:
			unfollow_flag = unfollow_flag + 1

		if user_medias < 100:
			unfollow_flag = unfollow_flag + 1

		if unfollow_flag == 3:
			bot.unfollow(trg_username)



