import matplotlib.pyplot as plt


def print_images(pil_imgs, titles=None, figsize=None, color='black'):
    figsize = figsize
    fig = plt.figure(figsize=figsize)
    fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
    n = len(pil_imgs)
    for i in range(n):
        img = pil_imgs[i]
        ax = fig.add_subplot(1, n, i+1)
        ax.imshow(img)
        if titles is not None:
            ax.set_title(titles[i], fontsize=10)
        ax.axis('off')
    return fig


def plot_image_grid(image_grid):
    num_rows = len(image_grid)
    num_cols = len(image_grid[0]) if num_rows > 0 else 0
    fig, axes = plt.subplots(num_rows, num_cols, figsize=(num_cols * 2, num_rows * 2))
    if num_rows == 1:
        axes = [axes]
    if num_cols == 1:
        axes = [[ax] for ax in axes]
    for i in range(num_rows):
        for j in range(num_cols):
            ax = axes[i][j]
            ax.imshow(image_grid[i][j])
            ax.axis('off')
    fig.tight_layout()
    return fig
