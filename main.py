import os
from pathlib import Path
import cv2
import numpy as np
from tqdm import trange
def create_green_energy_map(energy_map):
    normalized_map = cv2.normalize(energy_map, None, 0, 255, cv2.NORM_MINMAX)
    normalized_map = normalized_map.astype(np.uint8)
    green_energy_map = np.zeros((energy_map.shape[0], energy_map.shape[1], 3), dtype=np.uint8)
    green_energy_map[:, :, 1] = normalized_map
    return green_energy_map
def delete_seam(img, seam):
    rows, cols, _ = img.shape
    for row in range(rows):
        for col in range(int(seam[row]), cols - 1):
            img[row, col] = img[row, col + 1]
    output_img = img[:, 0:cols - 1]
    return output_img
def get_energy_map(img, filter_type):
    # use the gradient magnitude function to generate the energy map
    img = img.astype(np.uint8)
    # apply gaussian smoothing
    img = cv2.GaussianBlur(img, (3, 3), 0)
    # turn into greyscale
    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    if(filter_type == "laplace"): # use Laplace filter
        laplacian = cv2.Laplacian(grey, cv2.CV_64F)
        abs_laplacian = cv2.convertScaleAbs(laplacian)
        energy_map = abs_laplacian
    else: # use Sobel filter; default
        sobel_x = cv2.Sobel(grey, cv2.CV_64F, 1, 0, ksize=3)
        sobel_y = cv2.Sobel(grey, cv2.CV_64F, 0, 1, ksize=3)
        abs_sobel_x = cv2.convertScaleAbs(sobel_x)
        abs_sobel_y = cv2.convertScaleAbs(sobel_y)
        # merge into energy map
        energy_map = cv2.addWeighted(abs_sobel_x, 0.5, abs_sobel_y, 0.5, 0)
    return energy_map

def overlay_seam(seam, file):
    img = cv2.imread(results_dir+file)
    img_with_seam = np.copy(img)
    x, y = np.transpose([(i, int(j)) for i, j in enumerate(seam)])
    img_with_seam[x, y] = (0, 0, 255)
    cv2.imwrite(results_dir+file, img_with_seam)

def get_min_seam(img, energy_map):
    rows, cols, _ = img.shape
    seam = np.zeros(rows)
    dist = np.zeros((rows, cols)) + 100000000
    dist[0,:] = energy_map[0,:]
    edge = np.zeros((rows, cols))
    for row in range(rows-1):
        for col in range(cols):
            if col != 0:
                first = dist[row+1, col-1]
                prev = dist[row, col] + energy_map[row+1, col-1]
                dist[row+1, col-1] = min(first, prev)
                if first>prev:
                    edge[row+1, col-1] = 1
            second = dist[row+1, col]
            cur = dist[row, col] + energy_map[row+1, col]
            dist[row+1, col] = min(second, cur)
            if second>cur:
                edge[row+1, col] = 0
            if col != cols-1:
                third = dist[row+1, col+1]
                next_ = dist[row, col] + energy_map[row+1, col+1]
                dist[row+1, col+1] = min(third, next_)
                if third>next_:
                    edge[row+1, col+1] = -1
    seam[rows-1] = np.argmin(dist[rows-1, :])
    for i in (x for x in reversed(range(rows)) if x > 0):
        seam[i-1] = seam[i] + edge[i, int(seam[i])]
    return seam
def carve_seams(output_img):
    energy_map = get_energy_map(output_img, filter_type)
    for _ in trange(num_seams):
        seam = get_min_seam(output_img, energy_map)
        overlay_seam(seam, f"{image_name}_with_seams_{filter_type}.jpg") # to show all seams removed overlayed on the original image
        output_img = delete_seam(output_img, seam)
        energy_map = get_energy_map(output_img, filter_type) # get energy map of new image
    cv2.imwrite(results_dir+f"{image_name}_resized_{filter_type}.jpg", output_img)

if __name__ == '__main__':
    # 创建或确认 'testCode' 目录存在
    results_dir = os.path.join(os.path.dirname(__file__), "results/")
    Path(results_dir).mkdir(parents=True, exist_ok=True)
    # 读取图像
    image_name="dog.jpg"
    num_seams=100
    filter_type="sobel"
    images_dir = os.path.join(os.path.dirname(__file__), "images/"+image_name)
    img = cv2.imread(images_dir)
    img_with_seam = np.copy(img)
    if img is None:
        print(f"can not load: {images_dir}")
        exit(1)
    cv2.imwrite(results_dir + f"{image_name}_resized_{filter_type}.jpg", img)
    cv2.imwrite(results_dir + f"{image_name}_with_seams_{filter_type}.jpg", img)
    carve_seams(img)





