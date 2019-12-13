from django import forms
class PhotoForm(forms.Form):
    image = forms.ImageField()
    cate = forms.CharField(max_length=30, required=False)
    sub = forms.CharField(max_length=30, required=False)
    color = forms.CharField(max_length=30, required=False)
    type = forms.CharField(max_length=30, required=False)
    tag1 = forms.CharField(max_length=30, required=False)
    tag2 = forms.CharField(max_length=30, required=False)
    tag3 = forms.CharField(max_length=30, required=False)
    tag4 = forms.CharField(max_length=30, required=False)
    
class AccountForm(forms.Form):
    name = forms.CharField(max_length=100)
    sex  = forms.CharField(max_length=5)
    age  = forms.IntegerField()
    type = forms.CharField(max_length=30)
class PhotoOneForm(forms.Form):
    image = forms.ImageField()

    #post受付の際に使用、画像ファイル単体で受け取る方法が不明
    sub = forms.CharField(max_length=30,required=False)
    

