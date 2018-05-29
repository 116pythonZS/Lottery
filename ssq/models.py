from django.db import models


# Create your models here.


class SSQModel(models.Model):
    serialNo = models.IntegerField(db_column='serialNo', primary_key=True)
    pub_date = models.CharField(db_column='pub_date', max_length=10, null=True)
    balls = models.TextField(db_column='balls', null=True)
    origin = models.TextField(db_column='origin', null=True)

    def __lt__(self, other):
        return self.serialNo < other.serialNo

    def __gt__(self, other):
        return self.serialNo > other.serialNo

    class Meta:
        db_table = 'ssq'


class SSQTJSimpleModel(models.Model):
    serialNo = models.IntegerField(db_column='serialNo', primary_key=True)
    pub_date = models.CharField(db_column='pub_date', max_length=10, null=True)
    balls = models.TextField(db_column='balls', null=True)
    red01 = models.IntegerField(db_column='red01', null=True)
    red02 = models.IntegerField(db_column='red02', null=True)
    red03 = models.IntegerField(db_column='red03', null=True)
    red04 = models.IntegerField(db_column='red04', null=True)
    red05 = models.IntegerField(db_column='red05', null=True)
    red06 = models.IntegerField(db_column='red06', null=True)
    red07 = models.IntegerField(db_column='red07', null=True)
    red08 = models.IntegerField(db_column='red08', null=True)
    red09 = models.IntegerField(db_column='red09', null=True)
    red10 = models.IntegerField(db_column='red10', null=True)
    red11 = models.IntegerField(db_column='red11', null=True)
    red12 = models.IntegerField(db_column='red12', null=True)
    red13 = models.IntegerField(db_column='red13', null=True)
    red14 = models.IntegerField(db_column='red14', null=True)
    red15 = models.IntegerField(db_column='red15', null=True)
    red16 = models.IntegerField(db_column='red16', null=True)
    red17 = models.IntegerField(db_column='red17', null=True)
    red18 = models.IntegerField(db_column='red18', null=True)
    red19 = models.IntegerField(db_column='red19', null=True)
    red20 = models.IntegerField(db_column='red20', null=True)
    red21 = models.IntegerField(db_column='red21', null=True)
    red22 = models.IntegerField(db_column='red22', null=True)
    red23 = models.IntegerField(db_column='red23', null=True)
    red24 = models.IntegerField(db_column='red24', null=True)
    red25 = models.IntegerField(db_column='red25', null=True)
    red26 = models.IntegerField(db_column='red26', null=True)
    red27 = models.IntegerField(db_column='red27', null=True)
    red28 = models.IntegerField(db_column='red28', null=True)
    red29 = models.IntegerField(db_column='red29', null=True)
    red30 = models.IntegerField(db_column='red30', null=True)
    red31 = models.IntegerField(db_column='red31', null=True)
    red32 = models.IntegerField(db_column='red32', null=True)
    red33 = models.IntegerField(db_column='red33', null=True)

    blue01 = models.IntegerField(db_column='blue01', null=True)
    blue02 = models.IntegerField(db_column='blue02', null=True)
    blue03 = models.IntegerField(db_column='blue03', null=True)
    blue04 = models.IntegerField(db_column='blue04', null=True)
    blue05 = models.IntegerField(db_column='blue05', null=True)
    blue06 = models.IntegerField(db_column='blue06', null=True)
    blue07 = models.IntegerField(db_column='blue07', null=True)
    blue08 = models.IntegerField(db_column='blue08', null=True)
    blue09 = models.IntegerField(db_column='blue09', null=True)
    blue10 = models.IntegerField(db_column='blue10', null=True)
    blue11 = models.IntegerField(db_column='blue11', null=True)
    blue12 = models.IntegerField(db_column='blue12', null=True)
    blue13 = models.IntegerField(db_column='blue13', null=True)
    blue14 = models.IntegerField(db_column='blue14', null=True)
    blue15 = models.IntegerField(db_column='blue15', null=True)
    blue16 = models.IntegerField(db_column='blue16', null=True)

    def __setitem__(self, k, v):
        self.k = v

    class Meta:
        db_table = 'ssq_tj1'
