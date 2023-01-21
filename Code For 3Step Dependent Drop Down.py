# ================== Model ==============================================
class Country(models.Model):
    name = models.CharField(max_length=100)

class State(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

class City(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
# ================== Views =================================================

from django.http import JsonResponse

def load_states(request):
    country_id = request.GET.get('country')
    states = State.objects.filter(country_id=country_id).order_by('name')
    return JsonResponse(list(states.values()), safe=False)

def load_cities(request):
    state_id = request.GET.get('state')
    cities = City.objects.filter(state_id=state_id).order_by('name')
    return JsonResponse(list(cities.values()), safe=False)

# ================== URLS =================================================

from django.urls import path
from .views import load_states, load_cities

urlpatterns = [
    path('load-states/', load_states, name='load_states'),
    path('load-cities/', load_cities, name='load_cities'),
]

# ================== HTML =================================================

<form>
  <select id="country" name="country">
    {% for country in countries %}
      <option value="{{ country.id }}">{{ country.name }}</option>
    {% endfor %}
  </select>

  <select id="state" name="state">
  </select>

  <select id="city" name="city">
  </select>
</form>

<script>
  $(document).ready(function(){
    $("#country").change(function(){
      var country_id = $(this).val();
      $.ajax({
        url: "{% url 'load_states' %}",
        data: {
          'country': country_id
        },
        success: function(data){
          $("#state").html('');
          $("#state").append('<option value="">Select State</option>');
          $.each(data, function(index, value){
            $("#state").append('<option value="'+value.id+'">'+value.name+'</option>');
          });
        }
      });
    });

    $("#state").change(function(){
      var state_id = $(this).val();
      $.ajax({
        url: "{% url 'load_cities' %}",
        data: {
          'state': state_id
        },
        success: function(data){
          $("#city").html('');
          $("#city").append('<option value="">Select City</option>');
          $.each


# ==========================================================================