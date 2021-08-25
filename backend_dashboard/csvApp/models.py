from django.db import models

# Create your models here.
class dates(models.Model):
    date=models.CharField(max_length=150)
    def __str__(self):
        return self.date
#===============================================================================================================================#
class npv_total(models.Model):
    date=models.DateField(null=True)
    Total = models.CharField(max_length=150)
    TradeType = models.CharField(max_length=150)
    Maturity = models.CharField(max_length=150)
    MaturityTime = models.CharField(max_length=150)
    NPV = models.CharField(max_length=150)
    NpvCurrency=models.CharField(max_length=150)
    NPV_Base=models.FloatField()
    BaseCurrency=models.CharField(max_length=150)
    CE_Base=models.FloatField()
    def __str__(self):
        return self.Total



class npv_Counterparty(models.Model):
    date=models.DateField(null=True)
    Counterparty = models.CharField(max_length=150)
    TradeType = models.CharField(max_length=150)
    Maturity = models.CharField(max_length=150)
    MaturityTime = models.CharField(max_length=150)
    NPV = models.CharField(max_length=150)
    NpvCurrency=models.CharField(max_length=150)
    NPV_Base=models.FloatField()
    BaseCurrency=models.CharField(max_length=150)
    CE_Base=models.FloatField()
    def __str__(self):
        return self.Counterparty

class npv_creditrating(models.Model):
    date=models.DateField(null=True)
    Creditrating = models.CharField(max_length=150)
    TradeType = models.CharField(max_length=150)
    Maturity = models.CharField(max_length=150)
    MaturityTime = models.CharField(max_length=150)
    NPV = models.CharField(max_length=150)
    NpvCurrency=models.CharField(max_length=150)
    NPV_Base=models.FloatField()
    BaseCurrency=models.CharField(max_length=150)
    CE_Base=models.FloatField()
    def __str__(self):
        return self.Creditrating

class npv_nettingset(models.Model):
    date=models.DateField(null=True)
    nettingset = models.CharField(max_length=150)
    TradeType = models.CharField(max_length=150)
    Maturity = models.CharField(max_length=150)
    MaturityTime = models.CharField(max_length=150)
    NPV = models.CharField(max_length=150)
    NpvCurrency=models.CharField(max_length=150)
    NPV_Base=models.FloatField()
    BaseCurrency=models.CharField(max_length=150)
    CE_Base=models.FloatField()
   
    def __str__(self):
        return self.nettingset

class npv_trade(models.Model):
    date=models.DateField(null=True)
    trade = models.CharField(max_length=150)
    TradeType = models.CharField(max_length=150)
    Maturity = models.CharField(max_length=150)
    MaturityTime = models.CharField(max_length=150)
    NPV = models.CharField(max_length=150)
    NpvCurrency=models.CharField(max_length=150)
    NPV_Base=models.FloatField()
    BaseCurrency=models.CharField(max_length=150)
    CE_Base=models.FloatField()
    def __str__(self):
        return self.trade
#==================================================Xpv_Files=============================================================================#
class xpv_total(models.Model):
    date=models.DateField(null=True)
    TradeId = models.CharField(max_length=150)
    Total = models.CharField(max_length=150)
    CVA = models.FloatField()
    DVA = models.FloatField()
    FBA = models.FloatField()
    FCA=models.FloatField()
    COLVA=models.FloatField()
    CollateralFloor=models.FloatField()
    AllocatedCVA=models.FloatField()
    AllocatedDVA=models.FloatField()
    AllocationMethod=models.CharField(max_length=150)
    BaselEPE=models.FloatField()
    BaselEEPE=models.FloatField()
    def __str__(self):
        return self.TradeId

class xpv_creditrating(models.Model):
    date=models.DateField(null=True)
    TradeId = models.CharField(max_length=150)
    CreditRating = models.CharField(max_length=150)
    CVA = models.FloatField()
    DVA = models.FloatField()
    FBA = models.FloatField()
    FCA=models.FloatField()
    COLVA=models.FloatField()
    CollateralFloor=models.FloatField()
    AllocatedCVA=models.FloatField()
    AllocatedDVA=models.FloatField()
    AllocationMethod=models.CharField(max_length=150)
    BaselEPE=models.FloatField()
    BaselEEPE=models.FloatField()
    def __str__(self):
        return self.TradeId

class xpv_counterparty(models.Model):
    date=models.DateField(null=True)
    TradeId = models.CharField(max_length=150)
    Counterparty = models.CharField(max_length=150)
    CVA = models.FloatField()
    DVA = models.FloatField()
    FBA = models.FloatField()
    FCA=models.FloatField()
    COLVA=models.FloatField()
    CollateralFloor=models.FloatField()
    AllocatedCVA=models.FloatField()
    AllocatedDVA=models.FloatField()
    AllocationMethod=models.CharField(max_length=150)
    BaselEPE=models.FloatField()
    BaselEEPE=models.FloatField()
    def __str__(self):
        return self.TradeId

class xpv_nettingset(models.Model):
    date=models.DateField(null=True)
    TradeId = models.CharField(max_length=150)
    Nettingset = models.CharField(max_length=150)
    CVA = models.FloatField()
    DVA = models.FloatField()
    FBA = models.FloatField()
    FCA=models.FloatField()
    COLVA=models.CharField(max_length=150)
    CollateralFloor=models.CharField(max_length=150)
    AllocatedCVA=models.CharField(max_length=150)
    AllocatedDVA=models.FloatField()
    AllocationMethod=models.CharField(max_length=150)
    BaselEPE=models.FloatField()
    BaselEEPE=models.FloatField()
    def __str__(self):
        return self.TradeId
#===========================================ExposeureTotal=============================
class exposeur_total(models.Model):
    Total=models.CharField(max_length=150)
    Date= models.DateField(null=True)
    Time= models.CharField(max_length=150)
    EPE= models.FloatField()
    ENE= models.FloatField()
    PFE= models.FloatField()
    ExpectedCollateral=models.FloatField()
    BaselEE=models.FloatField()
    BaselEEE=models.FloatField()
    def __str__(self):
        return self.Total
#____________________________Limits______________________________________#

class  Limits_Counterparty(models.Model):
        Limits = models.CharField(max_length=150) 
        NPV = models.CharField(max_length=150) 
        CE = models.FloatField() 
        EEPE = models.FloatField()  
        Total_Exposeur = models.CharField(max_length=150) 
        ColVA = models.CharField(max_length=150) 
        CVA = models.FloatField() 
        DVA = models.FloatField() 
        FCA =models.FloatField() 
        FBA = models.FloatField() 
        FVA =models.FloatField() 
        IM = models.CharField(max_length=150)
         
class  Limits_CreditRating(models.Model):
        Limits = models.CharField(max_length=150) 
        NPV = models.CharField(max_length=150) 
        CE = models.FloatField() 
        EEPE = models.FloatField()  
        Total_Exposeur = models.CharField(max_length=150) 
        ColVA = models.CharField(max_length=150) 
        CVA = models.FloatField() 
        DVA = models.FloatField() 
        FCA =models.FloatField() 
        FBA = models.FloatField() 
        FVA =models.FloatField() 
        IM = models.CharField(max_length=150)
        def __str__(self):
            return self.Limits  
class  Limits_Nettingset(models.Model):
        Limits = models.CharField(max_length=150) 
        NPV = models.CharField(max_length=150) 
        CE = models.FloatField() 
        EEPE = models.FloatField()  
        Total_Exposeur = models.CharField(max_length=150) 
        ColVA = models.CharField(max_length=150) 
        CVA = models.FloatField() 
        DVA = models.FloatField() 
        FCA =models.FloatField() 
        FBA = models.FloatField() 
        FVA =models.FloatField() 
        IM = models.CharField(max_length=150)
        def __str__(self):
            return self.Limits  
class  Limits_Trade(models.Model):
        Limits = models.CharField(max_length=150) 
        NPV = models.CharField(max_length=150) 
        CE = models.FloatField() 
        EEPE = models.FloatField()  
        Total_Exposeur = models.CharField(max_length=150) 
        ColVA = models.CharField(max_length=150) 
        CVA = models.CharField(max_length=150)
        DVA = models.CharField(max_length=150)
        FCA =models.CharField(max_length=150) 
        FBA = models.CharField(max_length=150)
        FVA =models.CharField(max_length=150)
        IM = models.CharField(max_length=150)
        def __str__(self):
            return self.Limits 
class  Limits_Total(models.Model):
        Limits = models.CharField(max_length=150) 
        NPV = models.CharField(max_length=150) 
        CE = models.FloatField() 
        EEPE = models.FloatField()  
        Total_Exposeur = models.CharField(max_length=150) 
        ColVA = models.CharField(max_length=150) 
        CVA = models.FloatField() 
        DVA = models.FloatField() 
        FCA =models.FloatField() 
        FBA = models.FloatField() 
        FVA =models.FloatField() 
        IM = models.CharField(max_length=150) 
        def __str__(self):
            return self.Limits


class alldata(models.Model):
    creditrating=models.CharField(max_length=255)
    counterparty=models.CharField(max_length=255)
    nettingset=models.CharField(max_length=255)
    trade=models.CharField(max_length=255)
    metrice=models.CharField(max_length=255)
    limitValue=models.CharField(max_length=255)
    ConsumptionValue=models.CharField(max_length=255)
    date=models.CharField(max_length=255,null=True)
    cons=models.CharField(max_length=255)
    def __str__(self):
        return self.creditrating
    

class alldata2(models.Model):
    creditrating=models.CharField(max_length=255)
    counterparty=models.CharField(max_length=255)
    nettingset=models.CharField(max_length=255)
    trade=models.CharField(max_length=255)
    metrice=models.CharField(max_length=255)
    limitValue=models.CharField(max_length=255)
    ConsumptionValue=models.CharField(max_length=255)
    date=models.CharField(max_length=255,null=True)
    cons=models.CharField(max_length=255)
    def __str__(self):
        return self.creditrating