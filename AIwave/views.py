from django.shortcuts import render


def index(request):
    return render(request, "index.html", { 'title':'Home' })

def roadmap(request):
    return render(request, "roadmap.html", { 'title': 'Roadmap', 'mainTitle':'Roadmap'})

def utilize(request):
    return render(request, "utilize.html", { 'title': 'How to use', 'mainTitle':'How to use'})




# Pages

def styleGuide(request):
    return render(request, "pages/styleGuide.html", { 'title': 'Style Guide', 'mainTitle':'Style Guide'})

def blog(request):
    return render(request, "pages/blog.html", { 'title': 'Our Blog', 'mainTitle':'Our Blog'})

def blogDetails(request):
    return render(request, "pages/blogDetails.html", { 'title': 'Our Blog', 'mainTitle':'Our Blog'})

def pricing(request):
    return render(request, "pages/pricing.html", { 'title': 'Pricing', 'mainTitle':'Pricing Plans For Everyone'})

def contact(request):
    return render(request, "pages/contact.html", { 'title': 'Contact', 'mainTitle':'Get Started with a free quotation'})

def signin(request):
    return render(request, "pages/signin.html", { 'title': 'Sign in'})

def signup(request):
    return render(request, "pages/signup.html", { 'title': 'Sign up'})

def team(request):
    return render(request, "pages/team.html", { 'title': 'Team', 'mainTitle':'Our Team'})

def termsPolicy(request):
    return render(request, "pages/termsPolicy.html", { 'title': 'Terms and Policy'})

def privacyPolicy(request):
    return render(request, "pages/privacyPolicy.html", { 'title': 'Privacy Policy'})

def profileDetails(request):
    return render(request, "pages/profileDetails.html", { 'title': 'Profile Details', 'headTitle':"Profile Details"})

def notification(request):
    return render(request, "pages/notification.html", { 'title': 'Settings', 'headTitle':"Settings"})

def chatExport(request):
    return render(request, "pages/chatExports.html", { 'title': 'Chat Exports', 'headTitle':"Settings"})

def appearance(request):
    return render(request, "pages/appearance.html", { 'title': 'Settings', 'headTitle':"Settings"})

def plansBilling(request):
    return render(request, "pages/plansBilling.html", { 'title': 'Plans & Billing', 'headTitle':"Plans & Billing"})

def sessions(request):
    return render(request, "pages/sessions.html", { 'title': 'Sessions', 'headTitle':"Sessions"})

def application(request):
    return render(request, "pages/application.html", { 'title': 'Application', 'headTitle':"Application"})

def releaseNotes(request):
    return render(request, "pages/releaseNotes.html", { 'title': 'Releasse Notes'})

def help(request):
    return render(request, "pages/help.html", { 'title': 'Help Notes'})




# Tools

def textGenerator(request):
    return render(request, "tools/textGenerator.html", { 'title': 'Text Generator'})

def imageGenerator(request):
    return render(request, "tools/imageGenerator.html", { 'title': 'Image Generator'})

def codeGenerator(request):
    return render(request, "tools/codeGenerator.html", { 'title': 'Code Generator'})

def imageEditor(request):
    return render(request, "tools/imageEditor.html", { 'title': 'Image Editor'})

def videoGenerator(request):
    return render(request, "tools/videoGenerator.html", { 'title': 'Video Generator'})

def imageEditor(request):
    return render(request, "tools/imageEditor.html", { 'title': 'Image Editor'})

def emailGenerator(request):
    return render(request, "tools/emailGenerator.html", { 'title': 'Email Generator'})