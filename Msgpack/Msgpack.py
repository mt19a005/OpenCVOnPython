import msgpack
import cv2


imgSrc = cv2.imread("a.jpg")

obj1 = {
    "name": "Alice",
    "age": 27,
    "hist": [5, 3, 1]
}
obj2 = {
    "name": "Bob",
    "age": 33,
    "hist": [4, 5]
}

with open('data.msg', 'bw') as fd:
    fd.write(msgpack.packb(imgSrc))
    # fd.write(msgpack.packb(obj2))

for msg in msgpack.Unpacker(open('data.msg', 'rb')):
    print(msg)