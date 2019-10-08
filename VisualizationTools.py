# -*- coding: UTF-8 -*
import matplotlib.pyplot as plt
import matplotlib


def plot_bar(x_list, y_list, title):

    matplotlib.rcParams['axes.unicode_minus'] = False
    plt.ioff()
    # plt.barh(range(len(x_list)), y_list, tick_label=x_list)
    plt.barh(range(len(x_list)), y_list)
    plt.title(title)
    # for x,y in zip(range(len(x_list)), y_list):
    #     plt.text(y + 0.3, x - 0.15, '%.0f' % y, ha='center', va='bottom', fontsize=11)
    path_pc = u"./bars/"
    filename = "".join([title, u".png"])
    path_filename = "".join([path_pc, filename])
    plt.savefig(path_filename)
    # plt.show()
    plt.close()


def plot_hist(eqy_list, title="return_distribution"):

    plt.ioff()
    plt.hist(eqy_list, bins=100)
    path_pc = u"./bars/"
    filename = "".join([title, u".png"])
    path_filename = "".join([path_pc, filename])
    plt.savefig(path_filename)
    plt.show()

