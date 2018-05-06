# -*- coding: utf-8 -*-

import json, os


README_URL = os.environ['BUL_CBP__README_URL']

SUPER_USERS = json.loads( os.environ['BUL_CBP__SUPER_USERS_JSON'] )

STAFF_USERS = json.loads( os.environ['BUL_CBP__STAFF_USERS_JSON'] )  # can use admin

STAFF_GROUP = os.environ['BUL_CBP__STAFF_GROUP']

TEST_META_DCT = json.loads( os.environ['BUL_CBP__TEST_META_DCT_JSON'] )


EMAIL_SENDER = os.environ['BUL_CBP__APPARENT_SENDER']
EMAIL_REPLY_TO = os.environ['BUL_CBP__REPLY_TO']
