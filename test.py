from cmap_rwth_colours import rwth_cmap
import matplotlib as plt

plt.cm.register_cmap('extended_RWTH_discrete', rwth_cmap('extended_RWTH_discrete'))
plt.set_cmap('extended_RWTH_discrete')
