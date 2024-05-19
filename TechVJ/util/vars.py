# (c) @fligher
import os
from os import getenv, environ
from dotenv import load_dotenv 



load_dotenv()


class Var(object):



    LONG_DROPLINK_URL=str(getenv('LONG_DROPLINK_URL',"paisakamalo.in"))

    SHORTENER_API=str(getenv('SHORTENER_API',"9d7e32c571c44b3ee91a814fa25c31e0211f5aeb"))
