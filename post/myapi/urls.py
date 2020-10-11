from django.urls import path
from . import view

urlpatterns = [
	# path('snippets/',view.snipped_list),
	# path('snippets/',view.SnippetList.as_view()),
	# path('snippets/',view.SnippetListMixins.as_view()),
	path('snippets/',view.SnippetListGeneric.as_view()),
	# path('snippets/<int:pk>/',view.snippet_detail),
	# path('snippets/<int:pk>/',view.SnippetDetail.as_view())
	# path('snippets/<int:pk>/',view.SnippetDetailMixins.as_view())
	path('snippets/<int:pk>/',view.SnippetDetailGeneric.as_view())
]