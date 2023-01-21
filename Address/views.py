from django.shortcuts import render,redirect
# import json
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from . models import PresentAddress, Division, District, Upazila
from . forms import PresentAddressForm


def address(request):
    if request.method == 'POST':
        form = PresentAddressForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('Address:address')
    else:
        form = PresentAddressForm
        PresentAdd    =   PresentAddress.objects.all()
        data={'form':form, 'PresentAdd':PresentAdd}
        return render(request,'index.html',data)

# def load_districts(request):
#     country_id = request.GET.get('country')
#     states = State.objects.filter(country_id=country_id).order_by('name')
#     return JsonResponse(list(states.values()), safe=False)

def get_districts(request, division_id):
    Dist = District.objects.filter(Division_id=division_id)
    data = serializers.serialize('json', Dist)
    return HttpResponse(data, content_type='application/json')


def get_upazilas(request, district_id):
    Upaz = Upazila.objects.filter(District_id=district_id)
    data = serializers.serialize('json', Upaz)
    print(data)
    return HttpResponse(data, content_type='application/json')

