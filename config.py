#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Dark Angel

import os
import logging

class Config:
    
    API_ID = int(os.environ.get("API_ID", "9544521"))
    API_HASH = os.environ.get("API_HASH", "5cf32e97dc94510e46524f2286c95116")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5874353588:AAHKp1CZZowaVmcSQ_H1LbhagWIEqBZL_FE") 
    BOT_SESSION = os.environ.get("BOT_SESSION", "bot") 
    CAPTION = os.environ.get("CAPTION", "")
    FROM_CHANNEL = os.environ.get("FROM_CHANNEL", None)
    FILTER_TYPE = os.environ.get("FILTER_TYPE", "")
    OWNER_ID = os.environ.get("OWNER_ID", "1358657527")
    LIMIT = int(os.environ.get("LIMIT", "0"))
    SKIP_NO = int(os.environ.get("SKIP_NO", "0"))
    SESSION = os.environ.get("SESSION")
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001652903990"))
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
