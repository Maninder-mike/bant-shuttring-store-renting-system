from PyQt5.QtChart import QChart, QChartView, QPieSeries, QPieSlice
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen


def create_piechart():
    series = QPieSeries()
    # append all values with a sum of 360
    series.append("size 5", 5)
    series.append("size 10", 10)
    series.append("size 30", 30)
    series.append("size 45", 45)
    series.append("size 90", 90)
    series.append("size 180", 180)

    # adding slice
    slice = QPieSlice()
    slice = series.slices()[2]
    slice.setExploded(True)
    slice.setLabelVisible(True)
    slice.setPen(QPen(Qt.darkGreen, 1))
    slice.setBrush(Qt.green)
    slice = series.slices()[4]
    slice.setExploded(False)
    slice.setLabelVisible(True)
    slice.setPen(QPen(Qt.red, 1))
    # slice.setBrush(Qt.blue)

    # create chart
    chart = QChart()
    # chart.legend().hide()
    chart.addSeries(series)
    chart.createDefaultAxes()
    chart.setAnimationOptions(QChart.SeriesAnimations)
    chart.setTitle("The all 360 on  chart .")

    chart.legend().setVisible(True)
    chart.legend().setAlignment(Qt.AlignBottom)

    chartview = QChartView(chart)
    chartview.setRenderHint(QPainter.Antialiasing)
