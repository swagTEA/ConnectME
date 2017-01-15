import os.path
from pathlib import Path
import boto
import boto.s3
import sys
from boto.s3.key import Key

AWS_ACCESS_KEY_ID = 'AKIAJSDV7UIS2YYE2ZGA'
AWS_SECRET_ACCESS_KEY = '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'

bucket_name = 'azhack2017'
conn = boto.connect_s3(AWS_ACCESS_KEY_ID,
        AWS_SECRET_ACCESS_KEY)


bucket = conn.create_bucket(bucket_name,
	location=boto.s3.connection.Location.DEFAULT)

fileName = 'file.txt'
myFile = Path("/Users/swatimunjal/Downloads/"+fileName)
while not myFile.is_file():
	continue

file = open(fileName, "r+")
data = file.read()
search = data.split(',')
file.close()

#get file from s3
for key in bucket.list():
    key.get_contents_to_filename('/Users/swatimunjal/Downloads/bottle.txt')

with open('/Users/swatimunjal/Downloads/bottle.txt', "r+") as myfile:
    body = myfile.read()
print body
total = body.split('*')
result = []

for s in total:
	for a in search:
		if a.strip() in s:
			result.append(s)
			break
data =''
tags = ''
for s in search:
	tags = tags + s + ' '
for s in result:
	arr = s.split('\n');
	data = data + arr[1]+'<br />'
	data = data + 'Hosted By: ' + arr[0]
	data = data + '<br />' +'----------------------------'+'<br />'

print data
tags = tags + '\n'
f = open('/Users/swatimunjal/Downloads/landing-sumo/Theme/evList.html','w')

message = """<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="icon" href="assets/img/favicon.ico">

    <title>Theme 13 - Landing Sumo</title>

    <!-- Bootstrap core CSS -->
    <link href="assets/css/bootstrap.css" rel="stylesheet">

    <!-- Custom styles for this template -->
    <link href="assets/css/custom-animations.css" rel="stylesheet">
    <link href="assets/css/style2.css" rel="stylesheet">


    <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
    <script src="assets/js/ie10-viewport-bug-workaround.js"></script>

    <!-- HTML5 shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->
  </head>

  <body>

	<! -- ********** HEADER ********** -->
	<div id="h">
		<div class="container">
			<div class="row">
			    <li><button class="btn btn-lg btn-info btn-register">Register</button></li>
			    <div class="col-md-10 col-md-offset-1 mt">
			    	
			    	<h3 class="mb">Suggested Events</h3>
			    </div>
			    <div class="col-md-12 mt hidden-xs">
			    	<!img src="assets/img/greek.jpg" class="img-responsive aligncenter" alt="" data-effect="slide-bottom">
			    </div>
			</div>
		</div><! --/container -->
	</div><! --/h -->
	
	<! -- ********** FIRST ********** -->
	<div id="w">
		<div class="row nopadding">
			<div class="col-md-5 col-md-offset-1 mt">
				<h3> Based on your search: </h3> 
				<h4> """ + tags + """</h4> 
				<p> ----------------------------------------------------------------------</p> 
				<h4>"""+data+"""</h4>
				

				
			</div>
			
			<div class="col-md-6 pull-right">
				<!img src="assets/img/congress.png" class="img-responsive alignright" alt="" data-effect="slide-right">
			</div>
		</div><! --/row -->
	</div><! --/container -->"""

f.write(message)
f.close()
os.remove("file.txt")
os.remove("bottle.txt")