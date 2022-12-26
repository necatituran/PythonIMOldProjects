from typing import List, Optional, Union
import asyncio
from datetime import datetime
from wechaty_puppet import get_logger
from wechaty import (
    MessageType,
    FileBox,
    RoomMemberQueryFilter,
    Wechaty,
    Contact,
    Room,
    Message,
    Image,
    MiniProgram,
    Friendship,
    FriendshipType,
    EventReadyPayload
)

logger = get_logger(__name__)


class MyBot(Wechaty):

