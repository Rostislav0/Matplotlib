import matplotlib.pyplot as plt


with open('img/1.png', 'rb') as map_file:
    map_img_1 = plt.imread(map_file)

with open('img/2.png', 'rb') as map_file:
    map_img_2 = plt.imread(map_file)

with open('img/3.png', 'rb') as map_file:
    map_img_3 = plt.imread(map_file)

with open('img/4.png', 'rb') as map_file:
    map_img_4 = plt.imread(map_file)

fig, axes = plt.subplots(2, 2, figsize=(12, 6))

axes[0][0].imshow(map_img_1)
axes[0][0].axis('off')
axes[0][1].imshow(map_img_2)
axes[0][1].axis('off')
axes[1][0].imshow(map_img_3)
axes[1][0].axis('off')
axes[1][1].imshow(map_img_4)
axes[1][1].axis('off')

plt.subplots_adjust(wspace=0, hspace=0)
plt.show()