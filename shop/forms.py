from django import forms
from .models import Product

class RegisterForm(forms.Form):
    name = forms.CharField(
        error_messages={'required':"상품명을 입력하세요."},
        max_length = 32, label = "음식명"
    )

    description = forms.CharField(
        error_messages={'required':"음식 설명을 입력하세요"},
        label = "음식 설명"
    )
    
    image = forms.ImageField(
        error_messages={'required': "음식사진을 넣으세요"}
    )
    price = forms.DecimalField(
        max_digits=10,decimal_places=2,
        error_messages={'required' : "가격을 입력하세요."},
        label = "가격"
    )
    stock = forms.IntegerField(
        error_messages={'required':"수량을 입력하세요"},
        label = "재고"
    )
    

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        image = cleaned_data.get('image')
        description = cleaned_data.get('description')
        price = cleaned_data.get('price')
        stock = cleaned_data.get('stock')
        

        if not (name and image and description and price and stock):
            self.add_error('name', "필수 항목입니다")
            self.add_error('image', "필수 항목입니다")
            self.add_error('description', "필수 항목입니다")
            self.add_error('price', "필수 항목입니다")
            self.add_error('stock', "필수 항목입니다")
            
       