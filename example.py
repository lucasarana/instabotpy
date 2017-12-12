#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import time

sys.path.append(os.path.join(sys.path[0], 'src'))

from check_status import check_status
from feed_scanner import feed_scanner
from follow_protocol import follow_protocol
from instabot import InstaBot
from unfollow_protocol import unfollow_protocol

bot = InstaBot(
    login="",
    password="",
    like_per_day=3000,
    comments_per_day=150,
    tag_list=['pinamar'],
    tag_blacklist=[],
    user_blacklist={},
    max_like_for_one_tag=322074,
    follow_per_day=350,
    follow_time=1 * 60,
    unfollow_per_day=200,
    unfollow_break_min=350,
    unfollow_break_max=500,
    log_mod=1,
    proxy='',
    comment_list=["Veni a conocernos! La mejor parrilla de Pinamar"],
    unwanted_username_list=[],
    unfollow_whitelist=[])
while True:

    mode = 0

    if mode == 0:
        bot.new_auto_mod()

    elif mode == 1:
        check_status(bot)
        while bot.self_following - bot.self_follower > 200:
            unfollow_protocol(bot)
            time.sleep(10 * 60)
            check_status(bot)
        while bot.self_following - bot.self_follower < 400:
            while len(bot.user_info_list) < 50:
                feed_scanner(bot)
                time.sleep(5 * 60)
                follow_protocol(bot)
                time.sleep(10 * 60)
                check_status(bot)

    elif mode == 2:
        bot.bot_mode = 1
        bot.new_auto_mod()

    elif mode == 3:
        unfollow_protocol(bot)
        time.sleep(10 * 60)

    elif mode == 4:
        feed_scanner(bot)
        time.sleep(60)
        follow_protocol(bot)
        time.sleep(10 * 60)

    elif mode == 5:
        bot.bot_mode = 2
        unfollow_protocol(bot)

    else:
        print("Wrong mode!")
