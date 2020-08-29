import matplotlib.pyplot as plt
import seaborn as sb

color = ['#3498db']
target_dir = 'figures/'

def distplot(data, bins, xlabel, ylabel, title, name, export=False, font_scale=1.5):

    sb.set(rc={"figure.figsize": (8, 5)}, font_scale=font_scale)
    sb.set_style('white')

    ax = sb.distplot(data, bins=48, kde = False, color=color[0])
    ax.set(xlabel=xlabel, ylabel=ylabel)

    if title is not None:
        plt.title(title)

    plt.tight_layout()
    if not export:
        plt.show()
    else:
        file_name = target_dir + name
        plt.savefig(file_name)