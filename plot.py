import matplotlib.pyplot as plt

def plot_airplane(color='k',filename="plane.png"):
    """
    Make a plot of an airplane

    Uses Matplotib to create an airplane
    
    Parameters
    ----------
    color : str, optional
        Colour of airplane, 
        needs to readable by matplotlib colours, 
        by default 'k' for black

    filename : str, optional
        filename of output, by default "plane.png"
    """
    fig, ax = plt.subplots()

    ax.plot([0,1],[0,1], lw=5, color=color)
    ax.plot([0.3,1],[-2.5,1], lw=5, color=color)
    ax.plot([0,0.1],[0,-0.7], lw=5, color=color)
    ax.plot([0.1,1],[-0.7,1], lw=5, color=color)
    ax.plot([0.3,0.15],[-2.5,-1.3], lw=5, color=color)
    ax.plot([0.15,1],[-1.3,1], lw=5, color=color)
    ax.plot([0.1,0.11],[-0.7,-2.2], lw=5, color=color)
    ax.plot([0.11,0.15],[-2.2,-1.3], lw=5, color=color)
    ax.plot([0.11,0.225],[-2.2,-1.9], lw=5, color=color)

    # Remove the plot axis
    fig.frameon = False
    ax.axes.get_xaxis().set_visible(False)
    ax.axes.get_yaxis().set_visible(False)

    plt.tight_layout()
    fig.savefig(filename, transpaent=True)
    plt.show()
    
