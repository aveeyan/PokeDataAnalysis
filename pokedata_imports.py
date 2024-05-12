from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

class PokeTypeInfo:
    def __init__(self, poke_type: str = "Normal"):
        self.poke_type = poke_type

    def type_colors(self):
        color_dict = {
            "Normal": "#A8A77A",
            "Fire": "#EE8130",
            "Water": "#6390F0",
            "Electric": "#F7D02C",
            "Grass": "#7AC74C",
            "Ice": "#96D9D6",
            "Fighting": "#C22E28",
            "Poison": "#A33EA1",
            "Ground": "#E2BF65",
            "Flying": "#A98FF3",
            "Psychic": "#F95587",
            "Bug": "#A6B91A",
            "Rock": "#B6A136",
            "Ghost": "#735797",
            "Dragon": "#6F35FC",
            "Dark": "#705746",
            "Steel": "#B7B7CE",
            "Fairy": "#D685AD"
        }
        return color_dict[self.poke_type]
    
class PokePlot:
    def __init__(self) -> None:
        pass

    def pie_chart(
            self,
            data=[10, 10, 10, 10, 10],
            labels=["एक", "दुइ", "तिन", "चार", "पाँच"],
            autopct:str="%1.1f%%",
            title:str = "A Normal Pie-Chart",
            pctdistance:float = 0.8,
            show_legend:bool = False,
            figsize:tuple = (10, 10)
    ):
        plt.figure(figsize=figsize)
        plt.pie(data, labels=labels, autopct=autopct, pctdistance=pctdistance)
        plt.title(title)
        if show_legend:
            plt.legend(labels, loc="upper right")
        plt.show()