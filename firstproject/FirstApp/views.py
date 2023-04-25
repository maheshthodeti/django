from django.shortcuts import render
from django.http import HttpResponse;

# Create your views here.
def display(request): #view-function
	#ss ----> is html-data/code
	ss = '''		
			<center>
				<h2 style="color:Blue;">
					Hello User, Welcome to Django First-Project First-App
				</h2>
				<hr />
			</center>
		''';
	
	return HttpResponse(ss);



#default-url-request-view-func
def homepage(request):
    htmldata='''<center>
        <h1 style='color:blue;background-color:yellow;'>Welcome to DEFAULT Home-Page!!!</h1>
        <hr color='brown'/>
        <h2 style='color:green;background-color:cyan;'>Your Request Page is Not-Found...</h2>
        <hr color='brown'/>
        <h3 style='color:red;background-color:plum;'>Plz try other URL or Links!!!</h3>
		<hr color='brown'/>
    </center>''';
    return HttpResponse(htmldata);

