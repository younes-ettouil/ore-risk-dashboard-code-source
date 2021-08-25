from django.contrib import admin
from django.urls import path,include
from csvApp import views
from rest_framework import  routers
router = routers.DefaultRouter()
router.register(r'dates',views.datesView,'date')
router.register(r'npvs',views.npvView,'npv')
router.register(r'counterpartys',views.Counterpartyview,'counterparty')
router.register(r'nettingsets',views.nettingsetView,'nettingset')
router.register(r'trades',views.tradeView,'trade')
router.register(r'creditratings',views.creditratingView,'creditrating')
router.register(r'xpvCPs',views.xpv_counterpartyView,'xpvCP')
router.register(r'xpvNss',views.xpv_NettingsetlView,'xpvNs')
router.register(r'xpvCRs',views.xpv_creditratinglView,'xpvCR')
router.register(r'xpvs',views.xpv_totalView,'xpv')
router.register(r'exposeurT',views.exposeurtotalView,'exposeur')
router.register(r'Limits_total',views.limitsTotalView,'lt')
router.register(r'limite_CR',views.limitsCRView,'CR')
router.register(r'Limits_CP',views.limitsCPView,'CP')
router.register(r'Limits_NS',views.limitsNSlView,'NS')
router.register(r'Limits_TR',views.limitsTradeView,'TR')
router.register(r'allData',views.alldataView,'alldata')
router.register(r'allData2',views.alldata2View,'alldata2')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(router.urls)),
    path('', views.csvf_upload_npv_t),
    path('upload-npvT/', views.csvf_upload_npv_t),
    path('upload-npvC/',views.upload_npv_Counterparty),
    path('upload-npvN/',views.csvf_upload_npv_net),
    path('upload-npvTr/',views.csvf_upload_npv_trade),
    path('upload-npvCr/',views.csvf_upload_npv_creditrating),
    path('upload-xpvt/',views.csvf_upload_xpv_total),
    path('upload-xpvCounteP/',views.csvf_upload_xpv_counterparty),
    path('upload-xpvcredir/',views.csvf_upload_xpv_creditrating),
    path('upload-xpvNetts/',views.csvf_upload_xpv_nettingset),
    path('upload-exposeurt/',views.csvf_upload_exposeure_Total),
    path('upload-LT/',views.csvf_upload_LT),
    path('upload-CR/',views.csvf_upload_LCR),
    path('upload-CP/',views.csvf_upload_LCP),
    path('upload-NS/',views.csvf_upload_LNS),
    path('upload-TR/',views.csvf_upload_LTR),
    path('upload-ad/',views.csvf_upload_ad),
    path('upload-ad2/',views.csvf_upload_ad2),
    
]

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     # path('', include('csvApp.url')),
#     path('upload-csv/', csvf_upload_npv_t, name="profile_upload"),
#     path('upload-csv-nc/', npv_Counterparty1, name="npv_Counterparty"),
# ]
