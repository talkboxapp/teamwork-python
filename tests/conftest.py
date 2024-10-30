import os

import pytest

from teamwork import User

BOT_USER_TB_ID = os.getenv("BOT_USER_TB_ID")
BOT_USER_USERNAME = os.getenv("BOT_USER_USERNAME")
BOT_USER_DISPLAY_NAME = os.getenv("BOT_USER_DISPLAY_NAME")
TO_TB_ID = os.getenv("TO_TB_ID")
TO_TYPE = os.getenv("TO_TYPE")


@pytest.fixture
def bot_user():
    return User(
        tb_id=BOT_USER_TB_ID,
        username=BOT_USER_USERNAME,
        display_name=BOT_USER_DISPLAY_NAME,
        profile_pic="https://example.com/profile_pic.jpg",
        custom_fields={},
    )


@pytest.fixture
def to():
    return {"receiver_id": int(TO_TB_ID), "receiver_type": int(TO_TYPE)}
