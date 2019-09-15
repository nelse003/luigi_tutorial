import matplotlib.pyplot as plt

def plot_airplane(color='k',filename="plane.png"):
    """
    Make a plot of an airplane

    Uses Matplotibe to create an airplane

    Attributes
    -----------
    
    """
    plt.plot([0,1],[0,1], lw=5, color=color)
    plt.plot([0.3,1],[-2.5,1], lw=5, color=color)
    plt.plot([0,0.1],[0,-0.7], lw=5, color=color)
    plt.plot([0.1,1],[-0.7,1], lw=5, color=color)
    plt.plot([0.3,0.15],[-2.5,-1.3], lw=5, color=color)
    plt.plot([0.15,1],[-1.3,1], lw=5, color=color)
    plt.plot([0.1,0.11],[-0.7,-2.2], lw=5, color=color)
    plt.plot([0.11,0.15],[-2.2,-1.3], lw=5, color=color)
    plt.plot([0.11,0.225],[-2.2,-1.9], lw=5, color=color)

    cur_axes = plt.gca()
    cur_axes.axes.get_xaxis().set_visible(False)
    cur_axes.axes.get_yaxis().set_visible(False)

    plt.show()
    plt.savefig(filename)