from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

class Plot:
    def __init__(self):
        None
    
    def pie_chart(
            self,
            data,
            labels,
            autopct="%1.1f%%",
            title:str = "A Normal Pie-Chart",
    ):
        plt.pie(data, labels=labels, autopct=autopct)
        plt.title(title)
        plt.show()