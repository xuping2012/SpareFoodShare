from pyecharts import options as opts
from pyecharts.charts import Bar, Grid, Line, Liquid, Page, Pie, Tab
from pyecharts.commons.utils import JsCode
from pyecharts.components import Table
from pyecharts.faker import Faker
from . import ReadSQL as ReadSQL
import pdfkit
import os


def bar_datazoom_slider(Data):
    Date, Cont = ReadSQL.date_OrderCount(Data)
    c = (
        Bar()
            .add_xaxis(Date)
            .add_yaxis("Date", Cont)
            .set_global_opts(
            title_opts=opts.TitleOpts(title="Number of Orders Per Day"),
            datazoom_opts=[opts.DataZoomOpts( range_start = 0, range_end = 5)],
        )
    )
    return c


def line_markpoint(data):
    loc, avgPrice, avgQuan = ReadSQL.location_infor(data)
    c = (
        Line()
            .add_xaxis(loc)
            .add_yaxis(
            "Price",
            avgPrice,
            markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="last")]),
        )
            .add_yaxis(
            "Quantity",
            avgQuan,
            markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="last")]),
        )
            .set_global_opts(title_opts=opts.TitleOpts(title="Regional Quantity&Price"))
    )
    return c


def pie_rosetype(data):
    cata, cont = ReadSQL.cataCount(data)
    c = (
        Pie()
        #     .add(
        #     "",
        #     [list(z) for z in zip(cata, cont)],
        #     radius=["30%", "75%"],
        #     center=["25%", "50%"],
        #     rosetype="radius",
        #     label_opts=opts.LabelOpts(is_show=False),
        # )r
            .add(
            "",
            [list(z) for z in zip(cata, cont)],
            radius=["30%", "75%"],
            center=["35%", "50%"],
            rosetype="area",
        )
            .set_global_opts(title_opts=opts.TitleOpts(title="Distribution of Food Type"))
    )
    return c


def grid_mutil_yaxis(data):
    x_data, price, quan = ReadSQL.q_infor(data)
    x_data = ['2021Q1', '2021Q2', '2021Q3', '2021Q4', '2022Q1']
    # bar = (
    #     Bar()
    #     .add_xaxis(x_data)
    #     .add_yaxis(
    #         "Quarterly Average Transaction Value",
    #         price,
    #         yaxis_index=0,
    #         color="#d14a61",
    #     )
    #     # .add_yaxis(
    #     #     "Quarterly Average Number of Products",
    #     #     quan,
    #     #     yaxis_index=1,
    #     #     color="#5793f3",
    #     # )
    #     .extend_axis(
    #         yaxis=opts.AxisOpts(
    #             name=" Transaction Value",
    #             type_="value",
    #             min_=0,
    #             max_=1000000,
    #             position="right",
    #             axisline_opts=opts.AxisLineOpts(
    #                 linestyle_opts=opts.LineStyleOpts(color="#5793f3")
    #             ),
    #             axislabel_opts=opts.LabelOpts(formatter="{value} ml"),
    #         )
    #     )
    #     # .extend_axis(
    #     #     yaxis=opts.AxisOpts(
    #     #         type_="value",
    #     #         name="Number of Products",
    #     #         min_=0,
    #     #         max_=2000,
    #     #         position="left",
    #     #         axisline_opts=opts.AxisLineOpts(
    #     #             linestyle_opts=opts.LineStyleOpts(color="#675bba")
    #     #         ),
    #     #         axislabel_opts=opts.LabelOpts(formatter="{value} "),
    #     #         splitline_opts=opts.SplitLineOpts(
    #     #             is_show=True, linestyle_opts=opts.LineStyleOpts(opacity=1)
    #     #         ),
    #     #     )
    #     # )
    #     .set_global_opts(
    #         # yaxis_opts=opts.AxisOpts(
    #         #     name="Number of Products",
    #         #     min_=0,
    #         #     max_=2000,
    #         #     position="right",
    #         #     offset=80,
    #         #     axisline_opts=opts.AxisLineOpts(
    #         #         linestyle_opts=opts.LineStyleOpts(color="#5793f3")
    #         #     ),
    #         #     axislabel_opts=opts.LabelOpts(formatter="{value} ml"),
    #         # ) ,
    #         title_opts=opts.TitleOpts(title="Grid-多 Y 轴示例"),
    #         tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
    #     )
    # )
    #
    # line = (
    #     Line()
    #     .add_xaxis(x_data)
    #     .add_yaxis(
    #         "Number of Products",
    #         quan,
    #         yaxis_index=2,
    #         color="#675bba",
    #         label_opts=opts.LabelOpts(is_show=False),
    #     )
    # )
    #
    # bar.overlap(line)
    # return Grid().add(
    #     bar, opts.GridOpts(pos_left="5%", pos_right="20%"), is_control_axis_index=True
    # )
    c = (
        Bar()
            .add_xaxis(x_data)
            .add_yaxis("Price Value", price)
            .add_yaxis("Number of Products", quan)
            .set_global_opts(
            title_opts=opts.TitleOpts(title="Quarterly Prices and Quantities")

        ))
    return c


def liquid_data_precision() -> Liquid:
    c = (
        Liquid()
            .add(
            "Foods Marked as of Interest",
            ReadSQL.food_interested(),
            label_opts=opts.LabelOpts(
                font_size=50,
                formatter=JsCode(
                    """function (param) {
                        return (Math.floor(param.value * 10000) / 100) + '%';
                    }"""
                ),
                position="inside",
            ),
        )
            .set_global_opts(title_opts=opts.TitleOpts(title="Foods Marked as of Interest"))
    )
    return c


def table_base():
    table = Table()
    headers, rows = ReadSQL.getTable()
    table.add(headers, rows).set_global_opts(
        title_opts=opts.ComponentTitleOpts(title="Client Information Sheet")
    )
    return table


def page_draggable_layout():
    data = ReadSQL.read_data_from_sql()
    page = Page(layout=Page.DraggablePageLayout)
    page.add(
        bar_datazoom_slider(data),
        line_markpoint(data),
        pie_rosetype(data),
        grid_mutil_yaxis(data),
        #liquid_data_precision(),
        table_base(),
    )
    page.render("templates/dashboardGragh.html")
    Page.save_resize_html('templates/dashboardGragh.html',
                          cfg_file='templates/chart_config.json',
                          dest='templates/dashboardGragh.html')

def CreateDashboard():
    page_draggable_layout()
    data = ReadSQL.read_data_from_sql()
    tab = Tab()
    tab.add( bar_datazoom_slider(data), "Number of Orders Per Day")
    tab.add(line_markpoint(data), "Regional Quantity & Price")
    tab.add(pie_rosetype(data), "Distribution of Food Types")
    tab.add(grid_mutil_yaxis(data), "Quarterly Prices and Quantities")
    #tab.add(liquid_data_precision(), "Foods Marked as of Interest")
    tab.add(table_base(), "Client Information Sheet")
    tab.render("tab_base.html")
    path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
    #path_wkhtmltopdf = r'/usr/bin/wkhtmltopdf'
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
    path = os.getcwd()
    print(path)
    pdfkit.from_file('templates/dashboardGragh.html', 'static/dashboardGragh.pdf', configuration=config)

if __name__ == "__main__":
    page_draggable_layout()
    data = ReadSQL.read_data_from_sql()
    tab = Tab()
    tab.add( bar_datazoom_slider(data), "Number of Orders Per Day")
    tab.add(line_markpoint(data), "Regional Quantity & Price")
    tab.add(pie_rosetype(data), "Distribution of Food Types")
    tab.add(grid_mutil_yaxis(data), "Quarterly Prices and Quantities")
    #tab.add(liquid_data_precision(), "Foods Marked as of Interest")
    tab.add(table_base(), "Client Information Sheet")
    tab.render("tab_base.html")
    path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
    # path_wkhtmltopdf = r'/usr/bin/wkhtmltopdf'
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
    pdfkit.from_file('dashboardGragh.html', 'dashboardGragh.pdf', configuration=config)
