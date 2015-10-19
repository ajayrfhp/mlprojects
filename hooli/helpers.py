
'''
		re-rewriting url :p 
		
		pdf's images and other files should not opened

		locate first /[a-z], before that is parent





		src /students/facilitiesnservices/hostelsnmess/  

		target www.nitt.edu/students/facilitiesnservices/hostelsnmess/ 

		src ./pages 
		parent www.nitt.edu/a/b/c/d/e
		target www.nitt.edu/a/b/c/d/e/pages


		src ../pages   (generalizable)
		parent www.nitt.edu/a/b/c/d/e
		target www.nitt.edu/a/b/c/d/pages


		src pages
		parent www.nitt.edu/a/b/c/d/e
		target None

		src ./+action ignore 
		target None



		src https://www.facebook.com/pragyan.nitt
		target None

		other domain urls
		starts crawling into nitt.ac.in

'''

def rewrite(parent,url):

	if( parent.count('nitt.edu') == 0 ):
		return 
	if( url == None ):
		return 
	if( url.find('./+')!=-1 ):
		return 
	if( url.count('.exe') >=1 ):
		return 
	if(url[0] == '.'):
		url = dotParse(parent,url)
	
		

	if( url[0:8] != 'https://' and url[0:7] != 'http://'):
		if(url.find('/')==-1):
			url = '/' + url
		url = 'http://www.nitt.edu' + url
	


	return url		


def dotParse(p,c):
	if(c[0] != '.'):
		return 
	if(p[-1] == '/' and c[0] == '/' ):
		p = p[:-1]		

	if( p.split('/')[:-c.count('../')][-1] == c[c.rfind('/')+1:]  ):
		return 

	if(c.find('/') == 1):
		return str(p) + str(c[1:])
	return '/'.join(p.split('/')[:-c.count('../')]) + '/' + str(c[c.rfind('/')+1:])	 	