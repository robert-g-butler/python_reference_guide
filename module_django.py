
# Django Website: https://docs.djangoproject.com

# █████████████████████████████████████████████████████████████████████████████
#region Tutorial - Part 1 (Setup) █████████████████████████████████████████████

# Command Line  (Start a project and an app within that project) --------------
py -m django version  # Shows version #
django-admin startproject mysite  # Starts project "mysite" in current directory
py manage.py runserver  # Turns server on for use in browser ("py manage.py runserver 0:8000" runs it for all computers on network)
py manage.py startapp polls  # Starts new app "polls" in project folder

# mysite/polls/views.py  (Make a webpage for the "polls" app) -----------------
from django.http import HttpResponse
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

# mysite/polls/urls.py  (Allow URL path to go from polls to the main index) ---
from django.urls import path
from . import views
urlpatterns = [
    path(route='', view=views.index, name='index')
]

# mysite/urls.py  (Allow the URL path to go from the main index to polls) -----
from django.contrib import admin
from django.urls import include, path
urlpatterns = [
    path(route='polls/', view=include('polls.urls')),
    path(route='admin/', view=admin.site.urls)
]

# Command Line  (Run the app to check it) -------------------------------------
py manage.py runserver

#endregion ████████████████████████████████████████████████████████████████████
#region Tutorial - Part 2 (Models & Database) █████████████████████████████████

# mysite/settings.py  (Verify database type and timezone) ---------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
TIME_ZONE = 'America/Los_Angeles'

# Command Line  (Set up database) ---------------------------------------------
py manage.py migrate

# mysite/polls/models.py  (Add objects for the "polls" app) -------------------
from django.db import models
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

# mysite/settings.py  (Connect the "polls" app to the project by referencing its PollsConfig class from the mysite/polls/app.py file)
INSTALLED_APPS = [
    'polls.apps.PollsConfig',
    ...
]

# Command Line  (Migrate the database to add the "polls"app) ------------------
py manage.py makemigrations polls  # Configure the polls app for inclusion in the database.
py manage.py sqlmigrate polls 0001  # Visually review the new SQL code.
py manage.py migrate

# Command Line  (Add a Question object) ---------------------------------------
python manage.py shell  # Starts up python within the project
>>> from polls.models import Question, Choice
>>> Question.objects.all()
>>> from django.utils import timezone
>>> q = Question(question_text="What's new?", pub_date=timezone.now())
>>> q.save()
>>> q.id
>>> q.question_text
>>> q.pub_date
>>> q.question_text = "What's up?"
>>> q.save()
>>> Question.objects.all()

# mysite/polls/models.py  (Add __str__ to the models, so they are displayed correctly)
class Question(models.Model):
    ...
    def __str__(self):
        return self.question_text
class Choice(models.Model):
    ...
    def __str__(self):
        return self.choice_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

# Command Line  (Add Choice objects) ------------------------------------------
python manage.py shell
>>> from polls.models import Choice, Question
>>> Question.objects.all()
>>> Question.objects.filter(id=1)
>>> Question.objects.filter(question_text__startswith='What')
>>> from django.utils import timezone
>>> current_year = timezone.now().year
>>> Question.objects.get(pub_date__year=current_year)
>>> Question.objects.get(id=2)
>>> Question.objects.get(pk=1)
>>> q = Question.objects.get(pk=1)
>>> q.was_published_recently()
>>> q = Question.objects.get(pk=1)
>>> q.choice_set.all()
>>> q.choice_set.create(choice_text='Not much', votes=0)
>>> q.choice_set.create(choice_text='The sky', votes=0)
>>> c = q.choice_set.create(choice_text='Just hacking again', votes=0)
>>> c.question
>>> q.choice_set.all()
>>> q.choice_set.count()
>>> Choice.objects.filter(question__pub_date__year=current_year)
>>> c = q.choice_set.filter(choice_text__startswith='Just hacking')
>>> c.delete()

# Command Line  (Create an admin superuser, and check out the admin index) ----
py manage.py createsuperuser
# Name = admin
# Password = er...39
py manage.py runserver


# mysite/polls/admin.py (Add the Question class to the admin page) ------------
from django.contrib import admin
from .models import Question
admin.site.register(Question)

#endregion ████████████████████████████████████████████████████████████████████
#region Tutorial - Part 3 (Views & Templates) █████████████████████████████████

# Make Views for the App ------------------------------------------------------

# mysite/polls/views.py  (Update the views and URLs for polls in a hard-coded, SUB-OPTIMAL WAY)
...
def detail(request, question_id):
    return HttpResponse(content="You're looking at question {0}}.".format(question_id))
def results(request, question_id):
    response = "You're looking at the results of question {0}."
    return HttpResponse(content=response.format(question_id))
def vote(request, question_id):
    return HttpResponse(content="You're voting on question {}}.".format(question_id))

# mysite/polls/urls.py
from django.urls import path
from . import views
urlpatterns = [
    path(route='', view=views.index, name='index'),
    path(route='<int:question_id>/results/', view=views.results, name='results'),
    path(route='<int:question_id>/vote/', view=views.vote, name='vote'),
    path(route='<int:question_id>/', view=views.detail, name='detail'),
]

# mysite/polls/views.py  (Set the index view to show the latest 5 records)
from django.http import HttpResponse
from .models import Question
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(content=output)

# mysite/polls/templates/polls/index.html (Add a template for the index view and update the index view, which is a BETTER WAY of showing the latest 5 records)
{% if latest_question_list %}
    <ul>
    {% for question in latest_question_list %}
        <li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
    {% endfor %}
    </ul>
{% else %}
    <p>No polls are available.</p>
{% endif %}

# mysite/polls/views.py
from django.http import HttpResponse
from django.template import loader
from .models import Question
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template(template_name='polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(content=template.render(context, request))

# mysite/polls/views.py  (Remake the index view with render, which is the MOST OPTIMAL WAY of making views.)
from django.shortcuts import render
from .models import Question
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request=request, template_name='polls/index.html', context=context)

# Error-Catching & Dynamic Loading --------------------------------------------

# mysite/polls/views.py  (Remake the detail view in a SUB-OPTIMAL WAY to use a template and to return an error if the primary key doesn't exist)
from django.http import Http404
from django.shortcuts import render
from .models import Question
...
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request=request, template_name='polls/detail.html', context={'question': question})

# mysite/polls/templates/polls/detail.html
{{ quesiton }}

# mysite/polls/views/py  (Remake the details view with the MOST OPTIMAL WAY to do try-catch)
from django.shortcuts import get_object_or_404, render
from .models import Question
...
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request=request, template_name='polls/detail.html', context={'question': question})

# mysite/polls/templates/polls/detail.html  (Update the detail template)
<h1>{{ question.question_text }}</h1>
<ul>
{% for choice in question.choice_set.all %}
    <li>{{ choice.choice_text }}</li>
{% endfor %}
</ul>

# mysite/polls/templates/polls/index.html (Update HTML to update dynamically from the mysite/polls/urls.py file)
...
        <li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li>
...

# Adding Namespaces to Apps ---------------------------------------------------

# mysite/polls/urls.py  (Use "app_name" to add a Namespace to the Polls app)
...
app_name = 'polls'
urlpatterns = [
    ...
]

# mysite/polls/templates/polls.html  (Add the Namespace to the template)
...
        <li><a href="{% url 'polls:detail' question.id %}">{{ question.question_text }}</a></li>
...

#endregion ████████████████████████████████████████████████████████████████████
#region Tutorial - Part 4 (Template Buttons & Generic Views) ██████████████████

# mysite/polls/templates/polls/detail.html  (Add submit button to detail view)
<h1>{{ question.question_text }}</h1>

{% if error_message %}<p><strong>{{ error_message }}</strong></p>{% endif %}

<form action="{%url 'polls:vote' question.id %}" method="post">
  {% csrf_token %}
  {% for choice in questions.choice_set.all %}
    <input type="radio" name="choice" id="choice{{ forloop.counter }}" value="{{ choice.id }}">
    <label for="choice{{ forloop.counter }}">{{ choice.choice_text }}</label><br>
  {% endfor %}
  <input type="submit" value="Vote">
</form>

# mysite/polls/views.py  (Update the vote view to accept users' votes.)
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from .models import Choice, Question
...
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request=request,
            template_name='polls/detail.html',
            context={
                'question': question,
                'error_message': "You didn't select a choice."
            }
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse(
            'polls:results', args=(question.id,)
        ))

# Add a view for results ------------------------------------------------------

# mysite/polls/views.py
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request=request, template_name='polls/results.html', context={'question': question})

# mysite/polls/templates/polls/results.html
<h1>{{ question.question_text }}</h1>
<ul>
  {% for choice in question.choice_set.all %}
  <li>
    {{ choice.choice_text }} -- {{ choice.votes }} vote{{ choice.votes|pluralize }}
  </li>
  {% endfor %}
</ul>
<a href="{% url 'polls:detail' question.id %}">Vote again?</a>

# Switch to Generic Views -----------------------------------------------------

# mysite/polls/urls.py  (Update urls to generic views with "pk" in route)
...
urlpatterns = [
    path(route='', view=views.IndexView.as_view(), name='index'),
    path(route='<int:pk>/', view=views.DetailView.as_view(), name='detail'),
    path(route='<int:pk>/results/', view=views.ResultsView.as_view(), name='results'),
    path(route='<int:question_id>/vote/', view=views.vote, name='vote')
]

# mysite/polls/views.py (Update views to pull from Generic View classes)
...
from django.views import generic
...
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    def get_queryset(self):
        '''Return the last five published questions.'''
        return Question.objects.order_by('-pub_date')[:5]
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
...

#endregion ████████████████████████████████████████████████████████████████████
#region Tutorial - Part 5 (Automated Testing) █████████████████████████████████

# Identify the bug that was_published_recently() accepts future dates ---------

# Command Line
python manage.py shell
>>> import datetime
>>> from django.utils import timezone
>>> from polls.models import Question
>>> future_question = Question(pub_date=timezone.now() + datetime.timedelta(days=30))
>>> future_question.was_published_recently()

# Creating and running a test -------------------------------------------------

# mysite/polls/tests.py  (Add a test)
import datetime
from django.test import TestCase
from django.utils import timezone
from .models import Question
class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        '''
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        '''
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

# Command Line
py manage.py test polls

# Fix the bug and re-run the test ---------------------------------------------

# mysite/polls/models.py
...
class Question(models.Model):
    ...
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    ...

# Command Line
py manage.py test polls

# Add 2 more tests for testing the model --------------------------------------

# mysite/polls/tests.py
...
class QuestionModelTests(TestCase):
...
    def test_was_published_recently_with_old_question(self):
        '''
        was_published_recently() returns False for questions whose pub_date
        is older than 1 day.
        '''
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        '''
        was_published_recently() returns True for questions whose pub_date
        is within the last day.
        '''
        time = timezone.now() - datetime.timedelta(
            hours=23, minutes=59, seconds=59
        )
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)

# Use the shell to test a view ------------------------------------------------

# Command Line
py manage.py test polls
>>> from django.test.utils import setup_test_environment
>>> setup_test_environment()
>>> from django.test import Client
>>> client = Client()
>>> response = client.get('/')
>>> response.status_code                                    # Should be 404
>>> from django.urls import reverse
>>> response = client.get(reverse('polls:index'))
>>> response.status_code                                    # Should be 200
>>> response.content
>>> response.context['latest_question_list']

# Update the Index View to exclude future questions & create tests ------------

# /mysite/polls/views.py (Show only past questions)
...
from django.utils import timezone
...
class IndexView(generic.ListView):
    ...
    def get_queryset(self):
        '''
        Return the last five published questions (not including those set
        to be published in the future).
        '''
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]

# /mysite/polls/tests.py (Add tests for Index View)
def create_question(question_text, days):
    '''
    Create a question with the given 'question_text' and published the given
    number of 'days' offset to now (negative for questions published in the
    past, positive for questions that have yet to be published).
    '''
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)

class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        '''
        If no questions exist, an appropriate message is displayed.
        '''
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)

    def test_past_question(self):
        '''
        Questions with pub_date in the past are displayed on the index page.
        '''
        create_question(question_text='Past question.', days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            qs=response.context['latest_question_list'],
            values=['<Question: Past question.>']
        )

    def test_future_question(self):
        '''
        Questions with a pub_date in the future aren't displayed on the index
        page.
        '''
        create_question(question_text='Future question.', days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response=response, text='No polls are available.')
        self.assertQuerysetEqual(
            qs=response.context['latest_question_list'],
            values=[]
        )

    def test_future_question_and_past_question(self):
        '''
        Even if both past and future questions exist, only past questions are
        displayed.
        '''
        create_question(question_text='Past question.', days=-30)
        create_question(question_text='Future question.', days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            qs=response.context['latest_question_list'],
            values=['<Question: Past question.>']
        )

    def test_two_past_questions(self):
        '''
        The questions index page may display multiple questions.
        '''
        create_question(question_text='Past question 1.', days=-30)
        create_question(question_text='Past question 2.', days=-5)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            qs=response.context['latest_question_list'],
            values=[
                '<Question: Past question 1.>',
                '<Question: Past question 2.>'
            ]
        )

# Update the Details View to exclude future questions & create tests ----------

# mysite/polls/views.py (Exclude future questions)
...
class DetailView(generic.DetailView):
    ...
    def get_queryset(self):
        '''
        Excludes any questions that aren't published yet.
        '''
        return Question.objects.filter(pub_date__lte=timezone.now())

# mysite/polls/tests.py (Add tests for Details)
...
class QuestionDetailViewTests(TestCase):
    def test_future_question(self):
        '''
        The detail view of a question with a pub_date in the future returns a
        404 not found.
        '''
        future_question = create_question(
            question_text='Future question.',
            days=5
        )
        url = reverse(viewname='polls:detail', args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        '''
        The detail view of a question with a pub_date in the past displays the
        question's text.
        '''
        past_question = create_question(
            question_text='Past question.',
            days=-5
        )
        url = reverse(viewname='polls:detail', args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(
            response=response,
            text=past_question.question_text
        )

#endregion ████████████████████████████████████████████████████████████████████
#region Tutorial - Part 6 (Static Files) ██████████████████████████████████████

# Update CSS to make links green ----------------------------------------------

# mysite/polls/static/polls/styles.css
li a {
    color: green;
}

# mysite/polls/templates/polls/index.html
{% load static %}
<link rel='stylesheet' type='text/css' href="{% static 'polls/styles.css' %}">
...

# Add a background image with CSS ---------------------------------------------

# mysite/polls/styles/polls/images/background.gif
# Add a 'background.gif' file in this directory.

# mysite/polls/styles/polls/styles.css
...
body {
    background: white url('images/background.gif') no-repeat;
}

#endregion ████████████████████████████████████████████████████████████████████
#region Tutorial - Part 7 (Customizing the Admin Form) ████████████████████████

# Change the order of fields in each Question's admin page --------------------

# mysite/polls/admin.py
...
from .models import Choice, Question
...
class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']
admin.site.register(Question, QuestionAdmin)

# Separate fields in each Question's admin page into fieldsets ----------------

# mysite/polls/admin.py
...
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']})
    ]
...

# Add Choice to each Question's admin page ------------------------------------

# mysite/polls/admin.py
...
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
class QuestionAdmin(admin.ModelAdmin):
    ...
    inlines = [ChoiceInline]

# Update the Question model's admin page --------------------------------------

# mysite/polls/admin.py (Add fields to the Question model page)
...
class QuestionAdmin(admin.ModelAdmin):
    ...
    list_display = ['question_text', 'pub_date', 'was_published_recently']

# mysite/polls/models.py (Update how was_published_recently is displayed)
...
class Question(models.Model):
    ...
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published Recently?'

# mysite/polls/admin.py (Add a filter for pub_date)
...
class QuestionAdmin(admin.ModelAdmin):
    ...
    list_filter = ['pub_date']

# mysite/polls/admin.py (Add a search bar for Questions)
...
class QuestionAdmin(admin.ModelAdmin):
    ...
    search_fields = ['question_text']

# Update the admin page's template style --------------------------------------

# Make 'mysite/templates/admin' directory. Copy in django's base_site.html.

# mysite/settings.py
TEMPLATES = [
    {
        ...
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        ...
    }
]


#endregion ████████████████████████████████████████████████████████████████████
