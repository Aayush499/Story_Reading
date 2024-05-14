from scipy import io

subject_1 = io.loadmat('original/subject_1.mat')

from nilearn import plotting

display = plotting.plot_glass_brain(None)

coords = subject_1['meta']['colToCoord'][0][0]
display.add_markers([coords[0]], marker_size=70)

import nibabel
import numpy as np
from nilearn import image

data = subject_1['data']
image_12 = data[11, :]

new_img = nibabel.Nifti1Image(np.zeros((53, 61, 51)),
                              affine=subject_1['meta']['matrix'][0][0])
new_img_data = new_img.get_fdata()
for i in range(image_12.shape[0]):
    this_i_value = image_12[i]
    new_img_data[(coords[i][0], coords[i][1], coords[i][2])] = this_i_value
plotting.plot_stat_map(image.new_img_like(new_img, new_img_data), display_mode='x', cut_coords=10)


