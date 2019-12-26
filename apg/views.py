from django.shortcuts import render
from django.http import HttpResponse
from APG import models
from django.db.models import Q

# Create your views here.
app_name = 'APG'

def search(request):
	return render(request,'APG/search.html')

def teammates(request):
	return render(request,'APG/teammates.html')

def filter(request):
	match = request.GET.get('match')
	search_type = request.GET.get('search_category')
	content = request.GET.get('content')
	print(match)
	print(search_type)
	print(content)

	con = Q()

	matchQ = Q()
	matchQ.connector = 'OR'
	if match=="one_match":
		matchQ.children.append(('contig_place_condition','One'))
	if match=="two_match":
		matchQ.children.append(('contig_place_condition','Two'))
	if match=="all":
		matchQ.children.append(('contig_place_condition','One'))
		matchQ.children.append(('contig_place_condition','Two'))
	con.add(matchQ,'AND')

	if search_type == 'contig_name':
		contig_id_Q = Q(contig_name__startswith=content)
		con.add(contig_id_Q,'AND')

	if search_type == 'individuals':
		indiQ = Q(num_individuals__gt = int(content))
		con.add(indiQ,'AND')

	if search_type == 'gene_name':
		geneQ = Q(apggene__gene_name__contains=content)
		con.add(geneQ,'AND')

	contigs = models.ApgContig.objects.filter(con).distinct()
	contigs = contigs.extra(select={ 
       'a': "SUBSTR(contig_name, 6)", 
       'num': "CAST(substr(contig_name, 7) AS UNSIGNED)"}) 
	contigs = contigs.order_by('num')
	if contigs.exists():
		return render(request,'APG/filter.html',{'contigs':contigs})
	else:
		return render(request,'APG/noresult.html')

def getcontig(request,c_name):
	contig = models.ApgContig.objects.get(contig_name=c_name)
	chro = contig.apgchromosome
	gene = contig.apggene_set.all()
	scaffold = contig.apgscaffold_set.all()
	print(chro)
	print(gene)
	print(scaffold)
	return render(request,'APG/getcontig.html',{'contig':contig,'chro':chro,'gene':gene,'scaffold':scaffold})

def background(request):
	return render(request,'APG/background.html')

def visualization(request):
	return render(request,'APG/igv.html')