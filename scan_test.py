from agora_community_sdk import AgoraRTC
import time
import cv2
from skimage.filters import threshold_local
import imutils
client = AgoraRTC.create_watcher('4970dca4fd784a8683966e33bb37cb72', 'chromedriver.exe')
client.join_channel("test")
users = client.get_users()
user1 = users[0]
# time.sleep(10)
# binary_image = user1.frame
# binary_image.save("test.png")
# client.unwatch()
# image = cv2.imread("test.png") #read image
# #ratio = image.shape[0] / 500.0 #resize image
# #orig = image.copy() #
# #image = imutils.resize(image, height = 500)
# # convert the image to grayscale, blur it, and find edges
# # in the image
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# gray = cv2.GaussianBlur(gray, (5, 5), 0)
# edged = cv2.Canny(gray, 75, 200)
# plt.subplot(121),plt.imshow(image,cmap = 'gray')
# plt.title('Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(edged,cmap = 'gray')
# plt.title('Edged'), plt.xticks([]), plt.yticks([])

# plt.show()
# #cv2.imshow("Image", image)
# #cv2.imshow("Edged", edged)
# #cv2.waitKey(0)
# #cv2.destroyAllWindows()