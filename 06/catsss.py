import matplotlib.pyplot as plt
import cv2

catplt = plt.imread(r'C:\sonia\Python\20\06\amber-kipp-75715CVEJhI-unsplash.jpg')
catcv2 = cv2.imread(r'C:\sonia\Python\20\06\amber-kipp-75715CVEJhI-unsplash.jpg')
#показати котика через матплот
fig, ax = plt.subplots(figsize=(10,10))
ax.imshow(catplt)
ax.axis('off')
plt.show()
"""
#розрізати котика на червоний зелений і синій і показати через матплот
fig, axs = plt.subplots(1, 3, figsize=(15,5))
axs[0].imshow(catplt[:,:,0], cmap='Reds', aspect='auto')
axs[1].imshow(catplt[:,:,1], cmap='Greens', aspect='auto')
axs[2].imshow(catplt[:, :, 2], cmap='Blues', aspect='auto')
axs[0].axis('off')
axs[1].axis('off')
axs[2].axis('off')
axs[0].set_title('Red cats', color='red', style='italic')
axs[1].set_title('Green cats', color='green', style='italic')
axs[2].set_title('Blue cats', color='blue', style='italic')
plt.show()

#показати котика через св2 і через матплот правильно (реверснути св2)
cv2rgb = cv2.cvtColor(catcv2, cv2.COLOR_RGB2BGR)
fig, axs = plt.subplots(1, 2, figsize=(10,5))
axs[0].imshow(catplt)
axs[1].imshow(cv2rgb)
axs[0].axis('off')
axs[0].axis('off')
axs[1].axis('off')
axs[0].set_title('plt', color='red', style='italic')
axs[1].set_title('cv2', color='green', style='italic')
plt.show()

#сірий котик
cv2gray = cv2.cvtColor(catcv2, cv2.COLOR_RGB2GRAY)
fig, ax = plt.subplots(figsize=(10,10))
ax.imshow(cv2gray, cmap='gray')
ax.axis('off')
ax.set_title('Gray', color='black', style='italic')
plt.show()

#зменшення к-сті пікселів і загалом розмірів
resized_image = cv2.resize(catplt,None, fx=0.025, fy=0.025)
fig, ax = plt.subplots(figsize=(10,10))
ax.imshow(resized_image)
ax.axis('off')
ax.set_title('Resized image', color='black', style='italic')
plt.show()
#збільшення якості
kernel_sharpening = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
sharpened_image = cv2.filter2D(catplt, -1, kernel_sharpening)
fig, ax = plt.subplots(figsize=(10,10))
ax.imshow(sharpened_image)
ax.axis('off')
ax.set_title('Sharpened image', color='black', style='italic')
plt.show()

#bluring
kernel_3x3 = np.ones((3,3), np.float32)/10
blured = cv2.filter2D(catplt, -1, kernel_3x3)
fig, ax = plt.subplots(figsize=(10,10))
ax.imshow(blured)
ax.axis('off')
ax.set_title('Blured image', color='black', style='italic')
plt.show()

#saving the kitten
cv2.imwrite('some_file.jpg', image)
"""
#завдання з дз
img = cv2.imread(r'C:\sonia\Python\20\06\richard-brutyo-Sg3XwuEpybU-unsplash.jpg')
imgrgb = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
h, w = img.shape[:2]
left_half = imgrgb[0:h, 0:int(w/2)]
right_half = imgrgb[0:h, int(w/2):w]
top_half = imgrgb[0:int(h/2), 0:w]
bottom_half = imgrgb[int(h/2):h, 0:w]
fig, axs = plt.subplots(2, 2, figsize=(10,10))
axs[0,0].imshow(left_half, aspect='auto')
axs[0,1].imshow(top_half, aspect='auto')
axs[1,0].imshow(right_half, aspect='auto')
axs[1,1].imshow(bottom_half, aspect='auto')
axs[0,0].axis('off')
axs[0,1].axis('off')
axs[1,0].axis('off')
axs[1,1].axis('off')
axs[0,0].set_title('Left half', color='black', weight='bold')
axs[0,1].set_title('Top half', color='black', weight='bold')
axs[1,0].set_title('Right half', color='black', weight='bold')
axs[1,1].set_title('Bottom half', color='black', weight='bold')
print("Розміри фото:", img.shape[:2])
plt.show()
"""
cv2.imwrite('left_half.jpg', left_half)
cv2.imwrite('top_half.jpg', top_half)
cv2.imwrite('right_half.jpg', right_half)
cv2.imwrite('bottom_half.jpg', bottom_half)
"""