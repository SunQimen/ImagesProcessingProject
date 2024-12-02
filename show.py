
# Adjusting the paths to reflect the relative location
from pathlib import Path
import matplotlib.pyplot as plt
from PIL import Image

# Define the relative paths
base_path = Path("..") / "results"
output_path = base_path / "simple_landscape_comparison.png"

image1_path = base_path / "castel_resized.jpg"
image2_path = base_path / "castel_with_seams.jpg"
image3_path = base_path / "guilin_resized_laplace.jpg"
image4_path = base_path / "guilin_with_seams_laplace.jpg"

# Load the images using the adjusted paths
image1 = Image.open(image1_path)
image2 = Image.open(image2_path)
image3 = Image.open(image3_path)
image4 = Image.open(image4_path)

# Create a 2x2 subplot to display the images
fig, axs = plt.subplots(2, 2, figsize=(12, 10))

# Display the images
axs[0, 0].imshow(image1)
axs[0, 0].set_title("Castle Original")
axs[0, 0].axis('off')

axs[0, 1].imshow(image2)
axs[0, 1].set_title("Castle with Seams")
axs[0, 1].axis('off')

axs[1, 0].imshow(image3)
axs[1, 0].set_title("Pagoda Original")
axs[1, 0].axis('off')

axs[1, 1].imshow(image4)
axs[1, 1].set_title("Pagoda with Seams")
axs[1, 1].axis('off')

plt.tight_layout()

# Save the figure to the specified path
plt.savefig(output_path, dpi=300)
plt.close()

output_path = base_path / "complex_landscape_comparison.png"
image5_path = base_path / "eiffel_resized.jpg"
image6_path = base_path / "eiffel_with_seams.jpg"
image5 = Image.open(image5_path)
image6 = Image.open(image6_path)
fig, axs = plt.subplots(1, 2, figsize=(12, 4))
axs[0].imshow(image5)
axs[0].set_title("eiffel_resized")
axs[0].axis('off')

axs[1].imshow(image6)
axs[1].set_title("eiffel_with_seams")
axs[1].axis('off')

plt.tight_layout()

# Save the figure to the specified path
plt.savefig(output_path, dpi=300)
plt.close()


output_path = base_path / "clothes pattern affects.png"
image7_path = base_path / "people2_resized.jpg"
image8_path = base_path / "people2_with_seams.jpg"
image9_path = base_path / "people_resized.jpg"
image10_path = base_path / "people_with_seams.jpg"

# Load the images using the adjusted paths
image7 = Image.open(image7_path)
image8 = Image.open(image8_path)
image9 = Image.open(image9_path)
image10 = Image.open(image10_path)

# Create a 2x2 subplot to display the images
fig, axs = plt.subplots(2, 2, figsize=(12, 10))

# Display the images
axs[0, 0].imshow(image7)
axs[0, 0].set_title("Images with complex patterned clothing resized")
axs[0, 0].axis('off')

axs[0, 1].imshow(image8)
axs[0, 1].set_title("Images with complex patterned clothing Seams")
axs[0, 1].axis('off')

axs[1, 0].imshow(image9)
axs[1, 0].set_title("Images with people wearing simple clothing resized")
axs[1, 0].axis('off')

axs[1, 1].imshow(image10)
axs[1, 1].set_title("Images with people wearing simple clothing Seams")
axs[1, 1].axis('off')

plt.tight_layout()

# Save the figure to the specified path
plt.savefig(output_path, dpi=300)
plt.close()


output_path = base_path / "Removing seams vertically with a sample clothing pattern.png"
image12_path = base_path / "dog_resized.jpg"
image13_path = base_path / "dog_with_seams.jpg"
image12 = Image.open(image12_path)
image13 = Image.open(image13_path)
fig, axs = plt.subplots(1, 2, figsize=(8, 4))
axs[0].imshow(image12)
axs[0].set_title("simple_clothe_pattern_resized")
axs[0].axis('off')

axs[1].imshow(image13)
axs[1].set_title("simple_clothe_pattern_with_seams")
axs[1].axis('off')

plt.tight_layout()

# Save the figure to the specified path
plt.savefig(output_path, dpi=300)
plt.close()