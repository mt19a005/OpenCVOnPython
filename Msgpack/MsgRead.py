# coding: UTF-8

import msgpack

# for msg in msgpack.Unpacker(open('data.msg', 'r')):
#     print(msg)

msgpack.unpackb(open('data.msg', 'r'), raw=False)