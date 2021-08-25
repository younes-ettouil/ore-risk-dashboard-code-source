import csv, io
from django.shortcuts import render
from django.contrib import messages
from .models import *
from .serializers import *
from django.shortcuts import render
from rest_framework import viewsets

# Create your views here.

class npvView(viewsets.ModelViewSet):
    serializer_class = npv_totalserializer
    queryset = npv_total.objects.all()
    

class datesView(viewsets.ModelViewSet):
    serializer_class = datesSeerializer
    queryset = dates.objects.all()

class nettingsetView(viewsets.ModelViewSet):
    serializer_class = npv_netingsetSeerializer
    queryset = npv_nettingset.objects.all()

class Counterpartyview(viewsets.ModelViewSet):
    serializer_class = npv_Counterpartyserializer
    queryset = npv_Counterparty.objects.all()

class tradeView(viewsets.ModelViewSet):
    serializer_class = npv_tradeSeerializer
    queryset = npv_trade.objects.all()
class creditratingView(viewsets.ModelViewSet):
    serializer_class = npv_creditratingSeerializer
    queryset = npv_creditrating.objects.all()

#============================================

class xpv_totalView(viewsets.ModelViewSet):
    serializer_class = xpv_totalSeerializer
    queryset = xpv_total.objects.all()

class xpv_creditratinglView(viewsets.ModelViewSet):
    serializer_class = xpvcreditratingSeerializer
    queryset = xpv_creditrating.objects.all()

class xpv_NettingsetlView(viewsets.ModelViewSet):
    serializer_class = xpvNettingsetSeerializer
    queryset = xpv_nettingset.objects.all()
class xpv_counterpartyView(viewsets.ModelViewSet):
    serializer_class = xpvCounterpartySeerializer
    queryset = xpv_counterparty.objects.all()

class exposeurtotalView(viewsets.ModelViewSet):
    serializer_class = exposeurTotalSeerializer
    queryset = exposeur_total.objects.all()


class limitsTotalView(viewsets.ModelViewSet):
    serializer_class = LIMITS_TOSeerializer
    queryset = Limits_Total.objects.all()
class limitsCPView(viewsets.ModelViewSet):
    serializer_class = limits_CPSeerializer
    queryset = Limits_Counterparty.objects.all()
class limitsCRView(viewsets.ModelViewSet):
    serializer_class = limits_CRSeerializer
    queryset = Limits_CreditRating.objects.all()
class limitsNSlView(viewsets.ModelViewSet):
    serializer_class = limits_NSSeerializer
    queryset = Limits_Nettingset.objects.all()
class limitsTradeView(viewsets.ModelViewSet):
    serializer_class = limits_TrSeerializer
    queryset = Limits_Trade.objects.all()


class alldataView(viewsets.ModelViewSet):
    serializer_class = alldata_TrSeerializer
    queryset = alldata.objects.all()

class alldata2View(viewsets.ModelViewSet):
    serializer_class = alldata2_TrSeerializer
    queryset = alldata2.objects.all()


# one parameter named request



def csvf_upload_npv_t(request):
    # declaring template
    template = "profile_upload.html"
    data = npv_total.objects.all()
# prompt is a context variable that can have different values      depending on their context
    prompt = {
        'order': 'Uploade NPV_TOTAL ',
        'profiles': data
              }
    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        return render(request, template, prompt)
    csv_file = request.FILES['file']
    # let's check if it is a csv file
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
    data_set = csv_file.read().decode('UTF-8')
    # setup a stream which is when we loop through each line we are able to handle a data in a stream
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = npv_total.objects.update_or_create(
            Total=column[0],
            TradeType=column[1],
            Maturity=column[2],
            MaturityTime=column[3],
            NPV=column[4],
            NpvCurrency=column[5],
            NPV_Base=column[6],
            BaseCurrency=column[7],
            CE_Base=column[8],
        )
        
    
    context = {}
    return render(request, template, context)


def upload_npv_Counterparty(request):
    # declaring template
    template = "profile_upload.html"
    data = npv_Counterparty.objects.all()
# prompt is a context variable that can have different values      depending on their context
    prompt = {
        'order': 'Upload npv_Counterparty',
        'profiles': data
              }
    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        return render(request, template, prompt)
    csv_file = request.FILES['file']
    # let's check if it is a csv file
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
    data_set = csv_file.read().decode('UTF-8')
    # setup a stream which is when we loop through each line we are able to handle a data in a stream
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = npv_Counterparty.objects.update_or_create(
            Counterparty=column[0],
            TradeType=column[1],
            Maturity=column[2],
            MaturityTime=column[3],
            NPV=column[4],
            NpvCurrency=column[5],
            NPV_Base=column[6],
            BaseCurrency=column[7],
            CE_Base=column[8],
        )
    context = {}
    return render(request, template, context)


def csvf_upload_npv_net(request):
    # declaring template
    template = "profile_upload.html"
    data = npv_nettingset.objects.all()
# prompt is a context variable that can have different values      depending on their context
    prompt = {
        'order': 'upload _npv_nettingset ',
        'profiles': data
              }
    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        return render(request, template, prompt)
    csv_file = request.FILES['file']
    # let's check if it is a csv file
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
    data_set = csv_file.read().decode('UTF-8')
    # setup a stream which is when we loop through each line we are able to handle a data in a stream
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = npv_nettingset.objects.update_or_create(
            nettingset=column[0],
            TradeType=column[1],
            Maturity=column[2],
            MaturityTime=column[3],
            NPV=column[4],
            NpvCurrency=column[5],
            NPV_Base=column[6],
            BaseCurrency=column[7],
            CE_Base=column[8],
        )
    context = {}
    return render(request, template, context)

def csvf_upload_npv_trade(request):
    # declaring template
    template = "profile_upload.html"
    data = npv_trade.objects.all()
# prompt is a context variable that can have different values      depending on their context
    prompt = {
        'order': 'upload _npv_trade',
        'profiles': data
              }
    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        return render(request, template, prompt)
    csv_file = request.FILES['file']
    # let's check if it is a csv file
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
    data_set = csv_file.read().decode('UTF-8')
    # setup a stream which is when we loop through each line we are able to handle a data in a stream
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = npv_trade.objects.update_or_create(
            trade=column[0],
            TradeType=column[1],
            Maturity=column[2],
            MaturityTime=column[3],
            NPV=column[4],
            NpvCurrency=column[5],
            NPV_Base=column[6],
            BaseCurrency=column[7],
            CE_Base=column[8],
        )
    context = {}
    return render(request, template, context)

def csvf_upload_npv_creditrating(request):
    # declaring template
    template = "profile_upload.html"
    data = npv_creditrating.objects.all()
# prompt is a context variable that can have different values      depending on their context
    prompt = {
        'order': 'upload _npv_creditrating',
        'profiles': data
              }
    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        return render(request, template, prompt)
    csv_file = request.FILES['file']
    # let's check if it is a csv file
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
    data_set = csv_file.read().decode('UTF-8')
    # setup a stream which is when we loop through each line we are able to handle a data in a stream
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = npv_creditrating.objects.update_or_create(
            Creditrating=column[0],
            TradeType=column[1],
            Maturity=column[2],
            MaturityTime=column[3],
            NPV=column[4],
            NpvCurrency=column[5],
            NPV_Base=column[6],
            BaseCurrency=column[7],
            CE_Base=column[8],
        )
    context = {}
    return render(request, template, context)

def csvf_upload_xpv_total(request):
    # declaring template
    template = "profile_upload.html"
    data = xpv_total.objects.all()
# prompt is a context variable that can have different values      depending on their context
    prompt = {
        'order': 'upload _npv_creditrating',
        'profiles': data
              }
    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        return render(request, template, prompt)
    csv_file = request.FILES['file']
    # let's check if it is a csv file
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
    data_set = csv_file.read().decode('UTF-8')
    # setup a stream which is when we loop through each line we are able to handle a data in a stream
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = xpv_total.objects.update_or_create(
            TradeId=column[0],
            Total=column[1],
            CVA=column[2],
            DVA=column[3],
            FBA=column[4],
            FCA=column[5],
            COLVA=column[6],
            CollateralFloor=column[7],
            AllocatedCVA=column[8],
            AllocatedDVA=column[9],
            AllocationMethod=column[10],
            BaselEPE=column[11],
            BaselEEPE=column[12],
        )
    context = {}
    return render(request, template, context)


def csvf_upload_xpv_creditrating(request):
    # declaring template
    template = "profile_upload.html"
    data = xpv_creditrating.objects.all()
# prompt is a context variable that can have different values      depending on their context
    prompt = {
        'order': 'upload _npv_creditrating',
        'profiles': data
              }
    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        return render(request, template, prompt)
    csv_file = request.FILES['file']
    # let's check if it is a csv file
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
    data_set = csv_file.read().decode('UTF-8')
    # setup a stream which is when we loop through each line we are able to handle a data in a stream
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = xpv_creditrating.objects.update_or_create(
            TradeId=column[0],
            CreditRating=column[1],
            CVA=column[2],
            DVA=column[3],
            FBA=column[4],
            FCA=column[5],
            COLVA=column[6],
            CollateralFloor=column[7],
            AllocatedCVA=column[8],
            AllocatedDVA=column[9],
            AllocationMethod=column[10],
            BaselEPE=column[11],
            BaselEEPE=column[12],
        )
    context = {}
    return render(request, template, context)

def csvf_upload_xpv_nettingset(request):
    # declaring template
    template = "profile_upload.html"
    data = xpv_nettingset.objects.all()
# prompt is a context variable that can have different values      depending on their context
    prompt = {
        'order': 'upload _npv_creditrating',
        'profiles': data
              }
    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        return render(request, template, prompt)
    csv_file = request.FILES['file']
    # let's check if it is a csv file
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
    data_set = csv_file.read().decode('UTF-8')
    # setup a stream which is when we loop through each line we are able to handle a data in a stream
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = xpv_nettingset.objects.update_or_create(
            TradeId=column[0],
            Nettingset=column[1],
            CVA=column[2],
            DVA=column[3],
            FBA=column[4],
            FCA=column[5],
            COLVA=column[6],
            CollateralFloor=column[7],
            AllocatedCVA=column[8],
            AllocatedDVA=column[9],
            AllocationMethod=column[10],
            BaselEPE=column[11],
            BaselEEPE=column[12],
        )
    context = {}
    return render(request, template, context)

def csvf_upload_xpv_counterparty(request):
    # declaring template
    template = "profile_upload.html"
    data = xpv_counterparty.objects.all()
# prompt is a context variable that can have different values      depending on their context
    prompt = {
        'order': 'upload _npv_creditrating',
        'profiles': data
              }
    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        return render(request, template, prompt)
    csv_file = request.FILES['file']
    # let's check if it is a csv file
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
    data_set = csv_file.read().decode('UTF-8')
    # setup a stream which is when we loop through each line we are able to handle a data in a stream
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = xpv_counterparty.objects.update_or_create(
            TradeId=column[0],
            Counterparty=column[1],
            CVA=column[2],
            DVA=column[3],
            FBA=column[4],
            FCA=column[5],
            COLVA=column[6],
            CollateralFloor=column[7],
            AllocatedCVA=column[8],
            AllocatedDVA=column[9],
            AllocationMethod=column[10],
            BaselEPE=column[11],
            BaselEEPE=column[12],
        )
    context = {}
    return render(request, template, context)



def csvf_upload_exposeure_Total(request):
    # declaring template
    template = "profile_upload.html"
    data = exposeur_total.objects.all()
# prompt is a context variable that can have different values      depending on their context
    prompt = {
        'order': 'upload _npv_creditrating',
        'profiles': data
              }
    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        return render(request, template, prompt)
    csv_file = request.FILES['file']
    # let's check if it is a csv file
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
    data_set = csv_file.read().decode('UTF-8')
    # setup a stream which is when we loop through each line we are able to handle a data in a stream
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = exposeur_total.objects.update_or_create(
            Total=column[0],
            Date=column[1],
            Time=column[2],
            EPE=column[3],
            ENE=column[4],
            PFE=column[5],
            ExpectedCollateral=column[6],
            BaselEE=column[7],
            BaselEEE=column[8],
        )
    context = {}
    return render(request, template, context)




def csvf_upload_LCP(request):
    # declaring template
    template = "profile_upload.html"
    data = Limits_Counterparty.objects.all()
# prompt is a context variable that can have different values      depending on their context
    prompt = {
        'order': 'upload LIMITS',
        'profiles': data
              }
    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        return render(request, template, prompt)
    csv_file = request.FILES['file']
    # let's check if it is a csv file
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
    data_set = csv_file.read().decode('UTF-8')
    # setup a stream which is when we loop through each line we are able to handle a data in a stream
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = Limits_Counterparty.objects.update_or_create(
                Limits = column[0],
                NPV = column[1], 
                CE = column[2], 
                EEPE = column[3],
                Total_Exposeur = column[4],
                ColVA = column[5],
                CVA = column[6],
                DVA =column[7], 
                FCA =column[8],
                FBA = column[9],
                FVA =column[10], 
                IM = column[11],
 
        )
    context = {}
    return render(request, template, context)
def csvf_upload_LNS(request):
    # declaring template
    template = "profile_upload.html"
    data = Limits_Nettingset.objects.all()
# prompt is a context variable that can have different values      depending on their context
    prompt = {
        'order': 'upload LIMITS',
        'profiles': data
              }
    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        return render(request, template, prompt)
    csv_file = request.FILES['file']
    # let's check if it is a csv file
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
    data_set = csv_file.read().decode('UTF-8')
    # setup a stream which is when we loop through each line we are able to handle a data in a stream
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = Limits_Nettingset.objects.update_or_create(
                Limits = column[0],
                NPV = column[1], 
                CE = column[2], 
                EEPE = column[3],
                Total_Exposeur = column[4],
                ColVA = column[5],
                CVA = column[6],
                DVA =column[7], 
                FCA =column[8],
                FBA = column[9],
                FVA =column[10], 
                IM = column[11],
 
        )
    context = {}
    return render(request, template, context)
    
def csvf_upload_LTR(request):
    # declaring template
    template = "profile_upload.html"
    data = Limits_Trade.objects.all()
# prompt is a context variable that can have different values      depending on their context
    prompt = {
        'order': 'upload LIMITS',
        'profiles': data
              }
    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        return render(request, template, prompt)
    csv_file = request.FILES['file']
    # let's check if it is a csv file
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
    data_set = csv_file.read().decode('UTF-8')
    # setup a stream which is when we loop through each line we are able to handle a data in a stream
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = Limits_Trade.objects.update_or_create(
                Limits = column[0],
                NPV = column[1], 
                CE = column[2], 
                EEPE = column[3],
                Total_Exposeur = column[4],
                ColVA = column[5],
                CVA = column[6],
                DVA =column[7], 
                FCA =column[8],
                FBA = column[9],
                FVA =column[10], 
                IM = column[11],
 
        )
    context = {}
    return render(request, template, context)    
    
def csvf_upload_LCR(request):
    # declaring template
    template = "profile_upload.html"
    data = Limits_CreditRating.objects.all()
# prompt is a context variable that can have different values      depending on their context
    prompt = {
        'order': 'upload LIMITS',
        'profiles': data
              }
    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        return render(request, template, prompt)
    csv_file = request.FILES['file']
    # let's check if it is a csv file
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
    data_set = csv_file.read().decode('UTF-8')
    # setup a stream which is when we loop through each line we are able to handle a data in a stream
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = Limits_CreditRating.objects.update_or_create(
                Limits = column[0],
                NPV = column[1], 
                CE = column[2], 
                EEPE = column[3],
                Total_Exposeur = column[4],
                ColVA = column[5],
                CVA = column[6],
                DVA =column[7], 
                FCA =column[8],
                FBA = column[9],
                FVA =column[10], 
                IM = column[11],
 
        )
    context = {}
    return render(request, template, context)
def csvf_upload_LT(request):
    # declaring template
    template = "profile_upload.html"
    data = Limits_Total.objects.all()
# prompt is a context variable that can have different values      depending on their context
    prompt = {
        'order': 'upload LIMITS',
        'profiles': data
              }
    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        return render(request, template, prompt)
    csv_file = request.FILES['file']
    # let's check if it is a csv file
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
    data_set = csv_file.read().decode('UTF-8')
    # setup a stream which is when we loop through each line we are able to handle a data in a stream
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = Limits_Total.objects.update_or_create(
                Limits = column[0],
                NPV = column[1], 
                CE = column[2], 
                EEPE = column[3],
                Total_Exposeur = column[4],
                ColVA = column[5],
                CVA = column[6],
                DVA =column[7], 
                FCA =column[8],
                FBA = column[9],
                FVA =column[10], 
                IM = column[11],
 
        )
    context = {}
    return render(request, template, context)    




    
def csvf_upload_ad(request):
    # declaring template
    template = "profile_upload.html"
    data = alldata.objects.all()
# prompt is a context variable that can have different values      depending on their context
    prompt = {
        'order': 'upload LIMITS',
        'profiles': data
              }
    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        return render(request, template, prompt)
    csv_file = request.FILES['file']
    # let's check if it is a csv file
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
    data_set = csv_file.read().decode('UTF-8')
    # setup a stream which is when we loop through each line we are able to handle a data in a stream
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = alldata.objects.update_or_create(
                creditrating = column[0],
                counterparty = column[1], 
                nettingset = column[2], 
                trade = column[3],
                metrice = column[4],
                limitValue = column[5],
                ConsumptionValue = column[6],
                date =column[7], 
                cons =column[8],
        )
    context = {}
    return render(request, template, context) 




def csvf_upload_ad2(request):
    # declaring template
    template = "profile_upload.html"
    data = alldata2.objects.all()
# prompt is a context variable that can have different values      depending on their context
    prompt = {
        'order': 'upload LIMITS',
        'profiles': data
              }
    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        return render(request, template, prompt)
    csv_file = request.FILES['file']
    # let's check if it is a csv file
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
    data_set = csv_file.read().decode('UTF-8')
    # setup a stream which is when we loop through each line we are able to handle a data in a stream
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = alldata2.objects.update_or_create(
                creditrating = column[0],
                counterparty = column[1], 
                nettingset = column[2], 
                trade = column[3],
                metrice = column[4],
                limitValue = column[5],
                ConsumptionValue = column[6],
                date =column[7], 
                cons =column[8],
        )
    context = {}
    return render(request, template, context)    