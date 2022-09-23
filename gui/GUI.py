import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfile
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg as figureCanvas
from src.JsonReader import Json
from src.regression import Regression

class GUI:

    def __init__(self):
        self.root = tk.Tk()
        self.frameBtn = tk.Frame(self.root, bg="white")
        self.frameGraph = tk.Frame(self.root, bg="white")
        self.canvas = None
        self.table = None
        self.dataToPredict = None
        self.predictedData = None
        
        self.frameBtn.pack(side=tk.LEFT, expand=True, padx=20)
        self.frameGraph.pack(side=tk.RIGHT, expand=True)
    
    def start(self):
        self.root.title("Linear Regression")
        self.root.geometry("750x450")
        self.root.configure(bg="white")

        loadLabel = tk.Label(self.frameBtn, text="Select a JSON file with the data to operate", bg="white", font="Arial 10")
        loadLabel.pack()

        loadFileBtn = tk.Button(self.frameBtn, text="Load File", command=self.readFile)
        loadFileBtn.pack()

        graphLabel = tk.Label(self.frameGraph, text="Linear Regression Graph", font="Arial 15 bold", bg="white")
        graphLabel.pack(pady=0)

        self.graph("", "", [], [], Regression([], []))

        self.root.mainloop()

    def readFile(self):
        path = askopenfile(mode='r', filetypes=[('JSON Files', '*.json')])
        
        if path is not None:
            xName, yName, xData, yData, dataToPredict = Json(path.name).read()
            self.executeRegression(xName, yName, xData, yData, dataToPredict)

    def executeRegression(self, xName, yName, xData, yData, dataToPredict):
        regression = Regression(xData, yData)
        regression.start()
        predictedData = regression.predict(dataToPredict)
        
        print("For {} = {} the predicted {} is {}".format(xName, dataToPredict, yName, predictedData))
    
        xData.append(dataToPredict)
        yData.append(predictedData)

        self.graph(xName, yName, xData, yData, regression)

    def graph(self, xName, yName, xData, yData, regression):
        self.drawTable(xName, yName, xData, yData, xData[-1] if len(xData) > 0 else 0, yData[-1] if len(yData) > 0 else 0)
        if self.canvas is not None:
            self.canvas.get_tk_widget().destroy()
        
        figure = plt.Figure(figsize=(5, 4), dpi=100)
        ax = figure.add_subplot(111)
        canvas = figureCanvas(figure, self.frameGraph)
        ax.clear()
        canvas.draw()
        canvas.get_tk_widget().pack()
        self.canvas = canvas
        
        ax.scatter(xData, yData, color='red')
        ax.plot(xData, regression.predictList(xData), color='green')
        ax.set_title("{} vs {}".format(xName, yName))
        ax.set_xlabel(xName)
        ax.set_ylabel(yName)

    def drawTable(self, xName, yName, xData, yData, dataToPredict, predictedData):
        if self.table is not None:
            self.table.destroy()
            self.dataToPredict.destroy()
            self.predictedData.destroy()

        table = ttk.Treeview(self.frameBtn, columns=(xName, yName), show="headings")
        table.column(xName, width=100, anchor="center")
        table.column(yName, width=100, anchor="center")
        table.heading(xName, text=xName)
        table.heading(yName, text=yName)

        for i in range(len(xData) - 1):
            table.insert("", tk.END, values=(xData[i], yData[i]))

        dataToPredictLabel = tk.Text(self.frameBtn, height=1, font="Arial 10", bg="white", width=20, borderwidth=0)
        dataToPredictLabel.tag_configure("bold", font="Arial 10 bold")
        dataToPredictLabel.insert(tk.END, "Data to predict: ", "bold")
        dataToPredictLabel.insert(tk.END, dataToPredict)

        predictedDataLabel = tk.Text(self.frameBtn, height=1, font="Arial 10", bg="white", width=20, borderwidth=0)
        predictedDataLabel.tag_configure("bold", font="Arial 10 bold")
        predictedDataLabel.insert(tk.END, "Predicted data: ", "bold")
        predictedDataLabel.insert(tk.END, predictedData)
        
        self.table = table
        self.dataToPredict = dataToPredictLabel
        self.predictedData = predictedDataLabel
        table.pack(pady=30)
        dataToPredictLabel.pack(pady=10)
        predictedDataLabel.pack(pady=10)
