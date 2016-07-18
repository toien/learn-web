import asyncio

import www.orm
from www.models import User, Blog, Comment


def test_save():
    loop = asyncio.get_event_loop()

    loop.run_until_complete(www.orm.create_pool(loop, user='root', password='root', db='awesome'))

    u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')

    loop.run_until_complete(u.save())

    loop.stop()


test_save()