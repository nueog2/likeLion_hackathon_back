from django.shortcuts import render

# Create your views here.

# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .models import Order, Product_Order , Product , Category

# @api_view(['POST'])
# def Product_Order(request):
#     # 주문 생성 로직
#     # ...

#     # 대기번호 할당
#     order_id = Order.id  # 주문이 생성되면 해당 주문의 id를 가져옴
#     product_orders = Product_Order.objects.filter(order=order_id).order_by('created_at')
#     order_num = product_orders.count() + 1
#     Order.order_num = order_num
#     Order.save()

#     return Response({'message': '주문이 생성되었습니다.'}, status=status.HTTP_201_CREATED)
#  #  주문이 생성되는 시점에 해당 주문의 id 값을 가져와서 그 주문에 속하는 ProductOrder들을 생성된 시간 기준으로 정렬한 뒤,
#  #  해당 주문의 대기번호를 결정하고 저장하는 방식. 이후 order.order_num 값을 화면에 띄우면 대기번호가 표시됨
