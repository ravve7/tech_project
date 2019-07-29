from django.shortcuts import render
from django.http import HttpResponse
from ravi.models import Products, inventory
from ravi.forms import ProductForm
from django.template import Context
from rest_framework import viewsets, permissions
from .serializers import ProductSerializer, inventorySerializer
import plotly.graph_objs as go
from plotly.offline import plot
from  datetime import datetime
from . import jpqrser
import requests



class ProductViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer


class inventoryViewSet(viewsets.ModelViewSet):
    queryset = inventory.objects.all()
    serializer_class = inventorySerializer


def HomePageView(request):

    context = {}
    context['form'] = ProductForm()
    context['products']=[]
    data = jpqrser.all_data()
    for each in data:
        p_name=each
        for dt in data[p_name]:
            print("---->"+each)
            p_date=datetime.strptime(str(dt[0][:24]).split(".")[0], "%Y-%m-%dT%H:%M:%S")
            p_inv=dt[1]
            l_data= dict()
            l_data.setdefault('name', p_name)
            l_data.setdefault('date', (p_date).strftime("%d-%m-%Y %H:%M:%S"))
            l_data.setdefault('inv', p_inv)
            context['products'].append(l_data)



    # context['products'] = Products.objects.values(
    #     'id', 'product_name', 'inventory__date', 'inventory__inventory_level')
    for i in context['products']:
        print(i['name'])
    inv=[]
    date=[]

    if request.method == "POST":

        form = ProductForm(request.POST)

        if form.is_valid():

            prod_name=str(form.cleaned_data["selectproduct"])


            # id_of_product = (Products.objects.filter(product_name=str(
            #     form.cleaned_data["selectproduct"])).values_list('pk', flat=True)[0])
            #
            # name = Products.objects.filter(pk=id_of_product).values()[
            #     0]['product_name']
            # context['prod_name'] = name
            #
            # for h in inventory.objects.filter(
            #         products_id=id_of_product):
            #     date.append((h.date).strftime("%d-%m-%Y %H:%M:%S"))
            #     inv.append(h.inventory_level)

            getData=data[prod_name]
            context['products'] = []
            print(getData)
            for dt in getData:
                date.append(datetime.strptime(str(dt[0][:24]).split(".")[0], "%Y-%m-%dT%H:%M:%S"))
                inv.append(dt[1])
                p_date = datetime.strptime(str(dt[0][:24]).split(".")[0], "%Y-%m-%dT%H:%M:%S")
                p_inv = dt[1]
                l_data = dict()
                l_data.setdefault('name', prod_name)
                l_data.setdefault('date', datetime.strptime(str(dt[0][:24]).split(".")[0], "%Y-%m-%dT%H:%M:%S"))
                l_data.setdefault('inv', dt[1])
                context['products'].append(l_data)

            trace1 = go.Scatter(
                x=date,
                y=inv
            )

            data = [trace1]
            layout = go.Layout(

                width=900,
                height=600,
                #title=go.layout.Title(text="chart : {} ".format(prod_name)),

                xaxis=dict(
                    autorange=True
                ),
                yaxis=dict(
                    autorange=True
                )
            )
            fig = go.Figure(data=data, layout=layout)
            fig.update_xaxes(title_text='Date')
            fig.update_yaxes(title_text='Inventory_level')
            plot_div = plot(fig, output_type='div', include_plotlyjs=False)
            context['plot'] = plot_div


    return render(request, 'HomePage.html', context)
