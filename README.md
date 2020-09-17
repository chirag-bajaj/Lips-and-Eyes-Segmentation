# Lips-and-Eyes-Segmentation

## Data Collection
1. Downloading the dataset ->Pre-processing the dataset according to the requirement
-> Training U-net with Image as input and Mask as output -> Testing results on
images from testing data
2. Downloading the dataset ->Pre-processing the dataset according to the requirement
-> Training pix2pix GAN as a task of image-to-image translation ie. from A(Image) to
B(Mask) -> Testing results


## Dataset
CelebAMask-HQ is a large-scale face image dataset that has 30,000 high-resolution face
images selected from the CelebA dataset by following CelebA-HQ. Each image has
segmentation mask of facial attributes corresponding to CelebA.
The masks of CelebAMask-HQ were manually-annotated with the size of 512 x 512 and 19
classes including all facial components and accessories such as skin, nose, eyes, eyebrows,
ears, mouth, lip, hair, hat, eyeglass, earring, necklace, neck, and cloth.
Download Link: https://drive.google.com/file/d/1badu11NqxGf6qM3PTTooQDJvQbejgbTv/

## GAN (Generative Adversarial Networks)
### I. Data Preprocessing
Since our requirement is to segment only lips and eyes out of the whole face, we
need to first of all create masks of images which include the following :
u_lip,l_lip,l_eye and r_eye.
For training purposes I created masks for 10000 images using g_mask.py
Pix2pix architecture takes input as an image having 2 parts A and B, such that
mapping from A to B is intended. So the masks created from above script are then
combined with the original image in the following manner: A(Original
Image)B(Masked Image). This was done by process.py

### II. Model Architecture
The Pix2Pix model is a type of conditional GAN, or cGAN, where the generation of
the output image is conditional on an input.The discriminator is provided both with
a source image and the target image and must determine whether the target is a
plausible transformation of the source image.

#### Generator
The generator is an encoder-decoder model using a U-Net architecture. The model
takes a source image and generates a target image. It does this by first
downsampling or encoding the input image down to a bottleneck layer, then
upsampling or decoding the bottleneck representation to the size of the output
image. The U-Net architecture means that skip-connections are added between the
encoding layers and the corresponding decoding layers, forming a U-shape.

#### Discriminator
The discriminator is a deep convolutional neural network that performs image
classification. Specifically, conditional-image classification. It takes both the source
image and the target image as input and predicts the likelihood of whether target
image is real or a fake translation of the source image.

#### Loss
The generator is updated via a weighted sum of both the adversarial loss and the L1
loss. Discriminator loss is simply binary cross-entropy.
The model is updated with two targets, one indicating that the generated images
were real (cross entropy loss), forcing large weight updates in the generator toward
generating more realistic images, and the executed real translation of the image,
which is compared against the output of the generator model (L1 loss).

### III. Training
Pix2pix.py contains code for cGAN architecture for both Training and Testing.

### Results
GAN architecture was used it was very well able to generalize the results
on the images that weren’t present in dataset while training. Print.py is the python
script for outputting the results as mentioned in the task.
Since only 10000 images were used to train, I think if I utilize all the data for training
the results would further improve and the outputs we get would match the target
pixel perfect.
![image](https://github.com/chiragbajaj25/Lips-and-Eyes-Segmentation/blob/master/final.png)
