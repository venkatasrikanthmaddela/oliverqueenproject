from userManagement.models import PmUser
from newProjectIdeaManagement.models import NewProjectIdea

def get_all_user_activites(request):
    user_dashboard = dict()
    user_data = PmUser.objects.get(email=request.user.email)
    new_project_requests = NewProjectIdea.objects.filter(customerId=user_data.id)
    for each_object in new_project_requests:
        if "newProjectIdeas" not in user_dashboard:
            user_dashboard["newProjectIdeas"] =list()
            user_dashboard["newProjectIdeas"].append(each_object)
        else:
            user_dashboard["newProjectIdeas"].append(each_object)
    return user_dashboard