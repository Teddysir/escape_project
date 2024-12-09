from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import KeyStatus
from django.contrib.auth.decorators import login_required


def acquire_key(request):
    if request.method == "POST":
        # 익명 사용자를 위한 임시 열쇠 상태 생성
        user_id = request.session.get("user_id", None)
        if not user_id:
            user_id = request.session["user_id"] = f"anon_{request.session.session_key}"

        # KeyStatus 모델로 열쇠 상태 관리
        key_status, created = KeyStatus.objects.get_or_create(user_id=user_id)
        key_status.has_key = True
        key_status.save()
        return JsonResponse({"message": "열쇠를 획득했습니다!"})
    return JsonResponse({"error": "잘못된 요청입니다."}, status=400)

# 문 1 접근
# @login_required
def door1_view(request):
    # key_status = get_object_or_404(KeyStatus, user=request.user)
    # if key_status.has_key:
    return render(request, 'main/door1.html')
    # return render(request, 'no_key.html', {'message': '열쇠가 필요합니다.'})

# 문 2 접근
# @login_required
def door2_view(request):
    # key_status = get_object_or_404(KeyStatus, user=request.user)
    # if key_status.has_key:
    return render(request, 'main/door2.html')
    # return render(request, 'no_key.html', {'message': '열쇠가 필요합니다.'})

# 문 3 접근
# @login_required
def door3_view(request):
    # key_status = get_object_or_404(KeyStatus, user=request.user)
    # if key_status.has_key:
    return render(request, 'main/door3.html')
    # return render(request, 'no_key.html', {'message': '열쇠가 필요합니다.'})

def index(request):
    return render(request, 'main/index.html')

def mouse(request):
    return render(request, 'main/mouse.html')

def main(request):
    return render(request, 'main/main.html')

def activate(request):
    return render(request, 'main/activate.html') 



def door1(request):
    return render(request, 'main/door1.html') 

def door2(request):
    return render(request, 'main/door2.html') 

def door3(request):
    return render(request, 'main/door3.html') 

